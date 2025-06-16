# MY MAP

def square(x):
    return x*x

square(4)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(map(square, numbers)))


# LAMBDA FUNCTION WITH MAP

print(list(map(lambda x: x*x, numbers)))

# MAP MULTIPLE ITERABLES
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

added_numbers = list(map(lambda x, y: x + y, numbers1, numbers2))
print(added_numbers)

# MAP TO CONVERT A LIST OF STRINGS TO INTEGERS
str_numbers = ["1", "2", "3", "4", "5"]
int_numbers = list(map(int, str_numbers))
print(int_numbers)


words = ['apple', 'banana', 'cherry']
upper_word = list(map(str.upper, words))
print(upper_word)

def get_name(person):
    return person['name']

people = [
    {'name': 'Abby', 'age': '18'},
    {'name': 'Bethany', 'age': '16'},
]
print(list(map(get_name, people)))