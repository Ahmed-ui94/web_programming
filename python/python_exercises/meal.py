def main():
    time = input("What time is it? ")
    #calling the convert function
    convert(time)

# a function to convert string time to to float and 
# outputing the time for specific activity
def convert(time):
    hours, minutes = time.split(":")
    minutes1 = float(minutes)/60
    time1 = float(hours) + minutes1
    if 8.0>= time1 >= 7.0:
       print("breakfast time")
    elif  13.0 >= time1 >= 12.0:
        print("lunch time")
    elif 19.0 >= time1 >= 18.0:
        print("Dinner time")
    
          



if __name__ == "__main__":
    main()