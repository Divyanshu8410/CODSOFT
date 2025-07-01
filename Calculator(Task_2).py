num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display the operation choices
print("\nSelect an operation:")
print("1. Addition(+)")
print("2. Subtraction(-)")
print("3. Multiplication(*)")
print("4. Division(/)")

# Get the user's choice
choice = input("Enter choice : ")

# Perform the selected operation
if choice == '1':
    print(f"The Addition of {num1} and {num2} is : {num1 + num2}")
elif choice == '2':
    print(f"The Subtraction of {num1} and {num2} is : {num1 - num2}")
elif choice == '3':
    print(f"The Multiplication of {num1} and {num2} is : {num1 * num2}")
elif choice == '4':
    if num2 != 0:
        print(f"The Division of {num1} and {num2} is : {num1 / num2}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")
