def total(gallons, sickles, knuts):
    return (gallons * 17 + sickles) * 29 + knuts

# unpacking dictionaries with exactly the required number of element
coins = {'gallons': 100, 'sickles': 50, 'knuts': 25}

print(total(**coins), "knuts")