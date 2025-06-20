class MethodTypes:
    #define a class attribute
    people_cnt = 0
    
    #regular instance method -> constructor
    def __init__(self):
        #define instance/regular attribute
        self.regularid = 0
        #update instance attribute
        self.regularid += 1
        #define an encapsulated attribute
        self.__user_id = 0
        #update the encapsulated attribute
        self.__user_id += 1

    
    #class method with a decorator
    @classmethod
    def add_person(cls):
        cls.people_cnt += 1
        return cls.people_cnt
    
    #static method with a decorator
    @staticmethod
    def calculator(num1,num2):
         return num1 + num2
    
    #static method to update class attribute
    @staticmethod
    def set_id(val):
        MethodTypes.people_cnt = val
        return MethodTypes.people_cnt

#create a class object
obj1 = MethodTypes()
print(f"Non-encapsulated object attribute: {obj1.regularid}, Encapsulated object attribute: {obj1._MethodTypes__user_id}")
print(f"Update class attribute using class method: {MethodTypes.add_person()}")

#create a 2nd class object
obj2 = MethodTypes()
print(f"Non-encapsulated object attribute: {obj2.regularid}, Encapsulated object attribute: {obj2._MethodTypes__user_id}")
print(f"Update class attribute using class method: {MethodTypes.add_person()}")
print(f"Non-encapsulated object attribute: {obj2.regularid}, Encapsulated object attribute: {obj2._MethodTypes__user_id}")
print(f"Update class attribute using class method: {MethodTypes.add_person()}")

#update class attribute using static method
MethodTypes.set_id(10)
print(f"Class attribute updated using static method: {MethodTypes.people_cnt}")

#use static method using classname but not creating an instance
print(f"Static method invoked to add 5 + 10 gives {MethodTypes.calculator(5,10)}")


  