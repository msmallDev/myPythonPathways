# MY LIST
lst = ["apple", "banana", "cherry"]
# print(type(lst))

###########################################################################################

# LIST METHODS
lst.append("orange")
# print(lst)

lst.insert(1, "watermelon")
# print(lst)

lst.remove("watermelon") # removes the first occurance of an item
# print(lst)

poppedItem = lst.pop() # remove and return the last element
# print(poppedItem)

cIndex = lst.index("cherry")
# print(cIndex)

lst.insert(2, "banana")
# print(lst.count("banana"))

lst.sort() # sorts the list in ascending order
# print(lst)

lst.reverse() # reverse the list
# print(lst)

#lst.clear() # clears the list
# print(lst)

# for fruit in lst:
#     print(fruit)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for index, number in enumerate(nums): #interating with index
#     print(index, number)

###############################################################################################

# LIST COMPREHENSION
# lst2=[]
# for x in range(10):
#     lst2.append(x**2)
# print(lst2)

# print([x**2 for x in range(10)]) # [expression for item in iterable]

# even_numbers = [num for num in range(10) if num % 2 == 0] # [expression for item in iterable if condition]
# print(even_numbers)


####################################################################################################

# NESTED LIST COMPREHENSION
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd']

pair = [(i, j) for i in list1 for j in list2]
# print(pair)

words = ["hello", "bye", "greetings", "adios", "hola"]
lengths = [len(word) for word in words]
print(lengths)