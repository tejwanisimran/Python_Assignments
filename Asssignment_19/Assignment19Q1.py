####################################################################
#
# Description : Write a program which contains one lambda function
#               which accepts one parameter and return power of 2
# Input       : 4
# Output      : 16
#
####################################################################

####################################################################
#
# LambdaFunctionName : Power
# Description  : It is used to return the power of 2 of the 
#                given number
# Author       : Simran Naveen Tejwani
# Date         : 25/01/2026
#
####################################################################

Power = lambda iNo : iNo ** 2

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0
    iRet = 0

    print("Enter number : ",end = "")
    iValue = int(input())

    iRet = Power(iValue)

    print("Power is : ",iRet)
    
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 