games=[
    {"name":"One Piece","Volumes":"108 Volumes"},
    {"name":"Attack on Titans","Volumes":"34 Volumes"},
    {"name":"One-Punch Man","Volumes":"30 Volumes"}
]
for index, game in enumerate(games):
    print(f"{index}. {game["name"]} - {game["Volumes"]}")
