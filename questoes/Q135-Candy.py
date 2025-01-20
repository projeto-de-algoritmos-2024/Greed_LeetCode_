def candy(ratings):
    n = len(ratings)
    left = [1] * n
    right = [1] * n

    # Passagem da esquerda para a direita
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            left[i] = left[i - 1] + 1

    # Passagem da direita para a esquerda
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            right[i] = right[i + 1] + 1

    # Calcular o resultado somando os valores máximos de cada posição
    return sum(max(left[i], right[i]) for i in range(n))
