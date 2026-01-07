import csv
from collections import defaultdict

INPUT_FILE = "results.csv"
OUTPUT_FILE = "winstreaks.txt"

# Track current streaks
current_streak = defaultdict(int)
current_start_date = {}

# Track best (longest) streaks
best_streak = defaultdict(int)
best_start_date = {}
best_end_date = {}

current_event_date = None

def record_win(player, date):
    # Start new streak if needed
    if current_streak[player] == 0:
        current_start_date[player] = date

    current_streak[player] += 1

    # Update best streak if this one is longer
    if current_streak[player] > best_streak[player]:
        best_streak[player] = current_streak[player]
        best_start_date[player] = current_start_date[player]
        best_end_date[player] = date

def record_loss(player):
    current_streak[player] = 0
    current_start_date.pop(player, None)

with open(INPUT_FILE, newline="", encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        if not row:
            continue

        # Event header line (5 fields)
        if len(row) == 5:
            _, _, _, _, current_event_date = row
            continue

        # Match line (3 fields)
        if len(row) == 3:
            player_a, player_b, result = row

            if result == "1":
                record_win(player_a, current_event_date)
                record_loss(player_b)
            else:
                record_win(player_b, current_event_date)
                record_loss(player_a)

# Sort by longest streak descending
sorted_streaks = sorted(
    best_streak.items(),
    key=lambda x: x[1],
    reverse=True
)

with open(OUTPUT_FILE, "w", encoding="utf-8") as out:
    for player, streak in sorted_streaks:
        start = best_start_date.get(player, "N/A")
        end = best_end_date.get(player, "N/A")
        out.write(f"{player}: {streak} wins ({start} to {end})\n")

print(f"Longest win streaks written to {OUTPUT_FILE}")
