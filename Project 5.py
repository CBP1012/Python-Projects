# Cristian Keroles
# 11/15/23
# Lab 5

# This programs encodes words/sentences to morse code and decodes from morse code to regular english

# creating loop
run = True
messageOut = ''

# create encryptionKey tuple
translationKey = (('A','.-'), ('B','-...'), ('C','-.-.'), ('D','-..'), ('E','.'),
                 ('F','..-.'), ('G','--.'), ('H','....'), ('I','..'), ('J','.---'),
                 ('K','-.-'), ('L','.-..'), ('M','--'), ('N','-.'), ('O','---'),
                 ('P','.--.'), ('Q','--.-'), ('R','.-.'), ('S','...'), ('T','-'),
                 ('U','..-'), ('V','...-'), ('W','.--'), ('X','-..-'), ('Y','-.--'),
                 ('Z','--..'), ('  ',' / '))

# user greeting
print('This program will translate your message to morse code and translate morse code')
print('back to english. Note: for translating morse code back to english make sure to')
print('spaces in between code.')
print()

# start main program loop
while run == True:

    # get selection (encode/decode)
    which = input ('Enter (M) to translate a message to Morse code, and (A) to translate a message from Morse code to english: ').upper()

    # error check selection
    while which not in ('M','A'):
        which = input("Invalid - Enter 'M' or 'A': ").upper()

    print()
    # get message
    message = input('Enter a message to translate: ')

    # set up subindex variables depend on M or A 
    if which == 'M':

        # this is so the letter get put in upper or lower case for the morse code program
        message = message.upper()
        # adding a space due to the confusion of morse code
        space = '/'
        fromIndex = 0
        toIndex = 1

    else:
        
        #this splits up the morse code so each input is split to its own section
        message = message.split()
        # we put space here but make it = to nothing due to morse code going back to english
        space = ''
        fromIndex = 1
        toIndex = 0

    # moves through input message one character at a time
    for character in message:

        # iteration through the encryptionKey using mainIndex
        for mainIndex in translationKey:
            if character == mainIndex[fromIndex]: 
                messageOut = messageOut + mainIndex[toIndex] + space
    print()

    # output
    if which == 'M':
        print(message,'translated in morse code is', messageOut)
        print()

    else:
        print('translated back to english is', messageOut)
        print()
        
    # empty messageOut variable
    messageOut = ''

    # rerun code question
    runAgain = input('Would you like to translate another message? Y/N: ').upper()
    print()
    
    # error check
    while runAgain not in ('Y','N'):
        runAgain = input('Error please input Y/N: ').upper()
        print()

    # end loop
    if runAgain == 'N':
        run = False

# exit message
print()
print('Have a nice day!')
