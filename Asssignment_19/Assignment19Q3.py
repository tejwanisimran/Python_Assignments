####################################################################
#
# Description : . Write a program which contains filter(), map() and
#                 reduce() in it.
#                 Python application which contains one list of numbers.
#                 List contains the numbers which are accepted from user.
#                 Filter should filter out all such numbers which are 
#                 greater than or equal to 70 and less than or equal to 90.
#                 Map function will increase each number by 10.
#                 Reduce will return product of all that numbers.
# Input List  : [4,34,36,76,68,24,89,23,86,90,45,70] 
# List after filter  : [76,89,86,90,70]
# List after map : [86,99,96,100,80]
# Output of reduce : 6538752000
#
####################################################################

from functools import reduce

####################################################################
#
# LambdaFunctionName : Filter
# Description  : It is used to filter the elements in the list
# Author       : Simran Naveen Tejwani
# Date         : 26/01/2026
#
####################################################################

Filter = lambda iNo : (iNo >= 70 and iNo <= 90)

####################################################################
#
# LambdaFunctionName : Increment
# Description  : It is used to increase the whole list by 10
# Author       : Simran Naveen Tejwani
# Date         : 26/01/2026
#
###################################################################

Increment = lambda iNo : iNo + 10

####################################################################
#
# LambdaFunctionName : Product
# Description  : It is used to return the product of whole list
# Author       : Simran Naveen Tejwani
# Date         : 26/01/2026
#
###################################################################

Product = lambda iNo1 , iNo2 : iNo1 * iNo2

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iSize = 0
    iValue = 0
    FData = 0
    MData = 0
    RData = 0

    Arr = list()

    print("Enter the number of elements :  ")
    iSize = int(input())

    print("Enter the elements : ")

    for iCnt in range(iSize):
        iValue = int(input())
        Arr.append(iValue)

    FData = list(filter(Filter , Arr))
    print("Data after filter is : ",FData)

    MData = list(map(Increment , FData))
    print("Data after map is : ",MData)

    RData = reduce(Product , MData)
    print("Data after reduce is : ",RData)
    
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 