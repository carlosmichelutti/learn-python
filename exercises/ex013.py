phrase = str(input('Enter a sentence: ')).strip()

upper_phrase = phrase.upper()
count_a = upper_phrase.count('A')
first_a = upper_phrase.find('A')
last_a = upper_phrase.rfind('A')

print(f'The letter A appears {count_a} times in the sentence.')
print(f'The first letter A appeared at position {first_a + 1}.')
print(f'The last letter A appeared at position {last_a + 1}.')
