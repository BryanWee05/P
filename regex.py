import re
target_string = "The price of a PINEAPPLE ice cream is 20 dollars. \nThe price of a PINEAPPLE is 10 dollars. \nThe price of an APPLE is 5 dollars. \nThe price of an ORANGE is 4 dollars"
print(target_string)
print(re.findall(pattern="[A-Z]*",string=target_string))








# match_obj = re.search(pattern="PINEAPPLE",string=target_string)
# print(match_obj.group())
# Search for keyword
# if re.search(pattern="PINEAPPLE",string=target_string) is not None:
#     match_obj = re.search(pattern="PINEAPPLE",string=target_string)
#     print(match_obj.group())
# else:
#     print("Match not found")

