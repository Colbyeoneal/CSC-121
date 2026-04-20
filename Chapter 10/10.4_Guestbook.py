from pathlib import Path

guest_book = Path("guest_book.txt")

while True:
    name = input("Please enter your name (or type 'quit' to exit): ")

    if name.lower() == "quit":
        break

    print(f"Hello, {name}! You have been added to the guest book.")

    with guest_book.open("a") as file_object:
        file_object.write(name + "\n")