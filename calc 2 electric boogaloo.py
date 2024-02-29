
num1 = input("input first number: ")
num2 = input("input second number: ")
oper = input("input operation you want to do: ")

num1 = float(num1)
num2 = float(num2)

if oper == ("+"):
    print(num1 + num2)
elif oper == ("-"):
    print(num1 - num2)
elif oper == ("*"):
    print(num1 * num2)
elif oper == ("/"):
    print(num1 / num2)
else:
    print("error")