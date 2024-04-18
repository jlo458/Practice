# Program makes bank accounts and allows users to deposit/withdraw money as they please

class Account:
    def __init__(self, number, password, balance):
        self.__accountNumber = number
        self.__password = password
        self.__balance = balance

    def getNumber(self): 
        return self.__accountNumber
    
    def checkPassword(self, password): 
        if password == self.__password:
            return True

    def getBalance(self): 
        return self.__balance
    
    def setBalance(self, newBalance):
        self.__balance = newBalance

class Bank:
    def __init__(self):
        self.__accounts = []
        self.__latestAccount = -1 
            
    def login(self):
        accountNum = int(input("Enter account number: "))
        password = input("Enter password: ")
        if (self.__accounts[accountNum]).checkPassword(password):
            return accountNum 
        
        return -1

    def deposit(self, number):
        deposit = int(input("Enter amount to deposit: "))
        theBalance = (self.__accounts[number]).getBalance()
        (self.__accounts[number]).setBalance(theBalance + deposit)

    def withdraw(self, number):
        withdraw = int(input("Enter amount to withdraw: "))
        theBalance = (self.__accounts[number]).getBalance()
        (self.__accounts[number]).setBalance(theBalance - withdraw)

    def checkBalance(self, number):
        print("Money in account: ",(self.__accounts[number]).getBalance())

    def addAccount(self):
        self.__latestAccount += 1
        newNumber = self.__latestAccount
        print("Your account number is:", newNumber)
        password = input("Enter password: ")
        newAccount = Account(newNumber, password, 0)
        self.__accounts.append(newAccount)
        
        
def main():
    bank = Bank()
    loggedIn = False
    quitting = False
    
    while not loggedIn and not quitting:
        response = input("Do you have an account? (y/n/quit): ")
        if response == "y":
            account = bank.login()
            if account != -1:
                loggedIn = True
        elif response =="n":
            bank.addAccount()
        elif response =="quit":
            quitting = True
            
    while not quitting:
        option = input("Press 1 to check your balance\nPress 2 to deposit money\nPress 3 to withdraw money\nPress 4 to exit:\n")
        if option == "1":
            bank.checkBalance(account)
        elif option == "2": 
            bank.deposit(account)
            bank.checkBalance(account)
        elif option == "3":
            bank.withdraw(account)
            bank.checkBalance(account)
        elif option == "4":
            quitting = True
        else:
            print("Invalid option selected")


if __name__ == '__main__':
    main()
