#!/usr/bin/env python3

import csv
import json
from collections import defaultdict

# =========================
# Ladder Settings
# =========================

WIN_POINTS = 20
LOSS_POINTS = -15

# =========================
# MMR Settings
# =========================

INITIAL_RATING = 1500
K_FACTOR = 320

INPUT_FILE = "results.csv"
OUTPUT_FILE = "leaderboard.json"


# =========================
# Elo Logic (from mmr.py)
# =========================

def expected_score(rating_a, rating_b):
    return 1.0 / (1.0 + 10 ** ((rating_b - rating_a) / 400))


def update_ratings(rating_a, rating_b, result_a):
    expected_a = expected_score(rating_a, rating_b)
    expected_b = 1.0 - expected_a

    result_b = 1 - result_a

    new_rating_a = rating_a + K_FACTOR * (result_a - expected_a)
    new_rating_b = rating_b + K_FACTOR * (result_b - expected_b)

    return new_rating_a, new_rating_b


# =========================
# Rank Logic
# =========================

def get_rank_name(points):

    season_15_base = 30
    current_season_multiplier = 0.7920792079207921

    if points < season_15_base*1*current_season_multiplier:
        return "bronze_4"
    elif points < season_15_base*2*current_season_multiplier:
        return "bronze_3"
    elif points < season_15_base*3*current_season_multiplier:
        return "bronze_2"
    elif points < season_15_base*4*current_season_multiplier:
        return "bronze_1"
    elif points < season_15_base*5*current_season_multiplier:
        return "silver_4"
    elif points < season_15_base*6*current_season_multiplier:
        return "silver_3"
    elif points < season_15_base*7*current_season_multiplier:
        return "silver_2"
    elif points < season_15_base*8*current_season_multiplier:
        return "silver_1"
    elif points < season_15_base*9*current_season_multiplier:
        return "gold_4"
    elif points < season_15_base*10*current_season_multiplier:
        return "gold_3"
    elif points < season_15_base*11*current_season_multiplier:
        return "gold_2"
    elif points < season_15_base*12*current_season_multiplier:
        return "gold_1"
    elif points < season_15_base*13*current_season_multiplier:
        return "plat_4"
    elif points < season_15_base*14*current_season_multiplier:
        return "plat_3"
    elif points < season_15_base*15*current_season_multiplier:
        return "plat_2"
    elif points < season_15_base*16*current_season_multiplier:
        return "plat_1"
    elif points < season_15_base*17*current_season_multiplier:
        return "diamond_4"
    elif points < season_15_base*18*current_season_multiplier:
        return "diamond_3"
    elif points < season_15_base*19*current_season_multiplier:
        return "diamond_2"
    elif points < season_15_base*20*current_season_multiplier:
        return "diamond_1"
    elif points < season_15_base*21*current_season_multiplier:
        return "mythic"
    else:
        return "mythic"


# =========================
# Main
# =========================

def main():
    ladder_points = defaultdict(int)

    wins = defaultdict(int)
    losses = defaultdict(int)

    ratings = defaultdict(lambda: INITIAL_RATING)

    drafts = defaultdict(set)

    current_set = ""
    current_date = ""

    last_set = {}
    last_date = {}

    current_event = 1

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        for line_num, raw_line in enumerate(f, start=1):

            # Blank line = new event
            if not raw_line.strip():
                current_event += 1
                continue

            row = next(csv.reader([raw_line]))

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

            # --------------------------------
            # Draft counting
            # --------------------------------

            drafts[player_a].add(current_event)
            drafts[player_b].add(current_event)

            # --------------------------------
            # Last set / date
            # --------------------------------

            if len(row) >= 5:

                current_set = row[3].strip()
                current_date = row[4].strip()

                set_name = row[3].strip()
                date_str = row[4].strip()

            last_set[player_a] = current_set
            last_set[player_b] = current_set

            last_date[player_a] = current_date
            last_date[player_b] = current_date

            # --------------------------------
            # Ladder points
            # --------------------------------

            _ = ladder_points[player_a]
            _ = ladder_points[player_b]

            if result == 1:
                ladder_points[player_a] += WIN_POINTS

                ladder_points[player_b] += LOSS_POINTS
                ladder_points[player_b] = max(0, ladder_points[player_b])

                wins[player_a] += 1
                losses[player_b] += 1

            else:
                ladder_points[player_b] += WIN_POINTS

                ladder_points[player_a] += LOSS_POINTS
                ladder_points[player_a] = max(0, ladder_points[player_a])

                wins[player_b] += 1
                losses[player_a] += 1

            # --------------------------------
            # Elo
            # --------------------------------

            rating_a = ratings[player_a]
            rating_b = ratings[player_b]

            new_a, new_b = update_ratings(
                rating_a,
                rating_b,
                result
            )

            ratings[player_a] = new_a
            ratings[player_b] = new_b

    # =========================
    # Build leaderboard
    # =========================

    players = set()

    players.update(wins.keys())
    players.update(losses.keys())
    players.update(ratings.keys())

    leaderboard = []

    for player in players:

        if len(drafts[player]) < 3:
            continue

        w = wins[player]
        l = losses[player]

        games = w + l

        win_pct = (w / games * 100) if games > 0 else 0

        rank_name = get_rank_name(ladder_points[player])

        leaderboard.append({
            "name": player,
            "win_percentage_value": win_pct,
            "wins": w,
            "losses": l,
            "rank": f"/images/rank/{rank_name}.jpg",
            "total_drafts": len(drafts[player]),
            "elo": ratings[player],
            "last_set": last_set.get(player, ""),
            "last_date": last_date.get(player, "")
        })

    # Sort by win percentage descending
    leaderboard.sort(
        key=lambda x: (
            x["win_percentage_value"],
            x["wins"]
        ),
        reverse=True
    )

    output = []

    for standing, player in enumerate(leaderboard, start=1):

        output.append({
            "standing": str(standing),
            "rank": player["rank"],
            "name": player["name"],
            "win_percentage": f"{player['win_percentage_value']:.2f}%",
            "wins_losses": f"{player['wins']}-{player['losses']}",
            "total_drafts": str(player["total_drafts"]),
            "elo": f"{round(player['elo'])}",
            "last_set": player["last_set"],
            "last_date": player["last_date"]
        })

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)

    print(f"Saved {len(output)} players to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()