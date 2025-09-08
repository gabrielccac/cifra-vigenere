from vignere import VigenereCipher

def main():
    # Instancia a classe
    cipher = VigenereCipher()
    
    # Exemplo de uso - Cifração
    print("=== TESTE DE CIFRAÇÃO ===")
    texto = "HELLO WORLD"
    chave = "KEY"
    
    texto_cifrado = cipher.encrypt(texto, chave)
    print(f"Texto original: {texto}")
    print(f"Chave: {chave}")
    print(f"Texto cifrado: {texto_cifrado}")
    
    # Exemplo de uso - Decifração
    print("\n=== TESTE DE DECIFRAÇÃO ===")
    texto_decifrado = cipher.decrypt(texto_cifrado, chave)
    print(f"Texto decifrado: {texto_decifrado}")
    
    # Exemplo de uso - Quebra de cifra
    print("\n=== TESTE DE QUEBRA DE CIFRA ===")
    
    # Texto mais longo para teste
    texto_longo = """
    A criptografia e uma ciencia muito importante para a seguranca da informacao.
    Ela permite proteger dados sensveis atraves de algoritmos matematicos.
    A cifra de Vigenere foi uma das primeiras cifras consideradas seguras.
    """
    
    chave_secreta = "SEGURANCA"
    cifrado_longo = cipher.encrypt(texto_longo, chave_secreta)
    
    print(f"Texto cifrado: {cifrado_longo[:50]}...")
    print(f"Chave original: {chave_secreta}")
    
    # Quebra a cifra sem conhecer a chave
    chave_encontrada, texto_quebrado = cipher.break_cipher(cifrado_longo, 'pt')
    
    print(f"Chave encontrada: {chave_encontrada}")
    print(f"Texto quebrado: {texto_quebrado[:50]}...")

if __name__ == "__main__":
    main()