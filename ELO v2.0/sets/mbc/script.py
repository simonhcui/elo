
import csv
from collections import defaultdict

COLOR_IDENTITIES = {
    "Azorius": ["White", "Blue"],
    "Dimir": ["Blue", "Black"],
    "Rakdos": ["Black", "Red"],
    "Gruul": ["Red", "Green"],
    "Selesnya": ["Green", "White"],
    "Orzhov": ["White", "Black"],
    "Izzet": ["Blue", "Red"],
    "Golgari": ["Black", "Green"],
    "Boros": ["Red", "White"],
    "Simic": ["Green", "Blue"],
    "Esper": ["White", "Blue", "Black"],
    "Grixis": ["Blue", "Black", "Red"],
    "Jund": ["Black", "Red", "Green"],
    "Naya": ["Red", "Green", "White"],
    "Bant": ["White", "Blue", "Green"],
    "Abzan": ["White", "Black", "Green"],
    "Jeskai": ["White", "Blue", "Red"],
    "Sultai": ["Blue", "Black", "Green"],
    "Mardu": ["White", "Black", "Red"],
    "Temur": ["Blue", "Red", "Green"],
    "5c": ["White", "Blue", "Black", "Red", "Green"],
    "Four Color": ["White", "Blue", "Black", "Red", "Green"],
    "4c no blue": ["White", "Black", "Red", "Green"],
    "4c no white": ["Blue", "Black", "Red", "Green"],
    "4c no black": ["White", "Blue", "Red", "Green"],
    "4c no red": ["White", "Blue", "Black", "Green"],
    "4c no green": ["White", "Blue", "Black", "Red"],

    # Mono-color identities
    "Mono W": ["White"],
    "Mono U": ["Blue"],
    "Mono B": ["Black"],
    "Mono R": ["Red"],
    "Mono G": ["Green"],
}


def get_average(placements):
    return sum(placements) / len(placements)


def print_stats(title, stats):
    print(f"\n{'=' * 55}")
    print(title)
    print("=" * 55)

    if not stats:
        print("No data found.")
        return

    sorted_stats = sorted(
        stats.items(),
        key=lambda item: (get_average(item[1]), item[0].lower())
    )

    print(f"{'Name':<25} {'Avg Place':>10} {'Games':>8}")
    print("-" * 55)

    for name, placements in sorted_stats:
        print(
            f"{name:<25} {get_average(placements):>10.2f} "
            f"{len(placements):>8}"
        )


def print_commander_stats(commanders, total_games):
    print(f"\n{'=' * 85}")
    print("COMMANDER STATISTICS (RANKED BY MOST PLAYED)")
    print("=" * 85)

    sorted_commanders = sorted(
        commanders.items(),
        key=lambda item: (-len(item[1]), item[0].lower())
    )

    print(
        f"{'Rank':<6} {'Commander':<38} "
        f"{'Played':>8} {'Game %':>9} {'Avg Place':>11}"
    )
    print("-" * 85)

    for rank, (commander, placements) in enumerate(
        sorted_commanders, start=1
    ):
        count = len(placements)
        percentage = count / total_games * 100

        print(
            f"{rank:<6} {commander:<38} "
            f"{count:>8} {percentage:>8.1f}% "
            f"{get_average(placements):>11.2f}"
        )


def write_csv(filename, player_stats, pair_stats,
              color_stats, commander_stats, total_games):

    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)

        # Player averages
        writer.writerow(["PLAYER AVERAGES"])
        writer.writerow(["Player", "Average Placement", "Games"])

        for name, placements in sorted(
            player_stats.items(),
            key=lambda item: (get_average(item[1]), item[0].lower())
        ):
            writer.writerow([
                name,
                round(get_average(placements), 2),
                len(placements)
            ])

        writer.writerow([])

        # Color pair averages
        writer.writerow(["COLOR PAIR AVERAGES"])
        writer.writerow(["Color Identity", "Average Placement", "Games"])

        for name, placements in sorted(
            pair_stats.items(),
            key=lambda item: (get_average(item[1]), item[0].lower())
        ):
            writer.writerow([
                name,
                round(get_average(placements), 2),
                len(placements)
            ])

        writer.writerow([])

        # Individual color averages
        writer.writerow(["INDIVIDUAL COLOR AVERAGES"])
        writer.writerow(["Color", "Average Placement", "Games"])

        for name, placements in sorted(
            color_stats.items(),
            key=lambda item: (get_average(item[1]), item[0].lower())
        ):
            writer.writerow([
                name,
                round(get_average(placements), 2),
                len(placements)
            ])

        writer.writerow([])

        # Commander statistics
        writer.writerow(["COMMANDER STATISTICS"])
        writer.writerow([
            "Rank",
            "Commander",
            "Times Played",
            "Game Percentage",
            "Average Placement"
        ])

        sorted_commanders = sorted(
            commander_stats.items(),
            key=lambda item: (-len(item[1]), item[0].lower())
        )

        for rank, (commander, placements) in enumerate(
            sorted_commanders, start=1
        ):
            count = len(placements)
            percentage = count / total_games * 100

            writer.writerow([
                rank,
                commander,
                count,
                round(percentage, 2),
                round(get_average(placements), 2)
            ])


def main():
    player_placements = defaultdict(list)
    color_pair_placements = defaultdict(list)
    individual_color_placements = defaultdict(list)
    commander_placements = defaultdict(list)

    total_games = 0

    try:
        with open(
            "results.txt", "r", newline="", encoding="utf-8-sig"
        ) as file:
            reader = csv.reader(file)

            for line_number, row in enumerate(reader, start=1):
                if not row or all(not field.strip() for field in row):
                    continue

                if len(row) < 4:
                    print(f"Skipping invalid line {line_number}: {row}")
                    continue

                player = row[0].strip()
                color_pair = row[1].strip()

                try:
                    placement = int(row[2].strip())
                    if placement not in range(1, 5):
                        raise ValueError
                except ValueError:
                    print(f"Skipping invalid placement on line {line_number}")
                    continue

                if not player or not color_pair:
                    continue

                total_games += 1

                # Player statistics
                player_placements[player].append(placement)

                # Color pair statistics
                color_pair_placements[color_pair].append(placement)

                # Individual color statistics
                colors = COLOR_IDENTITIES.get(color_pair)

                if colors is None:
                    print(
                        f"Warning: Unknown color identity '{color_pair}' "
                        f"on line {line_number}"
                    )
                else:
                    for color in colors:
                        individual_color_placements[color].append(placement)

                # Commander statistics
                for index in (3, 4):
                    if len(row) > index:
                        commander = row[index].strip()

                        if commander and commander.upper() != "N/A":
                            commander_placements[commander].append(placement)

    except FileNotFoundError:
        print("Error: results.txt not found in the current directory.")
        return

    if total_games == 0:
        print("No valid game results found.")
        return

    # Print command-line statistics
    print_stats("PLAYER AVERAGES", player_placements)
    print_stats("COLOR PAIR AVERAGES", color_pair_placements)
    print_stats("INDIVIDUAL COLOR AVERAGES", individual_color_placements)

    print_commander_stats(commander_placements, total_games)

    # Export all statistics to CSV
    filename = "commander_stats.csv"

    write_csv(
        filename,
        player_placements,
        color_pair_placements,
        individual_color_placements,
        commander_placements,
        total_games
    )

    print(f"\nStatistics successfully saved to {filename}")


if __name__ == "__main__":
    main()
