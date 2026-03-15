#
#NOME: Yuri Gonçalves
#DISCIPLINA: Programação de Sistemas
#DATA: 03/03/2026
#DESCRIÇÃO: Sistema de Gestão de Estoque

estoque = [
    {"nome": "Teclado", "quantidade": 5},
    {"nome": "Mouse", "quantidade": 15},
    {"nome": "Monitor", "quantidade": 2}
]

print("-" * 30)
print("CADASTRO DE NOVOS PRODUTOS")
print("-" * 30)

while True:
    novo_nome = input("Digite o nome do produto (ou 'sair' para finalizar cadastro): ").strip()
    if novo_nome.lower() == 'sair':
        break
    
    while True:
        try:
            nova_qtd = int(input(f"Digite a quantidade de '{novo_nome}': "))
            if nova_qtd < 0:
                print("Erro: A quantidade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Erro: Por favor, digite um número inteiro válido.")
    
    estoque.append({"nome": novo_nome, "quantidade": nova_qtd})

resumo = {"Crítico": 0, "Adequado": 0, "Excesso": 0}
produto_mais_critico = None

print("\n" + "="*40)
print("RELATÓRIO DE ESTOQUE")
print("="*40)

for p in estoque:
    nome = p["nome"]
    qtd = p["quantidade"]
    
    # Definição da situação
    if qtd < 5:
        situacao = "Crítico"
    elif qtd <= 20:
        situacao = "Adequado"
    else:
        situacao = "Excesso"
    
    resumo[situacao] += 1
    if produto_mais_critico is None or qtd < produto_mais_critico["quantidade"]:
        produto_mais_critico = p
        
    print(f"Produto: {nome:<15} | Qtd: {qtd:>3} | Situação: {situacao}")

print("-" * 40)
print(f"RESUMO: Crítico: {resumo['Crítico']} | Adequado: {resumo['Adequado']} | Excesso: {resumo['Excesso']}")
if produto_mais_critico:
    print(f"MAIS CRÍTICO: {produto_mais_critico['nome']} ({produto_mais_critico['quantidade']} unidades)")
print("-" * 40)

while True:
    busca = input("\nDeseja consultar um produto específico? (Digite o nome ou 'não' para sair): ").strip().lower()
    
    if busca == 'não' or busca == 'nao':
        print("Encerrado!")
        break
        
    encontrado = False
    for p in estoque:
        if p["nome"].lower() == busca:
            print(f"-> Resultado: {p['nome']} possui {p['quantidade']} unidades em estoque.")
            encontrado = True
            break
    
    if not encontrado:
        print(f"Aviso: O produto '{busca}' não foi encontrado na lista.")