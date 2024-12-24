# Importando bibliotecas
import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_symbols=True):
    """Gera uma senha aleatória com base nos parâmetros fornecidos."""

    if length < 4:
        print("O comprimento mínimo recomendado para uma senha é 4.")
        return None

    # Base para a senha 
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    # Garante que pelo menos um caractere de cada tipo selecionado esteja presente
    password = []
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Preenche o restante da senha com caracteres aleatórios 
    password += random.choices(characters, k=length - len(password))

    # Embaralha os caracteres para evitar padrões 
    random.shuffle(password)
    return ''.join(password)


def main():
    print("=== Gerador de Senhas Aleatórias ===")
    try:
        length = int(input("Digite o comprimento da senha (mínimo 4): "))
        use_uppercase = input("Incluir letras maiúsculas? (s/n): ").strip().lower() == 's'
        use_digits = input("Incluir números? (s/n): ").strip().lower() == 's'
        use_symbols = input("Incluir símbolos? (s/n): ").strip().lower() == 's'

        password = generate_password(length, use_uppercase, use_digits, use_symbols)
        if password:
            print(f"\nSua senha gerada é: {password}")
    except ValueError:
        print("Por favor, insira um número válido para o comprimento da senha.")


if __name__ == "__main__":
    main()