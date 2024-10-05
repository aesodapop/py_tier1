## fahrenheit to celsius calculator
while 1==1:
    convert = input('hello, to convert the temp to celsius type c or to fahrenheit type f: ')
    if convert == 'c':
        input1 = float(input('input temp in fahrenheit: '))
        conversion = (input1 - 32) * (5/9)
        print(input1, 'degrees fahrenheit is equal to',round(conversion, 1),'degrees celsius')

    if convert == 'f':
        input1 = float(input('input temp in celsius: '))
        conversion = (input1 * (9/5) + 32)
        print(input1, 'degrees celsius is equal to',round(conversion, 1),'degrees fahrenheit')   

