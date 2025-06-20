#import class from another file
from getter_setter_example1 import Employee

#define an object of the imported class
obj1 = Employee()

#use the getter function to get value of encapsulated object
print(f"Default value of encapsulated attribute: {obj1.get_name()}")

#use setter method to update value of encapsulated object
obj1.set_name("ABC")
#print the updated value
print(f"New value of encapsulated attribute: {obj1.get_name()}")
