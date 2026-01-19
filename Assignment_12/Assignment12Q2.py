####################################################################
#
# Description : Write a program which accepts one number & prints
#               its factors
# Input       : 12
# Output      : 1 2 3 4 6 12 
#
####################################################################

####################################################################
#
# FunctionName : DisplayFactors()
# Description  : It is used to display factors of a given 
#                number
# Author       : Simran Naveen Tejwani
# Date         : 18/01/2026
#
####################################################################

def DisplayFactors(iNo):

    print("Factors are : ")

    for iCnt in range(1,iNo+1):
        if(iNo % iCnt == 0):
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

    DisplayFactors(iValue) 

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 