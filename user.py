class User: 
    bank_name = "Cardano Bank"
    def __init__(self):
        self.name = "Anna"
        self.email = "annaefitzgerald@gmail.com"
        self.account_balance = 0
        
    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        
    def display_user_balance(self, balance):
        self.account_balance = balance
    #bonus add transfer_money()
        #user1 transfers to user3
        #print both user balances
        
User()
frankie=User()
fiore=User()
#this is an instance of the class user
#now access the attributes of the parent class
print(frankie.name)
print(fiore.name)

frankie.name = "Frankie"
print(frankie.name)
fiore.name = "Fiore"
print(fiore.name)


User()
lola=User()
powers=User()
#this is an instance of the class user
#now access the attributes of the parent class
print(lola.name)
print(powers.name)

lola.name = "Lola"
print(lola.name)
powers.name = "Powers"
print(powers.name)

User()
lillian=User()
checkers=User()
#this is an instance of the class user
#now access the attributes of the parent class
print(lillian.name)
print(checkers.name)

lillian.name = "Lillian"
print(lillian.name)
checkers.name = "Checkers"
print(checkers.name)


#have first user make 3 deposits and 1 withdrawal
#display balance
frankie.make_deposit(4000)
frankie.make_deposit(2500)
frankie.make_deposit(9800)
frankie.make_withdrawal(1100)
print(frankie.account_balance)


#have second user make 2 deposits and 2 withdrawals
#display balance
lola.make_deposit(11000)
lola.make_deposit(130500)
lola.make_withdrawal(80000)
lola.make_withdrawal(25000)
print(lola.account_balance)


#have third user make 1 deposit and 3 withdrawals
#display balance
lillian.make_deposit(578000)
lillian.make_withdrawal(233000)
print(lillian.account_balance)


