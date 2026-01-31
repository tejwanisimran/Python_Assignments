####################################################################
#
# Description :  Design a Python application that creates two 
#                threads named Thread1 and Thread2.
#                Thread1 should display numbers from 1 to 50.
#                Thread2 should display numbers from 50 to 1 
#                in reverse order.
#                Ensure that:
#                Thread2 starts execution only after Thread1 has 
#                completed.
#                Use appropriate thread synchronization.
#
####################################################################

import threading

####################################################################
#
# FunctionName : DisplayNumbers
# Description  : It is used to display the numbers from 1 to 50
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def DisplayNumbers():

    for iCnt in range(1,51,1):
        print(iCnt,"\t",end = "")
    print("\n")

####################################################################
#
# FunctionName : DisplayReverseNumbers
# Description  : It is used to display the numbers from 50 to 1 
#                in reverse order
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def DisplayReverseNumbers():
    for iCnt in range(50,1,-1):
        print(iCnt,"\t",end = "")
    print("\n")

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    
    thread_1 = threading.Thread(target = DisplayNumbers)
    thread_1.start()

    thread_2 = threading.Thread(target = DisplayReverseNumbers)
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