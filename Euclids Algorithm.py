number1=float(input('what is the first number:'))
number2=float(input('what is the second number:'))
print(number1)
print(number2)
print('find GCD of','(',number1,number2,')')
number3= number1 % number2
if number3 == 0:
    print(number2)
number4= number2 % number3
if number4 == 0:
    print(number3)
number5= number3 % number4
if number5 == 0:
    print(number4)
number6= number4 % number5
if number6 == 0:
    print(number5)


