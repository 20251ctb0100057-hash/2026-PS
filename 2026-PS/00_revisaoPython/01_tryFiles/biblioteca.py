from datetime import datetime

# ================= CONFIG =================
ARQUIVO = "biblioteca.txt"
ARQUIVO_HISTORICO = "historico.txt"
SEPARADOR = "|"

# ================= DADOS =================
catalogo = [
    {"título": "O Programador Pragmático", "autor": "Andrew Hunt", "disponível": True},
    {"título": "Código Limpo", "autor": "Robert C. Martin", "disponível": False},
    {"título": "Padrões de Projeto", "autor": "Erich Gamma", "disponível": True},
]

# ================= FUNÇÕES =================

def registrar_historico(acao, livro):
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
    linha = f"{data_hora} - {acao}: {livro['título']} ({livro['autor']})\n"

    with open(ARQUIVO_HISTORICO, "a", encoding="utf-8") as f:
        f.write(linha)


def listar_livros():
    print("\n" + "="*50)
    print(" 📚CATÁLOGO DA BIBLIOTECA")
    print("="*50)

    if not catalogo:
        print("Nenhum livro cadastrado.")
        return
    
    for i, livro in enumerate(catalogo, 1):
        status = "✅ Disponível" if livro["disponível"] else "❌ Indisponível"
        print(f"{i}. {livro['título']} - {livro['autor']} [{status}]")

    print("="*50)


def adicionar_livro():
    print("\n--- Adicionar Novo Livro ---")

    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()

    if not titulo or not autor:
        print("⚠️ Título e autor são obrigatórios!")
        return

    # Evitar duplicatas
    for livro in catalogo:
        if livro["título"].lower() == titulo.lower():
            print("⚠️ Este livro já está cadastrado!")
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
        resultados = [
            livro for livro in catalogo
            if termo in livro["título"].lower() or termo in livro["autor"].lower()
        ]

        if not resultados:
            print("⚠️ Nenhum livro encontrado.")
            return
        
        print(f"\n{len(resultados)} resultado(s):")
        for livro in resultados:
            status = "✅ Disponível" if livro["disponível"] else "❌ Emprestado"
            print(f"- {livro['título']} - {livro['autor']} [{status}]")

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
            registrar_historico("EMPRÉSTIMO", livro)
            print(f"✅ Empréstimo de '{livro['título']}' registrado.")

    except ValueError:
        print("❌ Entrada inválida. Digite apenas número.")


def devolver_livro():
    listar_livros()
    if not catalogo:
        return

    print("\n--- Registrar Devolução ---")

    try:
        numero = int(input("Número do livro: "))
        livro = catalogo[numero - 1]

        if livro["disponível"]:
            print(f"⚠️ '{livro['título']}' já está disponível.")
        else:
            livro["disponível"] = True
            registrar_historico("DEVOLUÇÃO", livro)
            print(f"✅ Devolução de '{livro['título']}' registrada.")

    except ValueError:
        print("❌ Digite apenas número.")
    except IndexError:
        print("❌ Número inválido.")


def ver_historico():
    print("\n--- HISTÓRICO ---")
    try:
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
            conteudo = f.read()
            print(conteudo if conteudo else "Nenhuma operação registrada.")
    except FileNotFoundError:
        print("Nenhum histórico encontrado.")


def relatorio_acervo():
    print("\n--- RELATÓRIO DO ACERVO ---")

    total = len(catalogo)
    disponiveis = sum(1 for l in catalogo if l["disponível"])
    emprestados = total - disponiveis

    print(f"Total: {total}")
    print(f"Disponíveis: {disponiveis}")
    print(f"Emprestados: {emprestados}")

    contagem = {}

    try:
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
            for linha in f:
                if "EMPRÉSTIMO" in linha:
                    titulo = linha.split(":")[1].split("(")[0].strip()
                    contagem[titulo] = contagem.get(titulo, 0) + 1

        if contagem:
            mais_emprestado = max(contagem, key=contagem.get)
            print(f"Mais emprestado: {mais_emprestado}")
        else:
            print("Nenhum empréstimo registrado.")

    except FileNotFoundError:
        print("Sem histórico disponível.")


# ================= ARQUIVO =================

def carregar_catalogo():
    catalogo = []
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            for linha in f:
                if not linha.strip():
                    continue
                partes = linha.strip().split(SEPARADOR)
                if len(partes) != 3:
                    continue
                titulo, autor, disponivel_str = partes
                catalogo.append({
                    "título": titulo,
                    "autor": autor,
                    "disponível": disponivel_str == "True"
                })
    except FileNotFoundError:
        pass
    return catalogo


def salvar_catalogo(catalogo):
    try:
        with open(ARQUIVO, 'w', encoding='utf-8') as f:
            for livro in catalogo:
                linha = f"{livro['título']}{SEPARADOR}{livro['autor']}{SEPARADOR}{livro['disponível']}\n"
                f.write(linha)
        print("💾 Catálogo salvo.")
    except Exception as e:
        print(f"❌ Erro ao salvar: {e}")


# ================= MENU =================

def menu():
    print("\n📚 SISTEMA DE BIBLIOTECA")

    opcoes = {
        "1": ("Listar livros", listar_livros),
        "2": ("Adicionar livro", adicionar_livro),
        "3": ("Buscar livro", busca_livro),
        "4": ("Registrar empréstimo", registrar_emprestimo),
        "5": ("Registrar devolução", devolver_livro),
        "6": ("Ver histórico", ver_historico),
        "7": ("Relatório do acervo", relatorio_acervo),
        "0": ("Sair", None),
    }

    while True:
        print("\nOpções:")
        for chave, (desc, _) in opcoes.items():
            print(f"{chave}. {desc}")

        try:
            escolha = input("Escolha: ").strip()
            if escolha not in opcoes:
                raise ValueError("Opção inválida.")

        except ValueError as e:
            print(f"⚠️ {e}")
            continue

        if escolha == "0":
            print("Até logo!")
            break

        _, funcao = opcoes[escolha]
        funcao()


# ================= EXECUÇÃO =================

if __name__ == "__main__":
    catalogo = carregar_catalogo()

    if not catalogo:
        catalogo = [
            {"título": "O Programador Pragmático", "autor": "Andrew Hunt", "disponível": True},
            {"título": "Código Limpo", "autor": "Robert C. Martin", "disponível": False},
            {"título": "Padrões de Projeto", "autor": "Erich Gamma", "disponível": True},
        ]

    menu()
    salvar_catalogo(catalogo)