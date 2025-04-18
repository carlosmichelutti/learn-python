primeiro_termo = int(input('Qual o primeiro termo dessa progresão aritimetica? '))
razao_progressao = int(input('Qual a razão da progessão? '))
proximo_termo = primeiro_termo
cont = 1
resp = 1

for num in range(10):
    print(f'{proximo_termo} -> ', end='') if num < 9 else print(proximo_termo)
    proximo_termo += razao_progressao

quantidade_termos = int(input('Quer mostrar mais quantos termos? '))
while True:
    for num in range(0, quantidade_termos):
        print(f'{proximo_termo} -> ', end='') if num < quantidade_termos - 1 else print(proximo_termo)
        proximo_termo += razao_progressao

    quantidade_termos = int(input('Quer mostrar mais quantos termos? '))
    if quantidade_termos == 0:
        break
