####################################################################
#
# Description : Write a lambda function which accepts 2 numbers
#               and returns Multiplication of that 2 numbers
#
####################################################################

####################################################################
#
# LambdaFunctionName : Multiplication
# Description  : It is used to return the Multiplication of two numbers
# Author       : Simran Naveen Tejwani
# Date         : 21/01/2026
#
####################################################################

Multiplication = lambda iNo1 , iNo2 : iNo1 * iNo2

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue1 = 0
    iValue2 = 0
    iRet = 0

    print("Enter the first number : ")
    iValue1 = int(input())

    print("Enter the second number : ")
    iValue2 = int(input())

    iRet = Multiplication(iValue1 , iValue2)

    print("Multiplication is : ",iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 