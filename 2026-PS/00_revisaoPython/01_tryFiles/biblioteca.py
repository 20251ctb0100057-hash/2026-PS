from datetime import datetime  # importa a função pra pegar data e hora atual

# ================= CONFIG =================
ARQUIVO = "biblioteca.txt"  # nome do arquivo onde salva os livros
ARQUIVO_HISTORICO = "historico.txt"  # arquivo onde salva o histórico de ações
SEPARADOR = "|"  # símbolo usado pra separar os dados no arquivo

# ================= DADOS =================
catalogo = [  # lista inicial de livros (tipo um "banco de dados" simples)
    {"título": "O Programador Pragmático", "autor": "Andrew Hunt", "disponível": True},  # livro disponível
    {"título": "Código Limpo", "autor": "Robert C. Martin", "disponível": False},  # livro emprestado
    {"título": "Padrões de Projeto", "autor": "Erich Gamma", "disponível": True},  # livro disponível
]

# ================= FUNÇÕES =================

def registrar_historico(acao, livro):  # função pra salvar o que aconteceu (empréstimo/devolução)
    data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")  # pega data/hora atual formatada bonitinha
    linha = f"{data_hora} - {acao}: {livro['título']} ({livro['autor']})\n"  # monta a linha do histórico

    with open(ARQUIVO_HISTORICO, "a", encoding="utf-8") as f:  # abre o arquivo no modo adicionar
        f.write(linha)  # escreve a linha no arquivo


def listar_livros():  # função que mostra todos os livros
    print("\n" + "="*50)  # linha decorativa
    print(" 📚CATÁLOGO DA BIBLIOTECA")  # título
    print("="*50)  # linha decorativa

    if not catalogo:  # se não tiver nenhum livro
        print("Nenhum livro cadastrado.")  # avisa
        return  # sai da função
    
    for i, livro in enumerate(catalogo, 1):  # percorre lista com índice começando em 1
        status = "✅ Disponível" if livro["disponível"] else "❌ Indisponível"  # define status
        print(f"{i}. {livro['título']} - {livro['autor']} [{status}]")  # mostra livro

    print("="*50)  # linha final


def adicionar_livro():  # função pra adicionar livro novo
    print("\n--- Adicionar Novo Livro ---")  # título

    titulo = input("Título: ").strip()  # pega título e tira espaços extras
    autor = input("Autor: ").strip()  # pega autor

    if not titulo or not autor:  # se algum campo estiver vazio
        print("⚠️ Título e autor são obrigatórios!")  # avisa
        return  # sai

    # Evitar duplicatas
    for livro in catalogo:  # percorre livros existentes
        if livro["título"].lower() == titulo.lower():  # compara ignorando maiúsc/minúsc
            print("⚠️ Este livro já está cadastrado!")  # já existe
            return  # sai

    catalogo.append({  # adiciona novo livro na lista
        "título": titulo,
        "autor": autor,
        "disponível": True  # começa como disponível
    })

    print(f"✅ '{titulo}' adicionado com sucesso!")  # confirma


def busca_livro():  # função de busca
    print("\n--- Buscar Livro ---")  # título
    termo = input("Digite título ou autor: ").strip().lower()  # termo de busca

    try:
        resultados = [  # lista de resultados
            livro for livro in catalogo
            if termo in livro["título"].lower() or termo in livro["autor"].lower()  # verifica se bate
        ]

        if not resultados:  # se não achou nada
            print("⚠️ Nenhum livro encontrado.")
            return
        
        print(f"\n{len(resultados)} resultado(s):")  # mostra quantidade
        for livro in resultados:  # percorre resultados
            status = "✅ Disponível" if livro["disponível"] else "❌ Emprestado"
            print(f"- {livro['título']} - {livro['autor']} [{status}]")

    except Exception as e:  # se der erro inesperado
        print(f"⚠️ Erro inesperado: {e}")


def registrar_emprestimo():  # função pra emprestar livro
    listar_livros()  # mostra lista
    if not catalogo:  # se não tiver livros
        return

    print("\n--- Registrar Empréstimo ---")  # título

    try:
        numero = int(input("Número do livro: "))  # usuário escolhe número

        if numero < 1 or numero > len(catalogo):  # valida intervalo
            print("⚠️ Número fora do intervalo.")
            return
        
        livro = catalogo[numero - 1]  # pega livro (ajustando índice)

        if not livro["disponível"]:  # se já estiver emprestado
            print(f"⚠️ '{livro['título']}' já está emprestado.")
        else:
            livro["disponível"] = False  # marca como emprestado
            registrar_historico("EMPRÉSTIMO", livro)  # salva no histórico
            print(f"✅ Empréstimo de '{livro['título']}' registrado.")

    except ValueError:  # se não digitar número
        print("❌ Entrada inválida. Digite apenas número.")


