correct_password = "ABCD"
number_attempts = 3
user_password = ""

while (number_attempts >0 correct_password != user_password):
    user_password = input("Enter your password")
    if (correct_password == user_password):
        print("Correct pin")
        number_attempts = 0
    else:
        number_attempts = number_attempts -1
        if number_attempts >0:
            print("you tried incorrect password")
        else:
            print(" Reached max number of attempts")