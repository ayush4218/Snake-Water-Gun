import random

# Snake Water Gun Gauss and Check your Luck
def gameWin(comp, you):
    # If two values are equal, declareing tie!
    if comp == you:
        return None

    # Checking the  possibilities when computer chosen - 's'
    elif comp == 's':
        
        if you=='w':
            return False
        elif you=='g':
            return True
    
    # Checking the possibilities when computer chosen - 'w'
    elif comp == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    
    # Checking the possibilities when computer chosen - 'g'
    elif comp == 'g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("Comp Turn: Snake('s') Water('w') or Gun('g')?")
randNo = random.randint(1, 3) 
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")