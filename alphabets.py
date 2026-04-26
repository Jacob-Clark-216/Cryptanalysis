alphabets = {
    "english": "abcdefghijklmnopqrstuvwxyz",
    "greek": "αβγδεζηθικλμνξοπρσςτυφχψωάέήίόύώ",
    "cyrillic": "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
    "punctuation": r".,><?!'£$%^&*()#~`¬|[]}\{=+-_" + '"',
    "arabic numerals": "1234567890"
    }


def check_alphabets(letters):
    present_alphabets = {"english": False, "greek": False, "cyrillic": False, "punctuation": False}
    for l in letters:
        for a in alphabets:
            if l in alphabets[a]:
                present_alphabets[a] = True
                break
    return present_alphabets


if __name__ == "__main__":
    msg = "hello world κ"
    present_alphabets = check_alphabets(msg)
    for i in present_alphabets:
        if present_alphabets[i] == True:
            print(i)