import os
import csv
import re
from collections import defaultdict

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def is_card_line(line):
    # A card line has: number + condition (NM, EX, LP, etc.)
    return bool(re.search(r"\b\d+\s+(NM|EX|LP|MP|HP|DMG)\b", line))

def extract_card_and_count(line):
    """
    Extract card name and count correctly, ignoring collector numbers.
    """

    # Remove parenthetical text ONLY for parsing
    parse_line = re.sub(r"\([^)]*\)", "", line)

    # Match: <card name> <count> <condition>
    match = re.search(
        r"^(.*?)\s+(\d+)\s+(NM|EX|LP|MP|HP|DMG)\b",
        parse_line
    )

    if not match:
        return None, 0

    card_name = match.group(1).strip()
    count = int(match.group(2))

    return card_name, count


def main():
    set_totals = defaultdict(int)
    card_totals = defaultdict(int)

    txt_files = [
        f for f in os.listdir(SCRIPT_DIR)
        if f.lower().endswith(".txt")
    ]

    print(f"Found {len(txt_files)} text files")

    for filename in txt_files:
        path = os.path.join(SCRIPT_DIR, filename)
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            current_set = None

            for raw_line in f:
                line = raw_line.strip()
                if not line:
                    continue

                if not is_card_line(line):
                    current_set = line
                    continue

                if current_set:
                    card_name, count = extract_card_and_count(line)
                    set_totals[current_set] += count
                    card_totals[card_name] += count

    # Write CSVs next to the script
    set_csv = os.path.join(SCRIPT_DIR, "set_totals.csv")
    card_csv = os.path.join(SCRIPT_DIR, "card_totals.csv")

    with open(set_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Set Name", "Total Count"])
        for set_name, total in sorted(set_totals.items()):
            writer.writerow([set_name, total])

    with open(card_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Card Name", "Total Count"])
        for card_name, total in sorted(card_totals.items()):
            writer.writerow([card_name, total])

    print("Generated:")
    print(f" - {set_csv}")
    print(f" - {card_csv}")

if __name__ == "__main__":
    main()