import datetime

date = input("Enter a date in the format YYYY-MM-DD: ")
try:
    correctDate = datetime.datetime.strptime(date, "%Y-%m-%d")
    print("The date is valid.")
except ValueError:
    print("The date is invalid.")