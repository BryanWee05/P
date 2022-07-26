# Numerical comparison
print(2>3)

# Strings comparison
# Strings has a lexicographic order, where a has the smallest order and z has the highest order
print('a' > 'z')

num1 = 200
# 'and' requires both condition to be true or the returned result would be 'false'
print(num1 > 150 and num1 < 250)

# 'or' only requires one condition to be true for the returned boolean to be 'true'
print(num1 > 100 or num1 < 100)

# 'not' reverses the truth value of a single expression
print(not True == False )
# Value of 1 also equals to True
print(not False == 1)

# Operator precedence : Signs, not, and, or

# if and else statement
# elif keyword
language = "python"
if language == "python" :
    print(f"the main programming language is {language}")

singtel = 1.5
starhub = 1.8

# The else keyword is used after if to execute the next portion of code when the if condition is evaluated as False.
if singtel > starhub :
    print("singtel price higher than starhub")
else:
    print("starhub price is higher than singtel")

# elif continues the flow of the program to another 'if' statement if the first 'if' statement returns false
if singtel > starhub :
    print("singtel price higher than starhub")
elif singtel < starhub :
    print("starhub price is lower than singtel")
elif singtel == starhub :
    print("starhub price is equal to singtel")

# Create 2 variables with zero
sum_even = 0
sum_odd = 0

# Create a range of number 0 to 9 using range()
for num in range(10):
    if num % 2 == 0:
        sum_even += num
    else: sum_odd += num 

# print newline with \n
print(f"Even sum of 0 to 9 = {sum_even}\nOdd sum of of 0 to 9 = {sum_odd}")

# Example of break

# set a range of value from 50 to 99
range_value = range(50,100)

# use enumerate to include a counter for each loop
for count, num in enumerate(range_value):
    print(count, num)
    
    # 'for' loop stops executing at 5
    if count == 5:
        break

# continue can be used to skip certain iterations
for num in range(0,9) :
    if num == 2 or num == 3:
        continue
    print(num)

# Catch a value error

try:
    age = int(input("Enter an integer : "))

# except statement will execute when try statement fails
# the error type is spelled out after except keyword
except ValueError:
    print("The input is not an integer")
else:
    print(f"Your age is {age}")

def divide(num1, num2):
    try:
        print(num1/num2)

    except TypeError:
        print("Make sure it is a number")

    except ZeroDivisionError:
        print("Division by zero is not allowed")
        
    finally:
        print("end of function")

# Catch value error with finally keyword
try:
   user_input = int(input("Enter your age : "))

# except statement will execute when try statement fails
# the error type is spelled out after except keyword
except ValueError:
    print("You did not enter an integer")

else:
    print(f"Your age is {user_input + 10} in 10 years")

# finally will always execute 
finally:
    print("Your age calculation is dependent on your input")
        
