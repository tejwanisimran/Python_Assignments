####################################################################
#
# Description : Write a program which accept N Numbers from the
#               user & store it into a list . Return minimum of 
#               all elements from the list
# Input       : Number of elements : 6
#               Enetr elements : 13 5 45 7 4 56
# Output      : 4
#
####################################################################

####################################################################
#
# FunctionName : CheckMinimum
# Description  : It is used to return the minimum of elements
#                in the list
# Author       : Simran Naveen Tejwani
# Date         : 25/01/2026
#
####################################################################

def CheckMinimum(Arr):
    iMin = Arr[0]

    for iCnt in range(len(Arr)):
        if(Arr[iCnt] < iMin):
            iMin = Arr[iCnt]

        
    return iMin

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

    iRet = CheckMinimum(Arr)

    print("Minimum of All elements is : ",iRet)
    
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 