business = None

inpt = 'Chose from the list.\nType "A" for Add Business \nType "B" for Show Business \nType "C" for restock wares,\nType "D" to check price\nType "E" to check availability of wares\nType "F" for sell wares \nType "G" to add and remove current deals\nType "H" for Buying ware info\nType "X" to exit the program\n'

choice = input(inpt)

list = ('A','B','C','D','E','F','G','H','X')

while (choice not in list):
        print("\nError: Invalid option. Please type 'A','B','C','D','E','F','G','H', or 'X'\n")
        choice = input(inpt)

class Business:
    def __init__(self) -> None:
        pass

    def restock(BS,ma,ai):

        if ma >= 0:
            business[BS]['Ware Info'].update({"Available Items": ai})
            business[BS]['Ware Info'].update({"Money_Available": ma})
            print("\nYour business has been updated.\n")
        
        else:
            print("\nYou do not have enough of money to restore the business.\n")

    def check_price_of_wares(BS):
        nwp = business[BS]['Ware Info']['Price_of_each_ware'] - (business[BS]['Ware Info']['Price_of_each_ware'] * (business[BS]['Ware Info']['Current Deals']/100))
        tnwp = nwp * business[BS]['Ware Info']['Available Items']
        print('\nPrice of a ware with current deals is ' + str(nwp) +' NOK.')
        print('Total price of available wares is '+ str(tnwp) + ' NOK.\n')

    def check_availability_of_wares(BS):
        aw = business[BS]['Ware Info']['Available Items']
        print('\nThere are '+ str(aw) +' wares available.\n')

    def sell_wares(BS,ma,ai):
        if ai >= 0:
            business[BS]['Ware Info'].update({"Available Items": ai})
            business[BS]['Ware Info'].update({"Money_Available": ma})
            print("\nYour business has been updated.\n")
        
        else:
            print("\nYou do not have enough of itimes to sell the ware.\n")

    def add_or_remove_deals(BS,rate):
        business[BS]['Ware Info'].update({"Current Deals": rate})
        print("\nThe current deals for ware has been updated.\n")

class Sell:
    def __init__(self) -> None:
        pass

    def buying_info(Ware_name, Buy_price, Available_ware):
        print('\nWare Name = ' + Ware_name )
        print('Buy Price = ' + str(Buy_price) + ' NOK')
        print('Total wares = ' + str(Available_ware) + '\n')


obj = Business
obj1 = Sell

while (choice in list):

#----------------Add Business--------------
    while (choice == 'A'):
        try:
            a = input("Enter the business name?\n")
            b = input("Enter the Ware Name?\n")
            c = int(input('Enter the number of available items?\n'))
            if c < 0:
                c = int(input('Enter the positive number for available items?\n'))
            d = float(input('Enter the price of each ware in NOK.\n'))
            if d < 0:
                d = d*(-1)
            e = float(input('Enter the current deals in percentage. Note: If you do not want to any deals just enter "0".\n'))
            if e < 0:
                e = e*(-1)
            f = float(input('Enter the total money that you have for the bussiness in NOK.\n'))
            if c < 0:
                c = f*(-1)

            if business == None:

                business1 = {'Bussiness Name': a,'Ware Info':{
                    'Ware Name': b,"Available Items": c ,
                    "Price_of_each_ware": d ,'Current Deals':e,'Money_Available':f}}

                business = {
                    #Initial : business,
                    a : business1
                }
                #print(len(business))
                #print(business)

            else:

                business1 = {'Bussiness Name': a,'Ware Info':{
                    'Ware Name': b,"Available Items": c ,
                    "Price_of_each_ware": d ,'Current Deals':e,'Money_Available':f}}

                business[a] = business1
        except ValueError:
            print("\nErorr: Incorrect format. Please try again.\n")

        print('\nThe business has been added successfully\n')

        choice = input(inpt)
        while (choice not in list):
            print("\nError: Invalid option. Please type 'A','B','C','D','E','F','G','H', or 'X'\n")
            choice = input(inpt)


#---------------Show Business-----------
    while (choice =='B'):
        if business == None:
            print("\nError:There is not any business. Please add a business first.\n")

        else:
            print('\nYou have following Bussiness:\n')
            for x in business.values():
                print(x)
            print('\n')

        choice = input(inpt)
        while (choice not in list):
            print("\nError: Invalid option. Please type 'A','B','C','D','E','F','G','H', or 'X'\n")
            choice = input(inpt)
        

#----------------restock-------------
    while (choice =='C'):
        if business == None:
            print("\nError: There is not any business. Please add a business first.\n")

        else:
            BS = input("Enter the Business Name.\n")
            try:
                if ((BS) in business.keys()) == True:
                    try:
                        wn = input('Enter the ware name.\n')
                        if (('Ware Name', wn) in business[BS]['Ware Info'].items()):
                            additem = int(input("Enter the number of items that you want to add.\n"))
                            ni = int(business[BS]['Ware Info']["Available Items"]) + additem
                            ms = input("Enter the cost amount of a ware.\n")
                            nma = int(business[BS]['Ware Info']["Money_Available"]) - additem * int(business[BS]['Ware Info']["Price_of_each_ware"])
                            obj.restock(BS,nma,ni)

                        else:
                            print('\nWare Name not found.Please try again.\n')
                            
                    except ValueError:
                        print("\nErorr: Incorrect format. Please try again.\n")
                else:
                    print('\nBusiness Name not found.Please try again.\n')
            except ValueError:
                        print("\nErorr: Incorrect format. Please try again.\n")

        choice = input(inpt)
        while (choice not in list):
            print("\nError: Invalid option. Please type 'A','B','C','D','E','F','G','H', or 'X'\n")
            choice = input(inpt)


