# Cifra de Vigenère - Implementação Completa

Implementação da **Cifra de Vigenère** com interface web moderna, incluindo funcionalidades de cifração, decifração e ataque criptoanalítico.

## 📋 Características

### 🔐 Funcionalidades Principais
- **Cifração de Mensagens**: Codifique textos usando uma chave personalizada
- **Decifração de Mensagens**: Decodifique textos cifrados com a chave conhecida  
- **Ataque Criptoanalítico**: Quebra automática da cifra sem conhecer a chave

### 🎯 Técnicas de Criptoanálise
- **Índice de Coincidência (IC)**: Determinação do comprimento da chave
- **Análise de Frequência**: Identificação de cada letra da chave
- **Teste Qui-quadrado**: Comparação com frequências esperadas
- **Suporte Multilíngue**: Análise em Português e Inglês

### 💡 Interface Moderna
- Design responsivo com tema escuro
- Navegação por abas intuitiva
- Feedback visual em tempo real
- Componentes customizados (select personalizado)

## 🚀 Como Usar

### Cifração
1. Acesse a aba **"Cifrar"**
2. Digite o texto que deseja cifrar
3. Insira uma chave (ex: "CHAVE")
4. Clique em **"Cifrar Mensagem"**
5. O resultado aparecerá na área de resultado

### Decifração
1. Acesse a aba **"Decifrar"**
2. Digite o texto cifrado
3. Insira a chave utilizada na cifração
4. Clique em **"Decifrar Mensagem"**
5. O texto original será exibido

### Ataque Criptoanalítico
1. Acesse a aba **"Ataque Criptoanalítico"**
2. Cole o texto cifrado (mínimo 50 caracteres)
3. Selecione o idioma do texto original
4. Clique em **"Executar Ataque"**
5. Analise os resultados: chave descoberta e texto decifrado

## 🛠️ Tecnologias

### Frontend
- **HTML5**: Estrutura semântica
- **CSS3**: Estilização moderna com CSS Variables
- **JavaScript ES6+**: Lógica da aplicação

### Algoritmos Implementados
- Cifra de Vigenère (cifração/decifração)
- Cálculo do Índice de Coincidência
- Análise de frequência de letras
- Teste qui-quadrado para validação estatística

## 📁 Estrutura do Projeto

```
cifra-vignere/
├── page.html          # Interface web completa
├── main.py            # Implementação Python (opcional)
└── README.md          # Documentação
```

## 🎨 Design System

### Cores
- **Fundo Principal**: `#000000`
- **Elementos**: `#1D1D1D` / `#2C2C2C`
- **Texto Principal**: `#F8FAFC`
- **Texto Secundário**: `#878787`
- **Sucesso**: `#22C55E`
- **Aviso**: `#AFC522`

### Tipografia
- **Principal**: Geist (sans-serif)
- **Código**: Geist Mono (monospace)

## 🔬 Algoritmo de Ataque

O ataque criptoanalítico funciona em etapas:

1. **Determinação do Comprimento da Chave**:
   - Calcula o Índice de Coincidência para diferentes comprimentos
   - Seleciona o comprimento com maior IC (mais próximo de texto natural)

2. **Quebra de Cada Posição da Chave**:
   - Divide o texto em grupos baseados na posição da chave
   - Aplica análise de frequência em cada grupo
   - Usa teste qui-quadrado para encontrar a melhor correspondência

3. **Validação e Resultado**:
   - Reconstrói a chave completa
   - Decifra o texto usando a chave descoberta
   - Apresenta análise detalhada do processo

## 📊 Precisão

O algoritmo de ataque tem melhor performance com:
- **Textos longos**: Mínimo 50 caracteres (recomendado 200+)
- **Texto natural**: Evitar números e símbolos
- **Idioma correto**: Selecionar Português ou Inglês conforme o texto original

## 🎓 Contexto Acadêmico

**Disciplina**: CIC0201 - Segurança Computacional  
**Professora**: Priscila Solis  
**Autor**: Gabriel Farago

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais como parte do curso de Segurança Computacional.