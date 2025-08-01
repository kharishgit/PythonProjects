import csv
def parse_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader) # Skip header row
            for row in reader:
                try:
                    if int(row[2])>50000:
                        print(row[1])
                except Exception as e:
                    print(e)
    except FileNotFoundError:
        print("No file")

if __name__ == "__main__":
    parse_csv("data.csv")