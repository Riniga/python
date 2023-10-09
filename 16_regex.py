import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
x = re.findall("ai", txt)
print(x)
x = re.split("\s", txt)
print(x)
