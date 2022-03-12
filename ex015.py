km = float(input('Quantos Km rodados? '))
dias = int(input('Quantos dias o carro ficou alugado? '))
vkm = km*0.15
diasr = dias*60
aluguel = vkm + diasr
print(f'O valor total do aluguel é de R${aluguel:.2f}')