####################################################################
#
# Description : Write a program which accepts one number & prints
#               multiplication table of that number
# Input       : 4
# Output      : 4 8 12 16 20 24 28 32 36 40 
#
####################################################################

####################################################################
#
# FunctionName : MultiplicationTable()
# Description  : It is used to print the multiplication table of 
#                the given number
# Author       : Simran Naveen Tejwani
# Date         : 17/01/2026
#
####################################################################

def MultiplicationTable(iNo):
    iMult = 0

    for iCnt in range(1,11,1):
        iMult = iCnt * iNo
        print(iMult)

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0

    print("Enter the number : ",end = "")
    iValue = int(input())

    MultiplicationTable(iValue) 
        
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 