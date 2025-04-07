user_number = set()
wining_number={10,25,32,41,43,45,50}
prize= 0

while True:
    try:
        if len(user_number) < 7:
            num= int(input("Enter the Seven lottery numbers \n"))
        if num in user_number:
            print("The Number you enter is already here in the list")
            break
        else:
            user_number.add(num)
        if len(user_number)==7:
            break
    except ValueError:
        print("Invalid Data. Please enter number only")

if len(user_number)==7:
    matching_number= user_number.intersection(wining_number)
    count= len(matching_number)
    print(f"The matching numbers are {matching_number}")

if count ==3:
    prize = 4
elif count == 4:
    prize = 15
elif count == 5:
    prize = 200
elif count == 6:
    prize = 30000
elif count ==7:
    prize= 500000


if prize >= 3:
    print(f"You won ${prize}")
else:
    print("Sorry you didn't win anything")
