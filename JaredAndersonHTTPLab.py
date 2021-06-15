#CS2705
#HTTP with python
#Jared Anderson

import requests

#1
r = requests.get("http://Icarus.cs.weber.edu/~dweidman/CS2705HTMLLab.html")

#2
print("Status code is:")
out=r.status_code
print(out)
print()

print("Headers of the website are:")
out=r.headers
print(out)
print()

print("HTML code of the website is:")
out=r.text
print(out)
print()

print('Server type and version are:')
out=r.headers['Server']
print(out)
print()

#3
r = requests.get("http://Icarus.cs.weber.edu/~dweidman/CS2705HTMLLab2.html")

#4
print("Status code is:")
out=r.status_code
print(out)
print()

print("Headers of the website are:")
out=r.headers
print(out)
print()

print("HTML code of the website is:")
out=r.text
print(out)
print()

print('Server type and version are:')
out=r.headers['Server']
print(out)
print()

#5
#The Head Command doesnt request the message body but the GET command does.

#6
#so you can know how to interact with it, if you try to use a HTML5 code with a site that is only HTML it probably wont work

#7
#one just has some text to display and the other seems to be like a login page