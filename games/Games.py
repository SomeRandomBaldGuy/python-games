#This program acts as a small selection of mini games. 
#See each function section notes for more details.

import time
import random

print ("""
***********************************************************
Welcome to my program. It offers a few small games to play.
***********************************************************
""")

#############################################################################################################
#This function makes use of 5 smaller functions which get chosen from based on user input.
def games():

    choice = input ("""
    **************************
    What would you like to do?
    **************************
    
    A. Roll a Dice.
    B. Flip a Coin.
    C. Pick a Color.
    D. Pick a Number.
    E. Play Rock Paper Scissors.
    F. Quit
    
    Your Choice: """)
    
    print ()
    time.sleep(1)
#############################################################################################################
#This section defines the dice roll function which uses 2 functions. 
#One function is for single die play and another for multiple. 
    def dice_roll():
        mode = input ("""
    *******************************
    How many dice you like to roll?
    *******************************

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
            again = input ("""
    ******************************
    Would you like to roll again?: 
    ******************************
            
    Yes
    No
            
    Your Selection: """)
            if (again == "Yes" or again == "yes"):
                dice_roll()
            elif (again == "No" or again == "no"):
                print ()
                games()
            else:
                print ("Invalid Entry. Returning to Menu.")
                

            
        def multiple():
            amount = input ("""
    **************************************
    How many dice would you like to roll?:
    **************************************
            
    Two
    Three
    Four
            
    Your Selection: """)
            print ()
            
            if not choice.isalpha():
               print ("""
    ******************************
    Please make a valid selection.
    ******************************
          """)

            elif (amount == "Two" or amount == "two"):
                for i in range(2): 
                    number = random.randrange(1, 6, 1)
                    print ("The dice has rolled a: " + str(number) + ".")
            elif (amount == "Three" or amount == "Three"):
                for i in range(3): 
                    number = random.randrange(1, 6, 1)
                    print ("The dice has rolled a: " + str(number) + ".")
            elif (amount == "Four" or amount == "four"):
                for i in range(4): 
                    number = random.randrange(1, 6, 1)
                    print ("The dice has rolled a: " + str(number) + ".")
            else:
                print ("Please make another selection.")
                multiple()
                
            again = input ("""
    ******************************
    Would you like to roll again?:
    ******************************
            
    Yes
    No
            
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
            print("""
    *********************************
    Invalid Entry. Returning to Menu.
    *********************************
            """)
            dice_roll()
#############################################################################################################
#This section defines the coin flip function which uses 2 functions.
#One function acts a a single coin flip and another acts as a player vs cpu mode.
    def coin_flip():
        mode = input ("""
    ***************************
    What would you like to do?: 
    ***************************
        
    A. Flip a coin.
    B. Versus.
    C. Return to Main Menu.

    Your Choice: """)

        def single():
            coin = (random.choice(["Heads", "Tails"]))
            print ()
            print ("The coin is being flipped...")
            print ()
            time.sleep(1)
            print ("The side it landed on is: " + coin + ".")
            again = input ("""
    ******************************
    Would you like to flip again?:
    ******************************
            
    Yes
    No
                        
    Your Selection: """)
            if (again == "Yes" or again == "yes"):
                single()
            else:
                print ()
                coin_flip()
            
        def versus():
            choice  = input ("""
    ************************
    Please choose your side:
    ************************
            
    Heads
    Tails
            
    Your Choice: """)
            
            coin = (random.choice(["Heads", "Tails"]))
            print ()
            print ("The coin is being flipped...")
            print ()
            time.sleep(1)
            if (choice == "Heads" or choice == "heads") and (coin == "Heads"):
                print ("It's heads! You Win!")              
            elif (choice == "Tails" or choice == "tails") and (coin == "Tails"):
                print ("It's tails! You Win!")
            elif (choice == "Heads" or choice == "heads") and (coin == "Tails"):
                print ("It's tails! You Lose!")
            elif (choice == "Tails" or choice == "tails") and (coin == "Heads"):
                print ("It's heads! You Lose!")
            else:
                print ("A valid choice was not made. Please Try again.")
                versus()
            again = input (""""
    ******************************
    Would you like to flip again?:
    ******************************
            
    Yes 
    No
            
    Your Selection: """)
            
            if (again == "Yes" or again == "yes"):
                versus()
            else:
                coin_flip() 
                
        if (mode == "A" or mode =="a"):
            single()
        elif (mode == "B" or mode == "b"):
            versus()
        elif (mode == "C" or mode == "c"):
            games()
        else:
            print ("Please make a valid selection")
            print ()
            time.sleep(1)
            coin_flip()
#############################################################################################################
#This section defines the color picker function.
#This function currently only has one option to provide a single color when ran.
    def color_picker():

         mode = input ("""
    ***********************************************
    How many colors would you like to have picked?:
    ***********************************************

    Single
    Multiple

    Your Selection:  """)

         def single():
              print ("A color is being chosen...")
              print ()
              color = (random.choice(["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Black", "White"]))
              time.sleep(1)
              print ("The color that was picked is: " + color + ".")
              again = input ("""
    *********************************************
    Would you like to have another color picked?: 
    *********************************************
  
    Yes
    No
             
    Your Selection: """)
             
              if (again == "Yes" or again == "yes"):
                   color_picker()
              else:
                   print ()
                   games()

         def multiple():
              choice = input ("""

    ***************************************
    How many colors would you like to pick?
    ***************************************
    Two
    Three
    Four

    Your Selection: """)
              print ()
    
              if not choice.isalpha():
                   print ("""
    ******************************
    Please make a valid selection.
    ******************************
          """)

              elif (choice == "Two" or choice == "two"):
                   for i in range(2):
                        color = (random.choice(["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Black", "Gray", "White"]))
                        print ("The color chosen is: " + color + ".")
              elif (choice == "Three" or choice == "three"):
                   for i in range(3):
                        color = (random.choice(["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Black", "Gray", "White"])) 
                        print ("The color chosen is: " + color + ".")
              elif (choice == "Four" or choice == "four"):
                   for i in range(4):
                        color = (random.choice(["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Black", "Gray", "White"])) 
                        print ("The color chosen is: " + color + ".")
              else:
                   print ("""
    ******************************
    Please make a valid selection.
    ******************************
          """)
                   multiple()

              again = input ("""
    *************************************************
    Would you like to have another color set picked?: 
    *************************************************
             
    Yes
    No
             
    Your Selection: """)
             
              if (again == "Yes" or again == "yes"):
                   color_picker()          
              else:
                   print ()
                   games()

         if (mode == "Single" or mode == "single"):
              single()
         elif (mode == "Multiple" or mode == "multiple"):
              multiple()
         else:
              print ("""
    ******************************
    Please make a valid selection.
    ******************************
          """)
              color_picker()
#############################################################################################################
#This section defines the number picker function which uses 2 functions.
#One function for a random number generator and another acts as a player vs cpu mode.
    def number_picker():

        mode = input ("""
    ************************
    Please make a selection: 
    ************************
        
    A. Single.
    B. Versus.
    C. Return to Main Menu.
        
    Your Selection: """)

        def single():
            print ()
            print ("A number is being chosen...")
            print ()
            number = random.randrange(1, 1000000, 1)
            time.sleep(1)
            print ("The number that was chosen was: "+ (str(number)) + ".")
            again = input ("""
    **********************************************
    Would you like to have another number chosen?: 
    **********************************************
            
    Yes
    No
            
    Your Selection: """)
            
            if (again == "Yes" or again == "yes"):
                single()
            else:
                print ()
                games()
        
        def versus ():
            print ()
            choice = input ("""
    **************************************************************
    Please choose your number in numeric value between 1 and 1000.
    **************************************************************
              
            Your Selection: """)
            
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
            again = input ("""
    *****************************
    Would you like to play again?
    *****************************
            
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
            games()
#############################################################################################################
#This section define the rock paper scissors function.
#This section only has one mode currently where the player goes against the cpu.
    def rock_paper_scissors():

        cpu = (random.choice(["Rock", "Paper", "Scissors"]))

        choice = input ("""
    ***************************
    Please make your selection:
    ***************************
      
    Rock
    Paper
    Scissors
        
    Your Selection: """)
             
        if (cpu == "Rock") and (choice == "Scissors" or choice == "scissors"):
            print ("Rock beats Scissors. You Lose!")
        elif (cpu == "Paper") and (choice == "Rock" or choice == "rock"):
            print ("Paper covers Rock! You Lose!")    
        elif (cpu == "Scissors") and (choice == "Paper" or choice == "paper"):
            print ("Scissors beats Paper! You Lose!")
        elif (cpu == "Rock") and (choice == "Paper" or choice == "paper"):
            print ("Paper covers Rock! You Win!")
        elif (cpu == "Paper") and (choice == "Scissors" or choice == "scissors"):
            print ("Scissors cuts paper! You Win!")
        elif (cpu == "Scissors") and (choice == "Rock" or choice == "rock"):
            print ("Rock smashes Scissors! You Win!")
        elif (cpu == "Rock") and (choice == "Rock" or choice == "rock"):
            print ("It's a draw!. Try Again!")
        elif (cpu == "Paper") and (choice == "Paper" or choice == "paper"):
            print ("It's a draw!. Try Again!")   
        elif (cpu == "Scissors") and (choice == "Scissors" or choice == "scissors"):
            print ("It's a draw!. Try Again!")
        else:
            print ("""
    ****************************
    A valid choice was not made.
    ****************************""")
            rock_paper_scissors()
        
        again = input ("""
    ******************************
    Would you like to play again?: 
    ******************************
        
    Yes
    No
        
    Your Selection: """)
        
        if (again == "Yes" or again == "yes"):
            rock_paper_scissors()
        else:
            print ()
            games()
#############################################################################################################

    if not choice.isalpha():
        print ("Please only use letter values.")
        games()
    elif (choice == "A" or choice == "a"):
        dice_roll()
    elif (choice == "B" or choice == "b"):
        coin_flip()
    elif (choice == "C" or choice == "c"):
        color_picker()
    elif (choice == "D" or choice == "d"):
        number_picker()
    elif (choice == "E" or choice == "e"):
        rock_paper_scissors()
    elif (choice == "F" or choice == "f"):
        print ("""
*************************************
The program will now close. Good-bye.
*************************************
        """)
        exit
    else:
        print ("""
    ******************************
    Please make a valid selection.
    ******************************
        """)
        games()
games()
