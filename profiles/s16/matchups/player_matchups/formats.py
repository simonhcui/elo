import json
import os
from pathlib import Path

def convert_json_files(input_folder: str = ".", output_subfolder: str = "converted"):
    input_path = Path(input_folder)
    output_path = input_path / output_subfolder
    output_path.mkdir(exist_ok=True)

    json_files = [f for f in input_path.iterdir() if f.suffix == ".json" and f.is_file()]

    if not json_files:
        print(f"No JSON files found in '{input_folder}'.")
        return

    for json_file in json_files:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        converted = {"matchups": data}

        output_filename = json_file.name.replace(" ", "").replace("_", "", json_file.name.count("_") - json_file.name.replace(" ", "").count("_"))
        output_filename = "".join(json_file.stem.split()) + json_file.suffix
        output_file = output_path / output_filename

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(converted, f, indent=2, ensure_ascii=False)

        print(f"Converted: {json_file.name} -> {output_file}")

    print(f"\nDone! {len(json_files)} file(s) written to '{output_path}'.")

if __name__ == "__main__":
    convert_json_files()