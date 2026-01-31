####################################################################
#
# Description :  Write a Python program to implement a class named 
#                Arithmetic with the following characteristics:
#                The class should contain two instance variables:
#                Value1
#                Value2
#                Define a constructor (__init__) that initializes 
#                all instance variables to 0.
#                Implement the following instance methods:
#                Accept() – accepts values for Value1 and Value2 
#                from the user.
#                Addition() – returns the addition of Value1 and 
#                Value2.
#                Subtraction() – returns the subtraction of Value1 
#                and Value2.
#                Multiplication() – returns the multiplication of 
#                Value1 and Value2.
#                Division() – returns the division of Value1 and 
#                Value2 (handle division by zero properly).
#                Create multiple objects of the Arithmetic class and 
#                invoke all the instance methods.
#               
####################################################################


####################################################################
#
# ClassName : Airthematic
# Description  : It is used to do all the airthematic operations
# Author       : Simran Naveen Tejwani
# Date         : 30/01/2026
#
###################################################################
class Airthematic:
    
    def __init__(self):
        self.iNo1 = 0
        self.iNo2 = 0

    def Accept(self):

        print("Enter the first number : ")
        self.iNo1 = int(input())

        print("Enter the second number : ")
        self.iNo2 = int(input())

    def Addition(self):
        iAns = 0
        iAns = self.iNo1 + self.iNo2
        return iAns
    
    def Subtraction(self):
        iAns = 0
        iAns = self.iNo1 - self.iNo2
        return iAns
    
    def Multiplication(self):
        iAns = 0
        iAns = self.iNo1 * self.iNo2
        return iAns
    
    def Division(self):
        iAns = 0
        try :
            iAns = self.iNo1 / self.iNo2
        except ZeroDivisionError as zobj:
            print("Error : ",zobj)
        return iAns
        
####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iRet = 0

    aobj1 = Airthematic()
    aobj1.Accept()

    iRet = aobj1.Addition()
    print("Addition is : ",iRet)

    iRet = aobj1.Subtraction()
    print("Subtraction is : ",iRet)

    iRet = aobj1.Multiplication()
    print("Multiplication is : ",iRet)

    iRet = aobj1.Division()
    print("Division is : ",iRet)

    print("------------------------------------------")

    aobj2 = Airthematic()
    aobj2.Accept()

    iRet = aobj2.Addition()
    print("Addition is : ",iRet)

    iRet = aobj2.Subtraction()
    print("Subtraction is : ",iRet)

    iRet = aobj2.Multiplication()
    print("Multiplication is : ",iRet)

    iRet = aobj2.Division()
    print("Division is : ",iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 