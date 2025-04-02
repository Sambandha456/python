games =[]

while True:
    user_game= input("Enter your favorite games")
    if (user_game == ""):
        for game in games:
            print(game)
        break
    else:
         games.append(user_game)

    