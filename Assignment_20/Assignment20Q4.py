####################################################################
#
# Description :  Design a Python application that creates three 
#                threads named Small, Capital, and Digits.
#                All threads should accept a string as input.
#                The Small thread should count and display the 
#                number of lowercase characters.
#                The Capital thread should count and display the 
#                number of uppercase characters.
#                The Digits thread should count and display the 
#                number of numeric digits.
#                Each thread must also display:
#                Thread ID
#                Thread Name
# 
####################################################################

import threading

####################################################################
#
# FunctionName : CountCapital
# Description  : It is used to return the count of the capital 
#                letters in the string
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def CountCapital(String):
    iCountCapital = 0

    for char in String :
        if(char >= 'A' and char <= 'Z'):
            iCountCapital += 1

    print("Capital letters in the String are : ",iCountCapital)

####################################################################
#
# FunctionName : CountSmall
# Description  : It is used to return the count of the small 
#                letters in the string
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def CountSmall(String):
    iCountSmall = 0

    for char in String :
        if(char >= 'a' and char <= 'z'):
            iCountSmall += 1

    print("Small letters in the String are : ",iCountSmall)


####################################################################
#
# FunctionName : CountDigits
# Description  : It is used to return the count of the digits 
#                in the string
# Author       : Simran Naveen Tejwani
# Date         : 29/01/2026
#
###################################################################

def CountDigit(String):
    iDigits = 0

    for char in String :
        if( char >= '0' and char <= '9'):
            iDigits += 1

    print("Digits in the String are : ",iDigits)

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    String = None

    print("Enter the string : ")
    String = input()

    Capital = threading.Thread(target = CountCapital , args = (String,))
    Small = threading.Thread(target = CountSmall , args = (String,))
    Digit = threading.Thread(target = CountDigit , args = (String,))


    Capital.start()
    Small.start()
    Digit.start()

    Capital.join()
    Small.join()
    Digit.join()

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 