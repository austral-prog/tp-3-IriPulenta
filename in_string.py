def check_vowels():
    # Código a implementar utilizando input.
name = input("ingrese su nombre: ").lower()
print("contiene a: " + str("a" in name))
print("contiene e: " + str("e" in name))
print("contiene i: " + str("i" in name))
print("contiene o: " + str("o" in name))
print("contiene u: " + str("u" in name))

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
