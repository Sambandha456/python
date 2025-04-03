marks =[]
total = 0

while True:
    user_value= input("Enter the marks \n")
    if (user_value ==""):
            break
    else:
        marks.append (int(user_value))
for mark in marks :
    total = total + mark
length= len(marks)
average = total / length
print(f"You average is {average}")