####################################################################
#
# Description : . Write a program which contains filter(), map() 
#                 and reduce() in it.
#                 Python application contains one list of numbers.
#                 The list contains the numbers which are accepted 
#                 from the user.
#                 filter() should filter out all prime numbers.
#                 map() function will multiply each number by 2.
#                 reduce() will return the maximum number from the numbers.
#                 (You can also use normal functions instead of lambda 
#                 functions.)
# Input List  : [2,70,11,10,17,23,31,77]
# List after filter  : [2,11,17,23,31]
# List after map : [4,22,34,46,62]
# Output of reduce : 62
#
####################################################################

from functools import reduce

####################################################################
#
# FunctionName : CheckPrime
# Description  : It is used to filter the elements in the list that
#                are prime
# Author       : Simran Naveen Tejwani
# Date         : 26/01/2026
#
####################################################################

def CheckPrime(num):
    if num <= 1:
        return False

    for iCnt in range(2,num //2 + 1):
        if(num % iCnt == 0):    
            return False

    return True
            
####################################################################
#
# LambdaFunctionName : MultiplyBy2
# Description  : It is used to multiply each number by 2
#                in the list
# Author       : Simran Naveen Tejwani
# Date         : 26/01/2026
#
###################################################################

MultiplyBy2 = lambda iNo : iNo * 2

####################################################################
#
# LambdaFunctionName : CheckMaximum
# Description  : It is used to return maximum number 
#                from the list
# Author       : Simran Naveen Tejwani
# Date         : 26/01/2026
#
###################################################################

CheckMaximum = lambda iNo1,iNo2 : iNo1 if iNo1 > iNo2 else iNo2

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

    FData = list(filter(CheckPrime , Arr))
    print("Data after filter is : ",FData)

    MData = list(map(MultiplyBy2 , FData))
    print("Data after map is : ",MData)

    RData = reduce(CheckMaximum , MData)
    print("Data after reduce is : ",RData)
    
####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 