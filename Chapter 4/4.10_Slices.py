# Relevant code copied from 3-4

guest_list = ["Albert Einstein" , "Nikola Tesla" , "Werner Heisenberg"]
guest_list.insert (0 , 'Neil deGrasse Tyson')
guest_list.insert (2 , 'Michio Kaku')
guest_list.append ('Brian Cox')
guest_list.sort()

# Onto the assignment for 4.10 

# Number 1
print ("The first three items in the list are:")
for guest in guest_list [0:3]:
    print(guest.title())

# Number 2
print("Three items from the middle of the list are:")
for guest in guest_list [1:4]:
    print(guest.title())

# Number 3
print("The last three items in the list are:")
for guest in guest_list [3:]:
    print(guest.title())
# Printed again for ease of checking/debugging
print(f"{guest_list}")