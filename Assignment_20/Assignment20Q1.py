####################################################################
#
# Description : . Design a Python application that creates two 
#                 separate threads named Even and Odd.
#                 The Even thread should display the first 10
#                 even numbers.
#                 The Odd thread should display the first 10 
#                 odd numbers.
#                 Both threads should execute independently using
#                 the threading module.
#                 Ensure proper thread creation and execution.
#
####################################################################

import threading

####################################################################
#
# FunctionName : Even
# Description  : It is used to return the first 10 even numbers
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def Even():
    iCount = 0
    count_even = 2

    while(iCount < 10):
        print(count_even , "\t" , end = "")
        count_even += 2
        iCount += 1
    print("\n")

####################################################################
#
# FunctionName : Odd
# Description  : It is used to return the first 10 odd numbers
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def Odd():

    iCount = 0
    count_odd = 1

    while(iCount < 10):
        print(count_odd , "\t" , end = "")
        count_odd += 2
        iCount += 1
    print("\n")

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    Even = threading.Thread(target = Even)
    Odd = threading.Thread(target = Odd)

    Even.start()
    Odd .start()

    Even.join()
    Odd.join()

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 