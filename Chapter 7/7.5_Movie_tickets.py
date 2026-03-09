## Movie Tickets

## input() for total guests 
guests = int(input("How many tickets are needed?: "))

total_cost = 0
## >3 is free / 3-12 is 10$ / 13 and over 15$
for i in range(guests):
    age = int(input("Enter the age of the guest: "))

    if age < 3:
        print("Ticket is free")
        price = 0

    elif age <= 12:
        print("Ticket costs $10")
        price = 10

    else:
        print("Ticket costs $15")
        price = 15
## total it all
    total_cost += price

print("Total cost for tickets: $", total_cost)
