import json
from mymodule import person1 as pers
json_string = json.dumps(pers)
python_object = json.loads(json_string)

