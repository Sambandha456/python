correct_password = "ABCD"
number_attempts = 3

while (number_attempts >0):
    user_password = input("Enter your password")
    if (correct_password == user_password):
        print("Correct pin")
        number_attempts = 0
    else:
        number_attempts = number_attempts -1
        if number_attempts >0:
            print("you tried incorrect passowrd")
        else:
            print(" Reached max number of attempts")