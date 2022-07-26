# Comparison operator !=. <
# != represents not equal
print(3 != 4)
print(3 != 3)

print(3<6)
print(3<2)

# Addition assignment operator +=
number = 0
# number = number + 1
number += 1 # += is just a simplified form of the previous statement, which function is to make changes to the variable
number += 2
number += 3
print(number)

## while loop
number = 1 
while number < 5 :
    print(number)
    number += 1

# Using while loop and != function to create password system
# set_password = "Nice_cock"
# user_input = input("please enter your password : ")

# if the user input is not equal(!=) to set_password, the while function will loop and prompt the user to input another password until it's the correct one.
# while set_password != user_input :
#     user_input = input("Wrong password. Please enter again : ")

# print("Nice brah")

## for loop
# A for loop executes a body of code once for each item in a collection of items. The number of times that the code is executed is determined by the number of items in the collection. 
for letter in 'singapore':
    print(letter)

# enumerate
for index, letter in enumerate('singapore'):
    print(f"count {index} character {letter}")

# Range with for loop
# Range has 3 parameters, first is the first value you wish to return, second parameter is one above the value you wish to return. Third is the width between each item.
for number in range(1,6,2) :
    print(number)
