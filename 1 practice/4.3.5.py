import math as m
def calc():
    x = int(input("введите х"))
    y = int(input("введите y"))
    stroke = input("vvedite +, -, *, /, e, sin, cos, ^")
    if stroke == "+":
        print(f'x+y={x+y}')
    if stroke == "-":
        print(f'x-y={x-y}')
    if stroke == "*":
        print(f'x*y={x*y}')
    if stroke == "/":
        print(f'x/y={x/y}')
    if stroke == "e":
        print(f'e^x+y={pow(m.e(1),x+y)}')
    if stroke == "sin":
        print(f'sin(x+y)={m.sin(x+y)}')
    if stroke == "cos":
        print(f'cos(x+y)={m.cos(x+y)}')
    if stroke == "^":
        print(f'x^y={x**y}')

print(calc())