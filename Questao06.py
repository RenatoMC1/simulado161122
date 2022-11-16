# Questão 06
### 06. Um estacionamento cobra um valor mínimo de 10 reais, correspondente a 1h de uso. Cada hora adicional gera mais 5 reais de cobrança. Ex: um carro estacionado por 5 horas irá pagar 10 reais pela primeira hora + 5 reais pela segunda + 5 pela terceira + 5 pela quarta + 5 pela quinta, totalizando 30 reais.
### Faça um programa que pergunte para o usuário quanto tempo seu carro ficou estacionado e responde o valor em reais a ser pago.

for hora in range(1,2):
    hora = int(input(f"digite a hora(s) permanecida(s): "))
    if hora == 1:
        print(f"o valor a pagar é: {hora*10} reais")
    else:
        print(f"o valor a pagar é: {((hora - 1)*5)+10} reais")