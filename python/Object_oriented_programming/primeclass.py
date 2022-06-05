class Primefactors:
    def __init__(self,start, end):
        self.start = start
        self.end = end
    #function to check whether prime factors
    def prime_checker(self):
        for num in range(self.start,self.end+1):
            if num >1:
                for i in range(2,num):
                    if num %i==0:
                        break
                else:
                    print(num)
def main():
    start = int(input("start: "))
    end = int(input("End: "))

    Myprime_numbers = Primefactors(start,end)
    return Myprime_numbers.prime_checker()

if __name__ == "__main__":
    main()
        