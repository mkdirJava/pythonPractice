

class thing:
    def __init__(self,counter, name):
        self.name = name
        self.counter = counter
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
   
    def __eq__(self, other):
        return self.name == other.name
    def __hash__(self):
        return self.counter
        
    

listMe = [thing(1,'home'),thing(2,'time'),thing(1,'home'),thing(4,'now')]

print(listMe)

alreadyThere = thing(1,'s')
#alreadyThere = listMe.__getitem__(0)
print(len(listMe))


if alreadyThere not in listMe:
        print("I am not in the list")
if alreadyThere in listMe:
    print("I am in the list")
            

uniqueCollection = set(listMe)
print(uniqueCollection)
        
