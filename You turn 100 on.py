Name = str(input("What is your name: "))
Age = int(input("How old are you: "))
cYear = int(input("What year is it: "))

fYear = cYear + (100 - Age)
SfYear = str(fYear)

print("Hi " + Name + "." + "You will be turning 100 in the year " + SfYear + ".")
