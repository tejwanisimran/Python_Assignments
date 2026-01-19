####################################################################
#
# Description : Write a program which accepts one number & prints
#               all odd numbers till that number
# Input       : 11
# Output      : 1 3 5 7 9 11
#
####################################################################

####################################################################
#
# FunctionName : PrintOdd()
# Description  : It is used to print the all odd numbers till that
#                given number
# Author       : Simran Naveen Tejwani
# Date         : 17/01/2026
#
####################################################################

def PrintOdd(iNo):

    for iCnt in range(1,iNo+1):
        if(iCnt % 2 != 0):
            print(iCnt)
        
####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0

    print("Enter the number : ",end = "")
    iValue = int(input())

    PrintOdd(iValue) 

        
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 