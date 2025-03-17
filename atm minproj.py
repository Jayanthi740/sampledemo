balance=500
def deposit(amount):
    global balance
    balance+=amount
    print(f"deposited balance:RS{balance}")


def withdraw(amount):
    global balance
    if balance>=amount:
        balance-=amount
        print(f"with draw amount is {amount}")
        print(f"after withdraw of amount is {balance}")
    else:
        print("insufficent balance")

def balance_enquary(amount):
    print(f"available balance in your account is :{balance}")
print(balance_enquary)

while True:
    print("------------ATM menu------------")
    print("1.deposit")
    print("2.eithdraw")
    print("3.balance_enquary")
    print("4.exit")
    choice=input("enter  your choice:")
    if choice=="1":
        amount=int(input("enter the amount deposit your account"))
        deposit(amount)
    elif choice=="2":
        amount=int(input("enter the withdraw amount"))
        withdraw(amount)
    elif choice=="3":
        #amount=int(input("the remaing balance is"))
        balance_enquary()
    elif choice=="4":
        print("thank you vist again")
        #commit changes
    else:
        print("invalid choice,choose the coorect answer")
