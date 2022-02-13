import sys
import palavras
import numpy as np


#mensagem de menu

while True:
    #mensagem de input
    word = input()
    if len(word) == 5 and word.isalpha():
        break
    # mensagem de rro

letras_descobertas = dict()
palavras_possiveis = palavras.words
letras_nao_contidas = list()
resultado = 'derrota'

for tentativa in range(1,6):
    index_palavra_selecionada = np.random.randint(0,len(palavras_possiveis))
    palavra_selecionada = palavras_possiveis[index_palavra_selecionada]
    print(palavra_selecionada)
    
    if palavra_selecionada == word:
        resultado = 'vitória'
        break

    for posicao,letra in enumerate(palavra_selecionada):
        if word[posicao] == letra:
            letras_descobertas[letra] = posicao
        
        elif word.count(letra)>0:
            letras_descobertas[letra] = 10

        else:
            letras_nao_contidas.append(letra)
        
    for letra,posicao in letras_descobertas.items():
        if posicao == 10:
            palavras_possiveis = [palavra for palavra in palavras_possiveis if letra in palavra]
        else:
            palavras_possiveis = [palavra for palavra in palavras_possiveis if palavra[posicao] == letra]

    for letra in letras_nao_contidas:
        palavras_possiveis = [palavra for palavra in palavras_possiveis if not letra in palavra]    
                    
        
print(f'resultado: {resultado}')
print(palavras_possiveis)
