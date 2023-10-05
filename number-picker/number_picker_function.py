import random
import time

def number_picker():

    mode = input ("""Please make a selection: 
    
    A. Single.
    B. Versus.
    C. Return to Main Menu.
    
    Your Selection: """)

    def single():
        print ()
        print ("A number is being chosen...")
        print ()
        number = random.randrange(1, 1000, 1)
        time.sleep(1)
        print ("The number has been chosen.")
        print ()
        print ("The number that was chosen was: "+ (str(number)) + ".")
        again = input ("Would you like to have another number chosen?: ")
        if (again == "Yes" or again == "yes"):
            single()
        else:
            print ()
            games()
    
    def versus ():
        choice = input ("Please choose your number in numeric value between 1 and 1000.: ")
        number = random.randrange(1, 1000, 1)
        time.sleep(1)
        print ()
        if not choice.isnumeric():
            print ("Please only use numeric values")
            versus()
        elif (number > int(choice)):
            print ("A number has been chosen by the computer. The computer chose: " + str(number) + ".")
            print ()
            time.sleep(1)
            print ("The computer has chosen the higher number. You Lose!")
            print ()
        elif (number < int(choice)):
            print ("A number has been chosen by the computer. The computer chose: " + str(number) + ".")
            print ()
            time.sleep(1)
            print ("The player has chosen the higher number. You Win!")
            print ()
        elif (number == int(choice)):
            print ("A number has been chosen by the computer. The computer chose: " + str(number) + ".")
            print ()
            time.sleep(1)
            print ("The player and the computer have chosen the same number. It's a draw!")
            print ()
        else:
            print ("A valid choice was not made. Please try again.")
            versus()
        again = input ("""Would you like to play again?
        
        Yes
        No
        
        Your Selection: """)
        print ()
        if (again == "Yes" or again == "yes"):
            versus()
        elif (again == "No" or again == "no"):
            number_picker()
        else:
            print ("""
            *********************************
            Invalid entry. Returning to Menu.
            *********************************
            """)
            number_picker()
    
    if (mode == "A" or mode == "a"):
        single()
    elif (mode == "B" or mode == "b"):
        versus()
    elif (mode == "C" or mode == "c"):
        exit
        
games()