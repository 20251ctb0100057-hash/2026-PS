# =========================================================
# SISTEMA DE BIBLIOTECA
# =========================================================

# Disciplina : Programação de Sistemas (PS)
# Aula       : 05 - Revisão: Estruturas de Dados
# Autor      : Yuri Gonçalves Leuch
# Data       : 12/03/2026
# Repositório: https://github.com/20251ctb0100057-hash/2026-PS

# =========================================================

# DESCRIÇÃO:
# Catálogo de livros que demonstra o uso de listas
# e dicionários para armazenar, consultar e filtrar
# dados estruturados.

# =========================================================

# --- LISTAS: CONCEITO BÁSICO ---

# Criandp uma lista de títulos

titulos = [
    "O Programador Pragmático",
    "Código Limpo",
    "Entendendo Algoritmos",
]

# Acesso por índice (começa em 0, não em 1!)
print("Primeiro livro:", titulos[0])  # O Programador Pragmático
print("Último livro:", titulos[-1])  # Índice -1 - último elemento
print("Total de livros:", len(titulos))  

# --- MÉTODOS DE LISTA ---

print("\n--- Operações na lista ---")

# Adicionar um item ao final
titulos.append("Python Fluente")
print("Após append:", titulos)

# Verificar se um item existe

busca = "Código Limpo"
if busca in titulos:
    print(f"'{busca}' está no catálogo.")
else:
    print(f"'{busca}' não encontrado.")

# Ordenar a lista
titulos.sort()
print("Lista ordenada:", titulos)

# Remover um item

titulos.remove("Entendendo Algoritmos")
print("Após remove:", titulos)

# --- DICIONÁRIOS: CONCEITO BÁSICO ---

# Um dicionario representa um livro com seus atributos
livro = {
    "titulo": "O Programador Pragmático",
    "autor": "Andrew Hunt",
    "ano": 1999,
    "disponivel": True,
}

# Acessando valores pelas chaves
print("Título:", livro["titulo"])
print("Autor:", livro["autor"])
print("Ano:", livro["ano"])
print("Status:", "Disponível" if livro["disponivel"] else "Emprestado")

# ---- MODIFICANDDO E CONSULTANDO ---

# Atualizando um valor existente
livro["disponivel"] = False
print("\nApós empréstimo:", livro["disponivel"])

# Adicionando uma nova chave
livro["paginas"] = 352
print("Páginas:", livro["paginas"])

# ---- MODIFICANDO E CONSULTANDO -----

# Atualizando um valor existente

livro ["disponivel"] = False

print ("\nApos empréstimo:", livro["disponivel"] )

# livro foi emprestado

# + Adicionando uma nova chave

livro ["paginas"] = 352
print ("Paginas:", livro ["paginas"] )

# .get () - acesso seguro: retorna None (ou padrao) se a chave nao existir
editora = livro.get ("editora", "Nao informada")

print ("Editora:", editora) # nao lanca KeyError, retorna o padrao

# CATALOGO: LISTA DE DICIONARIOS

catalogo = [
    {"titulo": "O Programador Pragmatico", "autor": "Andrew Hunt", "ano": 1999,
     "disponivel": True},
    {"titulo": "Codigo Limpo", "autor": "Robert C. Martin", "ano": 2008,
     "disponivel": False},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "ano": 2016,
     "disponivel": True},
]

print(" === Catálogo da Biblioteca === ")

print()

# Percorrendo cada livro com for

for livro in catalogo:
    status = "✅ Disponível" if livro["disponivel"] else "❌ Emprestado"
    print(f'Livro: {livro["titulo"]} ({livro["ano"]})')
    print(f'Autor: {livro["autor"]} | {status}')
    print(" " + "-" * 40)

#CONSULTAS E FILTROS

print("\n --- Livros disponíveis --- ")

for livro in catalogo:
    if livro["disponivel"]:
        print(livro["titulo"])

# filtra apenas os disponíveis

print("\n === Busca por título === ")
busca = input("Digite o título (ou parte): ").lower()
encontrado = False

for livro in catalogo:
    if busca in livro["titulo"].lower():
        print(f'Encontrado: {livro["titulo"]} - {livro["autor"]}')
        encontrado = True

if not encontrado:
    print("Nenhum livro encontrado com esse termo.")

# .lower() ignora maiúsculas/minúsculas

print("\n --- Atributos do primeiro livro --- ")

for chave, valor in catalogo[0].items():
    print(f"{chave}: {valor}")

# .items() retorna pares (chave, valor)
disponiveis = 0
emprestados = 0

for livro in catalogo:
    if livro["disponivel"]:
        disponiveis += 1
    else:
        emprestados += 1

print(f"Disponíveis: {disponiveis} | Emprestados: {emprestados}")