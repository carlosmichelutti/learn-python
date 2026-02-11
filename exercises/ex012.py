value = input('Enter something: ')

print('The primitive type of this value is', type(value))
print('Is it alphanumeric?', value.isalnum())
print('Is it alphabetic?', value.isalpha())
print('Is it a number?', value.isnumeric())
print('Does it contain only spaces?', value.isspace())
