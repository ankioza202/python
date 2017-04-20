from operator import attrgetter

class Users:
    def __init__(self,x,y):
        self.name = x
        self.user_id = y
    def __repr__(self):
        return self.name + " : "+str(self.user_id)


users = [
    Users('Chris',67),
    Users('Ankita',34),
    Users('Phil',5),
    Users('Christina',90),
    Users('Mo',56)
]

for user in users:
    print(user)

print("-------")

for user in sorted(users,key=attrgetter('name')):
    print(user)

print("-------")

for user in sorted(users, key=attrgetter('user_id')):
    print(user)