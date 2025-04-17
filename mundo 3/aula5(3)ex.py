def maior(*num):
    print(f'FORAM REGISTRADOS {num}')
    maiorv = 0
    for c in range(0, len(num)):
        if num[c] > maiorv:
            maiorv = num[c]
    print(f'O MAIOR VALOR É {maiorv}')
    
c = 0
maior(4, 5, 6, 9, 15)
maior(1, 4, 5, 7, 3)
maior(1, 10)