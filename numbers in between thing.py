
def balls():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    while True:
        print(num1)
        num1 = num1 + 1
        if num1 == num2:
            print(num2)
            break
while True:
    balls()
