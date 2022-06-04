tempo = int(input('Digite por quantos dias o carro ficou sendo alugado: '))
km = float(input('Digite a quantidade de KM rodados com o carro no período que foi alugado: '))

total = (tempo * 60) + (km * 0.15)
print('O valor a ser pago é de R${:.2f}'.format(total))