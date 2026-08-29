"""
Write a program that will calculate the area and the circumference of a circle
{A=pi * radius^2;  C= 2pi * radius

Pseudocode:

1.Ask for the radius
2.calculate area
3. calculate circumference
4.display the results

"""

#Import libraries
import math

#read in radius

radius= float(input('Enter the radius:'))

#calculate area and circumference

area= math.pi* radius**2
circumference= 2*math.pi*radius

#display area and circumference 

print('The area is', round(area,2), 'and the circumference is', round(circumference,2))
print('The area is'+str(round(area,2)) + 'and the circumference is ' +str(round(circumference,2)))