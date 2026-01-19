####################################################################
#
# Description : Write a program which accepts one number & prints 
#               binary equivalent
# Input       : 10
# output      : 1010
#
####################################################################

####################################################################
#
# FunctionName : DisplayBinary()
# Description  : It is used to display binary equivalent of a 
#                given number
# Author       : Simran Naveen Tejwani
# Date         : 19/01/2026
#
####################################################################

def DisplayBinary(iNo):
    iDigit = 0
    iRev = 0
    binary = list()

    while(iNo != 0):
        iDigit = iNo % 2
        binary.append(str(iDigit))
        iNo = iNo // 2

    #print(binary)
    print("".join(binary[::-1]))

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0

    print("Enter the number : ",end = "")
    iValue = int(input())

    DisplayBinary(iValue)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 