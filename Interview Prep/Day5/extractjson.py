import json
def parse_user_data(filepath):
    try:
        with open(filepath, 'r') as file:
            for line in file:
                try:
                    record = json.loads(line.strip())
                    if record.get("age",0) > 25:
                        print(record.get("name","None"))
                except json.JSONDecodeError as e:
                    print(f"Failed to decode JSON: {e}")
                    continue
    except FileNotFoundError:
        print("File Not found")

parse_user_data("data.txt")