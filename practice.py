# Q2
# Write a function: deposit_calculator(deposit, interest_rate, no_years).
# The function will accumulate the interest earned per year plus the deposit.

# For example, given a $1000 deposit, 10% interest rate and 5 years, 
# the function will calculate the interest earn in 5 years plus the deposit. 
# When `print(deposit_calculator(1000,0.10,5)` is executed, it should return $1610.51

# Tip to calculate interest earn with deposit: 
# Year 1 = $1100 ($1000 * 1.1)
# Year 2 = $1210 ($1100 * 1.1)
# Year 3 = $1331 ($1210 * 1.1) 
# Year 4 = $1464 ($1331 * 1.1)
# Year 5 = $1610.51 ($1464 * 1.1)

# Round off decimals to 2 decimal places.

# BONUS: Can you use f-strings to include a $ symbol with the return value?

      
# def deposit_calculator(deposit, interest_rate, no_years):
#     for year in range(no_years):
#         deposit=deposit*(interest_rate+1)
    
#     return round(deposit,2)
# print(deposit_calculator(1000,0.1,5))

# year = 1
# def deposit_calculator(deposit,interest_rate,no_years):
#     global year
#     while year <= no_years:
#         deposit = deposit*(interest_rate+1)
#         year += 1
#     return round(deposit,2)
# print(deposit_calculator(1000,0.1,5))     
       
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)
  

# list = [1,2,3,4] 
# print(len(list))




def fitness_app(distance):
    """
    This function allows user to check fitness points earned by entering their distances walked or ran as the parameter
    """
    # Variable created to retrieve excess of minimum distance 32km
    # This variable will be used for conditions for function
    exdistance = distance - 32

    # Empty list created to append fitness points
    accpoints = []

    # Variable to contain summed list 'accpoints' as data value
    finalpoint = 0

    # Variables that contain fitness points earned per km for each respective distance range
    zero2thirtytwo = 0
    thirtythree2forty = 325
    fortyone2fortyeight = 550
    morethan48 = 600

    # If excess of minimum distance is less than or equal 0
    if exdistance <= 0:

       # Append fitness points earned for 0-32km into list
       accpoints.append(exdistance*zero2thirtytwo)

       # sum the list as data value for variable finalpoint
       finalpoint = sum(accpoints)

    # If excess of minimum distance is more than zero and less than/equal to 8
    elif exdistance >0 and exdistance<=8:

        # Append the fitness points earned for amount of km completed within the 33 to 40 km range
        accpoints.append(exdistance*thirtythree2forty)

        # sum the list as data value for variable finalpoint
        finalpoint = sum(accpoints)
    
    # If excess of minimum distance is more than 8 and less than/equal 16
    elif exdistance >8 and exdistance<=16:

        # Append the fitness points earned for amount of km completed within the 33 to 40 km range
        accpoints.append(8*thirtythree2forty)

        # Calculate distance completed within the 41 to 48 km range after fitness points are computed for first 33-40km
        exdistance = exdistance - 8

        # Append the fitness points earned for amount of km completed within the 41 to 48 km range
        accpoints.append(exdistance*fortyone2fortyeight)

        # sum the list as data value for variable finalpoint
        finalpoint = sum(accpoints)
    
    # If the excess of minimum distance completed exceeds 16km
    else:
        # Append the fitness points earned for amount of km completed within the 33 to 40 km range
        accpoints.append(thirtythree2forty*8)

        # Append the fitness points earned for amount of km completed within the 41 to 48 km range
        accpoints.append(fortyone2fortyeight*8)

        # Calculate excess distance of the first 33-48km completed 
        exdistance = exdistance - 16

        # Append the fitness points earned from excess distances of the first 33-48km completed
        accpoints.append(exdistance*morethan48)

        # sum the list as data value for variable finalpoint
        finalpoint = sum(accpoints)

    # Return variable finalpoint as final output for total fitness points earned
    return finalpoint

print(fitness_app(15))
print(fitness_app(37))
print(fitness_app(45))
print(fitness_app(50))
    
a, b = '12'
c, d = '34'
print(a, b, c)
