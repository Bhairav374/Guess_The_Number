import random
winning_no = random.randint(0,100)
for i in range (0,100):
    x = int(input("select the number between 0 to 100: "))
    if x == winning_no:
        print("you won the game")
        print(f"you guessed the number in {i} attempt")
        break
    elif x > winning_no:
        print("Too high")
    else:
        print("Too low")
    i += 1
    
    
    