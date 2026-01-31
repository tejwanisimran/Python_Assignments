####################################################################
#
# Description : Write a program which accepts N numbers from the 
#               user and stores them into a list. Return the 
#               addition of all prime numbers from that list.
#               The main Python file accepts N numbers from the 
#               user and passes each number to the ChkPrime() function, 
#               which is part of a user-defined module named MarvellousNum.
#               The name of the function from the main Python file should 
#               be ListPrime().
# Input      :
#               Number of elements : 11
#               Input Elements : 13  5  45  7  4  56  10  34  2  5  8

# Output     :
#               54 (13 + 5 + 7 + 2 + 5)
#
####################################################################
from MarvellousNum import CheckPrime

####################################################################
#
# FunctionName : ListPrime
# Description  : It is used to take the input from the user
# Author       : Simran Naveen Tejwani
# Date         : 25/01/2026
#
####################################################################
def ListPrime():

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

    CheckPrime(Arr)

####################################################################
#
# Entry Point Function
#
####################################################################

def main():

    ListPrime()
    

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 