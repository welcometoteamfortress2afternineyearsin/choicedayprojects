num1 = input("first number please: ")
num2 = input("second number please: ")

num1 = float(num1)
num2 = float(num2)

if num1 % num2 == (0):
    print("yep you can evenly divide it")
elif num1 % num2 >= (1):
    print("nope you cant")
else:
    print("whatever")