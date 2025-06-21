#Single Inheritance
print("Single level Inheritance\n")

#base class
class Parent:
    def __init__(self,name):
        self.name = name
    
    def greet(self):
        print(f"Hello, the person's name is {self.name}")

#child class
class Child(Parent):
    def __init__(self,name):
        #initialize the Constructor of parent class
        super().__init__(name)
        #invoke parent class method
        super().greet()

    def greet(self,language):
        print(f"{self.name} speaks {language}")

#parent class object
obj1 = Parent("Jane")
obj1.greet()

#child class object
obj2 = Child("John") # takes argument for Parent class constructor
obj2.greet("English") #argument for child class method

######################################################################

#Multilevel Inheritance

print("\nMulti-level Inheritance\n")

#Base class
class Grandparent:
    def __init__(self,name):
        self.name = name
    
    def tell_story(self):
        print(f"{self.name} tells stories")

#Intermediate class
class Parent(Grandparent):
    
    def working(self):
        print(f"{self.name} is working")

#Child class
class Children(Parent):

    def playing(self):
        print(f"{self.name} is playing")

#create child object
obj = Children("Charlie") #used to initialize the Contructor attribute of Parent class
obj.tell_story()
obj.working()
obj.playing()

######################################################################

#Hierarchial Inheritance

print("\nHierarchial Inheritance\n")

#base class
class Parent:
    def __init__(self,name):
        self.name = name
    
    def greet(self):
        print(f"hello this is {self.name}")

#1st child class
class Child1(Parent):

    def study(self):
        print(f"{self.name} is studying")

#2nd child class
class Child2(Parent):

    def play(self):
        print(f"{self.name} is playing")

#define child1 object
obj1 = Child1("Alice")
obj1.greet()
obj1.study()

#define child2 object
obj2 = Child2("Candy")
obj2.greet()
obj2.play()


######################################################################

#Multiple Inheritance
print("\nMultiple Inheritance\n")

#base class
class A:
    def __init__(self,name):
        self.name = name
    
    def greet(self):
        print(f"Hello from A, {self.name}")

#Intermediate class 1
class B(A):

    def greet(self):
        print(f"Hello from B, {self.name}")
        super().greet()

#Intermediate class 2
class C(A):

    def greet(self):
        print(f"Hello from C, {self.name}")
        super().greet()

#Child class
class D(B,C):

    def greet(self):
        print(f"Hello from D, {self.name}")
        super().greet() 

#create object of Child class
obj = D("Frank")
obj.greet()