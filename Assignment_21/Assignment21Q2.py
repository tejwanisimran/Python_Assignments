####################################################################
#
# Description :  Design a Python application that creates two threads.
#                Thread 1 should calculate and display the maximum 
#                element from a list.
#                Thread 2 should calculate and display the minimum 
#                element from the same list.
#                The list should be accepted from the user.
#               
####################################################################

import threading

####################################################################
#
# FunctionName : Maximum
# Description  : It is used to display maximum numbers from the list
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def Maximum(Arr):
    iMax = 0
    List = list()

    iMax = Arr[0]

    for iCnt in range(len(Arr)):
        if(Arr[iCnt] > iMax):
            iMax = Arr[iCnt]
    print("Maximum number from the list is : ",iMax)            

####################################################################
#
# FunctionName : Minimum
# Description  : It is used to display the minimum number from the list
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def Minimum(Arr):
    iMin = 0
    List = list()

    iMin = Arr[0]

    for iCnt in range(len(Arr)):
        if(Arr[iCnt] < iMin):
            iMin = Arr[iCnt]

    print("Minimum number from the list is : ",iMin) 
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
    
    thread_1 = threading.Thread(target = Maximum , args = (List,))
    thread_2 = threading.Thread(target = Minimum , args = (List,))

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