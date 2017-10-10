
"""
    1: Strings
"""

# ---String Manipulation---

# What are the valid indices of this string?

full_name = "Elana Gilbert"

# How would we access the first name of this string using those indices?

first_name = full_name[0:6]

# print(first_name)

# How would we access the last name of this string?

last_name = full_name[6:]

# print(last_name)

# What's the output of this code:
# letter = full_name[15]

# How would we get the last letter of this string? There are two ways

last_letter = full_name[len(full_name) - 1]
last_letter = full_name[-1]

#print(last_letter)

# How would we print that last letter 3 different times?

# print(last_letter * 3)

# Any questions?

# --- String Methods ---

my_other_string = "         Somebody stole my car radio and now we just sit in silence         "

# Strip the string of leading/trailing whitespaces and uppercase everything
my_other_string = my_other_string.strip().upper()
# print(my_other_string)


# Cool, what is the output of this then:

my_string = full_name[1:3] + full_name[4:7] + full_name[-2] + full_name[4:5] * 2
# print(my_string)


"""
    2: Arithmetic
"""

number_one = 7
number_two = 3

# Addition
addition_result = number_one + number_two
# print(addition_result)

# Subtraction
subtraction_result = number_one - number_two
# print(subtraction_result)

# Multiplication
multiplication_result = number_one * number_two
# print(multiplication_result)

# Division
division_result = number_one / number_two
# print(division_result)

# Exponents
exponent_result = number_one ** number_two
# print(exponent_result)

# Integer Division
integer_division_result = number_one // number_two
# print(integer_division_result)

# Modulus
modulus_result = number_one % number_two
# print(modulus_result)

# Augmented assignment operators?

number_one += 5 # Value 12
# print(number_one)

number_one **= 2 # 7 ^ 2 = 49
# print(number_one)

number_one %= 2 # Value is 1
# print(number_one)


"""
    3: Conditional Statements
"""

# How do we declare a conditional statement?

some_number = 10

if some_number > 5:
    # print("Number is greater than 5")
    pass
# What about an else?

else:
    # print("Number is not greater than 5")
    pass
# Let's do it again using elifs

if some_number > 5:
    # print("Number is greater than 5")
    pass

elif some_number == 5:
    # print("Number is equal to 5")
    pass

else:
    # print("Number is less than 5")
    pass
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

# Which lines of code get executed here:

other_number = 100

if other_number > 50:
    # print("Number greater than 5")
    pass

if other_number > 70:
    # print("Number is greater than 7")
    pass

elif other_number == 100:
    # print("Number equals 10")
    pass

# What's the difference between using consecutive ifs and if/else


"""
    4: Truthiness and short-circuit evaluation
"""

# What is truthiness?

# Switch up values for these to demonstrate truthiness
var_a = 5
var_b = ""

# Do this after, cover shirt-circuit versions as well

# var_c = var_a or var_b
# var_c = var_a and var_b
# print(var_c)

# Do these short-circuit?
if var_a or var_b:
    # print("One of the variables behaved like true")
    pass
else:
    # print("Neither variable behaved like true")
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

# Write a function that says "Hey, whatsup!" everytime we call it.

def say_hey():
    print("Hey, whatsup!")

# Should we run this? Not yet, we need to call our function

# say_hey()

# Now write a function that adds two numbers
# How do we give a function input? : Parameters

def add_two_numbers(number_one, number_two):

    sum = number_one + number_two

    # What do we have to do after we have my result? : return it
    return sum

# How do we add 5 and 10 using this function? : call it and pass in arguments
add_two_numbers(5, 10)

# Why didn't this give me output? : No print() function

# print(add_two_numbers(5, 10))

# What if we had to two integer variables?
n1 = 7
n2 = 10

# print(add_two_numbers(n1, n2))

# Do the names of the variables we pass in as arguments matter? : No they are arbitrary

# Write a function that takes in a list of integers and returns the average

def avg(some_list):
    total = sum(some_list)
    number_of_elements = len(some_list)
    average = total / number_of_elements
    return average

# create a list of integer

my_list = [1, 2, 3, 4, 5]

