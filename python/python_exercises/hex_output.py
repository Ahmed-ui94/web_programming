def hex_output():
    decnum = 0
    hex_num = input("Enter a hex number: ")
    for power, digit in enumerate(reversed(hex_num)):
        decnum += int(hex_num,16) * (16 ** power)
    print(decnum)
hex_output()