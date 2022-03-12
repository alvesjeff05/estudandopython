larg = float(input('Qual a largura da parede? '))
altu = float(input('Qual a altura da parede? '))
area = larg*altu
print(f'Sua parede tem o total de {area:.3f} m²')
print(f'Para pintar a parede será necessário um total de {area/2:.3f}l de tinta')