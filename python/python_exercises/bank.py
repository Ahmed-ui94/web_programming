greetings = input("Greetings: ")

if greetings.lower().startswith("hello"):
    print("$0")
elif greetings.lower().startswith('h'):
    print("$20")
else:
    print("$100") 