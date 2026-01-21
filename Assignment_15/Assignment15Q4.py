####################################################################
#
# Description : Write a lambda function using reduce() which accepts 
#               list of numbers and returns addition of all elements
#
####################################################################

from functools import reduce

####################################################################
#
# LambdaFunctionName : Add
# Description  : It is used to sum all the elements of the list 
# Author       : Simran Naveen Tejwani
# Date         : 20/01/2026
#
####################################################################

Add = lambda iNo1,iNo2 : iNo1 + iNo2

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iSize = 0
    iValue = 0
    RData = 0

    print("Enter number of elements : ")
    iSize = int(input())

    Data = list()

    print("Enter the elements : ")

    for iCnt in range(iSize):
        iValue = int(input())
        Data.append(iValue)

    RData = reduce(Add , Data)

    print("Addition of all elements from the list is : ",RData)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 