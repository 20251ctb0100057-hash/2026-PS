# =====================================================
# SISTEMA DE CÁLCULO DE IMC
# =====================================================
# [Cabeçalho de identificação do autor e disciplina]

# ---- FUNÇÃO SEM PARÂMETROS E SEM RETORNO ----

def exibir_cabecalho(): # Define a função que não precisa de dados externos
    """Exibe o cabeçalho do sistema no terminal."""  # Docstring para documentar o que a função faz

    print("=" * 40) # Imprime uma linha decorativa
    print("     SISTEMA DE CÁLCULO DE IMC") # Imprime o título
    print("=" * 40) # Imprime outra linha decorativa

# Chamando a função
exibir_cabecalho() # Executa os prints definidos dentro da função

# ---- FUNÇÃO COM PARÂMETROS E RETORNO ----

def calcular_imc(peso, altura): # Recebe dois valores (parâmetros) para trabalhar
    """Calcula e retorna o IMC. Fórmula: peso / altura²"""

    imc = peso / (altura ** 2)   # Realiza o cálculo matemático e guarda na variável imc
    return imc                   # Envia o resultado de volta para quem chamou a função

# Coletando dados do usuário
peso = float(input("Peso (kg): ")) # Lê o peso e converte para número real
altura = float(input("Altura (m): ")) # Lê a altura e converte para número real

# Chamando a função e armazenando o retorno
resultado = calcular_imc(peso, altura) # Executa o cálculo e guarda o retorno em 'resultado'

print(f"Seu IMC é: {resultado:.2f}") # Exibe o resultado formatado com 2 casas decimais

# ---- ESCOPO LOCAL vs. GLOBAL ----

versao = "1.0"   # Variável GLOBAL: visível em todo o arquivo

def demonstrar_escopo(): # Define função para testar visibilidade de variáveis
    mensagem = "Olá do interior da função"   # Variável LOCAL: só existe dentro desta função
    print("Dentro da função:") # Informativo
    print(f"  mensagem = {mensagem}")   
    print(f"  versao = {versao}")       

demonstrar_escopo() # Executa a demonstração

print("\nFora da função:") # Informativo
print(f"  versao = {versao}")   # Funciona: variável global é acessível aqui
# print(mensagem)              # ERRO: Se descomentar, falha pois 'mensagem' morreu ao fim da função

# ---- VALOR PADRÃO E MÚLTIPLOS RETORNOS ----

def classificar_imc(imc, unidade="kg/m²"): # 'unidade' é opcional; se não enviar, assume "kg/m²"
    """Classifica o IMC e retorna classificação e emoji de status."""
    
    if imc < 18.5: # Teste para baixo peso
        classificacao = "Abaixo do peso"
        emoji = "🩺"
    elif imc < 25.0: # Teste para peso ideal
        classificacao = "Peso normal"
        emoji = "✅"
    elif imc < 30.0: # Teste para sobrepeso
        classificacao = "Sobrepeso"
        emoji = "⚠️"
    else: # Caso seja maior ou igual a 30
        classificacao = "Obesidade"
        emoji = "🔴"
    
    return classificacao, emoji   # Retorna dois valores ao mesmo tempo (como uma tupla)

# Chamada sem o parâmetro opcional
imc_teste = 22.5 # Define um valor para teste
classificacao, emoji = classificar_imc(imc_teste) # Desempacota os dois retornos em duas variáveis
print(f"IMC {imc_teste} ({classificacao}) {emoji}") # Exibe os dados coletados

# Chamada informando o parâmetro opcional
classificacao, emoji = classificar_imc(imc_teste, unidade="lb/in²") # Substitui o valor padrão
print(f"Mesma chamada com unidade customizada: {classificacao} {emoji}") # Exibe

# ---- RECURSÃO BÁSICA ----

def contagem_regressiva(n): # Função que chama a si mesma
    """Exibe contagem regressiva de n até 0 usando recursão."""
    if n < 0:            # CASO BASE: Condição de parada para evitar loop infinito
        return # Sai da função sem retornar nada
    
    print(n) # Imprime o número atual
    contagem_regressiva(n - 1)   # CHAMADA RECURSIVA: chama a função novamente com n menor

print("\n--- Contagem regressiva ---")
contagem_regressiva(5) # Inicia a contagem do 5

def fatorial(n): # Outro exemplo de recursão
    """Calcula n! recursivamente."""
    if n == 0 or n == 1:   # Caso base: fatorial de 0 ou 1 é sempre 1
        return 1
    
    return n * fatorial(n - 1)   # Multiplica n pelo fatorial do número anterior

print("\n--- Fatorial ---")
for i in range(1, 7): # Loop de 1 a 6
    print(f"  {i}! = {fatorial(i)}") # Calcula e exibe cada fatorial

# ---- FUNÇÃO PRINCIPAL ----

def processar_pessoa(): # Função que agrupa a lógica principal de entrada e saída
    """Coleta dados, calcula IMC e exibe resultado completo."""
    
    nome = input("\nNome: ") # Pede o nome
    peso = float(input("Peso (kg): ")) # Pede o peso
    altura = float(input("Altura (m): ")) # Pede a altura

    imc = calcular_imc(peso, altura)   # Chama a função de cálculo criada anteriormente
    classificacao, emoji = classificar_imc(imc) # Chama a função de classificação

    print("\n--- Resultado ---")
    print(f"Nome          : {nome}")
    print(f"IMC           : {imc:.2f} kg/m²")
    print(f"Classificação : {classificacao} {emoji}")

# ---- EXECUÇÃO PRINCIPAL ----

exibir_cabecalho() # Mostra o título do programa

continuar = "s" # Variável de controle do loop

while continuar == "s": # Enquanto o usuário quiser continuar
    processar_pessoa() # Executa a coleta e cálculo
    continuar = input("\nProcessar outra pessoa? (s/n): ").lower() # Pergunta se quer repetir

# (Nota: a função exibir_rodape() precisaria ser definida antes de ser chamada aqui)
