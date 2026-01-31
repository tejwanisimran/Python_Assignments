####################################################################
#
# Description : Write a program which contains one lambda function
#               which accepts 2 parameters and return its 
#               multiplication
# Input       : 4 3 
# Output      : 12
#
####################################################################

####################################################################
#
# LambdaFunctionName : Multiplication
# Description  : It is used to return the Multiplication of 2 of the 
#                given numbers
# Author       : Simran Naveen Tejwani
# Date         : 25/01/2026
#
####################################################################

Multiplication = lambda iNo1,iNo2 : iNo1 * iNo2 

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue1 = 0
    iValue2 = 0
    iRet = 0

    print("Enter first number : ",end = "")
    iValue1 = int(input())

    print("Enter second number : ",end = "")
    iValue2 = int(input())

    iRet = Multiplication(iValue1, iValue2)

    print("Multiplication is : ",iRet)
    
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 