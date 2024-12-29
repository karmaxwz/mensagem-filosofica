import time
from pywhatkit import sendwhatmsg_instantly

ddd_pais = '55'
numero = input('digite seu número: ')
numero_completo = f"+{ddd_pais}{numero}"

lista = []
with open('frases.txt', 'r', encoding='utf-8') as file:
    for frase in file:
        lista.append(frase)


index = 0
while index <= len(lista) - 1:
    frase_posicao = lista[index]
    sendwhatmsg_instantly(numero_completo, frase_posicao, 10, True, 3)
    print(f'{index}º item da lista')
    time.sleep(86400)
    index += 1

