
import csv
from collections import Counter

INPUT_FILE = "results.csv"
OUTPUT_FILE = "set_counts.csv"

set_counts = Counter()

# Read the input CSV
with open(INPUT_FILE, "r", newline="", encoding="utf-8-sig") as file:
    reader = csv.reader(file)

    for row in reader:
        # Skip blank lines or lines that don't have all 5 fields
        if len(row) < 5:
            continue

        # Get the Set Code (4th field)
        set_code = row[3].strip()

        # Skip rows with an empty Set Code or TEST
        if not set_code or set_code.upper() == "TEST":
            continue

        # Increment the count for this set
        set_counts[set_code] += 1

# Write the results to a new CSV
with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Set Code", "Times Hosted"])

    for set_code, count in sorted(set_counts.items()):
        writer.writerow([set_code, count])

print(f"Finished! Set counts saved to {OUTPUT_FILE}")
