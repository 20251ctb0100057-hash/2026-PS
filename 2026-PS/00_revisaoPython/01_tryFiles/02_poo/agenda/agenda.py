import pickle

class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir(self):
            print(f"Nome: {self.nome}")
            print(f"Telefone: {self.telefone}")
            print(f"Email: {self.email}")
    
    def para_linha_txt(self):
            # Cada contato vira UMA linha, campos separados por ;
            return f"{self.nome};{self.telefone};{self.email}"


##
# FUNÇÕES DE PERSISTENCIA EM TEXTO (.TXT)
##

def salvar_em_txt(contatos, caminho):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        for c in contatos:
            arquivo.write(c.para_linha_txt() + '\n')
    print(f"👌 {len(contatos)} contato(s) salvo(s) em {caminho}")

def carregar_de_txt(caminho):
    contatos = []
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                linha = linha.strip()  # Remove espaços em branco e quebras de linha
                if not linha:
                    continue
                partes = linha.split(';')
                nome, telefone, email = partes[0], partes[1], partes[2]
                contatos.append(Contato(nome, telefone, email))
    except FileNotFoundError:
        print(f"❌ Arquivo {caminho} não encontrado. Retornando lista vazia.")
    return contatos

#=============
#PERSISTENCIA EM BINÁRIO (.BIN) COM PICKLE
#=============
# pickle "congela" o objeto inteiro: classe, atributos e tipos 
# preservados. Vantagem> zero parsing manual. Desvantagem: só Python lê e existe risco de segurança (malwares) ao abrir .bin de fontes desconhecidas.

def salvar_em_binario(contatos, caminho):
    with open(caminho, 'wb') as arquivo:
        pickle.dump(contatos, arquivo)
    print(f"👌 {len(contatos)} contato(s) salvo(s) em {caminho}")

def carregar_de_binario(caminho):
    try:
        with open(caminho, 'rb') as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        print(f"❌ Arquivo {caminho} não encontrado. Retornando lista vazia.")
        return []

#=============
# CRUD EM MEMÓRIA
#=============
# Operações que manipulam a lista de contatos enquanto o programa está rodando. Recebem a lista por parametro: assim, qualquer função pode trabalhar com ela sem usar variáveis globais.

def cadastrar(contatos):
    print("\n--- Novo contato ---")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contato = Contato(nome, telefone, email)
    contatos.append(contato)
    print(f"✅ Contato cadastrado: {contato.nome}")

def listar(contatos):
    if not contatos:
        print("\n(agenda vazia)")
        return
    print(f"\n--- Agenda: {len(contatos)} contato(s) ---")

    for i, c in enumerate(contatos, start=1):
        print(f"\nContato {i}:")
        c.exibir()

def remover(contatos):
    listar(contatos)
    if not contatos:
        return
    indice = int(input("\nN° do contato a remover: ")) - 1
    if 0 <= indice < len(contatos):
        removido = contatos.pop(indice)
        print(f"✅ Contato removido: {removido.nome}")
    else:
        print("Índice inválido.")

#==========
#MENU PRINCIPAL
#==========

def menu():
    contatos = carregar_de_binario("agenda.bin")  # Tenta carregar contatos salvos
    while True:
        print("\n ======= AGENDA ========")
        print("1. Cadastrar contato")
        print("2. Listar contatos")
        print("3. Remover contato")
        print("4. Salvar em .txt")
        print("5. Salvar em binário")
        print("0. Sair")
        opcao = input("Opção: ")

        if opcao == '1':
            cadastrar(contatos)
        elif opcao == '2':
            listar(contatos)
        elif opcao == '3':
            remover(contatos)
        elif opcao == '4':
            salvar_em_txt(contatos, 'agenda.txt')
        elif opcao == '5':
            salvar_em_binario(contatos, 'agenda.bin')
        elif opcao == '0':
            salvar_em_binario(contatos, 'agenda.bin')  # Salva automaticamente ao sair
            print("Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()