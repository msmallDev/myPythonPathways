# MY LAMBDA
def addition (a, b):
    return a + b

addition = lambda a, b: a + b
print(addition(5,6))

def even(num):
    if num % 2 == 0:
        return True
    
even1 = lambda num: num % 2 == 0
print(even1(12))


def addition(x, y, z):
    return x + y + z

addition1 = lambda x, y, z: x + y + z
print(addition1(12, 13, 14))

## map() - applies a function to all items in a list
numbers = [1, 2, 3, 4, 5, 6]
def square(number):
    return number**2
square(2)

map(lambda x: x**2, numbers)