#--------------- price check------------
    while (choice == 'D'):
        if business == None:
            print("\nError: There is not any business. Please add a business first.\n")

        else:
            BS = input("Enter the Business Name.\n")
            try:
                if ((BS) in business.keys()) == True:
                    try:
                        wn = input('Enter the ware name.\n')
                        if (('Ware Name', wn) in business[BS]['Ware Info'].items()):
                            obj.check_price_of_wares(BS)

                        else:
                            print('\nWare Name not found.Please try again.\n')

                    except ValueError:
                        print("\nErorr: Incorrect format. Please try again.\n")
                else:
                    print('\nBusiness Name not found.Please try again.\n')
            except ValueError:
                print("\nErorr: Incorrect format. Please try again.\n")

        choice = input(inpt)
        while (choice not in list):
            print("\nError: Invalid option. Please type 'A','B','C','D','E','F','G','H', or 'X'\n")
            choice = input(inpt)


#---------------Check availability of ware ----------------
    while choice == 'E':
        if business == None:
            print("\nError: There is not any business. Please add a business first.\n")

        else:
            BS = input("Enter the Business Name.\n")
            try:
                if ((BS) in business.keys()) == True:
                    try:
                        wn = input('Enter the ware name.\n')
                        if (('Ware Name', wn) in business[BS]['Ware Info'].items()):
                            obj.check_availability_of_wares(BS)

                        else:
                            print('\nWare Name not found.Please try again.\n')

                    except ValueError:
                        print("\nErorr: Incorrect format. Please try again.\n")
                else:
                    print('\nBusiness Name not found.Please try again.\n')
            except ValueError:
                print("\nErorr: Incorrect format. Please try again.\n")

        choice = input(inpt)
        while (choice not in list):
            print("\nError: Invalid option. Please type 'A','B','C','D','E','F','G','H', or 'X'\n")
            choice = input(inpt)

#------------ sell ware -----------

    while (choice =='F'):
        if business == None:
            print("\nError: There is not any business. Please add a business first.\n")

        else:
            BS = input("Enter the Business Name.\n")
            try:
                if ((BS) in business.keys()) == True:
                    try:
                        wn = input('Enter the ware name.\n')
                        if (('Ware Name', wn) in business[BS]['Ware Info'].items()):
                            sellitem = int(input("Enter the number of items that you want to sell.\n"))
                            ni = int(business[BS]['Ware Info']["Available Items"]) - sellitem
                            nma = business[BS]['Ware Info']['Money_Available'] + sellitem*(business[BS]['Ware Info']['Price_of_each_ware'] - (business[BS]['Ware Info']['Price_of_each_ware'] * (business[BS]['Ware Info']['Current Deals']/100)))
                            obj.sell_wares(BS,nma,ni)
                            #print(business)

                        else:
                            print('\nWare Name not found.Please try again.\n')
                    except ValueError:
                        print("\nErorr: Incorrect format. Please try again.\n")
                else:
                    print('\nBusiness Name not found.Please try again.\n')
            except ValueError:
                        print("\nErorr: Incorrect format. Please try again.\n")

        choice = input(inpt)
        while (choice not in list):
            print("\nError: Invalid option. Please type 'A','B','C','D','E','F','G','H', or 'X'\n")
            choice = input(inpt)

#-------------------add_or_remove_deals---------------
    while (choice =='G'):
        if business == None:
            print("\nError: There is not any business. Please add a business first.\n")

        else:
            BS = input("Enter the Business Name.\n")
            try:
                if ((BS) in business.keys()) == True:
                    try:
                        wn = input('Enter the ware name.\n')
                        if (('Ware Name', wn) in business[BS]['Ware Info'].items()):
                            ar = input("Please type 'A' to add a deal or type 'R' to remove the current deal.\n")
                            if ar == 'A':
                                rate = float(input('Enter the percentage of current deal.\n'))
                                if rate < 0:
                                    rate = rate*(-1)
                                obj.add_or_remove_deals(BS,rate)
                            elif ar == 'R':
                                rate = 0
                                obj.add_or_remove_deals(BS,rate)
                            else:
                                print('\nError: Incorrect choice. Try again.\n')
                            #obj.add_or_remove(BS,rate)
                        else:
                            print('\nWare Name not found.Please try again.\n')

                    except ValueError:
                        print("\nErorr: Incorrect format. Please try again.\n")
                else:
                    print('\nBusiness Name not found.Please try again.\n')
            except ValueError:
                        print("\nErorr: Incorrect format. Please try again.\n")

        choice = input(inpt)
        while (choice not in list):
            print("\nError: Invalid option. Please type 'A','B','C','D','E','F','G','H', or 'I'\n")
            choice = input(inpt)
    
#-------------Buy Ware----------
    while choice == 'H':
        if business == None:
            print("\nError: There are not any businesses. Please add a business first.\n")

        else:
            BS = input("Enter the Business Name.\n")
            try:
                if ((BS) in business.keys()) == True:
                    WN = business[BS]['Ware Info']['Ware Name']
                    BP = business[BS]['Ware Info']['Price_of_each_ware'] - (business[BS]['Ware Info']['Price_of_each_ware'] * (business[BS]['Ware Info']['Current Deals']/100))
                    AB = business[BS]['Ware Info']['Available Items']
                    obj1.buying_info(WN,BP,AB)

                else:
                    print('\nBusiness Name not found.Please try again.\n')
            except ValueError:
                print("\nErorr: Incorrect format. Please try again.\n")

        choice = input(inpt)
        while (choice not in list):
            print("\nError: Invalid option. Please type 'A','B','C','D','E','F','G','H', or 'X'\n")
            choice = input(inpt)

#-------------Exit-----------

    while choice == 'X':
        print("\nThank you, have a nice day.\n")
        raise SystemExit