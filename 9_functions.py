def my_function(fname, *kids):
  print("Hello {} these are yur kids: ".format(fname))
  for kid in kids:
    print(kid)
  return len(kids)

no_kids = my_function("Rickard", "Leo", "Felix")
print("you have {} kids".format(no_kids))

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))



def callbackFunc(age):
    print('the string length is: ', age)
def printFileLength(a_string, callback):
    the_length = len(a_string)
    callback(the_length)
printFileLength("a quit simple but nice string", callbackFunc)