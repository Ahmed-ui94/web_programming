from operator import truediv
import re, sys


def main():
    print(validate(input("IPv4: ")))


def validate(ip):
    patterun_match = r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$"
    if matches := re.search(patterun_match, ip):
        list_of_ip = ip.split(".")
        for i in list_of_ip:
            if int(i) < 0 or int(i) > 255:
                return False
            
        return True
    else:
        return False



if __name__ == "__main__":
    main()
