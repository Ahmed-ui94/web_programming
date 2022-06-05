import re, sys
from unicodedata import name


def main():
    print(validate(input("IPv4: ")))

def validate(ip):
    patterun_match = r"^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){3}.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){3}.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){3}.([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]){3}$"
    if matches := re.search(patterun_match,ip):
        return f"valid"
    else:
        return f'invalid'
    
if __name__ == "__main__":
    main()