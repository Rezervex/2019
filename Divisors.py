x = range(2, 11)

for elem in x:
    print(elem)

num = int(input("Please choose a number to divide: "))

Range = list(range(1, num+1))
DivList = []

for number in Range:
    if num % number == 0:
        DivList.append(number)

print(DivList)
