### Calculator 3 ###

""" содержит калькулятор.
Пользователь может вписать выражения вида 2*5 - 6 и посмотреть результат
Поддерживает такие операции как '+',  '-', '*', '/'.

"""
from operator import truediv, add, sub, mul

operators = {'+': add,
              '-': sub,
              '*': mul,
              '/': truediv
             }

def calculate(eq):
    try:
        if eq.isdigit(): #check whether user input numbers
            return float(eq) # prevrashaem input v float

        for key in operators.keys():
            left, op, right = eq.partition(key) # razdelim virajenie na chisla i operator
            if op in operators:
                return operators[op](calculate(left), calculate(right))
    except TypeError:
        print("Input should be numbers")
    except ZeroDivisionError:
        print("Division by zero not allowed")

expr = input("type expression: ")
print(f'Answer: {expr} = {calculate(expr)}')
