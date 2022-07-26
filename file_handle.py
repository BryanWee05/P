
## Creating Path object from strings + Path object
# A path object is created so that we can locate and perform reading and writing on the files
# import Path method from pathlib
from pathlib import Path

# create a path object by using strings
# Note that the `Path` refers Path function from pathlib 
# r refers to `raw strings` and is used to swtich off backslash `\` used in escape characters.
# otherwise `\` is treated as an escape for example new line `\n`.

file_path = Path(r"C:\Users\bryan\python4biz\test.txt")
# check the object class
print(type(file_path))
# print path
print(file_path)
# exists() method checks if file_path exists(), returns True or False.
print(file_path.exists())

print(2)
## Creating path objects from .home()
# This class method creates a Path object representing the user's home directory, which usually refers to c:\Users\Bryan
# import Path method from pathlib
from pathlib import Path
# instantiate an file path object to home directory
home = Path.home()
print(home)
# Use '/' to extend path to extend the file path
# This creates the file path c:\Users\bryan\python4biz\test.txt as home = c:\Users\bryan
file_path = home/"python4biz"/"test.txt"
# print path
print(file_path)
# check object class of file path. It returns a pathlib class object
print(type(file_path))
# check if file_path exists()
print(file_path.exists())

print(3)
## .cwd() method always represents your current location in the file system, which in this case is c:\Users\bryan\Documents\PYTHON_TUTORIAL
from pathlib import Path
# check file path of current working directory
print(Path.cwd())
# instantiate a file path object to current working directory
# extend to file name "user_input.py"
fp_cwd = Path.cwd()/"user_input.py"
print(fp_cwd.exists())

print(4)
# import Path method from pathlib
from pathlib import Path
# instantiate an file path object to home directory
home = Path.home()
# Use '/' to extend path to extend the file path
file_path = home/"python4biz"/"test.txt"
# access file name with .stem
print(f"stem:{file_path.stem}")
# access file extension with .suffix
print(f"sufix:{file_path.suffix}")

print(5)
# import Path method from pathlib
from pathlib import Path
# instantiate an file path object to home directory
home = Path.home()
# create a new file_path and extend it to 'python4biz' and create a new file 'contacts.text'
file_path = home/"python4biz"/"contacts.txt"
# create a new file with `.touch()`
file_path.touch()
# print the file path
print(file_path)
# check if new file exists
print(file_path.exists())

print(6)
# import Path method from pathlib
from pathlib import Path
# instantiate an file path object to home directory
home = Path.home()
file_path = home/"python4biz"
# `.iterdir()` iterates through file_path 
for file in file_path.iterdir():
    # if is_file returns True, print the name of the file.
    # if file_path is a directory, it returns false.
    if file.is_file():
        # use `.name` to print file name
        print(file.name)

print(7)
# import Path method from pathlib
from pathlib import Path
# instantiate a file path object to home directory
home = Path.home()
file_path = home/"python4biz"
# * acts like a wildcard character which replace any number of characters before the suffix
for file in file_path.glob("*.txt"):
    print(file)

print(8)
## reading and writing file
from pathlib import Path
# create a path object for test.txt
file_path = Path.home()/"python4biz"/"test.txt"
# open file with .open() to return a file object
# "r" represents read mode
file = file_path.open(mode = "r", encoding='UTF-8')
# Print text file will return an instance of the TextIOWrapper class.
print(file)
# use '.close()' to close a file
file.close()

print(9)
from pathlib import Path
file_path = Path.home()/"python4biz"/"test.txt"
# return value of file open is assigned to variable 'file' after as keyword
with file_path.open(mode="r",encoding="UTF-8") as file:
    # .read() reads the text in the textfile and returns the texts as a string in python output
    text = file.read()
print(text)
print(type(text))

print(10)
from pathlib import Path
file_path = Path.home()/"python4biz"/"test.txt"
with file_path.open(mode="r",encoding="UTF-8") as file :
    # .readlines() returns an iterable of lines from the file which allows a for loop to work
    for line in file.readlines():
        print(line)   

print(11)
from pathlib import Path
# create a path object for contacts.txt
file_path = Path.home()/"python4biz"/"contacts.txt"
with file_path.open(mode = "w") as file:
    file.write("Name: John \nAge: 19")

print(12)
from pathlib import Path
# create a path object for contacts.txt
file_path = Path.home()/"python4biz"/"contacts.txt"
# use mode ="a" to append data to file
with file_path.open(mode = "a") as file:
    file.write("\nGender: Male")

print(13)
from pathlib import Path
new_data = ["\n","Weight: 78","\n", "Height: 176"]
# create a path object for contacts.txt
file_path = Path.home()/"python4biz"/"contacts.txt"
with file_path.open(mode = "a") as file:
    # write multiple lines using .writelines()
    # but seperation of lines needs to be done manually using \n
    file.writelines(new_data)

print(14)
from pathlib import Path
import csv
file_path = Path.home()/"python4biz"/"dbs_shares.csv"
file_path.touch()
print(file_path.exists())
# 5 days of trading prices
# Each sublist contains 3 elements : Day, Opening Price, Closing Price
dbs_shares_price = [[1, 12.32, 11.2], [2, 12.31, 11.5], [3, 12.42, 11.6], [4, 12.52, 11.7], [5, 12.32, 12.85]]

# open the file
with file_path.open(mode = "w", encoding = "UTF-8", newline="") as file:
    # Create a writer object with csv.writer(). This will return a CSV writer object with methods for writing data to the CSV file.
    writer = csv.writer(file)
    # use .writerow() to write headers
    writer.writerow(["Day","Opening_Price","Closing_Price"])
    # Use .writerow() to write single line and iterate over a for loop
    for sublist in dbs_shares_price:
        writer.writerow(sublist)

# 1.Import Path function from pathlib 
from pathlib import Path
# Import csv module
import csv
file_path = Path.home()/"python4biz"/"dbs_shares.csv"
# create 'reader' object and print line if file path exists
with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file:
    # instantiate a reader object
    reader = csv.reader(file)
    next(reader)
# Print each lix returns each row as a list
    for line in reader:
        print(line)
    
# 1.Import Path function from pathlib 
from pathlib import Path
# Import csv module
import csv
empty_list = []
file_path = Path.home()/"python4biz"/"dbs_shares.csv"
# create 'reader' object and print line if file path exists
with file_path.open(mode = "r",encoding = "UTF-8", newline="") as file:
    # instantiate a read object
    reader = csv.reader(file)
    # use `next()` to skip the header.
    next(reader)
# Print each line returns each row as a list
# Header is skipped due to `next()` before for loop
    for line in reader:
        print(line)
        for value in line:
            empty_list.append(value)
print(empty_list)