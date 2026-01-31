####################################################################
#
# Description :  Design a Python application that creates two 
#                threads named EvenList and OddList.
#                Both threads should accept a list of integers 
#                as input.
#                The EvenList thread should:
#                Extract all even elements from the list.
#                Calculate and display their sum.
#                The OddList thread should:
#                Extract all odd elements from the list.
#                Calculate and display their sum.
#                Threads should run concurrently.
# 
####################################################################

import threading

####################################################################
#
# FunctionName : EvenList
# Description  : It is used to return the even numbers from 
#                the list
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def EvenNumbers(Arr):

    Even = list()

    for iCnt in range(len(Arr)):
        if(Arr[iCnt] % 2 == 0):
            Even.append(Arr[iCnt])

    print("Even Numbers from the list are : ",Even)

####################################################################
#
# FunctionName : OddList
# Description  : It is used to return the odd numbers from 
#                the list
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def OddNumbers(Arr):
    Odd = list()

    for iCnt in range(len(Arr)):
        if(Arr[iCnt] % 2 != 0):
            Odd.append(Arr[iCnt])

    print("Odd Numbers from the list are : ",Odd)

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    iSize = 0
    iValue = 0
    List = list()

    print("Enter the number of elements : ")
    iSize = int(input())

    print("Enter the elements : ")

    for iCnt in range(iSize):
        iValue = int(input())
        List.append(iValue)

    EvenList = threading.Thread(target = EvenNumbers , args = (List,))
    OddList = threading.Thread(target = OddNumbers , args = (List,))

    EvenList.start()
    OddList.start()

    EvenList.join()
    OddList.join()

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 