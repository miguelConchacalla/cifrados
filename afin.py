# Calcula el MCD usando el algoritmo de Euclides
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Verifica si 'a' es coprimo con 26
def are_coprime(a):
    return gcd(a, 26) == 1

# Calcula el inverso modular de 'a' módulo 26
def keyinverse(a):
    for i in range(26):
        if (a * i) % 26 == 1:
            return i
    raise ValueError("El valor de 'a' no tiene inverso modular.")

# Cifra un texto usando el cifrado Afín
def affine_encrypt(text, a, b):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((a * (ord(char) - base) + b) % 26 + base)
        else:
            result += char
    return result

# Descifra un texto usando el cifrado Afín
def affine_decrypt(text, a, b):
    inv_a = keyinverse(a)
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            result += chr((inv_a * ((ord(char) - base) - b)) % 26 + base)
        else:
            result += char
    return result

# Interfaz principal
if __name__ == "__main__":
    print("Seleccione operación:")
    print("e: Cifrar texto")
    print("d: Descifrar texto")
    
    op = input("Ingrese 'e' para cifrar o 'd' para descifrar: ").strip().lower()
    text = input("Ingrese el texto: ").strip()
    
    try:
        a = int(input("Ingrese el valor de 'a' (coprimo con 26): ").strip())
        b = int(input("Ingrese el valor de 'b': ").strip())
    except ValueError:
        print("Los valores de 'a' y 'b' deben ser números enteros.")
        exit()
    
    if not are_coprime(a):
        print("El valor de 'a' debe ser coprimo con 26.")
        exit()
    
    if op == "e":
        print("Texto cifrado:", affine_encrypt(text, a, b))
    elif op == "d":
        print("Texto descifrado:", affine_decrypt(text, a, b))
    else:
        print("Operación inválida. Use 'e' para cifrar o 'd' para descifrar.")
