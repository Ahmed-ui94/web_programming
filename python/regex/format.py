import re

#format the string of a name using regex
#take input from the user
name = input("What is your name? ").strip()
#lines for checking formating the name
matches = re.search("^(.+), (.+)$",name)
if matches:
    name = matches.group(2)+ " " + matches.group(1)

print(f"hello, {name}")
#using another way to format the name using a new python syntax 
# the syntax called := which is used for checking as well as asign
if matches :=re.search("^(.+), *(.+)$",name):
    name = matches.group(2) + " " + matches.group(1)