def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a/b

print('Select the operation')
print('1. Addition')
print('2. Subtraction')
print('3. Multiplication')
print('4. Division')

choice = int(input('Enter your choice 1/2/3/4'))
x = int(input('Enter first number'))
y = int(input('Enter second number'))
if choice == 1:
    print(add(x, y))
elif choice == 2:
    print(subtract(x, y))
elif choice == 3:
    print(multiply(x, y))
elif choice == 4:
    print(divide(x, y))
else:
    print('Wrong Choice')