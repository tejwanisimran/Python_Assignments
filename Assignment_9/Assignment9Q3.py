####################################################################
#
# Description : Write a program which accepts one number & prints
#               square of that number
# Input       : 5
# Output      : 25
#
####################################################################

####################################################################
#
# FunctionName : SquareX()
# Description  : It is used to display the square of the given number
# Author       : Simran Naveen Tejwani
# Date         : 17/01/2026
#
####################################################################

def SquareX(iNo):
    iSquare = 0

    iSquare = iNo * iNo

    return iSquare

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0
    iRet = 0

    print("Enter the number : ",end = "")
    iValue = int(input())

    iRet = SquareX(iValue) 

    print("The square of the given number is :",iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 