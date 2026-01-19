####################################################################
#
# Description : Write a program which accepts one number & prints
#               reverse of that number
# Input       : 123
# Output      : 321
#
####################################################################

####################################################################
#
# FunctionName : ReverseNumber()
# Description  : It is used to print the reverse of the given 
#                number 
# Author       : Simran Naveen Tejwani
# Date         : 17/01/2026
#
####################################################################

def ReverseNumber(iNo):
    iDigit = 0
    iRev = 0

    while(iNo != 0):
        iDigit = iNo % 10
        iRev = iRev * 10 + iDigit
        iNo = iNo // 10

    return iRev

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

    iRet = ReverseNumber(iValue) 

    print("Reverse of given number is : ",iRet)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 