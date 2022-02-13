import numpy as np

path = 'palavras.txt'

words = [word.strip('\n') for word in open(path) if len(word.strip('\n')) == 5] #coleta as palavras retirando as quebra de linhas
words = np.array(words)

