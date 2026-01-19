####################################################################
#
# Description : Write a program which accepts one number & prints
#               Factorial of that number
# Input       : 5
# Output      : 120
#
####################################################################

####################################################################
#
# FunctionName : Factorial()
# Description  : It is used to print the factorial of the 
#                given number
# Author       : Simran Naveen Tejwani
# Date         : 17/01/2026
#
####################################################################

def Factorial(iNo):
    iFact = 1

    for iCnt in range(1,iNo+1):
        iFact = iFact * iCnt
        
    return iFact

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

    iRet = Factorial(iValue) 

    print("Factorial ofthe given number is :",iRet)
        
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 