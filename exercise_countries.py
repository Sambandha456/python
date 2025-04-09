countries = [
    {"name": "China", "population": 1416096094},
    {"name": "India", "population": 1463865525},
    {"name": "USA", "population": 347275807}
]
biggest_country = countries[0]
for country in countries:
    print(f"Name: {country['name']} - Population: {country['population']}")
    if country['population'] > biggest_country['population']:
        biggest_country = country

print(f"Country with the largest Name: {biggest_country['name']} - Population: {biggest_country['population']} ")
