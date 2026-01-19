####################################################################
#
# Description : Write a program which accepts one character & checks
#               whether the given character is vowel or consonant
# Input       :a
# Output      : Vowel
#
####################################################################

####################################################################
#
# FunctionName : CheckVowel()
# Description  : It is used to check the given character is vowel 
#                or consonant 
# Author       : Simran Naveen Tejwani
# Date         : 18/01/2026
#
####################################################################

def CheckVowel(cCh):
    bFlag = False

    if((cCh == 'a') or (cCh == 'e') or (cCh == 'i') or (cCh == 'o') or (cCh == 'u') or (cCh == 'A') or (cCh == 'E') or (cCh == 'I') or (cCh == 'U')):
        bFlag = True

    return bFlag

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    cChar = '\0'
    bRet = False

    print("Enter the character : ",end = "")
    cChar = input()

    bRet = CheckVowel(cChar) 

    if(bRet == True):
        print("Character is a Vowel...")
    else:
        print("Character is a consonant...")


####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 