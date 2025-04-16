num=[]
while True: 
    user_value= input("Enter a number or press enter to stop")
    if (user_value == ""):
        break
    try:
        num.append(user_value)
    except ValueError:
        print("You cannot enter the Alphabets")

user_choice=input("Do you want to print the max (press 1) or min number (press 2)")
if (user_choice == "1"):
    print(f"Your max value is {max(num)}") 
elif(user_choice == "2"):
    print(f"Your min value is {min(num)}")
    