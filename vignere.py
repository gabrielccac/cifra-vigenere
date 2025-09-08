import string
import collections
from typing import List, Tuple, Dict
import math
import re

class VigenereCipher:
    """
    Implementação completa da Cifra de Vigenère
    Inclui cifração, decifração e ataque por análise de frequência
    """
    
    def __init__(self):
        # Frequências das letras em português (baseado na Wikipedia)
        self.freq_pt = {
            'A': 14.63, 'B': 1.04, 'C': 3.88, 'D': 4.99, 'E': 12.57,
            'F': 1.02, 'G': 1.30, 'H': 1.28, 'I': 6.18, 'J': 0.40,
            'K': 0.02, 'L': 2.78, 'M': 4.74, 'N': 5.05, 'O': 10.73,
            'P': 2.52, 'Q': 1.20, 'R': 6.53, 'S': 7.81, 'T': 4.34,
            'U': 4.63, 'V': 1.67, 'W': 0.01, 'X': 0.21, 'Y': 0.01,
            'Z': 0.47
        }
        
        # Frequências das letras em inglês
        self.freq_en = {
            'A': 8.12, 'B': 1.49, 'C': 2.78, 'D': 4.25, 'E': 12.02,
            'F': 2.23, 'G': 2.02, 'H': 6.09, 'I': 6.97, 'J': 0.15,
            'K': 0.77, 'L': 4.03, 'M': 2.41, 'N': 6.75, 'O': 7.51,
            'P': 1.93, 'Q': 0.10, 'R': 5.99, 'S': 6.33, 'T': 9.06,
            'U': 2.76, 'V': 0.98, 'W': 2.36, 'X': 0.15, 'Y': 1.97,
            'Z': 0.07
        }
    
    def prepare_text(self, text: str) -> str:
        """Remove caracteres não alfabéticos e converte para maiúscula"""
        return re.sub(r'[^A-Za-z]', '', text).upper()
    
    def encrypt(self, plaintext: str, key: str) -> str:
        """
        Cifra o texto usando a cifra de Vigenère
        
        Args:
            plaintext: Texto a ser cifrado
            key: Chave de cifração
            
        Returns:
            Texto cifrado
        """
        plaintext = self.prepare_text(plaintext)
        key = self.prepare_text(key)
        
        if not key:
            raise ValueError("Chave não pode estar vazia")
        
        ciphertext = ""
        key_index = 0
        
        for char in plaintext:
            if char.isalpha():
                # Converte caracteres para números (A=0, B=1, ...)
                plain_num = ord(char) - ord('A')
                key_num = ord(key[key_index % len(key)]) - ord('A')
                
                # Aplica a cifra
                cipher_num = (plain_num + key_num) % 26
                ciphertext += chr(cipher_num + ord('A'))
                
                key_index += 1
        
        return ciphertext
    
    def decrypt(self, ciphertext: str, key: str) -> str:
        """
        Decifra o texto usando a cifra de Vigenère
        
        Args:
            ciphertext: Texto cifrado
            key: Chave de decifração
            
        Returns:
            Texto decifrado
        """
        ciphertext = self.prepare_text(ciphertext)
        key = self.prepare_text(key)
        
        if not key:
            raise ValueError("Chave não pode estar vazia")
        
        plaintext = ""
        key_index = 0
        
        for char in ciphertext:
            if char.isalpha():
                # Converte caracteres para números
                cipher_num = ord(char) - ord('A')
                key_num = ord(key[key_index % len(key)]) - ord('A')
                
                # Aplica a decifração
                plain_num = (cipher_num - key_num) % 26
                plaintext += chr(plain_num + ord('A'))
                
                key_index += 1
        
        return plaintext
    
    def calculate_ic(self, text: str) -> float:
        """
        Calcula o Índice de Coincidência do texto
        
        Args:
            text: Texto para análise
            
        Returns:
            Valor do Índice de Coincidência
        """
        text = self.prepare_text(text)
        n = len(text)
        
        if n <= 1:
            return 0
        
        freq = collections.Counter(text)
        ic = sum(f * (f - 1) for f in freq.values()) / (n * (n - 1))
        
        return ic
    
    def find_key_length(self, ciphertext: str, max_length: int = 20) -> int:
        """
        Encontra o comprimento mais provável da chave usando Índice de Coincidência
        
        Args:
            ciphertext: Texto cifrado
            max_length: Comprimento máximo da chave a ser testado
            
        Returns:
            Comprimento mais provável da chave
        """
        ciphertext = self.prepare_text(ciphertext)
        ic_scores = {}
        
        for key_len in range(1, max_length + 1):
            # Divide o texto em grupos baseados na posição da chave
            groups = [''] * key_len
            
            for i, char in enumerate(ciphertext):
                groups[i % key_len] += char
            
            # Calcula IC médio para este comprimento de chave
            avg_ic = sum(self.calculate_ic(group) for group in groups) / key_len
            ic_scores[key_len] = avg_ic
        
        # Retorna o comprimento com maior IC (mais próximo de 0.065 para texto natural)
        return max(ic_scores.keys(), key=lambda k: ic_scores[k])
    
    def chi_squared_test(self, observed_freq: Dict[str, int], 
                        expected_freq: Dict[str, float], text_length: int) -> float:
        """
        Calcula o teste qui-quadrado para comparar frequências
        
        Args:
            observed_freq: Frequências observadas
            expected_freq: Frequências esperadas (em percentual)
            text_length: Comprimento do texto
            
        Returns:
            Valor do teste qui-quadrado
        """
        chi_squared = 0
        
        for letter in string.ascii_uppercase:
            observed = observed_freq.get(letter, 0)
            expected = (expected_freq.get(letter, 0) / 100) * text_length
            
            if expected > 0:
                chi_squared += ((observed - expected) ** 2) / expected
        
        return chi_squared
    
    def find_key_letter(self, ciphertext_group: str, language: str = 'pt') -> str:
        """
        Encontra a letra da chave para um grupo específico usando análise de frequência
        
        Args:
            ciphertext_group: Grupo de caracteres cifrados
            language: Idioma para análise ('pt' ou 'en')
            
        Returns:
            Letra mais provável da chave
        """
        freq_table = self.freq_pt if language == 'pt' else self.freq_en
        best_key_char = 'A'
        best_chi_squared = float('inf')
        
        # Testa cada possível deslocamento (A-Z)
        for shift in range(26):
            # Decifra o grupo com este deslocamento
            decrypted = ""
            for char in ciphertext_group:
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                decrypted += decrypted_char
            
            # Calcula frequências observadas
            observed_freq = collections.Counter(decrypted)
            
            # Calcula qui-quadrado
            chi_squared = self.chi_squared_test(observed_freq, freq_table, len(decrypted))
            
            if chi_squared < best_chi_squared:
                best_chi_squared = chi_squared
                best_key_char = chr(shift + ord('A'))
        
        return best_key_char
    
    def break_cipher(self, ciphertext: str, language: str = 'pt') -> Tuple[str, str]:
        """
        Quebra a cifra de Vigenère usando análise de frequência
        
        Args:
            ciphertext: Texto cifrado
            language: Idioma do texto original ('pt' ou 'en')
            
        Returns:
            Tupla (chave_encontrada, texto_decifrado)
        """
        ciphertext = self.prepare_text(ciphertext)
        
        # 1. Encontra o comprimento da chave
        key_length = self.find_key_length(ciphertext)
        print(f"Comprimento da chave estimado: {key_length}")
        
        # 2. Divide o texto em grupos baseados na posição da chave
        groups = [''] * key_length
        for i, char in enumerate(ciphertext):
            groups[i % key_length] += char
        
        # 3. Encontra cada letra da chave
        key = ""
        for i, group in enumerate(groups):
            key_letter = self.find_key_letter(group, language)
            key += key_letter
            print(f"Posição {i+1} da chave: {key_letter}")
        
        # 4. Decifra o texto com a chave encontrada
        decrypted_text = self.decrypt(ciphertext, key)
        
        return key, decrypted_text
    
    def kasiski_examination(self, ciphertext: str, min_length: int = 3) -> Dict[int, int]:
        """
        Realiza o exame de Kasiski para encontrar padrões repetidos
        
        Args:
            ciphertext: Texto cifrado
            min_length: Comprimento mínimo dos padrões a procurar
            
        Returns:
            Dicionário com distâncias e suas frequências
        """
        ciphertext = self.prepare_text(ciphertext)
        distances = []
        
        # Procura padrões repetidos
        for length in range(min_length, min(len(ciphertext) // 2, 10)):
            for i in range(len(ciphertext) - length):
                pattern = ciphertext[i:i + length]
                
                # Procura outras ocorrências deste padrão
                for j in range(i + length, len(ciphertext) - length + 1):
                    if ciphertext[j:j + length] == pattern:
                        distance = j - i
                        distances.append(distance)
        
        # Conta frequências das distâncias
        distance_freq = collections.Counter(distances)
        
        return dict(distance_freq)

def test_cipher():
    """Função de teste para verificar a implementação"""
    cipher = VigenereCipher()
    
    # Teste básico de cifração/decifração
    print("=== TESTE DE CIFRAÇÃO/DECIFRAÇÃO ===")
    plaintext = "HELLO WORLD"
    key = "KEY"
    
    encrypted = cipher.encrypt(plaintext, key)
    decrypted = cipher.decrypt(encrypted, key)
    
    print(f"Texto original: {plaintext}")
    print(f"Chave: {key}")
    print(f"Texto cifrado: {encrypted}")
    print(f"Texto decifrado: {decrypted}")
    print(f"Decifração correta: {plaintext.replace(' ', '') == decrypted}")
    
    print("\n=== TESTE DE QUEBRA DE CIFRA ===")
    # Exemplo com texto mais longo para teste de quebra
    long_text = """
    A criptografia é uma ciência que estuda métodos para codificar mensagens 
    de forma que apenas o destinatário autorizado possa lê-las. Ela é fundamental 
    para a segurança da informação em nosso mundo digital.
    """
    
    test_key = "SEGURANCA"
    encrypted_long = cipher.encrypt(long_text, test_key)
    
    print(f"Texto cifrado (primeiros 100 caracteres): {encrypted_long[:100]}...")
    print(f"Chave original: {test_key}")
    
    # Tenta quebrar a cifra
    found_key, decrypted_long = cipher.break_cipher(encrypted_long, 'pt')
    
    print(f"Chave encontrada: {found_key}")
    print(f"Primeiros 100 caracteres decifrados: {decrypted_long[:100]}...")
    
    # Verifica se a chave encontrada está correta
    verification = cipher.decrypt(encrypted_long, found_key)
    original_clean = cipher.prepare_text(long_text)
    print(f"Quebra bem-sucedida: {verification == original_clean}")

if __name__ == "__main__":
    test_cipher()