# computer itself gives number form random built in key.
from random import randint
a = []
for i in range(0,5):
    a.append(["O"]*5)

def done_a(a):
    for row in a:
        print(" ".join(row))
done_a(a)

def row(a):
    return randint(0, len(a)-1)

def col(a):
    return randint(0, len(a)-1)

ship_row = row(a)
ship_col = col(a)
print (ship_row)
print (ship_col)
for turn in range(10):
    print()
    print("Turn", turn +1)
    choice_row = int(input("choice_row :"))
    choice_col = int(input("choice_col :"))
    print()


    if ship_row == choice_row and ship_col == choice_col:
        print("You are able to find the battleship.")
        break
    else:
        if choice_row not in range(5) or choice_col not in range(5):
            print ("Thats not even in the ocean:")
        elif(a[choice_row][choice_col]=="X"):
            print ("You guessed that one already")
        
        else:
            print("You are not able to find the battleship.")
            print("Your answer is and notice index starts form 0.")
            a[choice_row][choice_col]="X"
            
        if (turn ==9):
            print ("Game over")
            print(done_a(a))

