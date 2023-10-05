import time
import random

print ("***Hello, this program acts as a basic coin toss program.***")
print ()
time.sleep(1)

def coin_toss():
     flip = (random.choice(["Heads", "Tails"]))
     print ()
     print ("The coin has been flipped.")
     print ("The result is: " + flip + ".")
     print ()

     retry = input ("Would you like to flip again?: ")
     if (retry == "Yes" or retry == "yes"):
          coin_toss()
     else:
          time.sleep(1)
          print()
          print ("***This program has now concluded. Good-bye.***")   
          print()      
          time.sleep(1)
coin_toss() 
