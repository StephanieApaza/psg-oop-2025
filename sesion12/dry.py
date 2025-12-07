def area(lado1: int, lado2: int) -> int:
    """Calcula el área de un rectángulo o cuadrado.

    Args:
        lado1 (int): El primer lado.
        lado2 (int): El segundo lado.

    Returns:
        int: El área calculada.
    """
    return lado1 * lado2
print(area(5, 10))  # Área del rectángulo
print(area(5, 5))      # Área del cuadrado