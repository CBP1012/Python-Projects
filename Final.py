# Cristian Keroles
# 11/30/23
# Final Project

# This program is a contact list, it will store names, phone number and
# email addresses

# contact list

contactList = [['Juan L','3234567899','JL@gmail.com'],['Eric G','9094567890','EG@gmail.com'],
               ['Pablo H','2134567890','Duck@gmail.com']]
# Greeting

print('Hello welcome to the contact list!')
print('Please input what action you would like to make.')
print()

# Input list for user
print()
print('Type A to add a contact.')
print('Type E to edit a contact.')
print('Type D to delete a contact.')
print('Type L to list all contacts.')
print('Type H to show this list again.')
print('Type X to exit the program.')
print()

# program loop
run = True
while run == True:
    
    # input for choice
    choice = input('please type what you would like to do: ').upper()

    # Error check
    while choice not in ('A','E','D','L','H','X'):
        choice = input('Invalid input - please select choice from list: ').upper()

    print()

    # this will allow use to add contact in list

    if choice == 'A':

        # input for new contact

        name = input('please input name: ')

        phoneNumber = input('please input phone numer: ')

        eMail = input ('please input email address: ')

        contactList.append([name,phoneNumber,eMail])
        
        print()
        print('New contact added!')

    # this will allow use to edit contact in list

    elif choice == 'E':

        checkList = []

        # select which part of the contact to edit

        methodChoice = input('Please select which part of the contact to edit, [N]ame, [P]hone Number, or [E]mail: ').upper()
        
        #error check
        
        while methodChoice not in ('N','P','E'):
            methodChoice = input('Input Error - Please select[N]ame, [P]hone Number, or [E]mail:').upper()

        # this is to edit the name in contact list using name
        
        if methodChoice == 'N':

            # this is to select name to change
            name = input('please input name you would like to change: ')


            # loop for name through contact list
            for mainIndex in contactList:
                checkList.append(mainIndex[0])
                
            # in the case name not found
            while name not in checkList:
                name = input('error name not found. please renter: ')

            # name matches    
                    
            for mainIndex in contactList:

                if name == mainIndex[0]:

                    # new name input
                    
                    newName = input('Please input new name:')

                    # to add new name to list

                    mainIndex[0] = newName
                    
                    print()
                    print('Name edited succesfully!')
                    
        # This will allow user to edit phone number
        
        elif methodChoice == 'P':

            # this is to select number to change
            phoneNumber = input('please input phone number you would like to change: ')

            # Loop for number through list
            
            for mainIndex in contactList:
                checkList.append(mainIndex[1])

            # this is in case number is not found in list

            while phoneNumber not in checkList:
                phoneNumber = input('error phone number not found. please renter: ')

            # number matches
            
            for mainIndex in contactList:
                if phoneNumber == mainIndex[1]:

                    # new number input

                    newNumber = input('Please input new number: ')

                    #to add new number to list

                    mainIndex[1] = newNumber
                    
                    print()
                    print('Number edited succesfully!')

        # this will allow user to edit email
        
        else:

            # this is select email to change

            eMail = input('please input email you would like to change: ')

            # this is to move email through contact list
            
            for mainIndex in contactList:
                checkList.append(mainIndex[2])

            # error check if email not found
            
            while eMail not in checkList:
                eMail = input('error email not found. please renter: ')

            # when email matches

            for mainIndex in contactList:

                if eMail == mainIndex[2]:

                    # new email input

                    newEmail = input('please input new email: ')
                    
                    # to add new email to list

                    mainIndex[2] = newEmail

                    print()
                    print('Email edited succesfully!')

    # allow use to delete contact in list
    
    elif choice == 'D':
        
        checkList = []

        # select the look up method of contact you wish to delete

        methodChoice = input('Please select which contact to delete through [N]ame, [P]hone Number, or [E]mail: ').upper()
        
        while methodChoice not in ('N','P','E'):
            
            methodChoice = input('Input Error - Please select[N]ame, [P]hone Number, or [E]mail:').upper()

        # delete contact through name
        
        if methodChoice == 'N':

            # this is to select name to delete
            name = input('please input name you would like to delete: ')

           # this check name through the list 

            for mainIndex in contactList:
                checkList.append(mainIndex[0])
                
            # in the case name not found in check list
            
            while name not in checkList:
                name = input('error name not found. please renter: ')
                
            # this is if name is found to delete contact
            
            for mainIndex in contactList:

                if name == mainIndex[0]:

                    del mainIndex[2]
                    del mainIndex[1]
                    del mainIndex[0]

                    contactList = list(filter(None,contactList))

                    print()
                    print('Contact succefully deleted!')

        # This is to delete contact through phone number
        
        elif methodChoice == 'P':

            # this is to select number to delete

            phoneNumber = input('please input number you would like to delete: ')

            # this is to check number through list
            
            for mainIndex in contactList:
                checkList.append(mainIndex[1])
                
            # in the case number not found
            
            while phoneNumber not in checkList:
                phoneNumber = input('error number not found. please renter: ')

            # If number is found through list deletes contact

            for mainIndex in contactList:

                if phoneNumber == mainIndex[1]:

                    del mainIndex[2]
                    del mainIndex[1]
                    del mainIndex[0]

                    contactList = list(filter(None,contactList))

                    print()
                    print('Contact succefully deleted!')

        # To delete contact through email
        
        else:


            # this is to select email to delete

            eMail = input('please input email you would like to delete: ')
            
            # this will check email through list

            for mainIndex in contactList:
                checkList.append(mainIndex[2])
                
            # in the case email not found
            
            while eMail not in checkList:
                eMail = input('error email not found. please renter: ')

            # if email is found then it will delete contact

            for mainIndex in contactList:

                if eMail == mainIndex[2]:

                    del mainIndex[2]
                    del mainIndex[1]
                    del mainIndex[0]

                    contactList = list(filter(None,contactList))

                    print()
                    print('Contact succefully deleted!')

    # This will allow use to see current list of contacts

    elif choice == 'L':

        for mainIndex in contactList:

            name = mainIndex[0]
            
            phoneNumber = mainIndex[1]

            eMail = mainIndex[2]

            print('-----------------------------------------')
            print('Contact name:   ', name)
            print('Phone number:   ', phoneNumber)
            print('E-mail:         ', eMail)
            print('-----------------------------------------')

    # this will display options again to user

    elif choice == 'H':
        print()
        print('Type A to add a contact.')
        print('Type E to edit a contact.')
        print('Type D to delete a contact.')
        print('Type L to list all contacts.')
        print('Type H to show this list again.')
        print('Type X to exit the program.')
        print()

    # allow user to exit program

    else:
        run = False

# exit message

print('Have a nice Day!')



        
        
    
