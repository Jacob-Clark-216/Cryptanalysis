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


# Split the content into individual lines
lines = content.splitlines()

# Replace all newline characters with spaces and then split the content at any spaces to get a list of words
words = content.replace("\n", " ").split(" ")

# Record Characters
chars = list(content.replace("\n", ""))
unique_chars = set(content.replace("\n", " "))

# Identify character counts
char_counts = {}
for c in unique_chars:
    char_counts[c] = content.count(c)
# Calculate character frequency
char_frequency = {}
for c in unique_chars:
    char_frequency[c] = (char_counts[c]*100)/len(chars)

# Provide Output
output = "\n\nFile contains:\n"
output += f"{len(lines)} lines\n"
output += f"{len(words)} words\n"
output += f"{len(chars)} non-whitespace characters\n\n"
output += f"{len(unique_chars)} Unique Characters Found: {unique_chars}\n\n"
output += f"Character stats:\n"
for i in char_counts:
    output += f"{i} | {char_counts[i]} | {char_frequency[i]:.2f}%\n"
print(output)

# print(f"{content}\n")
# print(f"{lines}\n")
# print(f"{words}\n")