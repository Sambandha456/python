products=[
    {"name":"Dell Laptop", "price":400},
    {"name":"Door Handel", "price":49},
    {"name":"Watch", "price":100},
    {"name":"Earbuds", "price":59}
]
couriers=[
    {"name":"National Post", "price":5},
    {"name":"DHL", "price":8},
    {"name":"DHL Express", "price":10},
    {"name":"La postale", "price":6}    
]
for index, product in enumerate(products):
    print(f"Index: {index}   - Name: {product["name"]} - Price: {product["price"]}")

while True:
    user_choice = int(input("Press the number that u want to purchase"))
    try:
        if user_choice < len(products) and user_choice >=0:
            break
        else:
            print("The number you entered doesnot exist")
    except ValueError:
        print("Enter the Numbers only")

choosen_product=products[user_choice]
print(f"You chose the Name: {choosen_product["name"]}- Price: {choosen_product["price"]}")

for index, courier in enumerate(couriers):
    print(f"Index: {index}   - Name: {courier["name"]} - Price: {courier["price"]}")
while True:
    try:
        user_choices = int(input("Press the number that u want to for delivery"))
        if user_choices < len(couriers) and user_choices >=0:
            break
        else:
            print("The number you entered doesnot exist")
    except ValueError:
        print("Enter the Numbers only")

choosen_courier=couriers[user_choices]
print(f"You chose the Name: {choosen_courier["name"]}- Price: {choosen_courier["price"]}")
total = choosen_courier["price"]+ choosen_product["price"]
print(f"Your total price is ${total}")



