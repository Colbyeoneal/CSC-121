# Dictionaries using rivers
rivers_and_country = {
    "Nile": "Egypt",
    "Ganges": "India",
    "Mississippi": "America"
}

# Universal statement
for river, country in rivers_and_country.items():
    print(f"People in early {country} depended heavily on the {river} river.")

# Statements for individual rivers
print(f"The Nile leaves a verdant scar in the desert sands of {rivers_and_country['Nile']}.")
print(f"The Ganges is sacred to millions living in {rivers_and_country['Ganges']}.")
print(f"The Mississippi carried trade and culture across {rivers_and_country['Mississippi']}.")

# Printing just rivers
print("\nRivers:")
for river in rivers_and_country.keys():
    print(river)

# Printing just countries
print("\nCountries:")
for country in rivers_and_country.values():
    print(country)