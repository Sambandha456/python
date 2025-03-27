user_choice = int(input("Press the number for the meal: "))

if (user_choice == 1):
    print(" Burger : $10")
elif ( user_choice == 2):
    print("Pizza : $12")
elif (user_choice == 3):
    print(" Sushi : $15")
else :
    print("Invalid Number")

guest_number = int(input("Enter the Number of Guest: "))

total_price= None;
if (user_choice == 1):
    total_price = guest_number * 10
elif ( user_choice == 2):
    total_price = guest_number * 12
else:
    total_price = guest_number * 15
print(f"Your total without Discount {total_price}")

if (total_price >= 100):
    new_total= total_price - 0.1 * total_price
    print(f"Your Total after discount is {new_total}")
elif (total_price >= 200):
    new_total = total_price - 0.2 * total_price
    print(f"Your Total after discount is {new_total}")
else: 
    print(f"Sorry, You are not eligible for discount and your total is {total_price}")