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
    if points < 150:
        return "bronze_4"
    elif points < 300:
        return "bronze_3"
    elif points < 450:
        return "bronze_2"
    elif points < 600:
        return "bronze_1"
    elif points < 750:
        return "silver_4"
    elif points < 900:
        return "silver_3"
    elif points < 1050:
        return "silver_2"
    elif points < 1200:
        return "silver_1"
    elif points < 1350:
        return "gold_4"
    elif points < 1500:
        return "gold_3"
    elif points < 1650:
        return "gold_2"
    elif points < 1800:
        return "gold_1"
    elif points < 1950:
        return "plat_4"
    elif points < 2100:
        return "plat_3"
    elif points < 2250:
        return "plat_2"
    elif points < 2400:
        return "plat_1"
    elif points < 2550:
        return "diamond_4"
    elif points < 2700:
        return "diamond_3"
    elif points < 2850:
        return "diamond_2"
    elif points < 3000:
        return "diamond_1"
    elif points < 3150:
        return "mythic"
    else:
        return "mythic"

# =========================
# XP Logic
# =========================

# Manual XP rewards
BONUS_XP = {
    'Nick D': 575,
    'Juwan': 175,
    'Matt Y': 400,
    'Evan S': 225,
    'Tony': 500,
    'Clayton': 900,
    'Chris A': 425,
    'Alberto': 225,
    'Alan': 350,
    'Noah': 350,
    'Eric K': 375,
    'John K': 100,
    'Jacob': 300,
    'Sonny': 100,
    'Walski': 400,
    'Stephen': 25,
    'Kevin S': 300,
    'Marco': 250,
    'Adam': 75,
    'Luis': 275,
    'Collin': 75,
    'Nathan': 100,
    'Jim': 25
}

def get_level_name(total_xp):
    if total_xp < 160:
        return "Novice"
    elif total_xp < 220:
        return "Prodigy"
    elif total_xp < 300:
        return "Apprentice"
    elif total_xp < 400:
        return "TaskMage"
    elif total_xp < 540:
        return "Adept"
    elif total_xp < 720:
        return "Spellshaper"
    elif total_xp < 960:
        return "Guildmage"
    elif total_xp < 1280:
        return "Invoker"
    elif total_xp < 1720:
        return "Sorcerer"
    elif total_xp < 2300:
        return "Battlemage"
    elif total_xp < 2300:
        return "Archmage"
    else:
        return "Archmage"


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

        if len(drafts[player]) < 40:
            continue

        # --------------------------------
        # XP
        # --------------------------------

        w = wins[player]
        l = losses[player]

        draft_count = len(drafts[player])

        stats_xp = (w * 3) + draft_count
        bonus_xp = BONUS_XP.get(player, 0)

        total_xp = stats_xp + bonus_xp

        level_name = get_level_name(total_xp)
        

        games = w + l

        win_pct = (w / games * 100) if games > 0 else 0

        rank_name = get_rank_name(ladder_points[player])

        leaderboard.append({
            "name": player,
            "win_percentage_value": win_pct,
            "wins": w,
            "losses": l,
            "rank": f"/images/rank/{rank_name}.jpg",
            "level": f"/images/planeswalker/{level_name}.jpg",
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
            "level": player["level"],
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