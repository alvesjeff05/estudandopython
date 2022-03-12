catop = float(input('Digite o valor do cateto oposto: '))
catead = float(input('Digite o valor do cateto adjacente: '))
hipot = catop**2 + catead**2
print(f'O valor da hipotenusa é {hipot**(1/2):.2f}.')