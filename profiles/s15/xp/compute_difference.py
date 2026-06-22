import csv

def read_csv_to_dict(filename):
    data = {}
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) < 2:
                continue  # skip invalid rows
            name = row[0].strip()
            try:
                value = float(row[1])
            except ValueError:
                value = 0.0
            data[name] = value
    return data

def compute_differences(file1, file2, output_file):
    data1 = read_csv_to_dict(file1)
    data2 = read_csv_to_dict(file2)

    all_names = set(data1.keys()).union(data2.keys())

    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        for name in all_names:
            val1 = data1.get(name, 0.0)
            val2 = data2.get(name, 0.0)
            difference = val1 - val2
            writer.writerow([name, difference])

if __name__ == "__main__":
    file1 = "experience.csv"
    file2 = "experience_last.csv"
    output = "output.csv"

    compute_differences(file1, file2, output)
    print(f"Output written to {output}")