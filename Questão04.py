#Questão 04
###Faça um programa que solicite a nota das 4 provas de um aluno e responde a sua média.

soma = 0
média = 0

for contador in range(1,5):
    nota = int(input(f"digite a {contador} nota: "))
    soma = soma + nota
    média = soma/contador

print(f"a média é: ", média)