#Parent/Base Class
class Animal:
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

#1st Child Class which inherits Base class 
class Dog(Animal):
    """
    define a function with same name as the function in Base Class
    Note: by default, the child class will inherit both the attributes and methods of Parent class
    However, if Child class has a method/attribute with same name as Parent, the Parent's class attributes and methods will be over-written
    Also, since this child class does not have its own constructor, by default parent class constructor is inherited
    """
    def speak(self):
        #name attribute is from parent class
        print(f"{self.name} barks")

#define object of parent class
obj1 = Animal("Animal")
obj1.speak()

#define object of 1st child class
obj2 = Dog("Dog")
#Method overloading occurs since child class method with same over-rides parent class method
obj2.speak()

#2nd Child class showcasing use of super()
class Bull(Animal):
    #Constructor overloading
    def __init__(self,name,breed):
        #using super function the Constructor for Parent class is invoked
        #since parent class constructor required a parameter, the same is provided below
        super().__init__(name)
        #next initialize the attribute for child class using the next parameter
        self.breed = breed
    
    def speak(self):
        print(f"{self.name} belongs to breed {self.breed}")

#define object of the second child class
#2 parameters provided in order for initializing constructors of Parent and Child classes
obj3 = Bull("Bull","Australian")
#Method overloading
obj3.speak()
