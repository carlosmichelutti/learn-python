wallet_amount = float(input('How much money do you have in your wallet? R$'))

dollars = wallet_amount / 5.21
euros = wallet_amount / 5.67
yen = wallet_amount * 25.01

print(f'With R${wallet_amount} you have US${dollars:.2f} dollars, €{euros:.2f} euros and ¥{yen:.2f} yen.')
