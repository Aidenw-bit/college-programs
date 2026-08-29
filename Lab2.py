"""
Name:Aiden Weldon
Date:9/4/25
Purpose:Lab 2 Calculate the Standard deviation of 6 numbers
"""
#open math library
import math

#Welcome Message
print('This Program will calculate the Standard deviation of a data set of 6 numbers, please enter your numbers below.')

#Entering your data set
num1=float(input('number 1:'))
num2=float(input('number 2:'))
num3=float(input('number 3:'))
num4=float(input('number 4:'))
num5=float(input('number 5:'))
num6=float(input('number 6:'))

#calculating sum and average
sum=num1+num2+num3+num4+num5+num6
print(sum)
average=sum/6
print(average)


#calculating difference and sum of difference squared
diff1=num1-average
diff2=num2-average
diff3=num3-average
diff4=num4-average
diff5=num5-average
diff6=num6-average

sumsq= diff1**2+diff2**2+diff3**2+diff4**2+diff5**2+diff6**2
print(sumsq)

#dividing sum of differences squared
quotient=sumsq/6
print(quotient)

#Taking the square root of quotient
Standard_Deviation= round(math.sqrt(quotient),2)

#display Standard Deviation
print('the standard deviation of this data set is:', Standard_Deviation)

#Ending Message
print('This program is now ending...')


