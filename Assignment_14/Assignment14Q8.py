####################################################################
#
# Description : Write a lambda function which accepts 2 numbers
#               and returns addition of that 2 numbers
#
####################################################################

####################################################################
#
# LambdaFunctionName : Addition
# Description  : It is used to return the addition of two numbers
# Author       : Simran Naveen Tejwani
# Date         : 21/01/2026
#
####################################################################

Addition = lambda iNo1 , iNo2 : iNo1 + iNo2

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

    iRet = Addition(iValue1,iValue2)

    print("Addition is : ",iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 