import json
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import time

def count_field(data, column_name):
    """Counts occurrences of the specified field in the data."""
    counts = Counter()
    for json_line in data:
        if column_name in json_line:
            counts[json_line[column_name]] += 1
    return counts

def read_json_file(filename):
    """Reads a file containing newline-delimited JSON."""
    data = []
    with open(filename, "r") as file:
        for line in file:
            json_line = json.loads(line.strip())
            data.append(json_line)
    return data

def main():
    filename = "car_org.json"

    # Start timing the script
    overall_start_time = time.time()

    # Reading the JSON file
    start_time = time.time()
    data = read_json_file(filename)
    end_time = time.time()
    print(f"Time to read JSON file: {end_time - start_time:.2f} seconds")

    # Using ThreadPoolExecutor for concurrency
    start_time = time.time()
    with ThreadPoolExecutor() as executor:
        future_name = executor.submit(count_field, data, "name")
        future_org = executor.submit(count_field, data, "org")

        name_counts = future_name.result()
        org_counts = future_org.result()
    end_time = time.time()
    print(f"Time to process data: {end_time - start_time:.2f} seconds")

    # Print results
    print("Counts for 'name' field:")
    print(dict(name_counts))
    print("\nCounts for 'org' field:")
    print(dict(org_counts))

    # End timing the script
    overall_end_time = time.time()
    print(f"Total execution time: {overall_end_time - overall_start_time:.2f} seconds")

if __name__ == "__main__":
    main()
