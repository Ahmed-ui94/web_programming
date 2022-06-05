import re

#take url input from the user
url = input("URL: ").strip()
# extracting the username from the url
username = re.sub("^(https?://)?(www\.)?twitter\.com/", "", url)
print(username)
# searching and printing if only the user types the protocols 
# we will use search and condition to check that and print
#if matches := re.search("^https?://(?:www\.)?twitter\.com/(.+)$", url, re.I):
#    print(f"username: {matches.group(1)}")


