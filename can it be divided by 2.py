Num = int(input("Insert a number: "))
Check = int(input("What do you want to divide it by: "))
Div = Num%2

if Div > 0:
    print(str(Num) + " is an odd number")
else:
    print(str(Num) + " is an even number")

if Num%4 == 0:
    print("Your number is also a multiple of 4")

if Num%Check == 0:
    print(str(Num) + " is divisble by " + str(Check))
else:
     print(str(Num) + " not divisble by " + str(Check))
    
    
