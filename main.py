#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
v = []
for i in range(10):
  n = float(input('{}/10 - digite um numero:'.format(i+1)))
  v.append(n)

print(v[::-1])