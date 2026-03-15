# =============================================================================
# DISCIPLINA: Algoritmos e Programação de Computadores
# DATA: 03/03/2026
# DESCRIÇÃO: Sistema de Gerenciamento de Biblioteca
# =============================================================================

# --- CATÁLOGO INICIAL 
catalogo = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "ano": 1899, "disponivel": True},
    {"titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "ano": 1937, "disponivel": False},
    {"titulo": "1984", "autor": "George Orwell", "ano": 1949, "disponivel": True}
]

def exibir_catalogo(lista):
    """Exibe todos os livros com título, autor e status formatado"""
    print("\n--- CATÁLOGO ATUAL ---")
    for livro in lista:
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f"Título: {livro['titulo']} | Autor: {livro['autor']} | Status: {status}")

def cadastrar_livro():
    """Permite cadastrar um novo livro via input e adiciona ao catálogo"""
    print("\n--- CADASTRO DE NOVO LIVRO ---")
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano de Publicação: "))
    
    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "disponivel": True
    }
    catalogo.append(novo_livro)
    print("Livro cadastrado com sucesso!")

def buscar_por_autor():
    """Busca livros por nome ou parte do nome do autor (Case-insensitive)"""
    print("\n--- BUSCA POR AUTOR ---")
    termo = input("Digite o nome do autor: ").lower()
    encontrados = [l for l in catalogo if termo in l["autor"].lower()]
    
    if encontrados:
        exibir_catalogo(encontrados)
    else:
        print(f"Nenhum livro encontrado para o autor '{termo}'.")

def alternar_status():
    """Registra empréstimo ou devolução invertendo o booleano 'disponivel'"""
    print("\n--- REGISTRO DE EMPRÉSTIMO/DEVOLUÇÃO ---")
    titulo_busca = input("Digite o título exato do livro: ").lower()
    
    encontrado = False
    for livro in catalogo:
        if livro["titulo"].lower() == titulo_busca:
            livro["disponivel"] = not livro["disponivel"]
            status_novo = "Disponível" if livro["disponivel"] else "Emprestado"
            print(f"Status de '{livro['titulo']}' alterado para: {status_novo}")
            encontrado = True
            break
    
    if not encontrado:
        print("Erro: Livro não localizado no acervo.")

def exibir_relatorio_final():
    """Exibe contagem de livros e lista de títulos emprestados"""
    total = len(catalogo)
    disponiveis = sum(1 for l in catalogo if l["disponivel"])
    emprestados = total - disponiveis
    titulos_emprestados = [l["titulo"] for l in catalogo if not l["disponivel"]]
    
    print("\n" + "="*30)
    print("RELATÓRIO FINAL DA BIBLIOTECA")
    print(f"Total de livros: {total}")
    print(f"Disponíveis: {disponiveis}")
    print(f"Emprestados: {emprestados}")
    if titulos_emprestados:
        print(f"Lista de Emprestados: {', '.join(titulos_emprestados)}")
    print("="*30)

# --- FLUXO PRINCIPAL DO PROGRAMA ---
def menu():
    while True:
        print("\nSISTEMA DE BIBLIOTECA 2026")
        print("1. Exibir Catálogo")
        print("2. Cadastrar Livro")
        print("3. Buscar por Autor")
        print("4. Empréstimo/Devolução")
        print("5. Sair e Gerar Relatório")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            exibir_catalogo(catalogo)
        elif opcao == "2":
            cadastrar_livro()
            exibir_catalogo(catalogo)
        elif opcao == "3":
            buscar_por_autor()
        elif opcao == "4":
            alternar_status()
        elif opcao == "5":
            exibir_relatorio_final()
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
