# -*- coding: utf-8 -*-
"""
Created on Wed May 18 07:51:28 2016

@author: ericgrimson
"""

import datetime

class Person(object):
    def __init__(self, name):
        """create a person called name"""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        """return self's last name"""
        return self.lastName
        
    def setBirthday(self,month,day,year):
        """sets self's birthday to birthDate"""
        self.birthday = datetime.date(year,month,day)

    def getAge(self):
        """returns self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
        
    
    def __lt__(self, other):
        """return True if self's ame is lexicographically
           less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName



    # other methods

    def __str__(self):
        """return self's name"""
        return self.name
        

# example usage

p1 = Person('Mark Zuckerberg')
p1.setBirthday(5,14,84)
p2 = Person('Drew Houston')
p2.setBirthday(3,4,83)
p3 = Person('Bill Gates')
p3.setBirthday(10,28,55)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')


personList = [p1, p2, p3, p4, p5]

for e in personList:
    print(e)
    
personList.sort()

print()

for e in personList:
    print(e)

class MITPerson(Person):
    nextIdNum = 0 # next ID number to assign

    def __init__(self, name):
        Person.__init__(self, name) # initialize Person attributes
        # new MITPerson attribute: a unique ID number
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    # sorting MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum
        
    def speak(self, utterance):
        return (self.name + " says: " + utterance)
        

# example usage

m1 = MITPerson('Mark Zuckerberg')
m1.setBirthday(5,14,84)
m2 = MITPerson('Drew Houston')
m2.setBirthday(3,4,83)
m3 = MITPerson('Bill Gates')
m3.setBirthday(10,28,55)
m4 = Person('Travis Kalanik')
m5 = Person('Steve Wozniak')

#
#MITPersonList = [m1, m2, m3, m4, m5]
#
#for e in personList:
#    print(e)
#    
#personList.sort()
#
#print()
#
#for e in personList:
#    print(e)
    
    

