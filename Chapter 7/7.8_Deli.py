# Sandwich Order Program

# List of sandwich orders
sandwich_orders = ['tuna', 'ham', 'turkey', 'veggie', 'chicken']

# Empty list for finished sandwiches
finished_sandwiches = []

# Make sandwiches until orders list is empty
while sandwich_orders:

    current_sandwich = sandwich_orders.pop()

    print(f"I made your {current_sandwich} sandwich")

    finished_sandwiches.append(current_sandwich)

# Print all finished sandwiches
print("\nThe following sandwiches were made:")

for sandwich in finished_sandwiches:
    print(sandwich)