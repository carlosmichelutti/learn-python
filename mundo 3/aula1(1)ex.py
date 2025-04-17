brasileirao = ('PALMEIRAS', 'INTERNACIONAL', 'FLUMINENSE', 'CORINTHIANS', 'FLAMENGO', 'AHTLETICO', 'ATLETICO', 'FORTALEZA', 'SÃO PAULO', 'AMERICA', 'BOTAFOGO', 'SANTOS', 'BRAGANTINO', 'CORITIBA', 'CUIABA', 'CEARA', 'ATLETICO GO', 'AVAÍ', 'JUVENTUDE')

print('LISTA DE TIMES DO BRASILEIRAO: ')
print('{}'.format(brasileirao))
print('=+='*10)

print('{:^20}'.format('G5'))
print('{}'.format(brasileirao[0:5]), end='\n')
print('=+='*10)


print('{:^20}'.format('Z4'))
print('{}'.format(brasileirao[15:20]))
print('=+='*10)

print('{:^20}'.format('ORDEM ALFABETICA'))
print('{}'.format(sorted(brasileirao)))
print('=+='*10)

print('{:^20}'.format('POSIÇÃO DO CORITIBA'))
print('{}'.format(brasileirao.index('SANTOS')+1))
print('=+='*10)


