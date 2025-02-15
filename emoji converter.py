while(True):
    x = input(">")
    word = x.split(' ')
    emoji = {
        ":)" : "🙂",
        ":(" : "🙁",
        "<3" : "❤️",
        ":*" : "😘",
        "=)" : "😊",
        ":/" : "🫤",
    }
    output = ""
    for i in word:
        output += emoji.get(i,i) + " "
    print(output)
