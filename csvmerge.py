import csv


def mergecsv(csv_list, output_path):

    fieldnames = []

    for file in csv_list:
        with open(file, "r", encoding="utf-8") as input_file:
            reader = csv.DictReader(input_file)
            fieldnames.extend(reader.fieldnames)

    # fieldnames = list(set(fieldnames))  # Remove duplicates

    with open(output_path, "w", encoding="utf-8", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list(fieldnames))
        # Header
        writer.writeheader()

        # Row data
        for file in csv_list:
            with open(file, "r", encoding="utf-8") as input_file:
                reader = csv.DictReader(input_file)
                for row in reader:
                    writer.writerow(row)


mergecsv(["file1.csv", "file2.csv"], "merged_output.csv")
