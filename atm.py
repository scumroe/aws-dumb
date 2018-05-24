#4.2ATMBasic
balance = float(round(0.0,2))

dispState = int(0)
money = {}

def getDispState():
    global dispState
    dispState = int(input("Please choose an option: "))
    return dispState

def getDisplay(int):
    global money

    main = ['Welcome to Northern Frock','Choose an option from the list below\n'\
            ,'1. Display balance', '2. Withdraw funds', '3. Deposit funds'\
            ,'9. Return card']

    wdrl = ['Please select withdraw amount:\n','1. £10', '2. £20', '3. £40',\
            '5. £60', '6. £80','7. £100', '8. Other amoount',\
            '9. Return to main menu.']


    if int == 0:
        for main in main:
            print(main)
    elif int == 1:
        print("Your current balance is: ", balance)
    elif int == 2:
        for wdrl in wdrl:
            print(wdrl)
            
def updateBalance(opt=0, int=0):
    global balance
    global money

    if  not opt == 0:
        newBalance = balance + int
        return newBalance
    else:
        passs
                
def main():
    while True:
        global dispState
        global money
        while dispState == 0:
            getDisplay(dispState)
            getDispState()
            if dispState == 1:
                while True:
                    getDisplay(dispState)
                    dispState = (int(input("Would you like to quit? (Press any ket to quit, 0to return to menu)")))
                    if dispState == 0:
                        break
                    else:
                        continue
            if dispState == 2:
                wdrlState = dispState
                getDisplay(wdrlState)
                wdrlState = getDispState()
                if wdrlState == 1:
                    print("Your new balance is", updateBalance(10))
                break
            else:
                continue
if __name__ == "__main__":
    main()




