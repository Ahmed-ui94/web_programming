PEOPLE = [
    {'first': 'Reuven', 'last': "Lerner", 'email': 'reuven@lerner.co.il'},
    {'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
    {'first': 'vladamir', 'last': 'Putin', 'email': 'president@kremavax.ru'}

]
def get_first_last(person):
    return person['last'], person['first']
#using lambda function to sort the listed dictionary
for i in sorted(PEOPLE, key=lambda person: (person['last', ['first']])):
    print(f'{i["last"]} {i["first"]}: {i["email"]}')