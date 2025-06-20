#define class
class Employee:
    def __init__(self):
        self.emp_id = 101
        #this is an encapsulated attribute
        self.__name = "Default User"
    
    #getter function
    def get_name(self):
        return self.__name
    
    #setter function
    def set_name(self,value):
        self.__name = value

"""    
#define class object
obj1 = Employee()
#get the default assigned value of the encapsulated attribute using below format
print(obj1._Employee__name)
#Python allows changing value of encapsulated attribute
obj1._Employee__name = "xyz"
#get the updated value of the encapsulated attribute
print(obj1._Employee__name)
"""