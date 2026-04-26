# This module processes the content by splitting it into its components

# Decorator function that makes function return list of unique values
def unique(items):
    unique_items = list(set(items))
    return unique_items

# Decorator to return dictionary of values and the number of occurences
def count(items, min=1):
    counts = {}
    for item in unique(items):
        if items.count(item) >= min:
            counts[item] = items.count(item)
    return counts

# Take content and return list of seperate lines
def get_lines(content):
    lines = content.splitlines()
    return lines

# Take content and return list of words
def get_words(content):
    words = content.replace("\n", " ").split(" ")
    return words

def get_characters(content):
    chars = list(content.replace("\n", " "))
    return chars

if __name__ == "__main__":
    msg = "hello world how are you world"
    lines = get_lines(msg)
    unique_lines = unique(lines)
    words = get_words(msg)
    unique_words = unique(words)
    word_counts = count(unique_words)
    chars = get_characters(msg)
    unique_chars = unique(chars)
    char_counts = count(unique_chars)
    print(lines)
    print(words)
    print(unique_words)
    print(word_counts)
    print(chars)
    print(unique_chars)
    print(char_counts)