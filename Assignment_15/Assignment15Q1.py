####################################################################
#
# Description : Write a lambda function using map() which accepts 
#               list of numbers and returns a list of squares of
#               each number 
#
####################################################################

####################################################################
#
# LambdaFunctionName : Square
# Description  : It is used to display square of given numbers
# Author       : Simran Naveen Tejwani
# Date         : 20/01/2026
#
####################################################################
Square = lambda iNo : (iNo * iNo)

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iSize = 0
    iValue = 0
    MData = 0

    print("Enter number of elements : ")
    iSize = int(input())

    Data = list()

    print("Enter the elements : ")

    for iCnt in range(iSize):
        iValue = int(input())
        Data.append(iValue)

    MData = list(map(Square , Data))

    print("Squares of numbers from the list is : ",MData)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 