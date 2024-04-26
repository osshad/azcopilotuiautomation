import csv


def write_array_to_csv(data, file_name):
    # Open the CSV file for writing
    with open(file_name, "w", newline="", encoding="utf-8") as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write the header row
        header = ["question", "answer", "is_problematic"]
        csv_writer.writerow(header)

        # Write the data rows
        for row in data:
            csv_writer.writerow(row)

    print(f"CSV file '{file_name}' has been written.")
