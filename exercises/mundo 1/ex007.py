comprimento = float(input('Digite o comprimento da parede: '))
largura = float(input('Digite a largura da parede: '))

area = comprimento * largura
tinta_necessaria = area / 2

print(f'Sua parede tem a dimensão {comprimento}x{largura} e a sua área é de {area}m².')
print(f'A sua parede de área {area}m² precisa de {tinta_necessaria:.0f} litros de tinta para ser pintada inteira.')
