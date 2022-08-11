import csv
import sys

def main():
    path1, path2 = user_input()
    convertor(path1, path2)


def user_input():
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif '.csv' not in sys.argv[1] or '.csv' not in sys.argv[2]:
        sys.exit("file is not a csv file")
    else:
        path = sys.argv[1:]
   
    return path


def convertor(path1, path2):
    with open(path1, "r") as file:
        files = csv.DictReader(file)

        with open(path2, 'w') as writer:
            fieldname = ["first", "last", "house"]
            csv_writer = csv.DictWriter(writer, fieldnames=fieldname)
            csv_writer.writeheader()

            for line in files:
                line1 = line['name'].split(',')
                csv_writer.writerow({'first': line1[1], 'last':line1[0], 'house': line['house']})


if __name__ == "__main__":
    main()