# If we wanted to store this average in a variable, how would we do this?
my_average = avg(my_list)

# Print it out
# print(my_average)

# WHAT IS FUNCTION COMPOSITION?
# CAN YOU GIVE ME AN EXAMPLE?

# Any questions?

"""
    6: Collections
"""


""""-------------LISTS--------------"""

# How do we create 5 numbers 1 - 5

list = [1, 2, 3, 4, 5]

# How do we know it's a list? : The brackets

# How do we grab the first item in this list?

first_item = list[0]

# What if we wanted the biggest item?
biggest_item = list[-1]

# print(biggest_item)

# Let's grab the biggest item again, but let's use a different list.

other_list = [7, 12, 213, 16, 14, 17]

# Accessing index @ position -1 won't work anymore, what do we have to do now? : Sort the list first, then access index -1
other_list = sorted(other_list)
biggest_item = other_list[-1]
# print(biggest_item)

# K so what about a sorted list like this:
other_other_list = ["1", "77", "2", "12", "16", "8"]
other_other_list = sorted(other_other_list)
# print(other_other_list)


# What about elements in a list?

# Is this legal?
my_list = [1, True, "", False, [7, 3, 4]]
# print(my_list)

# How would we change the value of the third element to be "Hey there"
my_list[2] = "Hey there"
# print(my_list)

# How do we access the 7 in the list contained inside of this list? : By indexing both lists to that position
element = my_list[-1][0]
# print(element)



"""--------------SETS--------------"""


# What do you know about sets that make them unique? : They're immutable, they don't have duplicates, they order integers

# Create this set

set = {5, 1, 7, 3, 7, 1, 2, 2, 8, 10, 6, 4, 6, 4, 2, 9}

# How do we know that this is a set? : Curly braces

# print(set)
# What did we notice?

# How do we access elements in a set?

# What is the value of this? : IT'S AN ERROR
# element = set[0]
# print(element)


# SETS CANNOT BE ACCESSED BY INDEX
# This far in the semester, we can't actually access elements in a list directly. But what we can do is use set methods to do some cool stuff with them.

# --------------Set Methods--------------

set_one = {1, 2, 3, 4, 5}
set_two = {2, 3, 4}

# Get elements from first that are in the second
set_three = set_one.intersection(set_two)
# print(set_three)

# Get elements that are in the first but not in the second
set_three = set_one.difference(set_two)
# print(set_three)

# Is the first set a subset of the second?
subset = set_one.issubset(set_two)
# print(subset)

# Is the first set a superset of the second?
superset = set_one.issuperset(set_two)
# print(superset)


"""--------------DICTIONARIES--------------"""

# How do we create a dictionary?

dictionary = {"Adam": "SI", "Maggie": "Professor", "Stefan": "Vampire"}

# How do we know it's a dictionary? : Key - Value pairs

# How do we access the first index in the dictionary? : You can't, dictionaries don't have order (position)
# How do you access a dictionary? : By key
value = dictionary["Adam"]
# print(value)

# How do I change the value at a key? Let's change The value associated with "Stefan" to the integer 7
dictionary["Stefan"] = 7
# print(dictionary)

# How do I create a new key?
# Add the key "Rick" and have it associate to the value "Morty"
dictionary["Rick"] = "Morty"
# print(dictionary)

# Would a dictionary like this be legal? : Yes
other_dictionary = {1: "True", False: 7, "True": [1,7,3,5,1,7]}
#print(other_dictionary)

# Dictionaries can have any datatype map to any other datatype.

# How would I grab the integer 7 from that list in the dictionary?
element = other_dictionary["True"][1]
#print(element)


"""--------------TUPLES--------------"""

# How do I create a tuple?
tuple = (1, 2, 3)

# What makes tuples unique? : Immutable, they cannot be changed
# How do I access elements in a tuple? : Index, just like with lists
element = tuple[0]
print(element)

# How do I change the value of an element? : I can't

tuple_one = (1, 2, 3)
tuple_two = (4, 5, 6)
tuple_three = (7, 8, 9)

tuple_four = tuple_one + tuple_three + tuple_two
print(tuple_four)

# When would you use specific datatypes in what situation?