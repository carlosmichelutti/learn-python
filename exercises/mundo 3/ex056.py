brasileirao = (
    'PALMEIRAS',
    'INTERNACIONAL',
    'FLUMINENSE',
    'CORINTHIANS',
    'FLAMENGO',
    'AHTLETICO',
    'ATLETICO',
    'FORTALEZA',
    'SÃO PAULO',
    'AMERICA',
    'BOTAFOGO',
    'SANTOS',
    'BRAGANTINO',
    'CORITIBA',
    'CUIABA',
    'CEARA',
    'ATLETICO GO',
    'AVAÍ',
    'JUVENTUDE',
)

print('Lista de times do brasileirao: ')
print('\n'.join(brasileirao), end='\n')
print('')

print('G5')
print('\n'.join(brasileirao[0:5]))
print('')

print('Z4')
print('\n'.join(brasileirao[15:20]))
print('')

print('Ordem alfabética')
print('\n'.join(sorted(brasileirao)))
print('')

print(f'O time da SANTOS está na {brasileirao.index('SANTOS')+1}ª posição')
print('')
