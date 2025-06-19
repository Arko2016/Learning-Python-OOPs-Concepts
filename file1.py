#initiate a class
class Employee:
    #special method/magic method/ dunder method/ constructor
    def __init__(self,name,id,designation):
        print("Start object creation")
        self.name = name
        self.id = id
        self.designation = designation
        print("End object creation")
    
    #function 1
    def func_datapull(self, expertise):
        print(f"{self.name} with id {self.id} is a {self.designation}, and is able to perform {expertise} level data pull")
    
#initiate an object of the class
employee1 = Employee("Employee 1",100,"Junior Analyst")
#call the function using above object
employee1.func_datapull("basic")

