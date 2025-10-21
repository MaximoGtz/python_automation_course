import os, random, math
import classes
from classes import User, SavingsAccount, Database
print("Who are you")
# user_name = input("")
users_array = []
user_name1 = "Maximo Gutierrez"
user1 = User(user_name1)
user1.create_account(23.4)
users_array.append(user1)
user_name2 = "Enrique Gutierrez"
user2 = User(user_name2)
user2.create_account(34.4)
users_array.append(user2)
user_name3 = "Ricardo Arjona"
user3 = User(user_name3)
user3.create_account(33.2)
users_array.append(user3)
user_name4 = "Bobby Pulido"
user4 = User(user_name4)
user4.create_account(14.2)
users_array.append(user4)
user_name5 = "Areidi Leal"
user5 = User(user_name5)
user5.create_account(80.2)
users_array.append(user5)

database = Database(users_array)
#initial_deposit = float(input())
os.system('cls')
print("Welcome to MaxBank!")
print("What is your name?")
user_name = str(input())
exist_user = False
for user in database.get_users():
    counter = 0
    if user.name == user_name:
        print("Welcome back, ",user_name,"!")
        final_user = database.get_users()[counter]
        exist_user = True
        break
    counter +=1
if not exist_user:
    print("Creating new account")
    final_user = User(user_name)
    print("How much will you deposit?")
    first_deposit = float(input())
    final_user.create_account(first_deposit)

menu_controller = 0
while menu_controller != 4:
    print("--------------------------------------")
    print("Logged as: ",final_user.name)
    print("What would you like to do?")
    print("1. Watch accounts")
    print("2. Create new account")
    print("3. Deposit to an account")
    print("4. Exit")
    menu_controller = int(input())
    match menu_controller:
        case 1:
            print("Watching accounts...")
            final_user.info()
        case 2:
            print("Creating new account...")
            print("How much would you like to deposit to your new account?")
            initial_deposit2 = float(input())
            final_user.create_account(initial_deposit2)
        case 3:
            print("Depositing money to an account")
            print("Introduce your account number:", end=' ')
            account_number = float(input())
            exist_account = False
            counter2 = 0
            for account in final_user.get_accounts():
                if account_number ==  account.account_number:
                    exist_account = True
                    print("How much would you like to deposit?")
                    deposit = float(input())
                    account.deposit(deposit)
                    print("Deposit succeded")
                    account.info()
            if not exist_account:
                print("Account not found, sorry.")

        case 4:
            break
        