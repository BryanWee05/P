# Data structure : tuple ()

# Tuple containing strings, with elements seperated by commas
tuple_strings = ("banking","accounting","tourism","itb")
# Indexing
print(tuple_strings[0])

# Slicing
# For slicing, the value of the ending index is not included.
print(tuple_strings[0:3])

# Indexing returns as a string
print(type(tuple_strings[0]))

# Slicing returns a tuple
print(type(tuple_strings[0:3]))

# Tuple containing numbers can include both float and integer
tuple_numbers = (30.5, 32.4, 28.3, 29, 30)
print(type(tuple_numbers[1]))
print(type(tuple_numbers[4]))

# Tuple containing both strings and numbers
tuple_mix = ("apple", 0.50, "orange", 0.60, "durians", 10.0)
print(type(tuple_mix[0]))
print(type(tuple_mix[1]))
print(type(tuple_mix[0:4]))

age = (25,27)
print(age)
# unpack tuple using comma
# number of variables has to be equal to number of elements
john, jane = age 
print(f"age of john : {john}, age of {jane}")

# Like strings, tuple are immutable objects
# tuple_height = (160, 170, 180, 190)
# tuple_height[0] = 175

# Find element in tuple using in function
tuple_fruits = ("apples", "oranges", "durians", "pears")
if "pears" in tuple_fruits:
    print("pear found")

# create a function  to return remainder and integer of a division
def moduloIntegerDivision(num1, num2):
    remainder = num1%num2
    intDiv = num1//num2
    # return remainder and intDiv variables as a tuple
    return(remainder, intDiv) 

# return data type of the function is a tuple.
remainder_integer = moduloIntegerDivision(6,2)

# the tuple returns value of remainder and integer of the division
print(remainder_integer)


# Data structure : List []
# Mutable objects

list_nation = ("singapore","malaysia","indonesia","thailand")
print(list_nation[0:3])

# Create a long strings with countries
# print the string
string_countries = "singapore, malaysia, indonesia, thailand"
print(string_countries)

# Use split() attribute to separate the countries as an individual item, turning it into a list
# "," is the separater in the string
countries = string_countries.split(",")
print(countries)
print(type(countries))

# A list allows a 'for loop' to extract items
for country in countries:
    if country == "singapore":
       print(country)

# List are mutable
# create a list 
list_nation = ["singapore", "malaysia", "indonesia", "thailand"]
print(f"Original list : {list_nation}")

# assigned 'laos' to index position 3
list_nation[3] = "laos"

# 'thailand' is replaced by 'laos'
print(f"Altered list 1 :{list_nation}")

# reset the list
list_nation = ["singapore", "malaysia", "indonesia", "thailand"]

# to replace more than one value, we can use : to slice the list 
# and replace it with a new list.

# assigned '"canada", "united states", "mexico" to index position 1,2,3
list_nation[1:4] = ["canada", "united states", "mexico"]
print(f"Altered list 2 :{list_nation}")

# list methods
# .pop(), .insert(), .append(), .extend()

local_banks = ["ocbc", "posb", "dbs","uob"]
# .pop() removes an element from the list
# By default, the last item is removed ; index can be supplied in parenthesis to remove indexed item
# Negative index can be used, -1 means last, -2 means second last and so on

# local_banks.pop()
# print(local_banks)

# # .insert() allows an item to be inserted before the indexed item

# local_banks.insert(0, "citibank")
# print(local_banks)

# .append() allows an item to be inserted at the back of the list
# append can only be used for list 
# local_banks.append("Maybank")
# print(local_banks)

# reset the list of banks to original
list_banks = ["ocbc", "posb", "dbs", "uob"]

# create a  new tuple
new_banks = ('citibank', 'rabobank', 'bank of china')

# add new list to existing list
list_banks.extend(new_banks)

print(list_banks)

# create a list of numbers
numbers = [1,2,3,4,5]

# create an empty list
empty_list = []

# multiple each number in the list by 10 
# append the values into empty list
for num in numbers:
    empty_list.append(num*10)

# print empty list
print(empty_list)

# create a temperature list
temperature = [10.4,20.2,31.5,22.1,5.7]

# find the average temperature using sum divide by length of the list
avg = sum(temperature) / len(temperature)

