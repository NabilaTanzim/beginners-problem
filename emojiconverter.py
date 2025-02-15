def emcon(x):
    word = x.split(' ')
    emoji = {
        ":)": "🙂",
        ":(": "🙁",
        "<3": "❤️",
        ":*": "😘",
        "=)": "😊",
        ":/": "🫤",
    }
    output = ""
    for i in word:
        output += emoji.get(i, i) + " "
    return output
