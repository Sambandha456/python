answer = "tokyo"
user_answer = ""
attempts=5

while True:
    user_answer=input("what is the capital city of Japan? \n")
    if (user_answer==answer):
        print("you are correct")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("incorrect answer")
        else:
            print("reached max attempts")
            break
