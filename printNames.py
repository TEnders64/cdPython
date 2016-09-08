
# This is the given list of dictionaries


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

# This portion prints out the first name and last name of each array index

def printNames(arr):

    # for loops through the array
    for i in range(len(arr)):
        # Accesses the keys and concatenates the first_name and last_name then prints
        print arr[i]['first_name'] + ' ' + arr[i]['last_name']

printNames(students)

# This is a given list of dictionaries

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

#  Function that prints the name, ID, and number of characters in each combined name):
def printNames2(users):

    #For loop cycles through the dictionary
    for key in users:

        #prints the key
        print key

        #For loop cycles through the dictionary
        for i in range(len(users[key])):
            fname = users[key][i]['first_name']
            lname = users[key][i]['last_name']
            #contactenates index, full_name, last_name, len(fullname + ' ' + last_name) and prints
            #print "%s - %s %s - %s" % (str(i+1), users[key][i]['first_name'], users[key][i]['last_name'], str(len(users[key][i]['first_name'] + users[key][i]['last_name'])))
            #print str(i+1) + ' - ' + users[key][i]['first_name'] + ' ' + users[key][i]['last_name'] + ' - ' + str(len(users[key][i]['first_name'] + users[key][i]['last_name']))
            print str(i+1) + ' - ' + fname + ' ' + lname + ' - ' + fname + ' ' + lname

printNames2(users)
