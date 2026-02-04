####################################################################
#
# Count Lines in a File
# Problem Statement : Write a program which accepts a file name from the
#                    user and counts how many lines are present in the file.
# Input : Demo.txt
# Expected Output : Total number of lines in Demo.txt.
# 
####################################################################

import os
import sys

####################################################################
#
# FunctionName : CountLinesInFile
# Description  : It is used to count number of lines in the file
# Author       : Simran Naveen Tejwani
# Date         : 04/02/2026
#
###################################################################
def CountLinesInFile(File_Name):
    Ret = os.path.exists(File_Name)
    if(Ret == False):
        print("Error : There is no such file or directory...")
        return
    
    fobj = open(File_Name,"r")

    Ret = len(fobj.readlines())

    print(f"Number of lines in {File_Name} is {Ret}")

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

    CountLinesInFile(File_Name)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 