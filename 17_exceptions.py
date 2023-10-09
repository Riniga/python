try:
  print("Hello")
  #raise Exception("Sorry, I just blew up...")
except Exception as exc:
  print("Something went wrong: " + str(exc) )
else:
  print("Nothing went wrong")
finally:
  print("The 'try except' is finished") 