import datetime
now = datetime.datetime.now()
leo = datetime.datetime(2005, 9, 13)
print(now.year)
print(leo.strftime("%A"))
print(now.strftime("%m/%d/%Y, %H:%M:%S"))
