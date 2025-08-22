def calcular_area(largura: int, comprimento: int):
    calculo = largura * comprimento
    print(f'A área de um terreno de {largura}x{comprimento} é igual a {calculo}m².')

largura = int(input('Digite a largura do terreno: '))
comprimento = int(input('Digite o cumprimento do terreno: '))

calcular_area(largura=largura, comprimento=comprimento)
