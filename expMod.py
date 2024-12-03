def mod_exp(base, exp, mod):
    result = 1
    base = base % mod  # Asegura que la base esté dentro de los límites del módulo

    while exp > 0:
        # Si el exponente es impar, multiplica el resultado por la base actual
        if exp % 2 == 1:
            result = (result * base) % mod
        
        # Divide el exponente por 2
        exp = exp // 2
        # Eleva la base al cuadrado
        base = (base * base) % mod
    
    return result

# Ejemplo de uso
print(mod_exp(3, 1803, 77))
