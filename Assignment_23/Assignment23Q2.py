####################################################################
#
# Description :  Write a Python program to implement a class named 
#                BankAccount with the following requirements:
#                The class should contain two instance variables:
#                Name (Account holder name)
#                Amount (Account balance)
#                The class should contain one class variable:
#                ROI (Rate of Interest), initialized to 10.5
#                Define a constructor (__init__) that accepts Name 
#                and initial Amount.
#                Implement the following instance methods:
#                Display() – displays account holder name and current 
#                balance
#                Deposit() – accepts an amount from the user and adds 
#                it to balance
#                Withdraw() – accepts an amount from the user and 
#                subtracts it from balance
#                (Ensure withdrawal is allowed only if sufficient balance exists
#                CalculateInterest() – calculates and returns interest 
#                using formula:
#                Interest = (Amount * ROI) / 100
#                Create multiple objects and demonstrate all methods.
#               
####################################################################


####################################################################
#
# ClassName : BankAccount
# Description  : It is used to display the info about the books 
#                inside the bookstore
# Author       : Simran Naveen Tejwani
# Date         : 30/01/2026
#
###################################################################
class BankAccount:
    ROI = 10.5

    def __init__(self , name , balance):
        self.name = name
        self.balance = balance

    def Display(self):
        print(f"Name  : {self.name}")
        print(f"balance  : {self.balance}")

    def Deposit(self):
        print("Enter the ammount that you want to deposit : ")
        ammount = int(input())

        self.balance = self.balance + ammount
        print("Ammount deposited successfully...")

    def Withdrawl(self):
        print("Enter the ammount that you want to withdraw : ")
        ammount = int(input())

        if ammount <= self.balance:
            self.balance = self.balance - ammount

        print("Ammount withdrawn successfully...")

####################################################################
#
# Entry Point Function
#
####################################################################

def main():
    bobj1 = BankAccount("Simran Naveen Tejwani" , 10000)
    bobj1.Display()

    bobj1.Deposit()
    bobj1.Display()

    bobj1.Withdrawl
    bobj1.Display()

    bobj2 = BankAccount("Geetika Naveen Tejwani" ,  50000)
    bobj2.Display()
    
    bobj2.Withdrawl()
    bobj2.Display()

    bobj2.Deposit()
    bobj2.Display()

####################################################################
#
# Starter
#
####################################################################

if __name__ == "__main__":
    main() 