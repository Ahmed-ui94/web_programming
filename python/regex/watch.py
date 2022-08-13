import re
import sys

def main():
    print(parse(input("HTML: ")))

# function to reformat youtube links
def parse(http):
    pattern = r'^<iframe.+src="(https?://)www\.(youtube\.)(com/embed)(/.+?)".+'
    if matches := re.search(pattern, http, re.I):
        match = matches.group(3).replace("com/embed", 'be')
        url = matches.group(1) + matches.group(2) + match + matches.group(4)
        return url
    else:
        return None

if __name__ == "__main__":
    main()