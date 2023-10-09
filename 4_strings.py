import datetime

multiline_string = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit."""
a_string = "Hello, World!"
print(a_string[1]) # as an array
print("ipsum" in multiline_string)
print("Universe" not in a_string)

print(multiline_string[2:5])
print(multiline_string[:5])
print(multiline_string[5:])

print(a_string.upper())
print(a_string.lower())
print(a_string.strip())
print(a_string + str(36))

a_string = "I want {} pieces of item {} for {} dollars."
print(a_string.format(3, 567, 49.95))

now = datetime.datetime.now()
print(now.strftime("%m/%d/%Y, %H:%M:%S"))

import locale
locale.setlocale(locale.LC_ALL, '')
print(locale.currency(12345.67, grouping=True))

print(f'{12345.9876:,}'  )
print("%.2f" % 12345.9876)

txt = "We are the so-called \"Vikings\" from the north."
escape = " \", \', \\, \n, \r, \t,  \b \f \157 \xf0  " 
print(escape);