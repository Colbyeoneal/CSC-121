### Dictionaries using rivers
rivers_and_country = {
    "Nile": "Egypt",
    "Ganges": "India",
    "Mississippi": "America"
}

for river, country in rivers_and_country.items():
    print(f"People in early {country} depended heavily on the {river} river.")

for river in rivers_and_country:
    print (river)
for river, country in rivers_and_country.items():
    print(country)