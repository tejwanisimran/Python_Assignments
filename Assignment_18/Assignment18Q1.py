####################################################################
#
# Description : Write a program which accept N Numbers from the
#               user & store it into a list . Return addition of 
#               all elements from the list
# Input       : Number of elements : 6
#               Enetr elements : 13 5 45 7 4 56
# Output      : 130
#
####################################################################

####################################################################
#
# FunctionName : SumElements
# Description  : It is used to return the sum of all the elements 
#                in the list
# Author       : Simran Naveen Tejwani
# Date         : 25/01/2026
#
####################################################################

def SumElements(Arr):
    iSum = 0

    for iCnt in range(len(Arr)):
        iSum = iSum + Arr[iCnt]
    
    return iSum

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0
    iSize = 0
    iRet = 0

    print("Enter number of elements : ",end = "")
    iSize = int(input())

    Arr = list()

    print("Enter the elements")

    for iCnt in range(iSize):
        iValue = int(input())
        Arr.append(iValue)

    iRet = SumElements(Arr)

    print("Sum of All elements is : ",iRet)
    
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 