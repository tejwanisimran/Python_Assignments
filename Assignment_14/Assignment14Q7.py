####################################################################
#
# Description : Write a lambda function which accepts 1 number
#               and returns True if divisible by 5
#
####################################################################

####################################################################
#
# LambdaFunctionName : CheckDivisible
# Description  : It is used to check whether the given number 
#                is Divisible or not
# Author       : Simran Naveen Tejwani
# Date         : 21/01/2026
#
####################################################################

CheckDivisible = lambda iNo : (iNo % 5 == 0)

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

    iRet = CheckDivisible(iValue)

    print(iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 