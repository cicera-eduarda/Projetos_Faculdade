##Conversor de temperatura

temperatura = float(input('Informe a temperatura em ºC:'))
kelvin = ( temperatura + 273.15 )
farenhit = (temperatura * 1.8 + 32 )
print('A temperatura de {}ºC, corresponde a {}K e a {}ºF'.format(temperatura, kelvin, farenhit))
