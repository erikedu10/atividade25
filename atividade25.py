# Exercício Python 25: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas

numero = [] 


for i in range(0,6):
    inserirNumero = int(input("DIGITE UM NUMERO "))
    
    if inserirNumero % 2 == 0:
        
        numero.append(inserirNumero) 

soma = sum(numero) 
print(soma)