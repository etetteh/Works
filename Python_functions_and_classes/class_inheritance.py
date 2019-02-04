""" Code to demonstrate inheritance (Object Oriented Programming) """"

class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color
        
        
class Child(Parent):
    def __init__(self, last_name, eye_color, friends):
        print("Child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.friends = friends
    

enoch = Child("Tetteh", "Brown", 29)
print(enoch.last_name)
print(enoch.eye_color)