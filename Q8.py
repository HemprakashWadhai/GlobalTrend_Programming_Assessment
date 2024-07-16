#8. Write a Python function that takes two numbers and an operator (as a string) and performs the corresponding arithmetic operation (addition, subtraction, multiplication, or division).
def arithmetic_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        else:
            return num1 / num2
    else:
        return "Error: Invalid operator!"

# Example usage:
num1 = 10
num2 = 5
operator = '+'
result = arithmetic_operation(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")

num1 = 15
num2 = 3
operator = '-'
result = arithmetic_operation(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")

num1 = 8
num2 = 4
operator = '*'
result = arithmetic_operation(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")

num1 = 12
num2 = 4
operator = '/'
result = arithmetic_operation(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")

num1 = 5
num2 = 0
operator = '/'
result = arithmetic_operation(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")

operator = '%'
result = arithmetic_operation(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")
