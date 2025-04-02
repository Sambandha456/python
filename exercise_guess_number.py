import random

my_number= random.randint(0 , 100)

while True:
    user_number= int(input("Enter the number between 0 and 100 \n"))
    try: 
        if ( user_number == my_number):
            print("you are correct")
            break
        elif (user_number<my_number):
            print("Guess higher Number")
        else:
            print("Guess Lower Number")
    except ValueError:
        print("invalid value")