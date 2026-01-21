####################################################################
#
# Description : Write a lambda function using filter() which accepts 
#               list of strings and returns list of strings with 
#               length greter than 5
#
####################################################################

from functools import reduce

####################################################################
#
# LambdaFunctionName : StringLength
# Description  : It is used to check the string greater than length 5
# Author       : Simran Naveen Tejwani
# Date         : 21/01/2026
#
####################################################################

StringLength = lambda string : (len(string)> 5)

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iSize = 0
    iValue = 0
    FData = 0

    print("Enter number of strings you want to enter : ")
    iSize = int(input())

    Data = list()

    print("Enter the strings : ")

    for iCnt in range(iSize):
        string = input()
        Data.append(string)

    FData = list(filter(StringLength , Data))

    print("minimum of all elements from the list is : ",FData)

    

    




####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 