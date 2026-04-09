'''
Projeto de mini Sistema: Geopolítica

Participantes: Mayara, Otávio e Yuri

Líder: Yuri

Nosso projeto: O projeto é um sistema de cadastro e consulta de países, onde o usuário pode: adicionar novos países, consultar a lista de países, atualizar o PIB de um país e remover um país. Os dados são salvos em um arquivo de texto para persistência. O sistema é simples e interativo, utilizando funções para organizar o código e facilitar a manutenção.

Data:26/03/2026
'''

#=============== YURI ==============

ARQUIVO = "paises.txt"  # nome do arquivo onde os dados dos países serão salvos
SEPARADOR = "|"  # Separa os dados no arquivo

def dados_iniciais():  # função que cria uma lista pronta de países
    return [  # retorna essa lista
        {"nome": "Brasil", "populacao": 203000000, "pib": 2.1},  # país com seus dados
        {"nome": "EUA", "populacao": 331000000, "pib": 25.0},  
        {"nome": "China", "populacao": 1400000000, "pib": 17.7},  
        {"nome": "Índia", "populacao": 1380000000, "pib": 3.2},  
        {"nome": "Japão", "populacao": 126000000, "pib": 5.0},  
        {"nome": "Alemanha", "populacao": 83000000, "pib": 4.0},  
        {"nome": "Reino Unido", "populacao": 67000000, "pib": 3.0},  
        {"nome": "França", "populacao": 67000000, "pib": 2.9},  
        {"nome": "Itália", "populacao": 60000000, "pib": 2.0}  
    ]

def carregar_dados():  # função para ler o arquivo
    paises = []  # cria uma lista vazia

    try:  # tenta executar o código abaixo
        with open(ARQUIVO, "r", encoding="utf-8") as f:  # abre o arquivo para leitura
            for linha in f:  # percorre cada linha do arquivo
                dados = linha.strip().split(SEPARADOR)  # separa os dados
                if len(dados) >= 3:  # verifica se tem os dados necessários
                    paises.append({
                        "nome": dados[0],  # nome do país
                        "populacao": int(dados[1]),  # transforma em número inteiro
                        "pib": float(dados[2])  # transforma em número decimal
                    })

    except:  # se der erro (ex: arquivo não existe)
        pass  # não faz nada (ignora o erro)

    return paises  # devolve a lista de países

def cadastrar(paises):
    print("\n" + "="*10 + " FUNDAÇÃO DE NOVA NAÇÃO " + "="*10)
    nome = input("Nome do país: ").strip()
    
    try:
        populacao = int(input("População Total (em milhões): "))
        pib = float(input("PIB (em trilhões): "))
        # Dados que alimentarão a função específica de HISTÓRIA
        ano_fundacao = int(input("Ano de Fundação: "))
        governante = input("Primeiro governante/líder: ").strip()
        fato_historico = input("Fato histórico marcante: ").strip()
        
    except ValueError:
        print("❌ Erro: Use apenas números para População, PIB e Ano.")
        return

    paises.append({
        "nome": nome,
        "populacao": populacao,
        "pib": pib,
        "ano_fundacao": ano_fundacao,
        "governante": governante,
        "fato_historico": fato_historico
    })
    print(f"\n✅ {nome} foi adicionado ao mapa mundi!")

def consultar(paises):
    """RELATÓRIO GERAL (Apenas dados numéricos e econômicos)"""
    print("\n" + "="*15 + " RELATÓRIO ECONÔMICO " + "="*15)
    if not paises:
        print("Nenhum dado cadastrado.")
        return

    for i, p in enumerate(paises, 1):
        status = "Potência" if p["pib"] > 1.5 else "Em desenvolvimento"
        print(f"{i}. {p['nome'].upper()} | Pop: {p['populacao']}M | PIB: ${p['pib']}T ({status})")

def exibir_historia(paises):
    """FUNÇÃO ESPECÍFICA DE HISTÓRIA (Onde os detalhes aparecem)"""
    print("\n" + "📜" + " ARQUIVOS HISTÓRICOS " + "📜")
    if not paises:
        print("A história ainda não foi escrita.")
        return

    nome_busca = input("Digite o nome da nação para ler sua história: ").strip().lower()
    
    achou = False
    ano_atual = 2026
    for p in paises:
        if p['nome'].lower() == nome_busca:
            idade = ano_atual - p['ano_fundacao']
            print(f"\n--- MEMÓRIAS DE {p['nome'].upper()} ---")
            print(f"Fundador: {p['governante']}")
            print(f"Ano de Fundação: {p['ano_fundacao']} ({idade} anos atrás)")
            print(f"📖 Fato Marcante: {p['fato_historico']}")
            print("=" * 30)
            achou = True
            break
    
    if not achou:
        print("Nação não encontrada nos registros históricos.")

def atualizar(paises):
    consultar(paises)
    if not paises: return
    try:
        i = int(input("\nNúmero do país para atualizar PIB: ")) - 1
        if 0 <= i < len(paises):
            paises[i]["pib"] = float(input(f"Novo PIB para {paises[i]['nome']}: "))
            print("✅ Economia atualizada!")
    except:
        print("❌ Erro na atualização.")

def dissolucao(paises):
    consultar(paises)
    if not paises: return
    try:
        i = int(input("\nNúmero do país para remover: ")) - 1
        if 0 <= i < len(paises):
            pais_removido = paises.pop(i)
            print(f"✅ {pais_removido['nome']} foi dissolvido do mapa mundi.")
        else:
            print("❌ Índice inválido.")
    except ValueError:
        print("❌ Entrada inválida. Digite apenas o número.")

def salvar_dados(paises):  # função para salvar no arquivo
    with open(ARQUIVO, "w", encoding="utf-8") as f:  # abre o arquivo para escrita
        for p in paises:  # percorre cada país da lista
            f.write(f"{p['nome']}|{p['populacao']}|{p['pib']}\n")  
            # escreve os dados separados por "|" e pula linha

# Mayara 
# ================= Otávio =================

def menu():
    paises = carregar_dados()   # puxa os dados salvos

    while True:  # mantem ele rodando sem fechar
        print("\n🌍 SISTEMA DE GEOPOLÍTICA")
        print("1. Cadastrar país")
        print("2. Consultar países")
        print("3. Atualizar PIB")
        print("4. Remover país")
        print("0. Sair")

        opcao = input("Escolha: ")   # escuta oq o usuário quer fazer

        if opcao == "1":
            cadastrar(paises)
        elif opcao == "2":
            consultar(paises)
        elif opcao == "3":
            atualizar(paises)
        elif opcao == "4":
            dissolucao(paises)

        # salva as alterações antes de encerrar
        elif opcao == "0":
            salvar_dados(paises)
            print("💾 Tudo certo, seus dados foram salvos. Até logo!")
            break  
        else:
            print("⚠️ Essa opção não existe.")


# ================= EXECUÇÃO =================
if __name__ == "__main__":
    menu()
# =========== Otávio ========