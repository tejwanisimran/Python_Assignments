####################################################################
#
# Description :  Design a Python application that creates two 
#                threads named EvenFactor and OddFactor.
#                Both threads should accept one integer number 
#                as a parameter.
#                The EvenFactor thread should:
#                Identify all even factors of the given number.
#                Calculate and display the sum of even factors.
#                The OddFactor thread should:
#                Identify all odd factors of the given number.
#                Calculate and display the sum of odd factors.
#                After both threads complete execution, the main 
#                thread should display the message:
#                “Exit from main”
#
####################################################################

import threading

####################################################################
#
# FunctionName : EvenFactors
# Description  : It is used to return the even factors and sum of 
#                all the even factors
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def EvenFactors(iNo):
    Factors = list()
    iSum = 0

    for iCnt in range(1,(iNo // 2)+1):
        if(iNo % iCnt == 0 and iCnt % 2 == 0):
            Factors.append(iCnt)    
    
    print("Even Factors are : ",Factors)

    for iCnt in Factors:
        iSum = iSum + iCnt

    print("Even Factors sum is : ",iSum)

####################################################################
#
# FunctionName : Odd
# Description  : It is used to return the first 10 odd numbers
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def OddFactors(iNo):
    Factors = list()
    iSum = 0

    for iCnt in range(1,(iNo // 2)+1):
        if(iNo % iCnt == 0 and iCnt % 2 != 0):
            Factors.append(iCnt)

    print("Odd Factors are : ",Factors)

    for iCnt in Factors:
        iSum = iSum + iCnt

    print("Odd Factors sum is : ",iSum)
####################################################################
#
# Entry Point Function
#
####################################################################

def main():

    print("Enter the number : ")
    iValue = int(input())

    EvenFactor = threading.Thread(target = EvenFactors , args = (iValue,))
    OddFactor = threading.Thread(target = OddFactors, args = (iValue,))

    EvenFactor.start()
    OddFactor .start()

    EvenFactor.join()
    OddFactor.join()

    print("Exit from main...")

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 