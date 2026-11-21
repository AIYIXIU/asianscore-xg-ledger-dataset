#!/usr/bin/env python3
"""
Zero-dependency market overround de-vigging (Proportional + Power Method)
and Brier Score audit verifier for asianscore_prediction_ledger.csv.

Interactive calculators: https://asianscore.com/tools.html
Live SHA-256 public ledger: https://asianscore.com/models.html#ledger
"""
import csv
import math
from pathlib import Path


def devig_proportional(decimal_odds: list[float]) -> tuple[float, list[float]]:
    raw = [1.0 / o for o in decimal_odds]
    overround = sum(raw)
    return round((overround - 1.0) * 100.0, 2), [p / overround for p in raw]


def devig_power(decimal_odds: list[float]) -> tuple[float, list[float]]:
    raw = [1.0 / o for o in decimal_odds]
    lo, hi = 1.0, 5.0
    for _ in range(45):
        mid = (lo + hi) / 2.0
        if sum(p ** mid for p in raw) > 1.0:
            lo = mid
        else:
            hi = mid
    k = (lo + hi) / 2.0
    return round(k, 4), [p ** k for p in raw]


def audit_csv(csv_path: Path) -> dict:
    settled = 0
    hits = 0
    briers = []
    hashes_ok = 0
    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            h = (row.get("inputHash") or "").strip()
            if len(h) == 64:
                hashes_ok += 1
            if (row.get("actualOutcome") or "").strip():
                settled += 1
                if str(row.get("isHit", "")).strip().lower() == "true":
                    hits += 1
                try:
                    briers.append(float(row["brierScore"]))
                except (ValueError, KeyError):
                    pass
    return {
        "rows_with_64char_sha256": hashes_ok,
        "settled_rows_in_csv": settled,
        "hits": hits,
        "hit_rate_pct": round(hits / settled * 100.0, 2) if settled else 0.0,
        "mean_brier": round(sum(briers) / len(briers), 4) if briers else None,
    }


if __name__ == "__main__":
    sample_odds = [2.10, 3.40, 3.60]
    vig, prop = devig_proportional(sample_odds)
    k, pwr = devig_power(sample_odds)
    print(f"Sample 3-way odds {sample_odds} (overround {vig}%):")
    print("  Proportional fair probs:", [round(x * 100, 2) for x in prop])
    print(f"  Power fair probs (k={k}):", [round(x * 100, 2) for x in pwr])

    csv_file = Path(__file__).parent / "asianscore_prediction_ledger.csv"
    if csv_file.exists():
        print("Ledger CSV audit:", audit_csv(csv_file))
