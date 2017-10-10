"""
    1: Strings
"""

# ---String Manipulation---

# What are the valid indices of this string?

full_name = "Elana Gilbert"


my_string = full_name[1:3] + full_name[4:7] + full_name[-2] + full_name[4:5] * 2
# print(my_string)









"""
    2: Arithmetic
"""
number_one = 15
number_two = 13

# ---Standard Division---
result = number_one / number_two
#print(result)


# ---Integer Division---
result = number_one // number_two
#print(result)


# ---Modulus---
result = number_one % number_two
#print(result)


# ----- Augmented Assignment Operators -----
number_one = 10
number_two = 7

#number_one += 5
#number_one = number_one + 5
number_one **= 2

number_one %= 2
# print(number_one)

"""
    3: Conditional Statements
"""

some_number = 10

# What's the output of this?

if some_number > 5:
    # print("Number is greater than 5")
    pass

elif some_number > 7:
    # print("Number is greater than 7")
    pass

else:
    # print("Number is less than or equal to 5")
    pass























# What's the difference between using consecutive ifs and if / elif / else?


"""
    4: Truthiness and short-circuit evaluation
"""

var_a = 0
var_b = "Hey"

var_c = var_a and var_b
# Do these short-circuit?
if var_a or var_b:
    #print("One of the variables behaved like true")
    pass
else:
    #print("Neither variable behaved like true")
    pass

























# What's the output of this
x = 3
if x % 2:
    # print("True")
    pass
else:
    # print("False")
    pass

# WHEN DOES SHORT CIRCUIT OCCUR IN AN "AND" STATEMENT? WHAT ABOUT AN "OR" STATEMENT?

"""
    5: Functions, Parameters, Arguments
"""


def addTwoNumbers(n1, n2):
    n3 = 7
    n4 = n1 + n2 + n3
    return n4

def main():
    n2 = 1352235
    n3 = 234
    addTwoNumbers(n2, n3)

main()
print(addTwoNumbers(7, 24))

x = 7
y = 2012

addTwoNumbers(x,y)


















# Now write a function that adds two numbers
# How do we give a function input?






















# How do we add two numbers, 5 and 10, using this function?

# What if we had to two integer variables we wanted to add?


n1 = 7
n2 = 10


# Write a function that takes in a list of integers and returns the average


"""
    6: Collections
"""


""""-------------LISTS--------------"""

list = [1, 2, 3, 4, 5]

# How do we know it's a list? : The brackets

# How do we grab the first item in this list?


# What if we wanted the biggest item? (multiple ways to do this)



























# Let's grab the biggest item again, but let's use a different list.

other_list = [7, 12, 213, 16, 14, 17]






# K, so what about a sorting a list like this:
other_other_list = ["1", "77", "2", "12", "16", "8"]
other_other_list = sorted(other_other_list)































# What about elements in a list?

# Is this legal?
my_list = [1, True, "", False, [7, 3, 4]]


# How would we change the value of the third element to be "Hey there"

# How do we access the 7 in the list contained inside of this list? : By indexing both lists to that position




"""--------------SETS--------------"""

set = {5, 1, 7, 3, 7, 1, 2, 2, 8, 10, 6, 4, 6, 4, 2, 9}

#print(set)


# What is the value of this?
# element = set[0]
# print(element)





























# --------------Set Methods--------------

set_one = {1, 2, 3, 4, 5}
set_two = {2, 3, 4}

# Get elements from first that are in the second

# Is the first set a subset of the second?

# Is the first set a superset of the second?























"""--------------DICTIONARIES--------------"""

dictionary = {"Adam": "SI", "Maggie": "Professor", "Stefan": "Vampire"}

# How do we know it's a dictionary?

# How do we access the first index in the dictionary?
# How do you access a dictionary?


# How do I change the value at a key? Let's change The value associated with "Stefan" to the integer 7
dictionary["Stefan"] = 7


dictionary[True] = "Hello"


#print(dictionary)


# How do I create a new key?
# Add the key "Rick" and have it associate to the value "Morty"






























# Would a dictionary like this be legal? : Yes
other_dictionary = {"p": {1:"Sup"}, 1: "True", False: 7, "True": [1, 7, 3, 5, 1, 7]}
other_dictionary[0] = False

# How would I grab the integer 7 from that list in the dictionary?


"""--------------TUPLES--------------"""

tuple = (1, 2, 3)

# What makes tuples unique?


# How do I access elements in a tuple?

# How do I change the value of an element?

tuple_one = (1, 2, 3)
tuple_two = (4, 5, 6)
tuple_three = (7, 8, 9)

tuple_four = tuple_one + tuple_three + tuple_two

# When would you use specific datatypes in what situation?
list1 = [1,2,3,4,5]
list2 = [6,7,8,9]
print(list1 + list2)