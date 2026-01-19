####################################################################
#
# Description : Write a program which accepts one number & prints
#               all even numbers till that number
# Input       : 10
# Output      : 2 4 6 8 10
#
####################################################################

####################################################################
#
# FunctionName : PrintEven()
# Description  : It is used to print the all even numbers till that
#                given number
# Author       : Simran Naveen Tejwani
# Date         : 17/01/2026
#
####################################################################

def PrintEven(iNo):

    for iCnt in range(1,iNo+1):
        if(iCnt % 2 == 0):
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

    PrintEven(iValue) 

        
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 