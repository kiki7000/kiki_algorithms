permutation = [0, 0, 1]

def permutation_dp(n: int):
    if n < len(permutation):
        return permutation[n]

    for i in range(len(permutation), n + 1):
        permutation.append((i - 1) * (permutation[i - 1] + permutation[i - 2]))

    return permutation[n]
    