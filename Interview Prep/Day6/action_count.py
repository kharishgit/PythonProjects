def count_actions(file_path):
    try:
        with open(file_path,'r') as file:
            data = file.read()
            sent =data.split('\n')
            freq ={}
            for w in sent:

                chk =w.split()
                freq[chk[2]]=freq.get(chk[2],0)+1
            result = '\n'.join(f'{key}:{value}' for key, value in freq.items())
            return result

    except FileNotFoundError:
        print("File Not Found")

count_actions("logs.txt")






def count_actions(file_path):
    try:
        freq = {}
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 3:  # Ensure valid format
                    action = parts[2]
                    freq[action] = freq.get(action, 0) + 1
        if not freq:
            return "No valid actions found"
        return '\n'.join(f'{key}:{value}' for key, value in sorted(freq.items()))
    except FileNotFoundError:
        return "File not found!"

# Test cases (create logs.txt with sample data)
print(count_actions("logs.txt"))