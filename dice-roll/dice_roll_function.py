import random
import time

def dice_roll():
    mode = input ("""How many dice you like to roll?

    A. Single.
    B. Multiple.
    C. Return to Main Menu.

    Your Selection: """)

    def single():
        print ("The dice is being rolled...")
        print ()
        dice = random.randrange(1, 6, 1)
        time.sleep (1)
        print ("The dice has been rolled.")
        print ()
        print ("The number rolled was: " + (str(dice)) + ".")
        again = input ("Would you like to roll again?: ")
        if (again == "Yes" or again == "yes"):
            dice_roll()
        elif (again == "No" or again == "no"):
            print ()
            exit
        else:
            print ("Invalid Entry. Returning to Menu.")
            

        
    def multiple():
        amount = input ("""How many dice would you like to roll?:
        
        Two
        Three
        Four
        
        Your Selection: """)
        
        if (amount == "Two" or amount == "two"):
            i = 2 
            for i in range(2): 
                number = random.randrange(1, 6, 1)
                print ("The dice has rolled a: " + str(number) + ".")
        elif (amount == "Three" or amount == "Three"):
            i = 3 
            for i in range(3): 
                number = random.randrange(1, 6, 1)
                print ("The dice has rolled a: " + str(number) + ".")
        elif (amount == "Four" or amount == "four"):
            i = 4 
            for i in range(4): 
                number = random.randrange(1, 6, 1)
                print ("The dice has rolled a: " + str(number) + ".")
        else:
            print ("Please make another selection.")
            multiple()
            
        again = input ("""Would you like to roll again?:
        
        A.Yes
        B.No
        
        Your Selection: """)
        
        if (again == "Yes" or again == "yes"):
            multiple()
        elif (again == "No" or again == "no"):
            dice_roll()
        else:
            print ("Invalid Entry. Returning to Menu.")
            dice_roll()
            
    if (mode == "A" or mode == "a"):
        single()
    elif (mode == "B" or mode == "b"):
        multiple()
    elif (mode == "C" or mode =="c"):
        games()
    else:
        print("Invalid Entry. Returning to Menu.")
        dice_roll()
dice_roll()