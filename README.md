# AsianScore Verifiable Football & NBA xG Prediction Ledger (CC BY 4.0)

[![Live Audit Dashboard](https://img.shields.io/badge/Live_Audit-asianscore.com-10b981)](https://asianscore.com/models.html#ledger)
[![Open REST API](https://img.shields.io/badge/REST_API-JSON_No_Key-3b82f6)](https://asianscore.com/api/ledger)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Open, cryptographically verifiable pre-match football & NBA probability benchmark maintained by **[AsianScore](https://asianscore.com/)**. Every prediction is locked **8–10 minutes before kickoff** with an immutable **SHA-256 input fingerprint** and automatically settled against official final scores via Brier Score.

## Latest Verified Benchmark Snapshot (`2026-11-22`)

- **Total Pre-Match Locked**: **355 matches**
- **Officially Settled & Audited**: **253 matches**
- **Top-1 Hit Rate**: **56.92%** (144 / 253)
- **Mean Brier Score**: **0.1783** (lower is better; uniform 3-way baseline = 0.2222)
- **Active Quant Model (`hybrid-xg-elo-v2`)**: 72% Power De-Vig market consensus + 28% Rolling Empirical-Bayes Elo & Dixon-Coles Bivariate Poisson xG + schedule rest-hours fatigue adjustment.

### League Breakdown (Live Snapshot)

| League | Settled | Correct | Hit Rate | Avg Brier |
| :--- | :---: | :---: | :---: | :---: |
| 欧国联 | 33 | 21 | 63.64% | 0.1698 |
| 非预赛 | 23 | 15 | 65.22% | 0.135 |
| NBA | 22 | 17 | 77.27% | 0.159 |
| 美职联 | 17 | 11 | 64.71% | 0.1804 |
| 日职联 | 15 | 4 | 26.67% | 0.2553 |
| 英冠 | 14 | 7 | 50% | 0.2071 |
| 意甲 | 11 | 7 | 63.64% | 0.1552 |
| 西甲 | 11 | 6 | 54.55% | 0.1847 |
| 英超 | 10 | 4 | 40% | 0.2112 |
| 德甲 | 9 | 7 | 77.78% | 0.1435 |

## Free Open REST API Endpoints (Zero API Key, CORS Enabled)

- **Public SHA-256 Audit Ledger**: `GET https://asianscore.com/api/ledger` ([Interactive Dashboard](https://asianscore.com/models.html#ledger))
- **Global Live Scores (22+ Leagues)**: `GET https://asianscore.com/api/scores` ([Live Scoreboard](https://asianscore.com/scores.html))
- **Live Match Telemetry (Events, Stats, Lineups, NBA Boxscore)**: `GET https://asianscore.com/api/match/telemetry?id=<matchId>`
- **Interactive Client-Side Quant Calculators (Bivariate Poisson xG, De-Vig, Half-Kelly, Free Shadow DOM Widget)**: [https://asianscore.com/tools.html](https://asianscore.com/tools.html)

```bash
curl -s https://asianscore.com/api/ledger | jq '.accuracy'
```

## Official Mirrors & Publications

- **Main Platform**: [https://asianscore.com/](https://asianscore.com/)
- **Kaggle Dataset**: [https://www.kaggle.com/datasets/asianscore/asianscore-football-and-nba-xg-prediction-ledger](https://www.kaggle.com/datasets/asianscore/asianscore-football-and-nba-xg-prediction-ledger)
- **Substack Quantitative Audit**: [https://asianscore.substack.com/](https://asianscore.substack.com/)
- **Dev.to Engineering Blog**: [https://dev.to/asianscore_lab](https://dev.to/asianscore_lab)
- **Medium Engineering**: [https://medium.com/@8748887](https://medium.com/@8748887)
- **Peerlist**: [https://peerlist.io/asianscore](https://peerlist.io/asianscore)

## License & Citation

Published under **CC BY 4.0**. If you use this benchmark in research, sports analytics tutorials, or calibration comparisons, please link to `https://asianscore.com/models.html#ledger`.
