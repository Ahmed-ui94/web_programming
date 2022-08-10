import sys

def main():
    path = command_argument()   
    print(readlines(path))

# function to count the number of lines in a file
def readlines(path):
    count = 0

    try: 
        with open(path, 'r') as file:
            line = file.readlines()
            for i in line:
                if i.startswith("#") or i in ("\n") or i.startswith('"""'):
                    continue
                else:
                    count += 1
    except FileNotFoundError:
        sys.exit("file not found in the directory")
    return (count)

# getting the proper file name
def command_argument():
    path = sys.argv
    if len(path) != 2:
        sys.exit("Too few command arguments")
    elif not path[1].endswith(".py"):
        sys.exit("Not a python file")
    
    return path

if __name__ == "__main__":
    main()