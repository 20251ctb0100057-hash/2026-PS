# =========================================================

# SISTEMA DE APROVAÇÃO DE ALUNOS

# =========================================================

# Disciplina : Programação de Sistemas (PS)
# Aula       : 04 - Revisão: Variáveis e Tipos e Controle de Fluxo
# Autor      : Yuri Gonçalves Leuch
# Data       : 05/03/2026
# Repositório: https://github.com/20251ctb0100057-hash/2026-PS

# =========================================================

#

# ------ ENTRADA DE DADOS ---------

print (" === Sistema de Aprovação de Alunos === ")
print () # linha em branco para organizar a saida

nome = input ("Digite o nome do aluno: ") # str - texto

notal = float (input ("Digite a nota 1 (0 a 10) : ") ) # float - decimal

nota2 = float (input ("Digite a nota 2 (0 a 10) : ") ) # float - decimal

# ---PROCESSAMENTO ----

media = (notal + nota2) / 2 # operador aritmético: soma e divisão

print ()

print (f"Aluno : {nome} ")
print (f"Nota 1 : {notal:.1f}")
print (f"Nota 2 : {nota2:.1f}")
print (f"Média : {media:.2f}") # :.2f = exibe com 2 casas decimais

# DECISAO

if media >= 6.0:
	situacao = "Aprovado"
elif media >= 4.0:
	situacao = "Recuperação"
else:
	situacao = "Reprovado"

print (f"Situação: {situacao}")
print ("-" * 40) # linha separadora: repete o caractere "-" 40 vezes

# --- DECISÃO ---

if media >= 6.0:
	situacao = "Aprovado"
elif media >= 4.0:
	situacao = "Recuperação"
else:
    situacao = "Reprovado"

if notal < 2.0 or nota2 < 2.0:
    print("⚠️ Atenção: nota muito baixa em uma das avaliações.")

print (f"Situação: {situacao}")
print ("-" * 40) # linha separadora: repete o caractere "-" 40 vezes

# ---- DADOS DA TURMA ---
# Uma lista de dicionários, onde cada dicionário representa um aluno

turma = [
    {"nome": "Ana", "nota1": 8.0, "nota2": 7.5},
    {"nome": "Bruno", "nota1": 4.5, "nota2": 5.0},
    {"nome": "Carla", "nota1": 2.0, "nota2": 3.5},
]

print("=== Resultado da Turma ===")
print()

# O 'for' percorre cada aluno da lista automaticamente

for aluno in turma:
    nome = aluno["nome"]
    nota1 = aluno["nota1"]
    nota2 = aluno["nota2"]
    media = (nota1 + nota2) / 2

    if media >= 6.0:
        situacao = "Aprovado"
    elif media >= 4.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    print(f"Aluno: {nome} - Média: {media:.2f} - Situação: {situacao}")

# --- MENU SIMPLES COM WHILE ---
while True:
    print("\n=== Menu ===")
    print("1. Exibir alunos da turma")
    print("2. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        for aluno in turma:
            nome = aluno["nome"]
            nota1 = aluno["nota1"]
            nota2 = aluno["nota2"]
            media = (nota1 + nota2) / 2
            if media >= 6.0:
                situacao = "Aprovado"
            elif media >= 4.0:
                situacao = "Recuperação"
            else:
                situacao = "Reprovado"
            print(f"Aluno: {nome} - Média: {media:.2f} - Situação: {situacao}")
    elif opcao == "2":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
