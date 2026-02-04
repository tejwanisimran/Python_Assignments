####################################################################
#
# Problem Statement: Write a program which accepts a file name and 
#                    one string from the user and returns the frequency 
#                    (count of occurrences) of that string in the file.
# Input : Demo.txt Marvellous
# 
# Expected Output : Count how many times "Marvellous" appears in Demo.txt.
# 
####################################################################

import os
import sys

####################################################################
#
# FunctionName : CountFrequency
# Description  : It is used to count of specific string in the file
# Author       : Simran Naveen Tejwani
# Date         : 04/02/2026
#
###################################################################
def CountFrequency(File_Name,target):
    Count = 0

    Ret = os.path.exists(File_Name)
    if(Ret == False):
        print("Error : There is no such file or directory...")
        return 
    
    fobj = open(File_Name,"r")
    if(fobj.closed == True):
        print("File is closed")
    else:
        print("File gets sucessfully opened...")

    Data = fobj.read().split()

    for word in Data:
        if target in word.split():
            Count += 1
    
    print("Count is : ",Count)

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    print("Enter the string : ")
    target = input()

    File_Name = sys.argv[1]

    if(len(sys.argv) != 2):
        print("Invalid number of arguments...")
        print("Specify name of the file...")
        return

    CountFrequency(File_Name,target)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 