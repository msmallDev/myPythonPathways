# MY SET
mySet = {1, 2, 3, 4, 5}
# print(mySet)
# print(type(mySet))

##############################################################

# BASIC SET OPERATIONS

mySet.add(7) # add element to a set
# print(mySet)

mySet.remove(7) #removes an element from a set
# print(mySet)

mySet.discard(11) # removes an element from a set but does not throw KeyError if it is not found
# print(mySet)

removed_element = mySet.pop() # pops the first element (FIFO)
# print(removed_element)
# print(mySet)

mySet.clear() # removes all elements from the set
# print(mySet)

##################################################################

# SET MEMBERSHIP TEST

my_set = {1, 2, 3, 4, 5}
# print(3 in my_set)
# print(10 in my_set)

##################################################################

# MATHMATICAL OPERATIONS

set1 = {1, 2, 3, 4, 5, 6}
set2 = {4, 5, 6, 7, 8, 9}

# union_set = set1.union(set2) # union
# print(union_set)

# intersection_set = set1.intersection(set2) # intersection - shows common numbers between the sets
# print(intersection_set)

# set1.intersection_update(set2) # intersection method but it updates the first element with the results of the operation
# print(set1)

# print(set1.difference(set2)) # returns the unique items from set1 after being compared to set2
# print(set2.difference(set1)) # returns the unique items from set2 after being compared to set1

# print(set1.symmetric_difference(set2))

################################################################

# SETS METHODS

numSet1 = {1, 2, 3}
numSet2 = {3, 4, 5}

# print(numSet1.issubset(numSet2)) # does numset2 have all the elements of numset1? Return boolean value

# print(numSet1.issuperset(numSet2)) # does numset1 have all the elements of numset2? Return boolean value

###############################################################

# EXAMPLE PROBLEMS


# REMOVE DUPLICATES
# solution - change list to a set

lt = [1, 2, 2, 3, 4, 4, 5]

# print(set(lt))

# COUNTING UNIQUE WORDS
# solution - use split to seperate words and convert list of words into set to get unique words

text = "I am learning about sets"
words = text.split()

unique_words = set(words)
# print(unique_words)
# print(len(unique_words))
