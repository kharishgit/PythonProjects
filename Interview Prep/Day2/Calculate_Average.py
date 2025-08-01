

def calculate_average(file_path):
    total=0
    count=0
    try:
        with open(file_path,'r') as file:
            for line in file:
                try:
                    num=int(line.strip())
                    total+=num
                    count+=1
                except Exception as e:
                    continue
            if count==0:
                return "No valid Data"
            return f"{total/count:.2f}"
    except FileNotFoundError:
        return "File Not Found"

if __name__ == '__main__':
    print(calculate_average("numbers.txt"))
