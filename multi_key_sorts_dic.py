from operator import itemgetter

users= [
    {'fname':'Bhavesh', 'lname':'Patel'},
    {'fname': 'Ankita', 'lname': 'Oza'},
    {'fname': 'Ankita', 'lname': 'Patel'},
    {'fname': 'Ankita', 'lname': 'Bruke'},
    {'fname': 'Dhiren', 'lname': 'Oza'},
    {'fname': 'Pooja', 'lname': 'Prajapati'},
    {'fname': 'Phil', 'lname': 'Hagen'},
    {'fname': 'Chris', 'lname': 'Bruke'},

]

for x in sorted(users, key=itemgetter('fname')):
    print(x)

print("--------")

for x in sorted(users, key=itemgetter('fname','lname')):
    print(x)