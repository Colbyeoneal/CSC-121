try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))

    answer = first_number + second_number
    print(f"The sum is {answer}.")

except ValueError:
    print("Please enter numbers only, not text.")