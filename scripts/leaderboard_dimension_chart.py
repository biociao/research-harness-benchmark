#!/usr/bin/env python3
"""Generate a per-paper x per-system x per-dimension score chart for the leaderboard.

Reads the five-dimension (D1-D5) scores for each leaderboard entry, for both the
Tyson 2004 (case 01) and Auton 2015 / 1000 Genomes Phase 3 (case 02) papers, and
renders a two-panel annotated heatmap (one panel per paper).

All dimension values are presented on a common 0-100 scale. Rows documented on
a 0-10 rubric are multiplied by 10 here so all entries share one display axis.

Rows are grouped by reviewer/evidence caliper (background band + legend). The
chart must not be read as a single controlled comparison across rounds.

Source: docs/leaderboard.md + evaluations/round-*.md
"""
import os
import matplotlib

os.environ["MPLCONFIGDIR"] = "/tmp/mplconf"
matplotlib.use("Agg")

# Register a CJK-capable font (macOS) so Chinese labels render; fall back to a
# bundled Noto Sans SC if available.
from matplotlib import font_manager

_CJK_CANDIDATES = [
    "/Library/Fonts/Arial Unicode.ttf",
    "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
    "/Users/ciao/Library/Fonts/NotoSansSC.ttf",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/System/Library/Fonts/Supplemental/Songti.ttc",
]
for _p in _CJK_CANDIDATES:
    if os.path.exists(_p):
        try:
            font_manager.fontManager.addfont(_p)
            _fam = font_manager.FontProperties(fname=_p).get_name()
            break
        except Exception:
            continue
else:
    _fam = None
if _fam:
    matplotlib.rcParams["font.sans-serif"] = [_fam] + matplotlib.rcParams["font.sans-serif"]
    matplotlib.rcParams["font.family"] = "sans-serif"

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch, Rectangle

# dimension labels + weights (from docs/rubric.md)
DIMS = ["D1 检索", "D2 理解", "D3 复现", "D4 实验", "D5 效率"]
WEIGHTS = [0.15, 0.30, 0.25, 0.20, 0.10]
# reusable recomputation for a reference "加权" column
def weighted(values):
    return 0.15 * values[0] + 0.30 * values[1] + 0.25 * values[2] + 0.20 * values[3] + 0.10 * values[4]

# caliper groups. Order = leaderboard rank (top -> bottom).
# Each entry: (label, caliper, tyson[5], auton[5])
DATA = [
    ("Rosalind · GPT-6 Astra", "R12工作目录", [95, 95, 90, 85, 70], [95, 95, 95, 90, 80]),
    ("Claude Science · DeepSeek-V1-Flash", "R03外评审", [80, 87, 81, 82, 80], [87, 89, 88, 86, 80]),
    ("dsh-science · DeepSeek-v4-Flash", "R03/R11混合", [90, 94, 92, 90, 87], [75, 75, 70, 80, 80]),
    ("workbuddy(auto) · GLM-5.2", "R03外评审", [75, 82, 75, 78, 76], [82, 90, 89, 88, 80]),
    ("Genpilot · DeepSeek-v4-Flash", "R10归档", [85, 85, 70, 75, 80], [80, 80, 80, 70, 80]),
    ("dsh-science · GLM-5.2", "R11工作目录", [85, 80, 60, 75, 65], [90, 85, 65, 85, 70]),
    ("dsh-science · GLM-5.3-Flash", "R11工作目录", [80, 65, 55, 75, 85], [80, 85, 75, 85, 80]),
    ("dsh-science · kimi k3", "R11工作目录", [70, 75, 55, 70, 85], [75, 75, 70, 65, 80]),
    ("ChatGPT-Rosalind · GPT-5.6 Sol", "R09成品", [70, 80, 60, 60, 60], [80, 80, 50, 70, 60]),
    ("dsh-science · GLM-5.3", "R11工作目录", [75, 60, 40, 50, 85], [80, 80, 65, 70, 75]),
]

# caliper -> band color + legend note
CALIPER = {
    "R12工作目录": ("#d7f0ec", "R12 GPT-6 Astra 完整工作目录评估"),
    "R03外评审": ("#dbe9fb", "R03 外部评审（六组合，同台可比）"),
    "R03/R11混合": ("#e7ddf5", "Tyson R03 + Auton R11 混合来源"),
    "R10归档": ("#fde8cf", "R10 已有评估归档复算（评审者未署名）"),
    "R11工作目录": ("#f6e1e5", "R11 GLM-5.3-Flash 工作目录审计"),
    "R09成品": ("#eee8d5", "R09 GPT-5.6-sol 最终 HTML 成品评估"),
}

