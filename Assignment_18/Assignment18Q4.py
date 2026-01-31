####################################################################
#
# Description : Write a program which accept N Numbers from the
#               user & store it into a list . And take one number 
#               from he user and return its frequency in the list
# Input       : Number of elements : 8
#               Enetr elements : 13 5 45 7 5 56 5 52
#               iTarget = 5
# Output      : 3
#
####################################################################

####################################################################
#
# FunctionName : CountFrequency
# Description  : It is used to return the count of number 
#                in the list
# Author       : Simran Naveen Tejwani
# Date         : 25/01/2026
#
####################################################################

def CountFrequency(Arr , iTarget):
    iCount = 0

    for iCnt in range(len(Arr)):
        if(Arr[iCnt] == iTarget):
            iCount = iCount + 1

    return iCount

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iValue = 0
    iTarget = 0
    iSize = 0
    iRet = 0

    print("Enter number of elements : ",end = "")
    iSize = int(input())

    Arr = list()

    print("Enter the elements")

    for iCnt in range(iSize):
        iValue = int(input())
        Arr.append(iValue)

    print("Enter the number whoose frequency you want to search : ",end = "")
    iTarget = int(input())

    iRet = CountFrequency(Arr,iTarget)

    print("Frequency of the number is : ",iRet)
    
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 