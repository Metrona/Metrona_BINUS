#%%
class Account:
    balance = 0
    
    def __init__(self,balance):
        self.balance = balance
        
    def getBalance(self):
        return self.balance
    
    def depo(self,amt):
        if (amt > 0):
            self.balance = self.balance + amt
            return True
        else:
            return False
    def withd(self,amt):
        if (amt > 0 and amt <= self.balance):
            self.balance = self.balance - amt
            return True
        else:
            return False
        
myAccount = Account(5)
myAccount.depo(5)
myAccount.withd(10)
print("account balance is >>", myAccount.getBalance())

class Customer:
    __fname = ""
    __lname = ""
    __account = Account(5000)
    
    def __init__(self,first,last):
        self.__fname = first
        self.__lname = last
        
    def getFirst(self):
        return self.__fname
    
    def getLast(self):
        return self.__lname
    
    def getAccount(self):
        return self.__account
    
    def Set(self,Aco):
        self.__account = Aco

MyAcc = Customer("Justin", "Baker")

print(MyAcc.getAccount().getBalance())
print(MyAcc.getFirst())
print(MyAcc.getLast())


class Bank:
    def __init__(self, bankName):
        self.bankName = bankName
        self.numOfCustomers = 0
        self.__customers = []

    def addCustomer(self, isClass, *data):
        if isClass:
            self.__customers.append(*data)
        else:
            self.__customers.append(Customer(*data))
        self.numOfCustomers += 1

    def removeCustomer(self, index):
        try:
            self.__customers.pop(index)
            self.numOfCustomers -= 1
            return True
        except IndexError:
            return False

    def getBankName(self):
        return self.bankName

    def getNumOfCustomers(self):
        return self.numOfCustomers

    def getCustomer(self, index):
        return self.__customers[index]

    def getCustomers(self):
        return self.__customers
