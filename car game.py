a = "help"
b = "start"
c = "stop"
d = "exit"
start = False

while True:
    y = input()
    if y.casefold() == a.casefold():
        print('''
    start = to start the car
    stop = to stop the car
    exit = to quit the game''')
    elif y.casefold() == b.casefold():
        if start:
            print("Car already moving")
        else:
            start = True
            print('''The car has started moving''')
    elif y.casefold() == c.casefold():
        if not start:
            print("Car already stopped")
        else:
            start = False
            print('''The car has stopped''')
    elif y.casefold() == d.casefold():
        break
    else:
        print("I dont understand")