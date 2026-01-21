####################################################################
#
# Description : Write a lambda function using reduce() which accepts 
#               list of numbers and returns minimum element
#
####################################################################

from functools import reduce

####################################################################
#
# LambdaFunctionName : CheckMinimum
# Description  : It is used to check the minimum numbers from the list
# Author       : Simran Naveen Tejwani
# Date         : 21/01/2026
#
####################################################################

CheckMinimum = lambda iNo1,iNo2 : iNo1 if iNo1 < iNo2 else iNo2

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

    RData = reduce(CheckMinimum , Data)

    print("minimum of all elements from the list is : ",RData)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 