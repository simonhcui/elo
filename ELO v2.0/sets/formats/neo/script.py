import re
import json


def parse_archetype_file(input_file, output_file):
    data = []

    # Example line:
    # 1   Naya            65.91%   Out of 22 drafts
    pattern = re.compile(
        r"^\s*(\d+)\s+(.+?)\s+(\d+(?:\.\d+)?)%\s+Out of\s+(\d+)\s+drafts\s*$"
    )

    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            match = pattern.match(line)
            if not match:
                print(f"Skipping malformed line: {line}")
                continue

            rank, archetype, winrate, num_drafts = match.groups()

            data.append({
                "rank": rank,
                "archetype": archetype,
                "winrate": f"{float(winrate):.2f}%",
                "num_drafts": num_drafts
            })

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"Wrote {len(data)} records to {output_file}")


if __name__ == "__main__":
    parse_archetype_file("input.txt", "output.json")