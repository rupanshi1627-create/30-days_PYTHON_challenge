#basic code to understand class and object
# class is just the blueprint of the object and object is the instance of the class.

#code

class Dog: #class: This is a special keyword in Python. It tells the computer: "Hey, I am about to define a new blueprint. Get ready."
    #Dog: This is the name of our blueprint. By convention, class names always start with a Capital Letter.
    def __init__(self,name,breed): #this is a special method called the constructor. It is automatically called when we create a new object of the class. It is used to initialize the attributes of the class.
        self.name=name
        self.breed=breed

    def bark(self): #because it is a method of the class dog, it takes self as an argument, self is the instance of the class dog
        print("woof!") #return and print both can be used in the method but print is used to display the output and return is used to return the value to the caller.
        # Accessing their data (attributes)
        # We press the cookie cutter twice to make two unique dog objects
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Rocky", "German Shepherd")
    
print(dog1.name)
print(dog2.breed)
    