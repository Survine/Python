import datetime

def convert_to_12hr_format(time):
    return time.strftime("%I:%M %p")

time = input("Enter time in 24hr format (HH:MM): ")
time = datetime.datetime.strptime(time, "%H:%M")
print(convert_to_12hr_format(time))