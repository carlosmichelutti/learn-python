player = {
    'Player Name': str(input('What is the player name? ')).lower().strip(),
    'Total Goals': 0,
    'Matches': []
}
matches = int(input(f'How many matches did player {player["Player Name"]} play? '))

for match in range(0, matches):
    goals = int(input(f'How many goals did player {player["Player Name"]} score in match {match + 1}? '))
    player['Matches'].append({'match': match + 1, 'goals': goals})
    player['Total Goals'] += goals

print(f'Player {player["Player Name"]} played {matches} matches.')

for match in range(0, matches):
    print(f'=> In match {match + 1}, player {player["Player Name"]} scored {player["Matches"][match]["goals"]} goals.')
