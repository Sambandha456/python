age = int(input("Enter the age"))

if(age >= 18):
    ticket_price = 10
elif (age >= 4 & age < 18):
    ticket_price = 8
else:
    ticket_price = 5
print(f"${ticket_price}")