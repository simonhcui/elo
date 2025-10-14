import csv
import json

def safe_int(s, default=0):
    try:
        return int(float(s))
    except Exception:
        return default

def compute_win_pct(wins, total):
    if total <= 0:
        return "0.00%"
    return f"{(wins / total) * 100:.2f}%"

def generate_matchup_json(csv_filename, json_filename, skip_header_auto=True):
    matchups = {}

    with open(csv_filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    # auto-detect header
    start_idx = 0
    if skip_header_auto and rows:
        first = rows[0]
        if len(first) >= 3:
            try:
                float(first[2])
            except Exception:
                start_idx = 1

    for row in rows[start_idx:]:
        if not row or len(row) < 2:
            continue

        player1 = row[0].strip()
        player2 = row[1].strip()
        p1_wins = safe_int(row[2]) if len(row) > 2 else 0
        p2_wins = safe_int(row[3]) if len(row) > 3 else 0

        if len(row) > 5:
            total_matches = safe_int(row[5], default=(p1_wins + p2_wins))
            if total_matches == 0:
                total_matches = p1_wins + p2_wins
        else:
            total_matches = p1_wins + p2_wins

        if total_matches == 0:
            total_matches = p1_wins + p2_wins

        p1_win_pct = compute_win_pct(p1_wins, total_matches)
        p2_win_pct = compute_win_pct(p2_wins, total_matches)

        if player1 not in matchups:
            matchups[player1] = []
        if player2 not in matchups:
            matchups[player2] = []

        matchups[player1].append({
            "Player": player2,
            "Record": f"{p1_wins}-{p2_wins}",
            "Win %": p1_win_pct,
            "Total Matches": str(total_matches)
        })

        matchups[player2].append({
            "Player": player1,
            "Record": f"{p2_wins}-{p1_wins}",
            "Win %": p2_win_pct,
            "Total Matches": str(total_matches)
        })

    # Sort each player's matchup list
    for p in matchups:
        matchups[p].sort(key=lambda x: x["Player"].lower())

    # Sort the top-level dictionary by player name
    sorted_matchups = {k: matchups[k] for k in sorted(matchups.keys(), key=str.lower)}

    # Write to JSON
    with open(json_filename, "w", encoding="utf-8") as f:
        json.dump(sorted_matchups, f, indent=4, ensure_ascii=False)

    print(f"JSON file '{json_filename}' created successfully, sorted alphabetically.")

# Example usage:
if __name__ == "__main__":
    generate_matchup_json("pairings.csv", "matchups.json")
