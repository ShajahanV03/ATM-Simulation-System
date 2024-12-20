        # Program on ATM Process

print("welcome to canara bank ATM")
print("---------------------------")
balance=50000

            # Card insertion

print("insert your card")
print("---------------------------")
print("Enter Any Number To Continue")
x=int(input())
if(x == True):
   print("1.card inserted successfully")
else:
   print("")  
print("---------------------------")
pin = 3123


        #language selection

print("select your language\n 1.english\n 2.hindi\n 3.kannada")
print("---------------------------")
lang=int(input())
if(lang == 1):
    print("enter your pin")
elif(lang == 2):
    print("enter your pin")
elif(lang == 3):
    print("enter your pin")
print("---------------------------")

        # pin validation
        
pin=int(input())
if(pin == 3123):
    print("select type of account\n1.savings\n2.current")
    print("---------------------------")
    account=int(input())
    if(account == 1):
     print("")
    elif(account == 2):
     print("")

        # amount withdrawal
        
    #  balance=50000
     print("choose your option")
    print("---------------------------")
    print("1.withdraw\n2.deposit\n3.balance enquire")
    option = int(input())
    if(option == 1):
     x=int(input("enter the amount to withdraw:"))
     print("---------------------------")
     if(x < balance):
        print("please collect your cash")
        print("---------------------------")
        available  = balance - x
        print("available balance:" , available)
        print("---------------------------")
        print("Thank You For Visiting")
        print("---------------------------")
     else:
        print("insufficient balance")

            # amount deposit

    #  balance=50000
    elif(option == 2):
     x=int(input("enter the amount to deposit:"))
     print("---------------------------")
     available = balance + x
     print(x , "amount deposited into your account")
     print("---------------------------")
     print("total amount:" , available)
     print("---------------------------")
     print("Thank You For Visiting")
     print("---------------------------")

            # balance enquire

    elif(option == 3):
     print("Available balance in your account:",balance)
     print("---------------------------")
     print("Thank You For Visiting")
     print("---------------------------")

else:
    print("You Have Entered Wrong Pin")
