#classes can represent real objects with dara that can be changed or modified
# depending on what we need to do with the class instance

#we can also use instance variables
#instance bariables can be set or changed upon the creation of an instance

# class Monkey. attributes - name and animal. Monkey will always have animal = monkey
#However we can change the name of each monkey upon instantiation (creation).

class Monkey:
    #class variable that will NOT change no matter how many copies
    #it can be changed after we create an instance.
    animal = "Monkey"
    #constructor or init - initialize the instance bariable with some data that the user or other parts of the program provide it.
    #Method - function inside of a class or a function that belongs to an object.
    #self - that individual's instance's value or variables

def __init__(self,name):
    self.name = name

    #create monkeys
Monkey1 = Monkey("Tom")
print(Monkey1.animal)
print(Monkey1.name)

Monkey2 = Monkey("Jim")
print(Monkey2.animal)
print(Monkey2.name)