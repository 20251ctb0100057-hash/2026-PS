import json
import os

ARQUIVO_JSON = "pets.json"
class Pet:
    def __init__(self, nome, especie, idade, peso, dono, vacinado=False, hospedado=False):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.peso = peso
        self.dono = dono
        self.vacinado = vacinado
        self.hospedado = hospedado

    def para_dicionario(self):
        return {
            "nome": self.nome,
            "especie": self
        }
    def exibir_dados(self):
        status = "Hospedado" if self.hospedado else "Livre"
        vacina = "Vacinado" if self.vacinado else "Não Vacinado"
        print(f"[{status:9}] {self.nome:10} | {self.especie:8} | Peso: {self.peso:>4}kg | {vacina:12} | Dono: {self.dono}")

    def emitir_resumo(self):
        print("-" * 30)
        print(f"RESUMO DO PET: {self.nome.upper()}")
        print(f"Responsável: {self.dono}")
        print(f"Espécie: {self.especie} | Idade: {self.idade} anos")
        print(f"Status Atual: {'Hospedado' if self.hospedado else 'Não está no hotel'}")
        print("-" * 30)

    # Método essencial para persistência em TXT
    #def para_linha_txt(self):
       # return f"{self.nome};{self.especie};{self.idade};{self.peso};{self.dono};{self.vacinado};{self.hospedado}"

# --- FUNÇÕES DE PERSISTÊNCIA ---

def salvar_binario(lista_pets):
    with open("pets_data.bin", "wb") as f:
        pickle.dump(lista_pets, f)
    print("\n[OK] Dados salvos em formato BINÁRIO.")

def carregar_binario():
    if os.path.exists("pets_data.bin"):
        with open("pets_data.bin", "rb") as f:
            return pickle.load(f)
    return []

def salvar_txt(lista_pets):
    with open("pets_data.txt", "w", encoding="utf-8") as f:
        for p in lista_pets:
            f.write(p.para_linha_txt() + "\n")
    print("\n[OK] Dados salvos em formato TEXTO (.txt).")

def carregar_txt():
    lista = []
    if os.path.exists("pets_data.txt"):
        with open("pets_data.txt", "r", encoding="utf-8") as f:
            for linha in f:
                # Quebra a linha e reconverte os tipos de dados
                dados = linha.strip().split(";")
                if len(dados) == 7:
                    p = Pet(dados[0], dados[1], int(dados[2]), float(dados[3]), 
                            dados[4], dados[5] == "True", dados[6] == "True")
                    lista.append(p)
    return lista

# --- INTERFACE ---

def main():
    # Pergunta ao iniciar qual base carregar
    print("Como deseja carregar os dados?")
    print("1. Arquivo Binário | 2. Arquivo TXT | 3. Iniciar Vazio")
    escolha_ini = input("Escolha: ")
    
    if escolha_ini == "1": pets = carregar_binario()
    elif escolha_ini == "2": pets = carregar_txt()
    else: pets = []

    while True:
        print("\n" + "="*40)
        print("      SISTEMA PETVILLE V2.0")
        print("="*40)
        print("1. Cadastrar Pet")
        print("2. Listar Todos")
        print("3. Buscar Pet (Nome)")
        print("4. Check-in/Out e Atualizar Peso")
        print("5. Relatório de Hospedados")
        print("6. Emitir Resumo Individual")
        print("7. SALVAR EM TXT")
        print("8. SALVAR EM BINÁRIO")
        print("0. Sair")
        
        op = input("\nSelecione: ")

        if op == "1":
            n = input("Nome: "); e = input("Espécie: "); i = int(input("Idade: "))
            p = float(input("Peso: ")); d = input("Dono: ")
            v = input("Vacinado? (s/n): ").lower() == 's'
            pets.append(Pet(n, e, i, p, d, v))

        elif op == "2":
            print("\nLISTAGEM GERAL:")
            for i, p in enumerate(pets):
                print(f"{i} - ", end=""); p.exibir_dados()

        elif op == "3":
            busca = input("Nome do pet: ").lower()
            encontrados = [p for p in pets if busca in p.nome.lower()]
            for p in encontrados: p.exibir_dados()

        elif op == "4":
            nome = input("Nome do pet: ")
            for p in pets:
                if p.nome.lower() == nome.lower():
                    # Gerencia hospedagem
                    p.hospedado = not p.hospedado
                    # Atualiza peso
                    p.peso = float(input(f"Peso atual de {p.nome}: "))
                    print(f"Dados de {p.nome} atualizados!")
                    break

        elif op == "5":
            print("\nPETS HOSPEDADOS:")
            hospedados = [p for p in pets if p.hospedado]
            for p in hospedados: p.exibir_dados()
            print(f"Total: {len(hospedados)} pets no hotel.")

        elif op == "6":
            nome = input("Nome para resumo: ")
            for p in pets:
                if p.nome.lower() == nome.lower():
                    p.emitir_resumo()

        elif op == "7":
            salvar_txt(pets)

        elif op == "8":
            salvar_binario(pets)

        elif op == "0":
            # Salva em ambos por segurança ao sair (Exigência Nível A)
            salvar_txt(pets)
            salvar_binario(pets)
            print("Sistema encerrado.")
            break

if __name__ == "__main__":
    main()