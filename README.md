# AsianScore Open Sports Prediction Ledger & Bivariate Poisson xG Toolkit

[![Live Ledger](https://img.shields.io/badge/Live_SHA256_Ledger-asianscore.com-10b981)](https://asianscore.com/models.html#ledger)
[![Interactive Simulator](https://img.shields.io/badge/Free_xG_Simulator-Tools_Lab-2563eb)](https://asianscore.com/tools.html)

Open, cryptographically verifiable dataset of pre-match football & NBA quantitative forecasts published by [AsianScore](https://asianscore.com/).

Every match projection is hashed with **SHA-256 prior to kickoff** (`inputHash`) and evaluated post-match using proper scoring rules (**Brier Score**), preventing hindsight edits or cherry-picking.

## Live Snapshot (2026-11-21 13:34 UTC)

| Metric | Value |
| :--- | :--- |
| **Total Pre-Match SHA-256 Locked Forecasts** | `310` |
| **Settled & Verified Matches** | `206` |
| **Correct Primary Outcome Predictions** | `127` (`61.65%`) |
| **Mean Brier Score (lower is better)** | `0.166` |
| **Covered Leagues** | `12` |

## Files Included

1. `asianscore_prediction_ledger.csv` — Recent settled + upcoming locked match forecasts with `probHome`/`probDraw`/`probAway`, 64-char SHA-256 `inputHash`, final `actualScore`, and `brierScore`.
2. `asianscore_league_accuracy.csv` — Aggregated hit rate and mean Brier score across 12 leagues.
3. `poisson_xg_demo.py` — Zero-dependency Python implementation of the **Bivariate Poisson + Dixon-Coles** expected goals (xG) scoreline matrix model.
4. `devig_and_audit.py` — Zero-dependency Proportional & Power market de-vigging plus CSV SHA-256 / Brier Score auditor.

## Live Open API & Free Web Tools (No Login Required)

- **Live JSON Ledger API (CORS `*`)**: `https://asianscore.com/api/ledger`
- **Interactive xG Poisson, De-Vig & NBA Pace Simulator**: https://asianscore.com/tools.html
- **Free Embeddable Live Scores & Ledger Widget**: https://asianscore.com/tools.html#embed
- **Live Match Telemetry & Analytics Portal**: https://asianscore.com/

## Quick Start

```bash
python3 poisson_xg_demo.py
python3 devig_and_audit.py
```

## License

Dataset released under **CC BY 4.0** (attribution to [AsianScore](https://asianscore.com/)); Python demo code released under **MIT License**.
