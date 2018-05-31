#ATM (redux) - core functionality works, need to review. need to add exceptions to routines where appropriate.
"""
To do:

- Add generic exit function
- Add exceptions
- Learn about how print functions work
"""
balance = int(1000)

"""def formatmoney(x):
    x = str(float(round(0.00,2)))"""


def printmenu(str):
    main = ['Welcome to Northern Frock','Choose an option from the list below\n'\
            ,'1. Display balance', '2. Withdraw funds', '3. Deposit funds'\
            ,'9. Return card']
    
    withdraw = ['Please select withdraw amount:\n','1. £10', '2. £20', '3. £40',\
            '4. £60', '5. £80','6. £100', '7. Other amoount',\
            '9. Return to main menu.']
    
    deposit = ['Please select deposit amount:\n','1. £10', '2. £20', '3. £40',\
            '4. £60', '5. £80','6. £100', '7. Other amoount',\
            '9. Return to main menu.']

    
    if str == 'main':
        for i in main:
            print(i)
    elif str == 'withdraw':
        for i in withdraw:
            print(i)
    elif str == 'deposit':
        for i in deposit:
            print(i)
    else:
        return

def getOption():
    option = int(input("Please choose an option: "))
    return option

def displayBalance():
    global balance
    print("Your current balance is £",balance)

def quitPrompt(int):

    query = ["Would you like to return to the menu? (Press any button to return to menu, press 0 to quit.",\
             "Would you like to quit the program? (Press any button to return to menu, press 0 to quit."]

    while True:
        print(query[int])
        i = input()
        if i != 0:
            break
        else:
            exit()


def modifyBalance(act = str, amt = int):
    global balance
    printmenu(act)
    while True:
        if act == 'withdraw':
            amt = getAmount()
            if balance >= amt:
                balance -= amt
                print("Withdrawl successful. Your balance is now £",balance)
                return
            else:
                print("Not enough money to perform this task. Choose another option")
                continue
        elif act == 'deposit':
            amt = getAmount()
            balance += amt
            print("Deposit successful. Your balance is now £",balance)
            return
            
def getAmount():
    opt = getOption()

    amounts = {1 : 10,
               2 : 20,
               3 : 40,
               4 : 60,
               5 : 80,
               6 : 100
               }

    if opt == 7:
        amounts[7] = int(input("Enter a custom amount: "))
        
    elif opt == 9:
        quitPrompt(0)
            
    return amounts.get(opt)

def main():
    while True:
        printmenu('main')
        userOption = getOption()
        if userOption == 1:
            while True:
                displayBalance()
                exitquery = input("Would you like to return to the menu (Press any button to return to menu, press 0 to quit.")
                if exitquery != '0' or 0:
                    break
                else:
                    return
        elif userOption == 2:
            modifyBalance('withdraw')
        elif userOption == 3:
            modifyBalance('deposit')
        elif userOption == 9:
            quitPrompt(1)
        else:
            continue

if __name__ == "__main__":
    main()

