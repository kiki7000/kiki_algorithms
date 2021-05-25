fibonacci_sequences = [0, 1, 1]


def fibonacci_recursion(n: int):
    if n in [0, 1, 2]:
        return 1

    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


def fibonacci_dp(n: int):
    if n < len(fibonacci_sequences):
        return fibonacci_sequences[n]

    for i in range(len(fibonacci_sequences), n + 1):
        fibonacci_sequences.append(fibonacci_sequences[i - 1] + fibonacci_sequences[i - 2])

    return fibonacci_sequences[n]
