import time
import random

print ()
print ("***Hello, this program will pick a random color for you.***")
print ()
time.sleep(1)

def color_picker():

     mode = input ("""How many colors would you like to have picked?:

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
     How many colors would you like to pick?

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
                    color = (random.choice(["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Black", "White"]))
                    print ("The color has been chosen, the color is: " + color + ".")
          elif (choice == "Three" or choice == "Three"):
               for i in range(3):
                    color = (random.choice(["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Black", "White"])) 
                    print ("The color has been chosen, the color is: " + color + ".")
          elif (choice == "Four" or choice == "Four"):
               for i in range(4):
                    color = (random.choice(["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Black", "White"])) 
                    print ("The color has been chosen, the color is: " + color + ".")
          else:
               print ("""
          ******************************
          Please make a valid selection.
          ******************************
          """)

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
color_picker()


