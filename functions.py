## Customising function

# 1.start with def keyword
# 2.name the function
# 3.A set of parenthesis and colon ()
# 4.Optional parameters within the parenthesis
# A body of code to serve the purpose of the function

## Example 1 : Convert metre to kilometre 

# 1,2,3 & 4 +  doc strings for function, return function
def convertMetretoKM(metre) :
    """
    - This function converts metre to kilometre
    - One parameter required : metre(as integer or float)
    """ 
    return metre * 0.001


# How it functions :
km = convertMetretoKM(10000)
print(km)

# Example 2 : Calculate BMi using weight and height

def bmi(weight, height) :
    """
    - This function calculates the user's BMi using his/her weight and height
    - user would have to enter two parameters, weight and height
    """
    return weight / height ** 2
bmi = round(bmi(65,1.62) , 2)
print(bmi)

## Scope
# scope is basically a region in which the variable exists and works

# local scope, variables inside the function
def add() :
    x = 10 # local variables
    y = 20
    print(x, y) # Variables CAN be used individually if it is referred to within the function
    z = x + y
    return z

print(add())

# global scope, variable can exist outside the function and still work
y = 20 # global variable
def add() :
    x = 10 # local variables
    z = x + y
    return z

print(add())

# Search order : LEGB (Local, Enclosing, Global, Built-in)

def accumulate(x) :
    y = 0
    y = y + x
    return y

print(accumulate(1))

# Goal is to accumulate 1 to the result of the previous function, but it will not work as "y=0" will still be referred first as a local variable 
print(accumulate(1)) 

y = 0
def accumulate(x) :
    global y # this will allow y = 0 to be used as a global variable without unboundlocalerror
    y = y + x
    return y

print(accumulate(1))
print(accumulate(1))