####################################################################
#
# Description : Write a program which accepts one number & prints
#               cube of that number
# Input       : 2
# Output      : 8
#
####################################################################

####################################################################
#
# FunctionName : CubeX()
# Description  : It is used to display the cube of the given number
# Author       : Simran Naveen Tejwani
# Date         : 17/01/2026
#
####################################################################

def CubeX(iNo):
    iCube = 0

    iCube = iNo * iNo * iNo

    return iCube

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

    iRet = CubeX(iValue) 

    print("The cube of the given number is :",iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 