import math
num1 = float(input("enter num1:"))
num2 = float(input("enter num2:"))
op = input("enter op:")
x = float(input("x:"))
y = int(input("y:"))

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2 
elif op == "/":
    result = num1 / num2
elif op == "sin":   
    result = math.sin(x)
elif op == "cos":    
    result = math.cos(x)
elif op == "tan":
    result = math.tan(x)
elif op == "cot":
    result = math.cot(x)
elif op == "factorial":
    result = math.factorial(y)
elif op == "radical":
    result = math.sqrt(y)
    
print(result)