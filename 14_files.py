import json
from mymodule import person1 as pers

file = open("person.json", "wt") #(r)ead, (a)ppend, (w)rite, create(x) (t)ext/(b)inary
json_string = json.dumps(pers)
file.write(json_string)
file.close()


file = open("person.json")
json_string = file.read()
person = json.loads(json_string)
file.close()
print(person["name"])

import os
os.remove("person.json")