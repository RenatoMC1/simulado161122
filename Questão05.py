#Questão 05
### Crie um algoritmo que informe o tipo de um valor informado pelo usuário

escreva = input("Digite alguma palavra: ")
print(type(escreva))

numero = int(input("Digite algum número: "))
print(type(numero))

numero_dec = float(input("Digite algum número decimal: "))
print(type(numero_dec))

logico = int(input("Você é maior de 18 anos?\n[1] Verdadeiro\n[2] Falso\n"))
Condicao_verdadeira = True
Condicao_falsa = False
if logico == 1:
    print(type(Condicao_verdadeira))
else:
    print(type(Condicao_falsa))