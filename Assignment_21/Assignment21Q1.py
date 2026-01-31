####################################################################
#
# Description :  Design a Python application that creates two 
#                threads named Prime and NonPrime.
#                Both threads should accept a list of integers.
#                The Prime thread should display all prime numbers 
#                from the list.
#                The NonPrime thread should display all non-prime 
#                numbers from the list.
#
####################################################################

import threading

####################################################################
#
# FunctionName : Prime
# Description  : It is used to display prime numbers from the list
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def Prime(Arr):

    List = list()

    for num in Arr:
        if num <= 1:
            continue
        bFlag = True
        for iCnt in range(2,num //2 + 1):
            if(num % iCnt == 0):
                bFlag = False
                break
        if bFlag:
            List.append(num) 
            
    print("Prime numbers from the list are : ",List)

####################################################################
#
# FunctionName : NotPrime
# Description  : It is used to display the numbers from the list 
#                that are not prime
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def NotPrime(Arr):
    List = list()

    for num in Arr:
        if num <= 1:
            List.append(num)
            continue
        for iCnt in range(2,(num // 2) +1):
            if(num % iCnt == 0):
                List.append(num)
                break
    print("NotPrime numbers from the list are : ",List)

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
    
    thread_1 = threading.Thread(target = Prime , args = (List,))
    thread_2 = threading.Thread(target = NotPrime , args = (List,))

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 