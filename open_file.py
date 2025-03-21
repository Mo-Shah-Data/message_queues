# count name and org

import json


def read_json_file(filename):
    data = []
    with open(filename, "r") as file:
        for line in file:
            json_line = json.loads(line.strip())
            data.append(json_line)
    return data


def main():
    filename = "car_org.json"
    data = read_json_file(filename)

    print("Complete")
    print(data)


if __name__ == "__main__":
    main()