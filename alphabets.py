alphabets = {
    "english": "abcdefghijklmnopqrstuvwxyz",
    "greek": "αβγδεζηθικλμνξοπρσςτυφχψω",
    "cyrillic": "абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
    "punctuation": r".,><?!'£$%^&*()#~`¬|[]}\{=+-_" + '"'}

msg = "hello world"

def check_alphabets(letters):
    present_alphabets = {}
    for l in letters:
        for a in alphabets:
            if l in alphabets[a]:
                present_alphabets[a] = True
            else:
                present_alphabets[a] = False
    return present_alphabets


if __name__ == "main":
    print(check_alphabets(msg))    