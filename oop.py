class OOP:
    def __init__(self, name):
        self.__name = None  # Initialize the private variable

        print(self.__name)  # Print the initial value (which is None)
        self.Setname(name)  # Call Setname method

    def Setname(self, name):
        self.__name = name

    def getName(self):
        return self.__name
class MyClass:
    def __init__(self):
        self.__private_var = 42
        name=10

    def __private_method(self):
        print("This is a private method.")
        print(self.name)

    def set_private_var(self, value):
        self.__private_var = value

class A(MyClass):
    def __init__(self, name):
        super().__init__()
        print("here")
        print(self.name)
        self.set_private_var(10)
# Creating an instance of the subclass A
a = A('example')

# Accessing the modified private variable using a public method
print(a._MyClass__private_var)  # Outputs: 10

obj = MyClass()
print(obj._MyClass__private_var) 
print(obj._MyClass__private_var)
# Outputs: 42
obj._MyClass__private_method()  # Outputs: "This is a private method."

    