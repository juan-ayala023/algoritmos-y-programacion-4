def validar_balanceo(expresion):
    pila = []

    pares = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    aperturas = set(pares.values())
    cierres = set(pares.keys())

    for token in expresion:
        if token in aperturas:
            pila.append(token)
            print(f"Agregando token {token} a la pila")
        elif token in cierres:
            if not pila or pila[-1] != pares[token]:
                return False
            pila.pop()
            print(f"Removiendo token {pares[token]} de la pila")

    return len(pila) == 0


# Ejemplos de prueba
if __name__ == "__main__":
    casos = [
        ("([]{})", True),
        ("{[()]}", True),
        ("([)]",   False),
        ("{[}",    False),
        ("",       True),
    ]

    for expresion, esperado in casos:
        resultado = validar_balanceo(expresion)
        estado = "OK" if resultado == esperado else "FALLO"
        print(f"{estado} | '{expresion}' -> {resultado}")