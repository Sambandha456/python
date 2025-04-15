games=[
    {"names": "GTA v", "minimum_age" : 18},
    {"names": "Minecraft", "minimum_age" : 7},
    {"names": "Call Of Duty", "minimum_age" : 12},
    {"names": "Animal Crossing", "minimum_age" : 3}
]

def check_age (game_age,user_age):
    return user_age >= game_age

user_age= int(input("Please, Enter Your age \n"))

for game in games:
    if check_age(game["minimum_age"],user_age):
        print(f"you can play {game["names"]}")
    else:
        print(f"You cannot play {game["names"]}")
    