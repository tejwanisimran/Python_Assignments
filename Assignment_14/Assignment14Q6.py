####################################################################
#
# Description : Write a lambda function which accepts 1 number
#               and returns True if Odd otherwise False
#
####################################################################

####################################################################
#
# LambdaFunctionName : CheckOdd
# Description  : It is used to check whether the given number 
#                is Odd or not
# Author       : Simran Naveen Tejwani
# Date         : 21/01/2026
#
####################################################################

CheckOdd = lambda iNo : (iNo % 2 != 0)

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0
    iRet = 0

    print("Enter the number : ")
    iValue = int(input())

    iRet = CheckOdd(iValue)

    print(iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 