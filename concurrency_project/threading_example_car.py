import threading
import time
import json
import os

def read_data(filename, data_list):
    """Reads data from the file and appends it to data_list."""
    with open(filename, 'r') as f:
        for line in f:
            try:
                data_list.append(json.loads(line))
            except json.JSONDecodeError:
                print(f"Warning: Invalid JSON line: {line.strip()}")

def count_organizations(data_list, org_counts):
    """Counts the occurrences of each organization."""
    time.sleep(1) # simulate a small delay.
    for item in data_list:
        org = item.get('org')
        if org:
            org_counts[org] = org_counts.get(org, 0) + 1

def find_unique_names(data_list, unique_names):
    """Finds all unique names in the data."""
    time.sleep(1) # simulate a small delay.
    for item in data_list:
        name = item.get('name')
        if name:
            unique_names.add(name)

def main():
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = os.path.join(parent_dir, 'car_org.json')
    data_list = []
    org_counts = {}
    unique_names = set()

    # Create threads
    thread1 = threading.Thread(target=read_data, args=(filename, data_list))
    thread2 = threading.Thread(target=count_organizations, args=(data_list, org_counts))
    thread3 = threading.Thread(target=find_unique_names, args=(data_list, unique_names))

    # Start threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Wait for threads to finish
    thread1.join()
    thread2.join()
    thread3.join()

    # Print results
    print("Organization Counts:", org_counts)
    print("Unique Names:", unique_names)

if __name__ == "__main__":
    main()