labels = [d[0] for d in DATA]
cals = [d[1] for d in DATA]
tyson = np.array([d[2] for d in DATA], dtype=float)
auton = np.array([d[3] for d in DATA], dtype=float)

# reference weighted totals per paper (0-100)
tyson_w = [weighted(v) for v in tyson]
auton_w = [weighted(v) for v in auton]

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16.5, 10.2), constrained_layout=False)
fig.subplots_adjust(left=0.31, right=0.99, top=0.81, bottom=0.18, wspace=0.68)

CMAP = "RdYlGn"

def draw_panel(ax, data, title, wref, combine_note):
    # caliper background bands
    n = len(labels)
    for i in range(n):
        color, _ = CALIPER[cals[i]]
        ax.add_patch(Rectangle((-0.72, i - 0.5), 6.62, 1.0, color=color, zorder=0, clip_on=False))
    # imshow heatmap of the 5 dims
    im = ax.imshow(data, cmap=CMAP, vmin=0, vmax=100, aspect="auto")
    # x tick labels
    ax.set_xticks(range(5))
    ax.set_xticklabels(DIMS, rotation=45, ha="right", fontsize=10)
    # y tick labels (system names); show rank + caliper
    ax.set_yticks(range(n))
    ylabels = [f"{i+1}. {labels[i]}" for i in range(n)]
    ax.set_yticklabels(ylabels, fontsize=9)
    ax.tick_params(axis="y", length=0)
    # annotate cells
    for i in range(n):
        for j in range(5):
            v = data[i, j]
            ax.text(j, i, f"{v:g}", ha="center", va="center",
                    color="black", fontsize=9,
                    fontweight="bold" if v >= 90 else "normal")
    # add reference weighted column as text to the right
    for i in range(n):
        ax.text(5.35, i, f"{wref[i]:.1f}", va="center", ha="center", fontsize=9,
                color="#8a1c1c", fontweight="bold")
    ax.set_xlim(-0.72, 6.1)
    ax.set_ylim(n - 0.5, -0.5)
    ax.axvline(5.05, color="grey", lw=0.8, ls="--")
    ax.text(5.55, -0.85, "加权\n复算", ha="center", va="center", fontsize=9, color="#8a1c1c")
    # weight annotation on top of dims
    ax.set_title(title, fontsize=12, fontweight="bold", pad=34)
    for j, w in enumerate(WEIGHTS):
        ax.text(j, -0.92, f"×{int(w*100)}%", ha="center", va="center", fontsize=8, color="#555")
    # gridlines
    ax.set_xticks(np.arange(-0.5, 5.5, 1), minor=True)
    ax.set_yticks(np.arange(-0.5, n, 1), minor=True)
    ax.grid(which="minor", color="white", lw=1.2)
    ax.tick_params(which="minor", length=0)
    return im

im1 = draw_panel(axes[0], tyson, "Tyson 2004（case 01）", tyson_w, None)
im2 = draw_panel(axes[1], auton, "Auton 2015 / 1000G Phase 3（case 02）", auton_w, None)

# global colorbar
cbar = fig.colorbar(im2, ax=axes, orientation="horizontal", fraction=0.040, pad=0.09, aspect=38)
cbar.set_label("分维度得分（0–100，统一化展示）", fontsize=10)

# legend for calipers
handles = [Patch(facecolor=CALIPER[c][0], label=CALIPER[c][1]) for c in CALIPER]
fig.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, 0.935),
           ncol=3, frameon=False, fontsize=9.0)

fig.suptitle("科研场景 Harness 总榜 · 分论文 × 分系统 × 分维度得分（五维）",
             fontsize=15, fontweight="bold", y=0.965)

# footnote
fig.text(0.02, 0.045,
         "注：各维度已统一为 0–100 展示以便并读；“加权复算”列按 得分=0.15·D1+0.30·D2+0.25·D3+0.20·D4+0.10·D5 复算。"
         "不同颜色背景代表不同评审或证据口径（见上方图例），跨轮次分数不可视为统一条件下的受控比较。",
         fontsize=8.5, color="#444")

out = os.path.join(os.path.dirname(__file__), "..", "docs", "leaderboard-dimensions.png")
out = os.path.abspath(out)
fig.savefig(out, dpi=200, bbox_inches="tight")
plt.close(fig)
print("saved:", out)
