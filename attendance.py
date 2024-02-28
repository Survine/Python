# Find if the student is eligible to sit in exam or not

tclass = int(input("Total number of classes held :"))
aclass = int(input("Total Classes the student attended :"))

apercent = (aclass/tclass) * 100

if apercent < 75.0:
    print("The follwowing student is not allowed to sit in exam.")
else:
    print("The following student can sit in exam.")
