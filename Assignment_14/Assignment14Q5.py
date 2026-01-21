####################################################################
#
# Description : Write a lambda function which accepts 1 number
#               and returns True if even otherwise False
#
####################################################################

####################################################################
#
# LambdaFunctionName : CheckEven
# Description  : It is used to check whether the given number 
#                is even or not
# Author       : Simran Naveen Tejwani
# Date         : 21/01/2026
#
####################################################################

CheckEven = lambda iNo : (iNo % 2 == 0)

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

    iRet = CheckEven(iValue)

    print(iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 