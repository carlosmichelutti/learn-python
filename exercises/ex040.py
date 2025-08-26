primeiro_termo = int(input('Qual o primeiro termo dessa progresão aritimetica? '))
razao = int(input('Qual a razão da progessão? '))

for num in range(primeiro_termo, (primeiro_termo + (11-1)*razao), razao):
    print(num, end=' -> ') if num < (primeiro_termo + (11-1)*razao - razao) else print(num)
