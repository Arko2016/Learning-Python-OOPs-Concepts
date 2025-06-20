#initiate a class
class Employee:
    #special method/magic method/ dunder method/ constructor
    def __init__(self,name,emp_id,designation):
        print("Start object creation")
        #get memory location of self
        print(id(self))
        #assign value to attributes
        self.name = name
        self.emp_id = emp_id
        self.designation = designation
        print("End object creation")
    
    #function 1
    def func_datapull(self, expertise):
        print(f"{self.name} with id {self.emp_id} is a {self.designation}, and is able to perform {expertise} level data pull")
    
#initiate an object of the class
employee1 = Employee("Employee 1",101,"Junior Analyst")
#in addition to defining attributes within the constructor, we can also define attributes of the object outside
employee1.location = "Delhi"
print(f"{employee1.name} resides in {employee1.location}")
#call the function using above object
employee1.func_datapull("basic")
#get memory location of the class object
print(f"Memory location of the class object: {id(employee1)}")

"""
Note:
As seen above, the memory location of self and class object is same.
This denotes that once the class instance (object) is created, it is instantiated by self
Thus, When you create an object from a class, self allows the methods of that class 
to access and manipulate the attributes and other methods belonging to that 
particular object 
"""


