class Employee:
    def __init__(self):
        print(id(self))
        self.id = 123
    def travel(self):
        print("hello world")

obj1 = Employee()