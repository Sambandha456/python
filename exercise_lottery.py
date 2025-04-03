user_number = set()

while True:
    user = int(input("Enter the Number: "))
    if user in user_number:
        print("Error")
        break
    else:
        user_number.add(user)
    if len(user_number) >= 7:
        for num in user_number:
            print(f"The numbers are {num}")
        break

        