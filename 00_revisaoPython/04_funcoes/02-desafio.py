"""
-------------------------------------------------------------------------------
IFPR - INSTITUTO FEDERAL DO PARANÁ
Disciplina: Programação de Sistemas
Nome: Yuri Gonçalves Leuch
Data: 05/03/2026
Repositório: https://github.com/20251ctb0100057-hash/2026-PS
-------------------------------------------------------------------------------
"""

# --- DEFINIÇÕES DE FUNÇÕES ---

def solicitar_notas(nome_aluno): # Define função para coletar e validar notas
    notas = [] # Cria uma lista vazia para armazenar as notas
    for i in range(1, 3): # Loop para repetir o processo 2 vezes (nota 1 e nota 2)
        while True: # Loop infinito para validação (só para se a nota for correta)
            try: # Tenta executar o bloco abaixo
                nota = float(input(f"Digite a {i}ª nota de {nome_aluno}: ")) # Lê nota como número real
                if 0 <= nota <= 10: # Verifica se a nota está no intervalo permitido
                    notas.append(nota) # Adiciona a nota válida à lista
                    break # Sai do loop while e vai para a próxima nota
                print("⚠️ Erro: A nota deve estar entre 0 e 10.") # Mensagem se fora do intervalo
            except ValueError: # Caso o usuário digite texto em vez de número
                print("⚠️ Erro: Digite um valor numérico válido.") # Mensagem de erro de tipo
    return notas[0], notas[1] # Retorna as duas notas separadamente

def calcular_media(nota1, nota2): # Define função que recebe as duas notas
    return (nota1 + nota2) / 2 # Retorna o resultado da média aritmética

def verificar_situacao(media): # Define função para classificar o aluno
    if media >= 6.0: # Se a média for 6 ou mais
        return "Aprovado" # Retorna a string de aprovação
    elif 4.0 <= media < 6.0: # Se a média estiver entre 4 e 5.9
        return "Recuperação" # Retorna a string de recuperação
    else: # Se a média for menor que 4
        return "Reprovado" # Retorna a string de reprovação

def gerar_relatorio(nome, media, situacao): # Define função de exibição individual
    print(f"\n--- Resultado: {nome} ---") # Exibe o nome formatado
    print(f"Média: {media:.2f}") # Exibe a média com 2 casas decimais
    print(f"Situação: {situacao}") # Exibe o status (Aprovado, etc)
    print("-" * 30) # Linha divisória estética

def calcular_media_turma(medias, index=0): # Função recursiva para média da turma
    if not medias: # Caso a lista esteja vazia
        return 0 # Retorna zero
    if index == len(medias) - 1: # Caso base: se chegar ao último elemento da lista
        return medias[index] / len(medias) # Retorna a última parte da média
    # Soma a nota atual dividida pelo total com o próximo nível da recursão
    return (medias[index] / len(medias)) + calcular_media_turma(medias, index + 1)

def resumo_turma(lista_alunos): # Define função para contar estatísticas finais
    # Conta quantos alunos têm cada situação usando list comprehension e sum
    aprovados = sum(1 for a in lista_alunos if a['situacao'] == "Aprovado")
    recuperacao = sum(1 for a in lista_alunos if a['situacao'] == "Recuperação")
    reprovados = sum(1 for a in lista_alunos if a['situacao'] == "Reprovado")
    return aprovados, recuperacao, reprovados # Retorna os três contadores

# --- PROGRAMA PRINCIPAL ---

def main(): # Função que orquestra a execução do programa
    turma = [] # Lista que guardará os dicionários de cada aluno
    total_alunos = 3 # Define que processaremos 3 alunos (Nível Intermediário)
    
    print("=== SISTEMA DE GESTÃO PEDAGÓGICA IFPR ===\n")
    
    for _ in range(total_alunos): # Loop para processar cada aluno da lista
        nome = input("Nome do aluno: ") # Coleta o nome do aluno
        n1, n2 = solicitar_notas(nome) # Chama função para pegar notas validadas
        
        med = calcular_media(n1, n2) # Chama função para calcular a média
        sit = verificar_situacao(med) # Chama função para definir a situação
        
        # Guarda os dados em um dicionário e adiciona na lista da turma
        turma.append({'nome': nome, 'media': med, 'situacao': sit})
        
        gerar_relatorio(nome, med, sit) # Exibe os dados do aluno atual

    # Extrai apenas as médias para uma nova lista para o cálculo recursivo
    todas_medias = [aluno['media'] for aluno in turma]
    media_geral = calcular_media_turma(todas_medias) # Calcula média da turma via recursão
    aprov, rec, repr_ = resumo_turma(turma) # Obtém os totais de cada situação

    # Bloco final de exibição do resumo (Nível Avançado)
    print("\n" + "="*40)
    print("        RESUMO FINAL DA TURMA")
    print("="*40)
    print(f"Média Geral da Turma: {media_geral:.2f}") # Exibe média da turma
    print(f"Total de Aprovados:    {aprov}") # Exibe contagem de aprovados
    print(f"Total em Recuperação:  {rec}") # Exibe contagem de recuperação
    print(f"Total de Reprovados:   {repr_}") # Exibe contagem de reprovados
    print("="*40)

if __name__ == "__main__": # Verifica se o script está sendo executado diretamente
    main() # Inicia a execução do programa principal
