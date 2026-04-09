# ==================================
# SISTEMA DE BOTÂNICA
# ==================================
# Disciplina: Programação de Sistemas (PS)
# Aula: 16 e 17
# Autor: Mayara, Yuri e Otávio.
# Data: 2026.04.09
# Repositório: https://github.com/20251ctb0100057-hash/2026-PS.git
# ==================================
#
# DESCRIÇÃO:
# Sistema feito para uma botânica para cadastarr plantas, obter informações, etc....
#
# ===================================


import os # Importa biblioteca para verificar existência de arquivos
from datetime import datetime # Importa módulo para trabalhar com datas e horários

# Variáveis globais de arquivos
dados = "dados.txt"  # Nome do arquivo que armazena as plantas
hist = "historico.txt" # Nome do arquivo que armazena os logs de ações

# FUNÇÃO 1: Lê o arquivo de texto e carrega as plantas para a lista em memória
def carregar_acervo():
    '''
    PARAMETROS: Nenhum.
    TIPOS DE DADOS: Lista (acervo) e Dicionário (plantas).
    '''
    acervo = [] # Cria uma lista vazia para receber os dados
    try: # Inicia bloco de tratamento de erro para evitar queda do programa
        '''
        ESTRUTURA DE DECISÃO: if not os.path.exists (Verifica existência do arquivo).
        '''
        if not os.path.exists(dados): # Verifica se o arquivo físico existe
            open(dados, "w", encoding="utf-8").close() # Se não existe, cria um arquivo novo
            return acervo # Retorna a lista vazia
        
        with open(dados, "r", encoding="utf-8") as f: # Abre o arquivo para leitura
            '''
            ESTRUTURA DE REPETIÇÃO: for linha in f (Percorre o arquivo).
            '''
            for linha in f: # Percorre o arquivo linha por linha
                '''
                OPERADORES LÓGICOS: and (Verifica se a linha tem texto E o separador).
                '''
                if linha.strip() and ";" in linha: # Verifica se a linha não é vazia e tem o separador
                    # Divide a linha no caractere ';' e atribui às variáveis
                    n, r, c, e = linha.strip().split(";")
                    # Cria um dicionário com as chaves e valores da planta
                    plantas = {"nome": n, "raridade": r, "clima": c, "estacoes": e}
                    acervo.append(plantas) # Adiciona o dicionário na lista principal
    except Exception as erro: # Captura erro caso a leitura falhe
        '''
        TRY EXCEPT: Captura falhas de leitura ou permissão de arquivo.
        '''
        print(f"Erro ao carregar: {erro}") # Exibe a mensagem do erro ocorrido
    return acervo # Devolve a lista preenchida para o programa

# FUNÇÃO 2: Grava os dados da lista de volta no arquivo de texto
def salvar_no_acervo(lista_para_salvar):
    '''
    PARAMETROS: lista_para_salvar (A lista atualizada do acervo).
    '''
    try: # Inicia tratamento de erro para escrita
        with open(dados, "w", encoding="utf-8") as f: # Abre o arquivo no modo escrita (sobrescreve)
            for p in lista_para_salvar: # Percorre cada dicionário da lista
                # Formata a string com os dados separados por ';' e quebra de linha
                linha = f"{p['nome']};{p['raridade']};{p['clima']};{p['estacoes']}\n"
                f.write(linha) # Grava a linha formatada no arquivo
    except: # Caso ocorra erro de permissão ou sistema de arquivos
        print("Erro ao salvar dados.") # Exibe aviso de falha na gravação

# FUNÇÃO 3: Registra histórico de ações com data e hora atual
def salvar_no_hist(texto):
    '''
    PARAMETROS: texto (A mensagem que será gravada no log).
    '''
    # Gera data e hora atual formatada em dia/mês/ano hora:minuto:segundo
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    # Abre o arquivo no modo 'a' (append) para adicionar texto sem apagar o anterior
    with open(hist, "a", encoding="utf-8") as f:
        f.write(f"[{agora}] {texto}\n") # Grava a mensagem de log com o carimbo de tempo

# FUNÇÃO 4: Realiza o cadastro e verifica se o nome já existe
def cadastrar_nova(lista_atual):
    '''
    PARAMETROS: lista_atual (A lista que está na memória).
    OPERADORES RELACIONAIS: == (Comparação de nomes).
    '''
    print("\n========= 🌿CADASTRO BOTÂNICO🌿 =========")
    n = input("Nome da planta: ").strip() # Recebe o nome e remove espaços nas pontas
    
    for p in lista_atual: # Percorre a lista para verificar duplicidade
        if p['nome'].lower() == n.lower(): # Compara nomes ignorando maiúsculas e minúsculas
            print(f"ERRO: A planta '{n}' já etá cadastrada! Cadastro recusado.")
            return # Encerra a função sem realizar o cadastro

    # Recebe as demais informações da planta
    r = input("Raridade: ").strip()
    c = input("Clima ideal: ").strip()
    e = input("Estações: ").strip()
    
    '''
    ESTRUTURA DE DECISÃO: if not (Validação de campos obrigatórios).
    '''
    if not n or not r or not c or not e:
        print("ERRO: Todos os campos devem ser preenchidos!")
        return # Encerra a função se houver campo vazio

    # Organiza os novos dados em um dicionário
    plantas = {"nome": n, "raridade": r, "clima": c, "estacoes": e}
    lista_atual.append(plantas) # Adiciona a nova planta na lista em memória
    salvar_no_acervo(lista_atual) # Atualiza o arquivo de texto no disco
    print(f"🌱 {n} cadastrada com sucesso!")

