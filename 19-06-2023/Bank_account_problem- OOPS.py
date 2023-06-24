#BANK_ACCOUNT PROBLEM
class Bank_Account:
    
    def __init__(self):
         self.account_number=input("enter account number:")
         self.date_of_opening=input("enter date of opening:")
         self.customer_name=input("enter your name:")
         self.balance=float(input("enter the balance:"))
    def deposit(self,deposit):
            self.balance+=deposit
            return self.balance
    def with_draw(self,with_draw):
        if self.balance>with_draw:
            self.balance-=with_draw
            return self.balance
        else:
            return "insufficient money"
    def check_balance(self):
        return self.balance
         
customer=Bank_Account()
print(customer.deposit(23))
print(customer.with_draw(34))
print(customer.check_balance())


