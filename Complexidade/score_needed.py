

def final_score_needed(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3  # 3 math operations and 1 atribution = 4

    if media >= 7 or media < 4:  # two condition (boolean expression) = 2
        return 0  # 1 : It is not the worst case, so we can discosiderer
    else:
        mediaFinal = 5  # 1
        pesoFinal = 0.4  # 1
        pesoMedia = 0.6  # 1
        precisa = (mediaFinal - pesoMedia * media) / pesoFinal  # 4 maths and 1 attribution = 5
        return precisa  # 1
#Complexity = f(n) = 4 + 2 + 1 + 1 + 1 + 1 + 5 + 1 = 16 operations


#  I
