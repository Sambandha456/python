color=[
    {"name":"blue", "score":50},
    {"name":"green", "score":60},
    {"name":"red", "score":10},
    {"name":"black", "score":100},
]

while True:
    user_name = input(" [bot] Enter your name \n")
    print(f"Hello {user_name}")
    age= int(input("[bot] Enter you age \n"))
    if(age <=18):
        print("[bot] you are at teenager and growing")
    elif (age>=18 and age <= 35 ):
        print("[bot] You are at the prime time")
    else:
        print("[bot] You are getting old")
    user_color= input(" [bot] Enter you favourite colour \n")
    for item in color:
        if (user_color == item["name"]):
            if (item["score"]>=80):
                print(f"[bot] I love {user_color} too")
            elif (item["score"]>=50):
                print(f"[bot] Cool but I dont really like {user_color}")
            else:
                print(f"[bot] I donot know about this {user_color} color")
    user_job = input("[bot] Enter you occupation \n")
    if (user_job =="student"):
        user_field=input("[bot] Ohhh, Which field are you on \n")
        if (user_field =="IT"):
            user_language=input("[bot] What is ur favourite coding language")
            if (user_language =="java"):
                print(f"[bot] ohh I also like {user_language}")
            else:
                print("[bot] hope you are doing good in the language")
        else:
            print("[bot] I hope you are doing well in your job")
    else:
        print("[bot] Hope you are doing good on your job")

