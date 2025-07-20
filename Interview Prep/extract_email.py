import re

def extract_emails(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            # Find emails with regex
            emails = re.findall(r'[a-zA-Z0-9._]+@[a-zA-Z0-9.]+\.com', text)
            for email in emails:
                print(email)
    except FileNotFoundError:
        print("File not found!")

# Test
extract_emails("email.txt")