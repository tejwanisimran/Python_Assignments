####################################################################
#
# Count Words in a File
# Problem Statement: Write a program which accepts a file name from 
#                    the user and counts the total number of words in 
#                    that file.
# Input : Demo.txt
# Expected Output : Total number of words in Demo.txt.
# 
####################################################################

import os
import sys

####################################################################
#
# FunctionName : CountWordsInFile
# Description  : It is used to count words in the file
# Author       : Simran Naveen Tejwani
# Date         : 04/02/2026
#
###################################################################
def CountWordsInFile(File_Name):
    Count = 0
    Ret = os.path.exists(File_Name)
    if(Ret == False):
        print("Error : There is no such file or directory...")
        return
    
    fobj = open(File_Name,"r")

    Data = fobj.read().split()

    for words in Data:
        words.split()
        Count += 1
    print(f"Number of words in {File_Name} is {Count}")

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    File_Name = sys.argv[1]

    if(len(sys.argv) != 2):
        print("Invalid number of arguments...")
        print("Specify name of the file...")
        return

    CountWordsInFile(File_Name)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 