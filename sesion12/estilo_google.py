def fibonacci(n: int) -> str:
    """Devuelve la secuencia de Fibonacci hasta el n-ésimo número.

    Args:
        n (int): El índice del número de Fibonacci a calcular.

    Returns:
        str: La secuencia de Fibonacci hasta el n-ésimo número.

    Raises:
        ValueError: Si n es negativo.

    Examples:
        >>> fibonacci(5)
        '0, 1, 1, 2, 3'
    """
    if n < 0:
        raise ValueError("El índice no puede ser negativo")
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return ', '.join(str(x) for x in fib[:n])
print (fibonacci(5))