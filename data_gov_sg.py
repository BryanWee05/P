import requests
url = "https://api.data.gov.sg/v1/environment/pm25?date=2021-08-23"
response = requests.get(url)
print(response)
print(response.headers.get('Content-Type'))

# retrieve data with .json from response and save it as data
data = response.json()

# check data type, which turns out to be a dict
print(type(data))

# Use '.keys()' attribute to retrieve the keys of a dict
print(data.keys())

print("region_metadata.".upper())
print(data["region_metadata"])
print("items".upper())
print(data["items"])
print("api_info".upper())
print(data["api_info"])

import json
print(json.dumps(data["items"],indent = 4))

# assign data["items"] to an object
pm25 = data["items"]

# create a empty list to store 'pm25_one_hourly'
pm_list = []

for item in pm25:
    # store the timestamp in the last index of the hourly data
    item["readings"]["pm25_one_hourly"].update({"timestamp": item["timestamp"]})
    # append the dictionary as item into the empty list
    pm_list.append(item["readings"]["pm25_one_hourly"])

print(pm_list)

from pathlib import Path
import csv

home = Path.home()
filepath = home/'python4biz/pm25_data.csv'
filepath.touch()

# csv.DictWriter( ) is used to create headers in the csv file.

if filepath.exists():
    with filepath.open('w', encoding = 'UTF-8', newline = '') as file:
        writer = csv.DictWriter(file, fieldnames = ['timestamp', 'west', 'east', 'central', 'south', 'north'])
        writer.writeheader()
        writer.writerows(pm_list)
        
    file.close()

else:
    print("file path does not exists")