birthdays = {'Chris': 'June 30th 1991', 'Van': 'September 1st 1996', 'Joseph': 'January 22nd 1995', 'Steve': 'January 3rd 1943', 'Kara': 'November 30th 1970', 'Duy': 'July 4th 1999', 'B': 'July 4th 1999', 'Our Relationship': 'July 7th 2017'}

while True:
    print('Please enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
         print('No Birthday information for that person')
         print('What is their Birthday?')
         bday = input()
         birthdays[name] = bday
         print('Birthday data has been updated!')
        
