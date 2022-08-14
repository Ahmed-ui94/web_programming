import email
import validators

#validating email using validators library
def main():
    email = input("Email: ")
    if validators.email(email):
        return f'valid'
    else:
        return f'invalid'


if __name__ == "__main__":
    print(main())