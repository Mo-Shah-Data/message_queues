import json
import random

def generate_jsonl_data(num_entries=10000):
    """Generates JSON Lines data with specified constraints."""
    data = []
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"]
    orgs = ["Nissan", "Toyota", "Honda", "Ford", "GM"]

    for _ in range(num_entries):
        entry = {
            "id": random.randint(1, 20),  # ID between 1 and 20
            "name": random.choice(names),  # Name from the list of 10 names
            "org": random.choice(orgs)  # Org from the list of 5 orgs
        }
        data.append(json.dumps(entry))  # Convert each entry to a JSON string

    return data

def write_jsonl_file(data, filename="data.jsonl"):
    """Writes JSON Lines data to a file."""
    with open(filename, "w") as f:
        for line in data:
            f.write(line + "\n")  # Write each JSON string as a line

# Generate and write the data
jsonl_data = generate_jsonl_data()
write_jsonl_file(jsonl_data)

print("data.jsonl created with 10000 lines, adhering to the specified constraints.")