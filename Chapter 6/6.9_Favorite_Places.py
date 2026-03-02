favorite_places = {
    "Kevin" : ["London", "Greenville", "Charleston"],
    "Aaron" : ["Outer Banks", "Las Vegas", "Austin" ],
    "Kelly" : ["Miami", "New York", "Atlanta"]
}
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are: {', '.join(places)}")