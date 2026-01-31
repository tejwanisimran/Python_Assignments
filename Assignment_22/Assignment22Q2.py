####################################################################
#
# Description :  Write a Python program to implement a class named
#                Circle with the following requirements:
#                The class should contain three instance variables:
#                Radius
#                Area
#                Circumference
#                The class should contain one class variable named 
#                PI , initialized to 3.14.
#                Define a constructor (__init__) that initializes 
#                all instance variables to 0.0.
#                Implement the following instance methods:
#                Accept() – accepts the radius of the circle from 
#                the user.
#                CalculateArea() – calculates the area of the circle 
#                and stores it in the Area variable.
#                CalculateCircumference() – calculates the circumference 
#                of the circle and stores it in the Circumference variable.
#                Display() – displays the values of Radius, Area, and 
#                Circumference.
#                Create multiple objects of the Circle class and invoke all 
#                the instance methods for each object.
#               
####################################################################


####################################################################
#
# ClassName : Circle
# Description  : It is used calculate the operations on circle
# Author       : Simran Naveen Tejwani
# Date         : 30/01/2026
#
###################################################################
class Circle:
    PI = 3.14

    def __init__(self):
        self.radius = 0.0
        self.area = 0.0
        self.circumference = 0.0

    def Accept(self):
        print("enter the radius : ")
        self.radius = float(input())

    def CalculateArea(self):
        self.area = Circle.PI * self.radius * self.radius

    def CalculateCircumference(self):
        self.circumference = 2 * Circle.PI * self.radius

    def Display(self):
        print(f"Value of radius is : {self.radius}")
        print(f"Value of area is : {self.area}")
        print(f"Value of circumference is : {self.circumference}")
        
####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    cobj1 = Circle()
    cobj1.Accept()
    cobj1.CalculateArea()
    cobj1.CalculateCircumference()
    cobj1.Display()

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 