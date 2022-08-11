import sys, tabulate
import csv

# using tabulate module to format dictionary data into table


# main function 
def main():
    path = fileName()[1]
    format_csv_file(path)

#validating user input
def fileName():
    path = sys.argv
    if len(path) != 2:
        sys.exit("Too few command arguments")
    elif not path[1].endswith(".csv"):
        sys.exit("Not csv file")
    
    return path

#function to format csv file
def format_csv_file(path):
    try:
        with open(path, newline='') as file:
            lines = csv.DictReader(file)
            print(tabulate.tabulate(lines, headers="keys",tablefmt="grid"))
            print(lines)
    except FileNotFoundError:
        sys.exit("file not exists")

if __name__ == "__main__":
    main()