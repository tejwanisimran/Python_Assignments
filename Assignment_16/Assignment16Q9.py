####################################################################
#
# Description : Write a program which display first 10 even 
#               numbers on screen
# Output      : 2 4 6 8 10 12 14 16 18 20
####################################################################

####################################################################
#
# FunctionName : CheckDivisible
# Description  : It is used to return the first 10 even numbers 
# Author       : Simran Naveen Tejwani
# Date         : 23/01/2026
#
####################################################################

def Display():
    
    iCount = 0
    count_even = 2

    while(iCount < 10):
        print(count_even , "\t" , end = "")
        count_even += 2
        iCount += 1
    print("\n")
            
####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    Display()

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 