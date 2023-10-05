print ("Hello, this program acts as a basic rock, paper, scissors game.")

import random

def rock_paper_scissors():

    cpu = (random.choice(["Rock", "Paper", "Scissors"]))

    choice = input ("""
    Please make your selection:
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
        
    again = input ("Would you like to play again?: ")
    if (again == "Yes" or again == "yes"):
        rock_paper_scissors()
    else:
        print ("""
**********************
Thank you for playing.
**********************""")
        print ()
        exit
        
rock_paper_scissors()