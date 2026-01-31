####################################################################
#
# Description : Create one module named as Arithmetic which 
#               contains 4 functions as
#               Add() for addition,
#               Sub() for subtraction,
#               Mult() for multiplication and
#               Div() for division.
#               All functions accept two parameters as numbers and 
#               perform the operation.
#               Write one Python program which calls all the 
#               functions from the Arithmetic module by accepting 
#               the parameters from the user.

####################################################################

import Airthematic

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue1 = 0
    iValue2 = 0
    iRet = 0

    print("Enter first number :",end = "")
    iValue1 = int(input())

    print("Enter second number :",end = "")
    iValue2 = int(input())

    iRet = Airthematic.Add(iValue1,iValue2)
    print("Addition is : ",iRet)

    iRet = Airthematic.Sub(iValue1,iValue2)
    print("Subtraction is : ",iRet)

    iRet = Airthematic.Mult(iValue1,iValue2)
    print("Multiplication is : ",iRet)

    iRet = Airthematic.Div(iValue1,iValue2)
    print("Division is : ",iRet)



####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 