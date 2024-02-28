# Check if the year is a leap year

year = int(input("Enter a year :"))
if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
    print(f"The year {year} is a Leap year.")
else:
    print(f"The year {year} is not a Leap year.")
