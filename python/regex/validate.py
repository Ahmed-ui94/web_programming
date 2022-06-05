import re
#take email input from the user
email = input("What's your email? ").strip()

# validating the input using regular expression
#validating the input
if re.search("^\w+@(\w+\.)?\w+\.edu$", email, flags=re.I):
    print("valid")
else:
    print("invalid")