MenuItems = ['Menu: ', '1 - Add', '2 - Amend', '3 - Delete', '4 - Display']
for MenuItems in MenuItems:
    print(MenuItems)

menuOption = int(input("Enter an option: "))

if menuOption == 1:
    print("Option 1 - Add selected")
elif menuOption == 2:
    print("Option 2 - Amend selected")
elif menuOption == 3:
    print("Option 3 - Delete selected")
elif menuOption  == 4:
    print("Option 4 - Display selected")
else:
    print("Invalid option selected")
