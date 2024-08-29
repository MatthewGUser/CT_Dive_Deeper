# [ Task 1 ]

year = int(input("Please enter a year: "))
out = False

if (year % 4) == 0:
    out = True

print(f"{year} is a leap year: {out}")