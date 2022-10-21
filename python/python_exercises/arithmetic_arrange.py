import operator


def arithmetic_arrange(problems, answers=False):
    for problem in problems:
        values = problem.split(" ")
        if "+" in values[1] or "-" in values[1]:
            if values[0].isdigit and values[2].isdigit:
                if len(values[0]) <= 4 and len(values[2]) <= 4:
                    if len(values[0]) > len(values[2]):
                        dash = "-" * len(values[0]) 
                    else:
                        dash = "-" * len(values[2]) 
                    spaces = " " * (len(values[0]) - len(values[2]))
                    print(f" {values[0]}\n{values[1]}{spaces}{values[2]}\n-{dash}")
                    
                else:
                    print("Error: the digits must be less than 4")
                
            else:
                print("Error: values of operands must digits only")

        else:
            print("Error: only + or - operators are allowed")
        
        # calculate and display the result for each problem
        if answers == True:
            if values[1] == "+":
                print(operator.add(int(values[0]), int(values[2])), end="")
            elif values[1] == "-":
                print(operator.sub(int(values[0]), int(values[2])), end="")
        
        print("    ")

    

list = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
list2 = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
arithmetic_arrange(list2, True)