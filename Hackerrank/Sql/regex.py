import re

'''
Metacharacter: .
. : Any Character (except \n newline)
a.c -> abc, aac, acc, adc, aec
'''

def vowels_words(arquivo):
    regex = r'^[aeiou][a-z]*'
    with open(arquivo, 'r') as file:
        linhas = file.read()
        #print(linhas)

    #linhas = 'ajiwejdweu'

    #teste = re.findall(regex, linhas)
    print(linhas)
    return linhas


vowels_words('city_names.txt')

