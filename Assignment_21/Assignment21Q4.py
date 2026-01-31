####################################################################
#
# Description :  Design a Python application that creates two threads.
#                Thread 1 should compute the sum of elements from a list.
#                Thread 2 should compute the product of elements from 
#                the same list.
#                Return the results to the main thread and display them.
#                
####################################################################

import threading

###################################################################

sum_result = None
product_result = None

###################################################################

####################################################################
#
# FunctionName : Add
# Description  : It is used to return the addition of all numbers 
#                from the list
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def Add(Arr):
    global sum_result
    iSum = 0

    for iCnt in range(len(Arr)):
        iSum = iSum + Arr[iCnt]
    sum_result = iSum
####################################################################
#
# FunctionName : Product
# Description  : It is used to return the Product of all numbers 
#                from the list
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def Product(Arr):
    global product_result
    iMult = 1

    for iCnt in range(len(Arr)):
        iMult = iMult * Arr[iCnt]

    product_result = iMult

####################################################################
#
# Entry Point Function
#
####################################################################

def main():

    iSize = 0
    iValue = 0
    List = list()
    iRet = 0

    print("Enter the number of elements : ")
    iSize = int(input())

    print("Enter the elements : ")

    for iCnt in range(iSize):
        iValue = int(input())
        List.append(iValue)
    
    thread_1 = threading.Thread(target = Add,args = (List,))
    thread_2 = threading.Thread(target = Product,args = (List,))

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("Addition is : ",sum_result)
    print("Product is : ",product_result)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 