# print average, min and max temperature in the list
print(f"average temp: {avg} \nminimum temp: {min(temperature)} \nmaximum temp: {max(temperature)}")

# Nested list
# Create a list with 3 sub-lists with 2 elements in each sub-list 
list_of_3 = [["savings", "fixed interest"], ["equity", "unit trusts"], ['mortgage', 'cpf']]

# Print list and check length of the list
print(list_of_3)
print(len(list_of_3))

# Print first sub-list with [0] 
print(list_of_3[0])

# Check length of first sub-list
print(len(list_of_3[0]))

# Print second sub-list with [1] 
print(list_of_3[1])

# Check length of second sub-list
print(len(list_of_3[1]))

# # Print third sub-list with [1] 
print(list_of_3[2])

# Check length of the third sub-list
print(len(list_of_3[2]))

# Accessing a nested list 
# To access first sublist [0] and its first item [0]
print(list_of_3[0][0])

# To access first sublist [0] and its second item [1]
print(list_of_3[0][1])

# To access second sublist [1] and its first item [0]
print(list_of_3[1][0])

# To access second sublist [1] and its second item [1]
print(list_of_3[2][1])

# Create a nested list with 2 sub-tuples
list_tuple = [(10,20), (30,40)]

# Check data object with type()
print(type(list_tuple))

# Check data object of position 0 
print(type(list_tuple[0]))

# Create a nested tuple with 2 sub-lists
tuple_list = ([10,20], [30,40])

# Check data object 
print(type(tuple_list))

# Check data object of position 0 
print(type(tuple_list[0]))

# Create a nested tuple with 1 sub-list and 1 sub-tuple
tuple_list2 = ([10,20], (30,40))

# Check data object with type()
print(type(tuple_list2))

# Check data object of position 0 with type()
print(type(tuple_list2[0]))

# Check data object of position 1 with type()
print(type(tuple_list2[1]))

# create a numerical and a string list
height_data = [190, 165, 175, 155, 182]
car_data = ["toyota", "honda", "mazda", "kia", "hyundai"]

# sort() function cna only be used for list 
# sort with default parameter
height_data.sort()
car_data.sort()

## since height_data consists of numeric datatype and it is sorted by ascending order  
# Data would be sorted from smallest to biggest
print(height_data)

## since car_data consists of string datatype and it is sorted by alphabetically order  
# data would be arranged by alphabetical order
print(car_data)

# reset height and car lists
height_data = [190, 165, 175, 155, 182]
car_data = ["toyota", "honda", "mazda", "kia", "hyundai"]

# sort height_data and set reverse to True
# Data  would now be sorted from biggest to smallest
height_data.sort(reverse=True)

# sort car_data with len function in the key parameter
# Data would now be sorted by amount of letters in the datas since len function is used 
car_data.sort(key=len)

print(height_data)
print(car_data)

tuple_weight = (43.5, 42.5, 64.2, 55.1, 80.2, 70.9)
# .sort() would not work on tuple and would return an attributeerror
# tuple_weight.sort()

# Instead, sorted() can be used 
# sorted() will arrange the number in ascending order and return a list 
listed_weight = sorted(tuple_weight)
print(listed_weight)

# Copy
# create a list and assign to list_a variable
list_a = [100, 200]
# assign list_a to a new variable list_b
list_b = list_a

print(f"Items in list_a and list_b : {list_a}, {list_b}")

# Adding values to the copied variable will also affect the original variable
# append a value '300' to list_b
list_b.append(300)

# check the values in list_a, has it been changed too?
print(f"Items in list_a and list_b : {list_a}, {list_b}")

# Using deepcopy to prevent change in original variable when copied variable is changed
# import the copy module 
import copy

# create a list and assign to list_c variable
list_c = [300,400]

# use 'deepcopy()' function to assign list_c to a new variable list_d
list_d = copy.deepcopy(list_c)

# append a new value to list_d
list_d.append(400)

# check the values in list_c, has it been changed?
print(f"Items in list_c and list_d : {list_c}, {list_d}")

# Converting tuple to list
# create a new tuple
tuple_fruits = ('apples', 'oranges', 'durians')

# convert the tuple to a list 
list_fruits = list(tuple_fruits)

