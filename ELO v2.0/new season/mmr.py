#!/usr/bin/env python3

import csv
from collections import defaultdict

# Configuration
INITIAL_RATING = 1500
K_FACTOR = 320


def expected_score(rating_a, rating_b):
    """Expected score for player A."""
    return 1.0 / (1.0 + 10 ** ((rating_b - rating_a) / 400))


def update_ratings(rating_a, rating_b, result_a):
    """
    Update Elo ratings.

    result_a:
        1 = Player A wins
        0 = Player B wins
    """
    expected_a = expected_score(rating_a, rating_b)
    expected_b = 1.0 - expected_a

    result_b = 1 - result_a

    new_rating_a = rating_a + K_FACTOR * (result_a - expected_a)
    new_rating_b = rating_b + K_FACTOR * (result_b - expected_b)

    return new_rating_a, new_rating_b


def main():
    ratings = defaultdict(lambda: INITIAL_RATING)

    with open("results.csv", newline="", encoding="utf-8") as f:
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

            rating_a = ratings[player_a]
            rating_b = ratings[player_b]

            new_a, new_b = update_ratings(rating_a, rating_b, result)

            ratings[player_a] = new_a
            ratings[player_b] = new_b

    ranked_players = sorted(
        ratings.items(),
        key=lambda x: x[1],
        reverse=True
    )

    print(f"{'Rank':<6}{'Player':<25}{'MMR':>10}")
    print("-" * 45)

    for rank, (player, rating) in enumerate(ranked_players, start=1):
        print(f"{rank:<6}{player:<25}{rating:>10.1f}")


if __name__ == "__main__":
    main()