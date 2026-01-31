####################################################################
#
# Description : Write a program which contains one function named as 
#               Add() which accept 2 numbers from user & return 
#               the addition of 2 numbers
# Input       : 11 10
# Output      : 21
#
####################################################################

####################################################################
#
# FunctionName : Add
# Description  : It is used to return the addition of 2 numbers
# Author       : Simran Naveen Tejwani
# Date         : 23/01/2026
#
####################################################################

def Add(iNo1 , iNo2):
    iAns = 0

    iAns = iNo1 + iNo2

    return iAns

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

    iRet = Add(iValue1 , iValue2)

    print("Addition is : ",iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 