catalogo = [
    {"título": "O Programador Pragmático", "autor": "Andrew Hunt", "disponível": True},
    {"título": "Código Limpo", "autor": "Robert C. Martin", "disponível": False},
    {"título": "Padrões de Projeto", "autor": "Erich Gamma", "disponível": True},
]

def listar_livros():
    """Exibe todos os livros com numeração e status"""
    print("\n" + "="*50)
    print(" 📚CATÁLOGO DA BIBLIOTECA")
    print("="*50)

    if not catalogo:
        print("Nenhum livro cadastrado.")
        return
    
    for i, livro in enumerate(catalogo, 1):
        status = "✅ Disponível" if livro["disponível"] else "❌ Indisponível"
        print(f"  {i}. {livro['título']} - {livro['autor']} [{status}]")

    print("="*50)

def adicionar_livro():
    """Coleta dados via input e adiciona um novo livro ao catálogo"""
    print("\n--- Adicionar Novo Livro ---")

    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()

    if not titulo or not autor:
        print("⚠️ Título e autor são obrigatórios!")
        return
    
    catalogo.append({
        "título": titulo,
        "autor": autor,
        "disponível": True
    })
    print(f"✅ '{titulo}' adicionado com sucesso!")


def busca_livro():
    print("\n--- Buscar Livro ---")
    termo = input("Digite título ou autor: ").strip().lower()

    try:
        resultados = [livro for livro in catalogo if termo in livro["título"].lower() or termo in livro["autor"].lower()]

        if not resultados:
            print("  ⚠️ Nenhum livro encontrado.")
            return
        
        print(f"\n {len(resultados)} resultado(s):")
        for livro in resultados:
            status = "✅ Disponível" if livro["disponível"] else "❌ Emprestado"
            print(f"  - {livro['título']} - {livro['autor']} [{status}]")


    except Exception as e:
        print(f"⚠️ Erro inesperado: {e}")


def registrar_emprestimo():
    listar_livros()
    if not catalogo:
        return
    print("\n--- Registrar Empréstimo ---")

    try:
        numero = int(input("Número do livro: ")) 

        if numero < 1 or numero > len(catalogo):
            print("⚠️ Número fora do intervalo.")
            return
        
        livro = catalogo[numero - 1]

        if not livro["disponível"]:
            print(f"⚠️ '{livro['título']}' já está emprestado.")
        else:
            livro["disponível"] = False
            print(f"✅ Empréstimo de '{livro['título']}' registrado.")

    except ValueError:
        print("❌ Entrada inválida. Digite apenas o número.")

def devolver_livro():
    listar_livros()
    if not catalogo:
        return
    print("\n--- Registrar Devolução ---")

    try:
        numero = int(input("Número do livro a devolver: "))
        livro = catalogo[numero - 1]

        if livro["disponível"]:
            print(f"⚠️ '{livro['título']}' já está disponível.")
        else:
            livro["disponível"] = True
            print(f"✅ Devolução de '{livro['título']}' registrada.")

    except ValueError:
        print("❌ Digite apenas o número do livro.")
    except IndexError:
        print("❌ número fora da lista. Verufique os livros cadastrados.") # Permite tratar cada erro de forma adequada e evita que falhas inesperadas no código sejam escondidas por um tratamento genérico.


def menu():
    print("\n📚SISTEMA DE BIBLIOTECA - v1 (em memória)")

    opcoes = {
        "1": ("Listar livros", listar_livros),
        "2": ("Adicionar livro", adicionar_livro),
        "3": ("Buscar livro", busca_livro),
        "4": ("Registrar empréstimo", registrar_emprestimo),
        "5": ("Registrar devolução", devolver_livro),
        "0": ("Sair", None),
    }

    while True:
        print("\n Opções:")
        for chave, (descrição, _) in opcoes.items():
            print(f"  {chave}. {descrição}")

        
        try:
            escolha = input("\n Sua escolha: ").strip()
            if escolha not in opcoes:
                raise ValueError(f"Opção '{escolha}' inválida.")

        except ValueError as e:
            print(f"⚠️ {e}")
            continue

        else:
            # Executado SOMENTE quando try termina sem exceção
            if escolha == "0":
                print("\n Até logo! 📚")
                break
            _, funcao = opcoes[escolha]
            funcao()

        finally:
            # Executado SEMPRE - com ou sem exceção
            # Aqui didático. Em produção: fecha arquivos, conexões, etc.
            pass

if __name__ == "__main__":
    menu()