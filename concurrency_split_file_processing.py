import json
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from itertools import chain
import time

def read_and_split_file(filename, split_field):
    """Reads the file and splits data based on the split_field."""
    grouped_data = {}
    with open(filename, "r") as file:
        for line in file:
            json_line = json.loads(line.strip())
            key = json_line.get(split_field, "unknown")  # Use "unknown" if field is missing
            if key not in grouped_data:
                grouped_data[key] = []
            grouped_data[key].append(json_line)
    return grouped_data

def count_field(data, column_name):
    """Counts occurrences of a specific field value in the dataset."""
    counts = Counter()
    for json_line in data:
        if column_name in json_line:
            counts[json_line[column_name]] += 1
    return counts

def main():
    filename = "car_org.json"
    split_field = "org"
    count_field_name = "name"

    # Start timing the script
    overall_start_time = time.time()

    # Read and split file
    start_time = time.time()
    grouped_data = read_and_split_file(filename, split_field)
    end_time = time.time()
    print(f"Time to read and split file: {end_time - start_time:.2f} seconds")

    # Concurrent processing with ProcessPoolExecutor
    start_time = time.time()
    with ProcessPoolExecutor() as executor:
        # Process each group concurrently
        futures = {
            org: executor.submit(count_field, data, count_field_name)
            for org, data in grouped_data.items()
        }

        # Gather results
        results = {org: future.result() for org, future in futures.items()}
    end_time = time.time()
    print(f"Time to process data: {end_time - start_time:.2f} seconds")

    # Merge all counts
    total_counts = Counter(chain.from_iterable(results.values()))

    # Print results
    print("Individual group counts:")
    for org, counts in results.items():
        print(f"{org}: {dict(counts)}")
    print("\nTotal counts for all groups:")
    print(dict(total_counts))

    # End timing the script
    overall_end_time = time.time()
    print(f"Total execution time: {overall_end_time - overall_start_time:.2f} seconds")

if __name__ == "__main__":
    main()
