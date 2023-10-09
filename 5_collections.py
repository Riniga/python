a_list = ["apple", "banana", 3.14]
print(len(a_list))
print(type(a_list))
another_list = list((1,1,2,3,5,8,13)) # note the double round-brackets
a_bytearray = bytearray(another_list) 
print(a_bytearray)

a_tuple = ("apple", "banana",  3.14)
another_tuple = tuple(("apple", "banana",  3.14)) 

a_range  = range(6) # a list (as range) from 0 to 5

a_set = {"apple", "banana", "cherry",5, 7, 9, 3, False,5}
a_set.add(3.14)
a_set.remove(7)
another_set = set(("apple", "banana", "cherry")) # note the double round-brackets
a_frozen_set = frozenset(("apple", "banana", "cherry",5, 7, 9, 3, False,5)) #immutable
print(a_set)
print(a_frozen_set)

a_dictionary = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(a_dictionary["brand"])
print(len(a_dictionary))
print(type(a_dictionary))
another_dictionary  = dict(name = "John", age = 36, country = "Norway")