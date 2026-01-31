####################################################################
#
# Description :  Write a Python program to implement a class named 
#                Demo with the following specifications:
#                The class should contain two instance variables:
#                no1 and no2.
#                The class should contain one class variable named 
#                Value.
#                Define a constructor (__init__) that accepts two 
#                parameters and initializes the instance variables.
#                Implement two instance methods:
#                Fun() – displays the values of instance variables 
#                no1 and no2.
#                Gun() – displays the values of instance variables 
#                no1 and no2.
#                Create two objects of the Demo class as follows:
#                Obj1 = Demo(11, 21)
#                Obj2 = Demo(51, 101)
#                Call the instance methods in the given sequence:
#                Obj1.Fun()
#                Obj2.Fun()
#                Obj1.Gun()
#                Obj2.Gun()
#               
####################################################################


####################################################################
#
# ClassName : Demo
# Description  : It is used for the demo purpose of OOP
# Author       : Simran Naveen Tejwani
# Date         : 30/01/2026
#
###################################################################
class Demo:

    iValue = 0

    def __init__(self,iNo1 , iNo2):
        self.iNo1 = iNo1
        self.iNo2 = iNo2

    def Fun(self):
        print(f"Values from Fun are : {self.iNo1} & {self.iNo2}")

    def Gun(self):
        print(f"Values from Gun are : {self.iNo1} & {self.iNo2}")

        
####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    dobj1 = Demo(11,21)
    dobj2 = Demo(51,101)

    dobj1.Fun()
    dobj2.Fun()
    dobj1.Gun()
    dobj2.Gun()

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 