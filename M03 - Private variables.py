# to privatize variables (make them non-accessible to any outside of the class)

class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

# cannot call to variables as it's hidden my dunders
# need getters to fetch data
    def get_name(self):
        return self.__name
    def get_animal_tyle(self):
        return self.__animal_type
    def get_age(self):
        return self.__age
    
    #setters
    def set_name(self, name):
        self.__name = name
    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type
    def set_age(self, age):
        self.__age = age