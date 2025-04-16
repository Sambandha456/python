num = []
while True:
    print("Choose an option")
    print("1. Add Item")
    print ("2. View Inventory")
    print ("3. Calculate total Inventory")
    print("4. Exit")
    user_choice = int(input("Enter the number 1/2/3/4 : "))

    if(user_choice ==1):
        name = input("Enter the name of item : ")
        quantity = int(input("Enter the quantity : "))1
        price = int(input("Enter the price : "))
        num.append ({"name": name, "quantity": quantity, "price": price})
        print(f"Added Item: {name} with quantity:{quantity} and price: ${price}")
    elif ( user_choice == 2):
        for item in num:
            print(f"Item: {item["name"]}, Quantity: {item["quantity"]}, price: {item["price"]}")
    elif(user_choice ==3):
        fix_value= 0
        for item in num:
            fix_value += item["quantity"]*item["price"]
        print(f"The total price is ${fix_value}") 
    else:
            print("thank u for visiting")


