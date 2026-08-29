"""
Aiden Weldon
10/21/2025
purpose: creating different shapes using nested FOR loops
"""

#welcome message
print('This program will create shapes using various types of nested loops, the program will stop running after a shape is displayed.')
print('The program will not run if a number higher than 4 or lower than 1 is entered.')

#loop condition
running = True

#establishing loop
while running == True:
    #read in a pattern
    pat = int(input('To begin the program, please select a pattern: 1, 2, 3, or 4.'))
    print('You have selected pattern', pat)
    
    #pattern 1: Right Triangle
    if pat ==1:
        print('\n','pattern 1: Right Triangle')
        for row in range(6):
            for col in range(row):
                print('*', end="")
            print()
        
    
    #Pattern 2: Right Triangle
    elif pat == 2:
        print('Pattern2: Right Triangle')
        for row in range(5,0,-1):
            for col in range(row):
                print('*', end="")
            print()
       
    
    #Pattern 3: Pyramid
    elif pat ==3:
        print("Pattern 3: Pyramid")
        for row in range(1,5):
            for col in range(5-row):
                print(' ', end="")
            for col in range(2*row-1):
                print("*", end="")
            print()
        
    
    #Pattern 4: Diamond
    elif pat ==4:
        print("Pattern 4: Diamond")
        for row in range(6):
            for col in range(5-row):
                print(" ", end="")
            for col in range(2*row-1):
                if (col+ row) % 2==0:
                    print('#', end="")
                else:
                    print('*', end="")
            print()
        for row in range(1,5):
            for col in range(row):
                print(' ',end="")
            for col in range(4-(2*row-5)):
                if (col+row) % 2==0:
                    print('*',end="")
                else:
                    print('#',end="")        
            print()
        
    else:
        print('pattern entered is invalid..')
        
    response = input('Would you like to see another pattern? y/n')
    if not response == 'y':
        running = False

#ending message
print('Programing ending...')
        
