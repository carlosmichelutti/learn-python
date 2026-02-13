brazilian_league = (
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

print('List of Brasileirao teams: ')
print('\n'.join(brazilian_league), end='\n')
print('')

print('Top 5')
print('\n'.join(brazilian_league[0:5]))
print('')

print('Bottom 4')
print('\n'.join(brazilian_league[15:20]))
print('')

print('Alphabetical order')
print('\n'.join(sorted(brazilian_league)))
print('')

print(f"SANTOS is in position {brazilian_league.index('SANTOS') + 1}")
print('')
