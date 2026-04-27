from pathlib import Path

# Find and load the english dictionary file
eng_file = Path("english_dict.txt")

while not eng_file.exists():
    print("The english dictionary file could not be located. Please check the file location and enter it here:\n")
    eng_file = input(">")

eng_dict = eng_file.read_text()
eng_dict = eng_dict.splitlines()

# Check words against english
def check_english(words):
    matches = 0
    fails = []
    for word in words:
        if word.lower() in eng_dict:
            matches += 1
        else:
            fails.append(word)
    percentage = (matches*100)/len(words)
    return matches, percentage, fails

if __name__ == "__main__":
    words = ["test", "Hello", "WORLD", "jslscm", "Alice"]
    matches, percentage, fails = check_english(words)
    print(f"{matches}/{len(words)} matched ({percentage:.2f}%)\nFailed Words:")
    for f in fails:
        print(f)