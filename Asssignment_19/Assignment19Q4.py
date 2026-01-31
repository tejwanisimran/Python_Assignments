####################################################################
#
# Description : . Write a program which contains filter(), map() 
#                 and reduce() in it. Python application which 
#                 contains one list of numbers. List contains the 
#                 numbers which are accepted from user. Filter should 
#                 filter out all such numbers which are even. 
#                 Map function will calculate its square. Reduce 
#                 will return addition of all that numbers.
# Input List  : [5,2,3,4,3,4,1,2,8,10] 
# List after filter  : [2,4,4,2,8,10]
# List after map : [4,16,16,4,64,100]
# Output of reduce : 204
#
####################################################################

from functools import reduce

####################################################################
#
# LambdaFunctionName : CheckEven
# Description  : It is used to filter the elements in the list that
#                are even
# Author       : Simran Naveen Tejwani
# Date         : 26/01/2026
#
####################################################################

CheckEven = lambda iNo : (iNo % 2 == 0)

####################################################################
#
# LambdaFunctionName : Square
# Description  : It is used to claculate the square of element 
#                in the list
# Author       : Simran Naveen Tejwani
# Date         : 26/01/2026
#
###################################################################

Square = lambda iNo : iNo * iNo

####################################################################
#
# LambdaFunctionName : Addition
# Description  : It is used to return addition of all elements 
#                in the list
# Author       : Simran Naveen Tejwani
# Date         : 26/01/2026
#
###################################################################

Addition = lambda iNo1 , iNo2 : iNo1 + iNo2

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

    FData = list(filter(CheckEven , Arr))
    print("Data after filter is : ",FData)

    MData = list(map(Square , FData))
    print("Data after map is : ",MData)

    RData = reduce(Addition , MData)
    print("Data after reduce is : ",RData)
    
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 