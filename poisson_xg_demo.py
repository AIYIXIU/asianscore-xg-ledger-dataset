#!/usr/bin/env python3
# Standalone Bivariate Poisson + Dixon-Coles Expected Goals (xG) Scoreline Simulator.
# Interactive web version: https://asianscore.com/tools.html
# Public SHA-256 pre-match prediction audit ledger: https://asianscore.com/models.html#ledger
import math


def dixon_coles_matrix(lam_home: float, lam_away: float, rho: float = -0.06, max_goals: int = 6):
    def pois(k: int, lam: float) -> float:
        return (lam ** k) * math.exp(-lam) / math.factorial(k)

    def tau(x: int, y: int) -> float:
        if x == 0 and y == 0:
            return max(0.0, 1.0 - lam_home * lam_away * rho)
        if x == 0 and y == 1:
            return max(0.0, 1.0 + lam_home * rho)
        if x == 1 and y == 0:
            return max(0.0, 1.0 + lam_away * rho)
        if x == 1 and y == 1:
            return max(0.0, 1.0 - rho)
        return 1.0

    grid = {}
    total = 0.0
    for h in range(max_goals + 1):
        for a in range(max_goals + 1):
            p = pois(h, lam_home) * pois(a, lam_away) * tau(h, a)
            grid[(h, a)] = p
            total += p

    p_home = sum(p for (h, a), p in grid.items() if h > a) / total
    p_draw = sum(p for (h, a), p in grid.items() if h == a) / total
    p_away = sum(p for (h, a), p in grid.items() if h < a) / total
    p_over25 = sum(p for (h, a), p in grid.items() if h + a >= 3) / total
    p_btts = sum(p for (h, a), p in grid.items() if h >= 1 and a >= 1) / total
    top5 = sorted(((p / total, f"{h}:{a}") for (h, a), p in grid.items()), reverse=True)[:5]
    return {
        "home_win": round(p_home * 100, 2),
        "draw": round(p_draw * 100, 2),
        "away_win": round(p_away * 100, 2),
        "over_2_5": round(p_over25 * 100, 2),
        "btts": round(p_btts * 100, 2),
        "top5_scores": [(sc, round(pr * 100, 2)) for pr, sc in top5],
    }


if __name__ == "__main__":
    res = dixon_coles_matrix(1.62, 1.18, rho=-0.06)
    print("Bivariate Poisson + Dixon-Coles (xG 1.62 vs 1.18):", res)
