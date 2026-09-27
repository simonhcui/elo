#!/usr/bin/env python3

import csv
from collections import defaultdict

# Ladder settings
WIN_POINTS = 20
LOSS_POINTS = -15

INPUT_FILE = "results.csv"
OUTPUT_FILE = "leaderboard.csv"


def main():
    ladder_points = defaultdict(int)
    wins = defaultdict(int)
    losses = defaultdict(int)

    with open(INPUT_FILE, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)

        for line_num, row in enumerate(reader, start=1):
            if len(row) < 3:
                print(f"Skipping invalid line {line_num}: {row}")
                continue

            player_a = row[0].strip()
            player_b = row[1].strip()

            try:
                result = int(row[2])
            except ValueError:
                print(f"Skipping invalid result on line {line_num}: {row}")
                continue

            if result not in (0, 1):
                print(f"Skipping invalid result on line {line_num}: {row}")
                continue

            # Ensure both players exist
            _ = ladder_points[player_a]
            _ = ladder_points[player_b]

            if result == 1:
                # Player A wins
                ladder_points[player_a] += WIN_POINTS

                ladder_points[player_b] += LOSS_POINTS
                ladder_points[player_b] = max(0, ladder_points[player_b])

                wins[player_a] += 1
                losses[player_b] += 1

            else:
                # Player B wins
                ladder_points[player_b] += WIN_POINTS

                ladder_points[player_a] += LOSS_POINTS
                ladder_points[player_a] = max(0, ladder_points[player_a])

                wins[player_b] += 1
                losses[player_a] += 1

    leaderboard = []

    for player in ladder_points:
        w = wins[player]
        l = losses[player]
        games = w + l

        winrate = (w / games * 100) if games > 0 else 0

        leaderboard.append({
            "player": player,
            "points": ladder_points[player],
            "wins": w,
            "losses": l,
            "games": games,
            "winrate": winrate
        })

    leaderboard.sort(
        key=lambda x: (x["points"], x["winrate"], x["games"]),
        reverse=True
    )

    print(
        f"{'Rank':<6}"
        f"{'Player':<25}"
        f"{'Points':>10}"
        f"{'W':>8}"
        f"{'L':>8}"
        f"{'WR%':>10}"
    )

    print("-" * 70)

    for rank, player in enumerate(leaderboard, start=1):
        print(
            f"{rank:<6}"
            f"{player['player']:<25}"
            f"{player['points']:>10}"
            f"{player['wins']:>8}"
            f"{player['losses']:>8}"
            f"{player['winrate']:>9.1f}"
        )

    # Save leaderboard to CSV
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow([
            "Rank",
            "Player",
            "Points",
            "Wins",
            "Losses",
            "Games",
            "WinRate"
        ])

        for rank, player in enumerate(leaderboard, start=1):
            writer.writerow([
                rank,
                player["player"],
                player["points"],
                player["wins"],
                player["losses"],
                player["games"],
                f"{player['winrate']:.2f}"
            ])

    print(f"\nSaved leaderboard to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()