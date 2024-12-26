nome = str(input('Escreva seu nome: '))
altura = float(input('Escreva sua altura em metros: '))
peso = float(input('Escreva seu peso em Kg: '))
imc = peso / (altura * altura)

print(f"{nome} tem {altura:.2f} de altura, seu peso é de {peso} quilos e seu IMC é de {imc:.2f}.")