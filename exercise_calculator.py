num1= float(input("Enter the First Number: "))
num2= float(input("Enter the Second Number: "))
operate = input("Enter the operation: ")

if(operate == "+"):
    calculation= num1 + num2
elif(operate == "-"):
    calculation = num1 - num2
elif ( operate ==  "*"):
    calculation = num1 * num2
else:
    calculation = num1 / num2
print(f"Your result is {calculation}")