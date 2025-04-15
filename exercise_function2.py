def get_price_with_vat(price):
    return price + price *20/100

user_value=int(input("Enter the price \n"))
total = get_price_with_vat(user_value)
print(f"your total is {total}")