factorial_sequences = [0, 1, 2]


def factorial_recursion(n: int):
    if not n:
        return 1

    if n in [1, 2]:
        return n

    return factorial_recursion(n - 1) * n


def factorial_dp(n: int):
    if n < len(factorial_sequences):
        return factorial_sequences[n]

    for i in range(len(factorial_sequences), n + 1):
        factorial_sequences.append(factorial_sequences[i - 1] * i)

    return factorial_sequences[n]
