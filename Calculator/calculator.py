import math

while True: #User options to select calculator function
    print("\nWelcome to the Calculator: Choose The Math Operation.\n\n0 - Addition\n1 - Subtraction\n2 - Multiplication\n3 - Division\n4 - Modulo\n5 - Raising to a Power\n6 - Square Root\n7 - Logarithm\n8 - Sine\n9 - Cosine\n10 - Tangent\n")
    
    oper = input("\nYour Option from the Main Menu: ") #user input for calculator functions
    #Addtion
    if oper == "0": 
        val1 = float(input("\nFirst Value: ")) #first user input value
        val2 = float(input("\nSecond Value: ")) #second user input value
        #calculation
        print("\nThe Result is: " + str(val1 + val2) + "\n")
        
        back = input('\nGo Back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break
            
    #subtraction
    elif oper == "1": 
        val1 = float(input("\nFirst Value: ")) #first user input value
        val2 = float(input("\nSecond Value: ")) #second user input value
        #calculation
        print("\nThe Result is: " + str(val1 - val2) + "\n")
        #back to the main menu
        back = input('\nGo Back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break

    #Multiplication
    elif oper == "2": 
        val1 = float(input("\nFirst Value: ")) #first user input value
        val2 = float(input("\nSecond Value: ")) #second user input value
        #calculation
        print("\nThe Result is: " + str(val1 * val2) + "\n")
        #back to the main menu
        back = input('\nGo Back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break
            

    #Division
    elif oper == "3": 
        val1 = float(input("\nFirst Value: ")) #first user input value
        val2 = float(input("\nSecond Value: ")) #second user input value
        #calculation
        print("\nThe Result is: " + str(val1 / val2) + "\n")
        #back to the main menu
        back = input('\nGo Back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break

    #Modulo
    elif oper == "4":
        val1 = float(input("\nFirst Value: ")) #first user input value
        val2 = float(input("\nSecond Value: ")) #second user input value
        #calculation
        print("\nThe Result is: " + str(val1 % val2) + "\n")
        #back to the main menu
        back = input('\nGo Back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break
            
    #Raising to the a power
    elif oper == "5":
        val1 = float(input("\nFirst Value: ")) #first user input value
        val2 = float(input("\nSecond Value: ")) #second user input value
        #calculation
        print("\nThe Result is: " + str(math.pow(val1, val2)) + "\n")
        #back to the main menu
        back = input('\nGo Back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break
            
  #square root
    elif oper == "6":
        val1 = float(input("\nEnter Value for extracting Square root: ")) #user input value
        #calculation
        print("\nThe Result is: " + str(math.sqrt(val1)) + "\n")
        #back to the main menu
        back = input('\nGo Back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break
            
  #Logarithm
    elif oper == "7":
        val1 = float(input("\nEnter Value for extracting Logarithm: ")) #user input value
        #calculation
        print("\nThe Result is: " + str(math.log(val1, 2)) + "\n")
        #back to the main menu
        back = input('\nGo Back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break

  #Sine
    elif oper == "8":
        val1 = float(input("\nEnter the Value in (degrees) for calculating the sine: "))  #user input value
        #calculation
        print("\nThe Result is: " + str(math.sin(math.radians(val1))) + "\n") 
        #back to the main menu
        back = input('\nGo Back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break
            
  #Cosine
    elif oper == "9":
        val1 = float(input("\nEnter the Value in (degrees) for calculating the cosine: ")) #user input value
        #calculation
        print("\nThe Result is: " + str(math.cos(math.radians(val1))) + "\n")
        #back to the main menu
        back = input('\nGo Back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break
            
  #Tangent
    elif oper == "10":
        val1 = float(input("\nEnter the Value in (degrees) for calculating the tangent: "))
        #calculation
        print("\nThe Result is: " + str(math.tan(math.radians(val1))) + "\n")
        #back to the main menu
        back = input('\nGo Back to the main menu? (y/n) ')
        
        if back == 'y':
            continue
        else:
            break
            
#if invalid option selected by user
    else:
        print("\nInvalid Option! Please select options from 1 - 10")
        continue
        
#end of the program