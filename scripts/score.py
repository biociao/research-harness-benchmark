#!/usr/bin/env python3
import argparse
import json

WEIGHTS = {"D1": 0.15, "D2": 0.30, "D3": 0.25, "D4": 0.20, "D5": 0.10}

def score(values):
    missing = [k for k in WEIGHTS if k not in values or values[k] is None]
    if missing:
        raise ValueError(f"Missing scores: {', '.join(missing)}")
    if any(not (0 <= float(values[k]) <= 10) for k in WEIGHTS):
        raise ValueError("Each score must be between 0 and 10.")
    return sum(float(values[k]) * WEIGHTS[k] for k in WEIGHTS)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("json_file")
    args = p.parse_args()
    data = json.load(open(args.json_file, encoding="utf-8"))
    total = score(data["scores"])
    print(f"{total:.2f}")

if __name__ == "__main__":
    main()