# FUNÇÃO 5: Localiza planta pelo nome e exibe informações básicas
def buscar_especie(lista_atual):
    '''
    PARAMETROS: lista_atual.
    ESTRUTURA DE REPETIÇÃO: for p in lista_atual (Busca linear).
    '''
    if not lista_atual: # Verifica se a lista está vazia
        print("Acervo vazio. 🥀")
        return
    busca = input("\nBuscar por nome: ").strip().lower() # Recebe critério de busca
    for p in lista_atual: # Percorre a lista em busca do nome
        if p['nome'].lower() == busca: # Se encontrar correspondência
            print(f"\n========= BUSCA =========")
            print(f"Nome: {p['nome']} | Clima: {p['clima']}") # Exibe os dados
            salvar_no_hist(f"Busca: {p['nome']}") # Registra a busca no histórico
            return # Encerra a busca após encontrar
    print("Nenhum resultado para este critério.") # Aviso caso não encontre nada

# FUNÇÃO 6: Exibe todos os registros numerados e o total geral
def gerar_relatorio(lista_atual):
    '''
    ESTRUTURA DE REPETIÇÃO: for i, p in enumerate (Geração de índices).
    '''
    if not lista_atual: # Verifica se há dados para exibir
        print("\nO acervo está vazio.")
        return
    print("\n" + "="*40)
    print(f"{' 🪴 RELATÓRIO DO ACERVO BOTÂNICO':^40}") # Cabeçalho centralizado
    print("="*40)
    for i, p in enumerate(lista_atual):
        # Exibe o ID (índice), nome alinhado e clima
        print(f"ID: {i} | Planta: {p['nome']:<15} | Clima: {p['clima']}")
    print("-" * 40)
    print(f"Total de plantas cadastradas: {len(lista_atual)}") # Exibe quantidade de itens
    print("="*40)

# FUNÇÃO 7: Remove uma planta da lista baseada no índice numérico
def excluir_por_indice(lista_atual):
    '''
    PARAMETROS: lista_atual.
    OPERADORES RELACIONAIS: <= e < (Verificação de intervalo de índice).
    '''
    gerar_relatorio(lista_atual) # Exibe a lista numerada para escolha
    
    if not lista_atual: # Se a lista estiver vazia, encerra
        return

    try: # Inicia tratamento para garantir que a entrada seja um número
        idx = int(input("\nDigite o ID da planta que deseja remover: "))
        if 0 <= idx < len(lista_atual):
            removida = lista_atual.pop(idx) # Remove o item da lista pelo índice
            salvar_no_acervo(lista_atual) # Atualiza o arquivo no disco após a remoção
            salvar_no_hist(f"Exclusão: {removida['nome']}") # Registra a remoção no histórico
            print(f" Planta '{removida['nome']}' removida do sistema!")
        else: # Caso o número não corresponda a nenhum índice
            print(" Erro: ID inexistente.")
    except ValueError: # Caso o usuário digite algo que não seja um número inteiro
        '''
        TRY EXCEPT: Trata entrada de texto onde se espera número inteiro.
        '''
        print("Erro: Digite um número inteiro válido.")

# BLOCO PRINCIPAL: Controla o fluxo do menu e execução do sistema
def main():
    '''
    ESTRUTURA DE REPETIÇÃO: while True (Mantém o sistema ativo).
    TIPOS DE DADOS: Escolha (String do input).
    '''
    acervo = carregar_acervo() # Carrega os dados persistidos logo ao iniciar

    while True: # Loop infinito para manter o menu ativo
        print("\n========= 🌱 SISTEMA BOTÂNICO 🪻 =========")
        print("1 - Cadastrar")
        print("2 - Relatório ")
        print("3 - Buscar ")
        print("4 - Remover ")
        print("5 - Encerrar ")
        print("==========================================")

        try: # Tratamento de erro para entradas no menu
            escolha = input("Opção: ") # Recebe a opção do usuário
            '''
            ESTRUTURA DE DECISÃO: if / elif / else (Controle do Menu).
            '''
            if escolha == "1": # Direciona para cadastro
                cadastrar_nova(acervo)
            elif escolha == "2": # Direciona para relatório
                gerar_relatorio(acervo)
            elif escolha == "3": # Direciona para busca
                buscar_especie(acervo)
            elif escolha == "4": # Direciona para exclusão
                excluir_por_indice(acervo)
            elif escolha == "5": # Finaliza o programa
                print("🌿 Encerrando o sistema...")
                break # Sai do loop while
            else: # Caso digite uma opção fora de 1-5
                print("Opção inválida!")
        except Exception as e: # Captura falhas inesperadas no loop
            print(f"Erro: {e}") # Exibe o erro para diagnóstico

if __name__ == "__main__":
    main()