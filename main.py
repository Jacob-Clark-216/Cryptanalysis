from pathlib import Path
import content_processor as cp

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

print("Processing Lines...")
lines = cp.get_lines(content)
unique_lines = cp.unique(lines)
print("Processing Words...")
words = cp.get_words(content)
unique_words = cp.unique(words)
word_counts = cp.count(unique_words)
print("Processing Characters")
chars = cp.get_characters(content)
unique_chars = cp.unique(chars)
char_counts = cp.count(chars)

# Provide Output
output = "\n\nFile contains:\n"
output += f"{len(lines)} lines\n"
output += f"{len(words)} words ({len(unique_words)} unique)\n"
output += f"{len(chars)} characters\n\n"
output += f"{len(unique_chars)} Unique Characters Found: {unique_chars}\n\n"
output += f"Character stats:\n"
for i in char_counts:
    output += f"{i} | {char_counts[i]} ({(char_counts[i]*100)/len(chars):2.2f}%)\n"
print(output)

# print(f"{content}\n")
# print(f"{lines}\n")
# print(f"{words}\n")