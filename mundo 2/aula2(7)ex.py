frase =  str(input('ESCREVA UMA FRASE: ')).strip().upper().replace(' ', "")
string = frase[::-1].strip().upper().replace(' ', "")

if frase.strip().upper().replace(' ', "") == string:
    print('''A FRASE {} É UM POLÍNDROMO E ELA É COMPLETAMENTE IGUAL DE FRENTE PARA TRÁS COMO DE TRÁS PARA FRENTE \n
    FRASE NORMAL: {}
    FRASE AO CONTRÁRIO: {}\n'''.format(frase, frase, string))
elif frase[::-1].strip().upper != string:
    print('A FRASE {} NÃO É UM POLIDROMO.'.format(frase))