# print list
print(list_fruits)

# print return type after conversion
print(type(list_fruits))

# Converting list to tuple
# create a new list
list_fruits = ['apples', 'oranges', 'durians']

# convert the list to a tuple
tuple_fruits = tuple(list_fruits)

# print tuple
print(tuple_fruits)

# check return type after conversion
print(type(tuple_fruits))

# create a list with Singapore dollars as the context
sgd = [1200, 2400, 955, 3420, 10400, 7300, 100000, 6300, 5500, 4320] 

# create two empty lists to append value from iteration
lowerforex_bucket  = []
higherforex_bucket  = []

# initialise the two exchange rates to convert Singapore dollars to US dollars
lower_forex = 0.71
higher_forex = 0.74

# multiply each item in list and append to the empty lists
# if value is >= 10000, multiply the item by 0.71 and append to lowerforex_bucket
# else multiply the item by 0.74 and append to higherforex_bucket
for amount in sgd:
    if amount >= 10000:
        lowerforex_bucket.append(amount * lower_forex)
    else:
        higherforex_bucket.append(amount * higher_forex)

print(lowerforex_bucket)
print(higherforex_bucket)

# Data structure : Dictionaries {}
# One way to create a dictionary literal is to use a pair of curly braces and colon to store data in each key/value pair: {key: value}.
best_artist = {
    "pop" : "one direction",
    "opera" : "josh groban",
    "jazz" : "stacey kent",
    "classical" : "2 cellos"
}

# check type of object
print(type(best_artist))

# check the length of dictionary
print(len(best_artist))

# Data in dictionaries can be accessed by the key instead of indexing for tuple and list
# access artist from pop genre
print(best_artist["pop"])

# access artist from classical genre
print(best_artist["classical"])

# You can use either [] or .get() method to retrieve the values.
print(best_artist.get("pop"))
print(best_artist.get("classical"))

# Dictonaries are mutable
# change the value of "pop" key to "dua lipa"
best_artist["pop"] = "dua lipa"

# add a new key/value pair: rock/bon jovi
best_artist["rock"] = "bon jovi"

# delete a key/value pair using del function.
del best_artist["opera"]

# print to check changes in dictionary
print(best_artist)

# reset best_artist
best_artist = {
    "pop" : "one direction",
    "opera" : "josh groban",
    "jazz" : "stacey kent",
    "classical" : "2 cellos"
    }

# print the keys with a for loop
for key in best_artist:
    print(f"genre: {key}")

# print the values with a for loop
for key in best_artist:
    print(f"best artist: {best_artist[key]}")

# .items() arrange the key and its values in tuple format
# print the output dictionary using .items() method
print(best_artist.items())

# check object type when using .items() method
print(type(best_artist.items()))

# check the length of when using .items() method
print(len(best_artist.items()))

# Use a for loop to itereate over '.items()'
# Since .items() returns key/value pair as 2 values in a tuple,
# 2 temporary variables (named them as genre and artist) are used
# to represent the key and value.

for genre, artist in best_artist.items():
    print(f"best artist for {genre} is {artist}!")

song_title = {
    "2002" : {"artist" : "ann-marie",
              "length" : 234,
              "album" : "2002",
              "genre" : "pop"},

    "Forever in love" : {"artist": "kenny g",
                         "length": 275.4,
                         "album": "breatheless",
                         "genre" : "jazz"},

    "The prayer": {"artist": "andre bocelli",
                   "length": 256.8,
                   "album": "these are special times",
                   "genre": "opera"},
    
    "November rain": {"artist": "guns n roses",
                      "length" : 513.6,
                      "album" : "use your illusion 1",
                      "genre" : "rock"}

}

# Use of if statement to filter song title based on genre
for song in song_title:
    if song_title[song]["genre"] == "rock":
        print(song)
        
# for song in song_title:
#     if song_title[song]["genre"] == "pop":
#         print(song)


# user_input = input("Please enter a song title : ")
# for song in song_title:
#     if song_title == song:
#         print(f'song : {song} | artist : {song_title[song]["artist"]} | length : {song_title[song]["length"]}secs | album : {song_title[song]["album"]} | genre {song_title[song]["genre"]}')