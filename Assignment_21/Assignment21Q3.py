####################################################################
#
# Description :  Design a Python application where multiple threads 
#                update a shared variable.
#                Use a Lock to avoid race conditions.
#                Each thread should increment the shared counter 
#                multiple times.
#                Display the final value of the counter after all 
#                threads complete execution.
#                
####################################################################

import threading

####################################################################
#
# Counter name : iCount
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

iCount = 0

####################################################################
#
# Lock Object
#
###################################################################

lock = threading.Lock()

####################################################################
#
# FunctionName : Increment
# Description  : It is used to display maximum numbers from the list
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def Increment():
    global iCount

    for iCnt in range(10):
        lock.acquire()
        iCount += 1
        lock.release()

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    
    thread_1 = threading.Thread(target = Increment)
    thread_2 = threading.Thread(target = Increment)

    thread_1.start()
    thread_2.start()

    thread_1.join()
    thread_2.join()

    print("Final Value of counter is : ",iCount)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 