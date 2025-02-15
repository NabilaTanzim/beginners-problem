num = 9
i = 0
while i < 3:
    x=int(input(f'Guess {i+1}: '))
    i+=1
    if(x == num):
        print("Congratulations!!")
        break
else:
    print("Game over")