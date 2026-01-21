####################################################################
#
# Description : Write a lambda function using reduce() which accepts 
#               list of numbers and returns product of all elements
#
####################################################################

from functools import reduce

####################################################################
#
# LambdaFunctionName : Product
# Description  : It is used to product all the elements of the list 
# Author       : Simran Naveen Tejwani
# Date         : 21/01/2026
#
####################################################################

Product = lambda iNo1,iNo2 : iNo1 * iNo2

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

    RData = reduce(Product , Data)

    print("Product of all elements from the list is : ",RData)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 