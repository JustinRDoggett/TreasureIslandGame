print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇
choice = input("Do you want to go left or right? ")
if choice == 'right' or choice == 'Right':
  print("You fell into a hole. Game Over!")
elif choice == 'left' or choice == 'Left':
  choice = input("Do you want to swim or wait? ")
  if choice == 'swim' or choice == 'Swim':
    print("You got eaten by a sea monster. Game Over!")
  elif choice == 'wait' or choice == 'Wait':
    choice = input("Which door do you want to go in: Red, Blue, or Yellow? ")
    if choice == 'red' or choice == 'Red':
      print("You got burned by fire. Game Over!")
    elif choice == 'blue' or choice == 'Blue':
      print("You ran into a room full of beasts. Game Over!")
    elif choice == 'yellow' or choice == 'Yellow':
      print("You Win!")
    else:
      print("Game Over!")
      
print("Thank you for playing!")
