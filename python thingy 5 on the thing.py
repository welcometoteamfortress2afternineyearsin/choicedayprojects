
numlist = []
def balls():
    num1 = 1
    num2 = int(input("enter number: "))
    while True:
        numlist.append(num1)
        print(num1)
        num1 = num1 + 1
        if num1 == num2:
            print(num2)
            numlist.append(num2)
            break
while True:
    balls()
    print(numlist)
    ammount = 1
    for i in numlist:
        ammount = i*ammount
    print(ammount)
    numlist = []





