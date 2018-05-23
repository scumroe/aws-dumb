#4.2ATMBasic

def getMenu(int):

    main = ['Welcome to Northern Frock','Choose an option from the list below\n'\
            ,'1. Display balance', '2. Withdraw funds', '3. Deposit funds'\
            ,'9. Return card']

    withdraw = ['Please select withdraw amount:\n', '10', '20', '40', '60', '80',\
                     '100', 'Other amoount', 'Return to main menu.']


    if int == 0:
        for main in main:
            print(main)

    if int == 1:
        print("Your current balance is: ", balance)
        
    elif int == 2:
        for withdraw in withdraw:
            print(withdraw)
    return

def withdrawaloptions(str):
    return
    
def main():
    getMenu(0)
    while getMenu(0):
        optMenu = input()]
main()







