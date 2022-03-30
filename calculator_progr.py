
""" Simple calculator """
def add_numbers(a, b):
    return a + b

def substract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    return a / b

def power_of(a, b):
    return a ** b

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.To the power")

while True:
    # we will use While loop because we do not know how many operations we want
    choice = input("Enter choice( 1 /2 /3 /4 /5): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f'{num1} + {num2} = {add_numbers(num1, num2)}')


            elif choice == '2':
                print(f'{num1} - {num2} = {substract_numbers(num1, num2)}')

            elif choice == '3':
                print(f'{num1} * {num2} = {multiply_numbers(num1, num2)}')

            elif choice == '4':
                print(f'{num1} / {num2} = {divide_numbers(num1, num2)}')

            elif choice == "5":
                print(f'{num1} ** {num2} = {power_of(num1, num2)}')

        except ValueError:
            print("Input should be numeric")



        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")