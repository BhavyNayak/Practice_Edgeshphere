# 94. Create a number guessing game.
import random 
def number_gussing():
    actual=random.randint(1,5)
    g=int(input("enter a no. in range 1 to 5 : "))
    if actual==g:
        print("you guess perfect ")
    else:
        print(f"sorry try again cause no was{actual}")
        number_gussing()
number_gussing()