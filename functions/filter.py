# MY FUNCTION

def even(num):
    if num % 2 == 0: 
        return True

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

print(list(filter(even, lst)))

# filter with a lambda function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)

# filter with a lambda function and multiple conditions
even_and_greater_than_five = list(filter(lambda x: x > 5 and x % 2 == 0, numbers))
print(even_and_greater_than_five)

# filter() to check if the age is greater than 25 in dictionary
people = [
    {'name': 'Abby', 'age': 27},
    {'name': 'Bethany', 'age': 16},
]
def age_greater_than_25(person):
    return person['age'] > 25

print(list(filter(age_greater_than_25, people)))