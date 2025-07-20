# Validate Dates in a String
#
# Description: You’re given a text file dates.txt containing dates in the format DD-MM-YYYY, one per line.
# Write a Python script to read the file and print only the valid dates. A date is valid if:
#
#     Day is between 1 and 31 (assume all months have 31 days for simplicity).
#     Month is between 1 and 12.
#     Year is between 1900 and 2099. Handle invalid formats or values gracefully.

def validate_dates(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    day, month, year = map(int, line.strip().split('-'))
                    if 1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2099:
                        print(line.strip())
                except ValueError:
                    continue  # Skip invalid formats or non-numeric values
    except FileNotFoundError:
        print("File not found!")

# Test
validate_dates("dates.txt")