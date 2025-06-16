# MY DICTIONARY
empty_dict = {}

student = {"name": "Abby", "age": 32, "grade": "A"}
#print(student)

# accessing dictionary elements
#print(student['grade'])

# accessing using get() method
# print(student.get('grade'))
# print(student.get('last_name', 'Not Available')) 

################################################################

# MODIFYING DICTIONARY ELEMENTS

student['age'] = 33 # update
# print(student)
student["address"] = "Covington Street" #add new key and value
# print(student)

del student['grade']
# print(student)

###################################################################

# DICTIONARY METHODS

keys = student.keys() #get all the keys
# print(keys)
values = student.values() # get all the values
# print(values)

items = student.items() #get all key value pairs
# print(items)

student_copy = student
# print(student)
# print(student_copy)

student['name'] = 'Abby2'
# print(student)
# print(student_copy)

student_copy1 = student.copy() #shallow copy
# print(student_copy1)
# print(student)
student["name"] = "Abby3"
# print(student_copy1)
# print(student)

############################################################

# ITERATING OVER DICTIONARIES

# for keys in student.keys():
#     print(keys)

# for values in student.values():
#     print(values)

# for key, value in student.items():
#     print(f"{key}: {value}")

###############################################################

# NESTED DICTIONARY

students = {
    "student1": {"name": "Abby", "age": 32},
    "student2": {"name": "Bryan", "age": 29},
}
# print(students)

# Access nested dictionaries elements
# print(students["student2"]["name"])

# Iterating over nested dictionaries
# for student_id, student_info in students.items():
#     print(f"{student_id}: {student_info}")
#     for key, value in student_info.items():
#         print(f"{key} : {value}")


################################################################

# DICTIONARY COMPREHENSION

squares = { x:x**2 for x in range(5) }
# print(squares)

# Conditional dictionary comprehension
evens = {x:x**2 for x in range(10) if x%2==0}
# print(evens)

###############################################################

# PRACTICAL EXAMPLES
# use a dictionary to count the frequence of elements in list

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
# print(frequency)

# merge two dictionaries into one

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

merged_dict = {**dict1, **dict2}
print(merged_dict)