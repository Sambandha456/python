games=[
    {"name":"Clash of Clans","editor":"John Doe","year":2010}
]

name_input_new_game=input("Enter the name of the game \n")
editor_input_new_game= input("Enter the editor of the game \n")
year_input_new_game = input("Enter the year \n")

new_game ={
    "name":name_input_new_game,
    "editor":editor_input_new_game,
    "year":year_input_new_game
}
games.append(new_game)

for game in games:
    print("Name:", game["name"])
    print("Editor:", game["editor"])
    print("Year:", game["year"])