# Update values in Dictionaries and Lists

x = [ [5,2,3], [15,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Bryant'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Andres', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 30} ]

################################################################################################

#Iterate Through a List of Dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'Kobe', 'last_name' : 'Bryant'}
    ]
def iterateDictionary(students):
    for s in students:
        print('first name -',s['first_name'],',',' last name -',s['last_name'])

print(iterateDictionary(students))



iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - Kobe, last_name - Bryant
################################################################################################

#Get Values From a List of Dictionaries

def iterateDictionary2(key_name, some_list):
    for s in students:
        print(s[key_name])

print(iterateDictionary2('first_name', students))
print(iterateDictionary2('last_name', students))

################################################################################################

#Iterate Through a Dictionary with List Values

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']}

def printInfo(dojo):
    print(len(dojo['locations']), "LOCATIONS")
    for location in dojo['locations']:
        print(location)

    print(dojo)

    print(len(dojo['instructors']), "INSTRUCTORS")
    for instructor in dojo['instructors']:
        print(instructor)

printInfo(dojo)