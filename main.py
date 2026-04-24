from pathlib import Path

# Take file location from the user
def get_file_location():
    file_loc = input("File Location: ")

    while not file_loc.endswith(".txt"):
        print("Sorry, file must be a txt file.")
        file_loc = input("File Location: ")
    return file_loc

# Read content of file
content = None

while content == None:
    file = Path(get_file_location())
    try:
        content = file.read_text()
    except FileNotFoundError:
        print("Sorry, that file cannot be found. It may be missing or be in a differnt location. Please check the file location and spelling before trying again.")

print(content)