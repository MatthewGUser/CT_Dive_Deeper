# [ Task 1 ]

# Original
'''
number = input("Enter a number: ")

if number > 0:
    print("The number is positive.")
elif number = 0:
    print("The number is zero.")
else number < 0:
    print("The number is negative.")
'''

number = input("Enter a number: ")

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# = is used to assign a value, == is used to compare: this needed changed.
# else cannot have a condition as it applies if any other condition fails.
# If that would like to be used it would need to be an elif instead of an else.