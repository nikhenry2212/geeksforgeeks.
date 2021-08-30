# Programa Python3 para encontrar o máximo
# produto de um subconjunto.
 
# def para encontrar o máximo
# produto de um subconjunto
 
 
def minProductSubset(a, n):
    if (n == 1):
        return a[0]
 

# Encontre a contagem de números negativos,
# contagem de zeros, valor máximo
# número negativo, valor mínimo
# número positivo e produto
# de números diferentes de zero
    max_neg = float('-inf')
    min_pos = float('inf')
    count_neg = 0
    count_zero = 0
    prod = 1
    for i in range(0, n):
 
        # Se o número for 0, não
        # multiplique por produto.
        if (a[i] == 0):
            count_zero = count_zero + 1
            continue
 
        # Conte os negativos e mantenha
        # faixa de valor máximo
        # negativo.
        if (a[i] < 0):
            count_neg = count_neg + 1
            max_neg = max(max_neg, a[i])

        # Rastrear mínimo positivo
        # número da matriz
        if (a[i] > 0):
            min_pos = min(min_pos, a[i])
 
        prod = prod * a[i]
 
    # Se houver apenas zeros
    # ou nenhum número negativo
    # presente
    if (count_zero == n or (count_neg == 0
                            and count_zero > 0)):
        return 0

    # Se houver todos positivos
    if (count_neg == 0):
        return min_pos

    # Se houver número par de
    # números negativos e count_neg
    # não 0
    if ((count_neg & 1) == 0 and
            count_neg != 0):
 
        # Caso contrário, o resultado é produto de
        # todos não zeros divididos por
        # valor máximo negativo.
        prod = int(prod / max_neg)
 
    return prod
  
# Código do driver
a = [-1, -1, -2, 4, 3]
n = len(a)
print(minProductSubset(a, n))