def devolver_livro():  # função pra devolver livro
    listar_livros()  # mostra lista
    if not catalogo:
        return

    print("\n--- Registrar Devolução ---")  # título

    try:
        numero = int(input("Número do livro: "))  # pega número
        livro = catalogo[numero - 1]  # pega livro

        if livro["disponível"]:  # se já estiver disponível
            print(f"⚠️ '{livro['título']}' já está disponível.")
        else:
            livro["disponível"] = True  # marca como devolvido
            registrar_historico("DEVOLUÇÃO", livro)  # salva no histórico
            print(f"✅ Devolução de '{livro['título']}' registrada.")

    except ValueError:
        print("❌ Digite apenas número.")  # erro de digitação
    except IndexError:
        print("❌ Número inválido.")  # número fora da lista


def ver_historico():  # mostra histórico
    print("\n--- HISTÓRICO ---")
    try:
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:  # abre arquivo
            conteudo = f.read()  # lê tudo
            print(conteudo if conteudo else "Nenhuma operação registrada.")  # mostra ou avisa vazio
    except FileNotFoundError:
        print("Nenhum histórico encontrado.")  # se não existir arquivo


def relatorio_acervo():  # mostra estatísticas
    print("\n--- RELATÓRIO DO ACERVO ---")

    total = len(catalogo)  # total de livros
    disponiveis = sum(1 for l in catalogo if l["disponível"])  # conta disponíveis
    emprestados = total - disponiveis  # calcula emprestados

    print(f"Total: {total}")
    print(f"Disponíveis: {disponiveis}")
    print(f"Emprestados: {emprestados}")

    contagem = {}  # dicionário pra contar empréstimos

    try:
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
            for linha in f:  # percorre histórico
                if "EMPRÉSTIMO" in linha:  # só pega empréstimos
                    titulo = linha.split(":")[1].split("(")[0].strip()  # extrai título
                    contagem[titulo] = contagem.get(titulo, 0) + 1  # soma contador

        if contagem:
            mais_emprestado = max(contagem, key=contagem.get)  # pega o mais emprestado
            print(f"Mais emprestado: {mais_emprestado}")
        else:
            print("Nenhum empréstimo registrado.")

    except FileNotFoundError:
        print("Sem histórico disponível.")


# ================= ARQUIVO =================

def carregar_catalogo():  # carrega os livros do arquivo
    catalogo = []  # começa com lista vazia
    try:
        with open(ARQUIVO, 'r', encoding='utf-8') as f:
            for linha in f:  # lê linha por linha
                if not linha.strip():  # pula linhas vazias
                    continue
                partes = linha.strip().split(SEPARADOR)  # separa os dados
                if len(partes) != 3:  # se estiver errado
                    continue
                titulo, autor, disponivel_str = partes  # separa valores
                catalogo.append({
                    "título": titulo,
                    "autor": autor,
                    "disponível": disponivel_str == "True"  # converte string pra booleano
                })
    except FileNotFoundError:
        pass  # se não existir arquivo, ignora
    return catalogo  # retorna lista


def salvar_catalogo(catalogo):  # salva os livros no arquivo
    try:
        with open(ARQUIVO, 'w', encoding='utf-8') as f:  # abre pra sobrescrever
            for livro in catalogo:
                linha = f"{livro['título']}{SEPARADOR}{livro['autor']}{SEPARADOR}{livro['disponível']}\n"
                f.write(linha)  # escreve cada livro
        print("💾 Catálogo salvo.")  # confirma
    except Exception as e:
        print(f"❌ Erro ao salvar: {e}")  # erro


# ================= MENU =================

def menu():  # menu principal
    print("\n📚 SISTEMA DE BIBLIOTECA")

    opcoes = {  # dicionário com opções
        "1": ("Listar livros", listar_livros),
        "2": ("Adicionar livro", adicionar_livro),
        "3": ("Buscar livro", busca_livro),
        "4": ("Registrar empréstimo", registrar_emprestimo),
        "5": ("Registrar devolução", devolver_livro),
        "6": ("Ver histórico", ver_historico),
        "7": ("Relatório do acervo", relatorio_acervo),
        "0": ("Sair", None),
    }

    while True:  # loop infinito até sair
        print("\nOpções:")
        for chave, (desc, _) in opcoes.items():
            print(f"{chave}. {desc}")  # mostra opções

        try:
            escolha = input("Escolha: ").strip()  # pega escolha
            if escolha not in opcoes:  # valida
                raise ValueError("Opção inválida.")

        except ValueError as e:
            print(f"⚠️ {e}")
            continue

        if escolha == "0":  # se quiser sair
            print("Até logo!")
            break

        _, funcao = opcoes[escolha]  # pega função
        funcao()  # executa função


# ================= EXECUÇÃO =================

if __name__ == "__main__":  # só roda se for o arquivo principal
    catalogo = carregar_catalogo()  # tenta carregar do arquivo

    if not catalogo:  # se não tiver nada salvo
        catalogo = [  # recria lista padrão
            {"título": "O Programador Pragmático", "autor": "Andrew Hunt", "disponível": True},
            {"título": "Código Limpo", "autor": "Robert C. Martin", "disponível": False},
            {"título": "Padrões de Projeto", "autor": "Erich Gamma", "disponível": True},
        ]

    menu()  # abre o menu
    salvar_catalogo(catalogo)  # salva antes de fechar