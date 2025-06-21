### Topics Covered:
- Class, Object, Attributes and Functions/Methods through a working example
- Understand advantages of OOPs
- Advanced concepts: 
  - Encapsulation
  - Getter and Setter
  - Static method
- Inheritance
  - Example through Code
  - Need for Inheritance
  - What gets Inherited?
  - Constructor Overloading vs Method Overloading
  - Super Keyword
  - Types of Inheritance

### Advantage of having a Constructor
In software development, it helps to define variables or attributes of the class which will usually not be updated by the user of the application

*Note:* While the attributes within class are automatically defined, functions need to be invoked

### Advantages of OOPs:
- Create your own datatype (i.e Class)
- Code reusability through functions
- Easy to debug
- Easy to collaborate

### What is Encapsulation? What are it's uses?
- Encapsulation in Python's Object-Oriented Programming (OOP) refers to the bundling of data (attributes) and methods (functions that operate on the data) within a single unit, which is a class
- Primary Uses:
  - **Data Hiding and Protection:** Encapsulation helps to protect the internal state of an object from direct, unauthorized access and modification from outside the class. This prevents accidental corruption of data and ensures data integrity. However, Python doesnn't strictly impose encapsultion but specifies a specific format to access the attributes
  - **Controlled Access via Getters and Setters:** Instead of allowing direct access to attributes, encapsulation promotes the use of public methods (getters and setters) to access and modify the data
  - **Abstraction:** Encapsulation supports the principle of abstraction by hiding the internal complexities of an object and exposing only the necessary functionalities through its public methods

### Difference and Application of Instance, Class and Static Methods:
- Class methods can be accessed using a class attribute and not by object attribute
- Static methods are outside access of Object instances, but can be accessed using Class name without the need for creating an instance of the class
- For more information on the above refer:
  - [Instance vs Class vs Static Methods](https://www.digitalocean.com/community/tutorials/python-static-method#python-static-method)

### Inheritance:
- Process by which child class can access Constructors, Non-private/Non-encapsulated attributes and methods of the parent class (not the other way around)
- This is beneficial for Code reusability since the child class can use the existing attributes and methods of parent class and also add unique attributes and methods for its own use



