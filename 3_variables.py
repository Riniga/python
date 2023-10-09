an_integer = 5
a_float = 3.14
a_string = "En sträng av tecken"
a_complex = 1j
a_boolean = True
some_bytes = b"Hello"
a_nothing = None
a_bytearray = bytearray(5) # bytearray with five bytes
a_memoryview = memoryview(bytes(5)) # An object with reference to the memory

import datetime
now = datetime.datetime.now()

print(type(a_nothing))
print()
print (bytearray(a_boolean))

#casting
to_int = int(4.2)
to_float = float("4.2")
to_string = str(3.14)



