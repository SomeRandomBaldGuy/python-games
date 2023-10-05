import time
import random

def coin_flip():
    mode = input ("""What would you like to do?: 
    
    A. Versus.
    B. Flip a coin.
    C. Return to Main Menu.

    Your Choice: """)
        
    def versus():
        choice  = input ("""Please choose your side:
        
        Heads
        Tails
        
        Your Choice: """)
        
        coin = (random.choice(["Heads", "Tails"]))
        print ("The coin is being flipped...")
        print ()
        time.sleep(1)
        print ("The coin has been flipped.")
        print ()
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
        again = input ("Would you like to flip again?: ")
        if (again == "Yes" or again == "yes"):
            versus()
        else:
            coin_flip() 

    
    def single():
        coin = (random.choice(["Heads", "Tails"]))
        print ("The coin is being flipped...")
        print ()
        time.sleep(1)
        print ("The coin has been flipped.")
        print ()
        print ("The side it landed on is: " + coin + ".")
        again = input ("Would you like to flip again?: ")
        if (again == "Yes" or again == "yes"):
            single()
        else:
            print ()
            coin_flip()
            
    if (mode == "A" or mode =="a"):
        versus()
    elif (mode == "B" or mode == "b"):
        single()
    elif (mode == "C" or mode == "c"):
        exit
    else:
        print ("Please make a valid selection")
        print ()
        time.sleep(1)
        coin_flip()
            
coin_flip()