####################################################################
#
# Description :  Check File Exists in Current Directory
#                Problem Statement:
#                Write a program which accepts a file name from the
#                user and checks whether that file exists in the 
#                current directory or not.
# Input       :  Demo.txt
# Expected Output: Display whether Demo.txt exists or not.
# 
####################################################################

import os

####################################################################
#
# FunctionName : FileExists
# Description  : It is used to check whether the file exists or not
#                in the current directory
# Author       : Simran Naveen Tejwani
# Date         : 02/02/2026
#
###################################################################

def FileExists(File_Name):

    Ret = os.path.exists(File_Name)

    if(Ret == False):
        print("File doesn't exists in the current directory...")
    else:
        print("File exists in the current directory...")

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    print("Enter the file name : ",end = "")
    File_Name = input()

    FileExists(File_Name)

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 