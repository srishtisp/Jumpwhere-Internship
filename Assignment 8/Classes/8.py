# 8) Write a python class which has 2 methods get_string and print_string. get_string takes a string from the user and print_string prints the string in reverse order

class StringManipulator:
    def __init__(self):
        self.user_string = ""

    def get_string(self):
        self.user_string = input("Enter a string: ")

    def print_string(self):
        print(self.user_string[::-1])

manipulator = StringManipulator()
manipulator.get_string()       
manipulator.print_string()     
