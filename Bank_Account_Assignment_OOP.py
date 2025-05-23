class Bank_Acount ():
    def __init__ (self,name,balance,password):
        self.name = name
        self.balance = balance
        self.password = password
    
    def Withdraw (self,amount,access):

        if access == self.password:
            if amount > self.balance:
                print ("Error\nNot Enough in Balance\n")
            else:
                self.balance -= amount
        else:
            print ("Error\nIncorrect Password\n")

    def Deposit (self,amount,access):
        if access == self.password:
            if amount >= 0:
                self.balance += amount
            else:
                print ("Error\nNeagative Value Given\n")
        else:
            print ("Error\nIncorrect Password\n")

    def show_balance (self):
        print ("Balance: ",self.balance,"\n")

    def account_info (self):
        print ("Name: ",self.name,"\nBalance: ",self.balance,"\nPassword: ",self.password,"\n")

John = Bank_Acount ("John",500,"my_password")
John.Withdraw (200,"my_password")
John.show_balance ()
John.Deposit (-700,"my_password")
John.Deposit (700,"my_password")
John.show_balance ()
John.account_info ()

Diane = Bank_Acount ("Diane",2000,"get_money_money")
Diane.Deposit (400,"Get_MONEY_MONEY")
Diane.Deposit (400,"get_money_money")
Diane.show_balance ()
Diane.Withdraw (2500,"get_money_money")
Diane.Withdraw (1700,"get_money_money")
Diane.show_balance ()
Diane.account_info ()