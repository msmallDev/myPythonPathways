# MY TUPLE

numbers = tuple([1, 2, 3, 4, 5, 6])
# print(numbers)

mixed_tuple = (1, "hello world!", 3.14, True)
# print(mixed_tuple)

#################################################

# ACCESSING TUPLE ELEMENTS

# print(numbers[0])
# print(numbers[-1])

# print(numbers[0:4])
# print(numbers[::-1])

#################################################

# TUPLE OPERATIONS

concatenation_tuple = numbers + mixed_tuple
#print(concatenation_tuple)

##################################################

# IMMUTABLE NATURE OF TUPLES

lst = [1, 2, 3, 4, 5]
#lst[1] = "Abby" 

#numbers[1] = "Abby" #Immutable :)

##################################################

# TUPLE METHODS

# print(numbers.count(1))
# print(numbers.index(3))

packed_tuple = 1, "Hello", 3.14
# print(packed_tuple)

a, b, c = packed_tuple
# print(a)
# print(b)
# print(c)

numbers = (1, 2, 3, 4, 5, 6)
first, *middle, last = numbers
# print(first)
# print(middle)
# print(last)

lst = [[1, 2, 3, 4], [6, 7, 8, 9], [1, "Hello", 3.14, "c"]]
# print(lst[0][2])

nested_tuple = ((1, 2, 3), ("a", "b", "c"), (True, False))
for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item, end = " ")
    print()