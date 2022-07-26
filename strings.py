# A pair of quotation is used to set any characters to strings.

# Double quotation
print("Hello World!")

# Single quotation
print('2022')

# single quotation as an apostrophe in a sentence
# double quotation as delimiter for strings 

print("What's your name?")

# \'s escapes the inner ' 
# Python treat the inner ' as a string instead of a delimiter
print('What\'s your name?')

# \n is used to print each word in a string on newlines
print("What's\nyour\nname?")

# create firstname variable using = and assign "tom" to the variable.
firstname = "tom"

# create lastname variable using = and assign "matthew" to the variable.
lastname = "matthew"
print(firstname)
print(lastname)

# use == to compare if two values are the same

# 'tom' and 'tom' are the same value, so it returns a True value
print('tom' == 'tom')

# strings are case sensitivity 
# 'T' and 't' are treated as different values, so it will return a False value 
print('Tom' == 'tom') 

# create firstname variable using = and assign "tom" to the variable.
firstname = "tom"

# create lastname variable using = and assign "matthew" to the variable.
lastname = "matthew"

# concatenate two strings using `+`
fullname = firstname + lastname
print(fullname)

# use " " to include a whitespace between 2 strings, 
fullname = firstname + " " + lastname
print(fullname)

# use "\n" to include newline between 2 strings, 
fullname = firstname + "\n" + lastname
print(fullname)

# create firstname variable 
firstname = "tom"

# create lastname variable 
lastname = "matthew"

# len will return value of 3 since the variable contains 3 characters
print(len(firstname))

# len will return value of 7 lastname variable contains 7 characters
print(len(lastname))

# create firstname variable 
firstname = "tom"

# type() wil return the class of the variable.
# `str` is a  shortform for strings.
print(type(firstname))

# create fullname variable 
fullname = "Tom Matthew"

# The first index position starts at zero.
# this will return 'T'
print(fullname[0]) 

# The second index position is 1 
#  this will return 'o'
print(fullname[1])

# Use ':' to specify a range of positions
# [0:3] will return 'Tom'. 
# Index position 3 is the stopping position 
# The value at index position 3 will not be included.
print(fullname[0:3])

# create fullname variable 
fullname = "Tom Matthew"

# last index position is at -1 
# -1 returns `w`
print(fullname[-1])

# second last index position is at -2
# -2 returns `e`
print(fullname[-2])

# ':' to specify a range
# -7: refers to the last 7th index position onwards
print(fullname[-7:])

# create firstname variable 
firstname = "tom"

# assign 'b' to index position 0 
# to replace 't' with 'b'
# firstname[0] = 'b'

# create fullname variable 
fullname = "Tom Matthew"

# convert fullname variable from lower to uppercase with .upper()
print(fullname.upper())

# convert ABC letters from upper to lower case with .lower()
print("A,B,C".lower())

# create a string variable with whitespaces.
# whitespace are on both the right and left of `Main Street`
# before enclosed by quotation.
street = "     Main Street    "

# check the number of characters with len()
# notice whitespaces are also included as part of 
# the string?
print(len(street))

# create a string variable with whitespaces.
street = "     Main Street    "

# Use `.rstrip()` to strip whitespace on the right 
# and assign to a variable named street_right
street_right = street.rstrip()
print(street_right)

# check number of characters after stripping whitespace on the right
print(len(street_right))

# create a string variable with whitespaces.
street = "     Main Street    "

# Use `.lstrip()` to strip whitespace on the left 
# and assign to a variable named street_left
street_left = street.lstrip()
print(street_left)

# check number of characters after stripping whitespace on the left
print(len(street_left))

# create a string variable with whitespaces.
street = "     Main Street    "

# strip whitespace on the left and right,
# and assign to a variable named street_leftright
street_leftright = street.strip()
print(street_leftright)

# check number of characters after stripping whitespace on the left and right
print(len(street_leftright))

# create a variable and assign "30"
# since "30" is enclosed by quotation, it will be treated as a string
age = "30"

# use int() to convert "30" to integer data type
age_int = int(age)

# use float() to convert "30" to float data type
age_float = float(age)

# print the values of the variables
print(age_int)
print(age_float)

# check the data type with type()
print(type(age_int))
print(type(age_float))

# create two strings variables
name = 'tony'
age = "30"

# use f-strings to print both variables
# the variables are enclosed by {}
# .upper() in the string variable  converts lower case to upper case
print(f"Your name is {name.upper()} and your age is {age}")

