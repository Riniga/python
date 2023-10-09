a = 200
b = 33
c = 222
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

if a > b and c > a: print("Both conditions are True")
if a > b or a > c: print("At least one of the conditions is True")
if a > b: print("a is greater than b")
if not a > b: print("a is NOT greater than b")

print("A") if a > b else print("B")
print("A") if a > b else print("=") if a == b else print("B")

lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")
    case "Python":
        print("You can become a Data Scientist")
    case "C#":
        print("You can become a backend developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")