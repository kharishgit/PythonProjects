import csv
def parse_csv(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if int(row[2])>50000:
                    print(row[1])
    except FileNotFoundError:
        print("No file")

if __name__ == "__main__":
    parse_csv("/Users/harishk/PycharmProjects/pythonProject/Interview Prep/data.csv")