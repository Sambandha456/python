correct_pin = 5566
total_amount= 500
attempt = 3

while True:
    user_pin= int(input("Enter your pin"))
    if (user_pin == correct_pin):
        print("Correct pin")
        break
    else:
        attempt = attempt -1
        print(f"Incorrect pin. You have {attempt} attempt(s) left.")
while True:    
    print("Choose an option")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Blance")
    print("4. Exit")
    user_choice=int(input("Enter your choice 1/2/3/4 :"))
    if (user_choice == 2 ):
        user_amount=int(input("Enter the amount your want to withdraw"))
        if (user_amount<=total_amount):
            print("Withdraw on process")
            break
        else:
            print("insufficient amount")
    elif (user_choice ==3):
        print(f"The amount you have is ${total_amount}")
    elif (user_choice ==4):
        print("Thanks you")
    else:
        print("Invalid number")


