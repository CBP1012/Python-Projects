# Cristian Keroles
# 10/26/23
# Lab 4

# This program converts inches to centimeters and vice versa, centermeteres to inches and
# viceversa, grams to ounces and viceversa, and kilometers to miles and viceversa.

# Description of program

print('Hello! This program converts Inches to Centimeters, Centimeters to Inches, Grams')
print('to Ounces, Ounces to Grams, Kilometers to Miles, or Miles to Kilometer')
print()

# Loop
run=True
while run==True:
    # User input choices
    print('Enter I to convert from Inches to Centimeters.')
    print('Enter C to convert from Centimeters to Inches.')
    print('Enter O to convert from Ounces to Grams.')
    print('Enter G to convert from Grams to Ounces.')
    print('Enter M to convert from Miles to Kilometers.')
    print('Enter K to convert from Kilometers to Miles.')
    print()
    
    # User Input
    choice=input('what caculation would you like to do:').upper()
    while choice not in ('I','C','O','G','M','K'):
        choice=input('Input Error: Please enter I,C,O,G,M or K:').upper()
        
    # User Input for measurement or weight
    A=float(input('Enter the measure/weight to convert: '))
    print()

    # Calulations used depending on user input
    
    if choice=='I':
        AnswerI = A * 2.54
        
        print(A,'Centimeters equals to',format(AnswerI, ',.2f'), 'inches.')
        print()

    elif choice=='C':
        AnswerC = A / 2.54
        
        print(A,'Inches equals to',format(AnswerC, ',.2f'), 'Centimeters.')
        print()
        
    elif choice=='O':
        AnswerO = A * 28.3495231
        
        print(A,'Ounces equals to',format(AnswerO, ',.2f'), 'Grams.')
        print()

    elif choice=='G':
        AnswerG = A / 28.3495231
        
        print(A,'Grams equals to',format(AnswerG, ',.2f'), 'Ounces.')
        print()

    elif choice=='M':
        AnswerM = A * 1.609344
        
        print(A,'Miles equals to',format(AnswerI, ',.2f'), 'Kilometers.')
        print()

    else:
        choice=='K'
        AnswerK = A / 1.6093344
        
        print(A,'Kilometers equals to',format(AnswerK, ',.2f'), 'Miles.')
        print()

# run again question
        
runAgain=input('want to do another calculations, y/n:').lower()
while runAgain not in ('y','n'):
    runAgain=input('Input Error y/n:').lower()

if runAgain=='n':
    run=False

# Exit message

print('Have a nice day')


       
        
