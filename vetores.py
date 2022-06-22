lista = [22174.16, 24537.66, 26139.61, 26742.66, 42889.22, 46251.17, 11191.47, 3847.48, 373.78,
         2659.75, 48924.24, 18419.26, 35240.18, 43829.16, 18235.68,
         4355.06, 13327.10, 25681.83, 1718.12, 13220.49, 8414.61]
maior = 0
menor = 0
i = 0
while i < len(lista):
    if lista[i] > maior:
        maior = lista[i]
    if lista[i] < menor:
        menor = lista[i]

print('O maior valor é {}'.format(maior))
print()
print('O menor valor é {}'.format(menor))