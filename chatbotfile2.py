#Brief example to show modularity through OOPs

#import the user-defined class that we built in the chatbotfile1.py
#from chatbotfile1 import chatbot
from file1 import Employee

#since we have imported the class, we can now create object of the class in this file
#user1 = chatbot()

#similarly create an object from Employee class
obj1 = Employee("Employee 1",101,"Junior Analyst")
print(obj1.name)
#in order to access an encapsulated attribute, need to follow below format
print(obj1._Employee__salary)

