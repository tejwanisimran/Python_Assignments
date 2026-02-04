####################################################################
#
# Search a Word in File
# Problem Statement : Write a program which accepts a file name and 
#                     a word from the user and checks whether that word 
#                     is present in the file or not.
# Input : Demo.txt Marvellous
# Expected Output : Display whether the word Marvellous is found 
#                   in Demo.txt or not.
# 
####################################################################

import os
import sys

####################################################################
#
# FunctionName : CheckWordIsPresent
# Description  : It is used to copy the file contents from one
#                file to another
# Author       : Simran Naveen Tejwani
# Date         : 02/02/2026
#
###################################################################

def CheckWordIsPresent(File_Name,target):
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
            Ret = True
            break
        else : 
            Ret = False
            

    if(Ret == True):
        print("Word is found...")
    else :
        print("Word is not found...")

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    File_Name = sys.argv[1] 
    target = sys.argv[2]

    if(len(sys.argv) != 3):
        print("Invalid number of arguments...")
        print("Specify name of the file...")
        return

    CheckWordIsPresent(File_Name,target)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 