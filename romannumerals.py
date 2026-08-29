"""
Name: Aiden Weldon
Date: 10/2/2025
Purpose: Converting a number to its roman numeral version.
"""

#welcome message
print('This program will convert a 3 digit integer into its roman numeral form.')
print('If the user inputs a non 3 digit number they will recieve a message saying\nthe number is invalid and the program will not run.')


#import library
import sys


#user prompt
print("\nPlease enter any integer in the range of 1 to 999\n" + "If you want to enter 300, type 300 and hit enter.\n"+"\n-->")

#assign value entered to variable
number = int(input())
romanNumeral = str()

#validation of number
if number <=0 or number >=1000:
    print("The number you have entered is invalid")
    sys.exit(1)
else:
    print("The number you have entered is valid.")
    
#isolating the unit places
units_One_Digit = number % 10
units_Ten_Digit = ((number % 100)- units_One_Digit)//10
units_Hundred_Digit = ((number % 1000)-units_Ten_Digit)//100

#Display the isolated digit for units
print("The isolated numbers are: " +str(units_Hundred_Digit), " " +str(units_Ten_Digit), " " +str(units_One_Digit) + "\n\n")

#if-elif-else statement for all 10 possible hundreds digits

if units_Hundred_Digit == 9:
    romanNumeral += "CM"
elif units_Hundred_Digit == 8:
    romanNumeral += "DCCC"
elif units_Hundred_Digit == 7:
    romanNumeral += "DCC"
elif units_Hundred_Digit == 6:
    romanNumeral += "DC"
elif units_Hundred_Digit == 5:
    romanNumeral += "D"
elif units_Hundred_Digit == 4:
    romanNumeral += "CD"
elif units_Hundred_Digit == 3:
    romanNumeral += "CCC"
elif units_Hundred_Digit == 2:
    romanNumeral += "CC"
elif units_Hundred_Digit == 1:
    romanNumeral += "C"
else:
    romanNumeral += " "


#if-elif-else statement for all ten possible tens digits

if units_Ten_Digit == 9:
    romanNumeral += "XC"
elif units_Ten_Digit == 8:
    romanNumeral += "LXXX"
elif units_Ten_Digit == 7:
    romanNumeral += "LXX"
elif units_Ten_Digit == 6:
    romanNumeral += "LX"
elif units_Ten_Digit == 5:
    romanNumeral += "L"
elif units_Ten_Digit == 4:
    romanNumeral += "XL"
elif units_Ten_Digit == 3:
    romanNumeral += "XXX"
elif units_Ten_Digit == 2:
    romanNumeral += "XX"
elif units_Ten_Digit == 1:
    romanNumeral += "X"
else:
    romanNumeral += " "

#if-elif-else statement for all ten possible ones digits
if units_One_Digit == 9:
        romanNumeral += "IX"
elif units_One_Digit == 8:
        romanNumeral += "VIII"
elif units_One_Digit == 7:
        romanNumeral += "VII"
elif units_One_Digit == 6:
        romanNumeral += "VI"
elif units_One_Digit == 5:
        romanNumeral += "V"
elif units_One_Digit == 4:
        romanNumeral += "IV"
elif units_One_Digit == 3:
        romanNumeral += "III"
elif units_One_Digit == 2:
        romanNumeral += "II"
elif units_One_Digit == 1:
        romanNumeral += "I"
else:
    romanNumeral += " "


#display results
print("The unit place of the value of"," "+str(number) + " in roman numerals is " +str(romanNumeral) + ".\n\n")

#termination message
print('Program ending')

