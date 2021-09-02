#basic calculator using if and functions

def calculator(op, a, b):                   #function to fascilate calculating function
    if op =="+":
        result = a + b
        return result
    elif op =="+":
        result = a + b
        return result
    elif op =="+":
        result = a + b
        return result
    elif op =="+":
        result = a + b
        return result
    else:
        print("invalid operator")

#pilot code

opertor = input("choose an operation from (+,-,*,/) : ")
num1 = float(input("enter first number = "))
num2 = float(input("enter second number : "))
ans = calculator(opertor, num1, num2)
print(ans)