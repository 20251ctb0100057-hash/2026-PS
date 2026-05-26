import json
import os

ARQUIVO_JSON = "pets.json"

class Pet:
    def __init__(self, nome, especie, idade, peso, dono, data_nascimento, altura, vacinado=False, hospedado=False):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.peso = peso
        self.dono = dono
        self.data_nascimento = data_nascimento
        self.altura = altura
        self.vacinado = vacinado
        self.hospedado = hospedado

    def exibir_dados(self):
        status = "Hospedado" if self.hospedado else "Livre"
        vacina = "Vacinado" if self.vacinado else "Não Vacinado"

        print(
            f"[{status:9}] "
            f"{self.nome:10} | "
            f"{self.especie:8} | "
            f"Peso: {self.peso:>5.2f}kg | "
            f"Altura: {self.altura:>4.2f}m | "
            f"{vacina:12} | "
            f"Dono: {self.dono}"
        )

    def emitir_resumo(self):
        print("\n" + "-" * 30)
        print(f"RESUMO DO PET: {self.nome.upper()}")
        print(f"Responsável: {self.dono}")
        print(f"Espécie: {self.especie} | Idade: {self.idade} anos")
        print(f"Nascimento: {self.data_nascimento} | Altura: {self.altura}m")
        print(f"Status Atual: {'Hospedado' if self.hospedado else 'Não está no hotel'}")
        print("-" * 30)

    def para_dicionario(self):
        """Converte o objeto para um dicionário compatível com JSON."""
        return {
            "nome": self.nome,
            "especie": self.especie,
            "idade": self.idade,
            "peso": self.peso,
            "dono": self.dono,
            "data_nascimento": self.data_nascimento,
            "altura": self.altura,
            "vacinado": self.vacinado,
            "hospedado": self.hospedado
        }

    @staticmethod
    def criar_de_dicionario(dados):
        """Recria o objeto Pet a partir de um dicionário vindo do JSON."""
        return Pet(
            nome=dados["nome"],
            especie=dados["especie"],
            idade=dados["idade"],
            peso=dados["peso"],
            dono=dados["dono"],
            data_nascimento=dados["data_nascimento"],
            altura=dados["altura"],
            vacinado=dados["vacinado"],
            hospedado=dados["hospedado"]
        )


# --- FUNÇÕES DE PERSISTÊNCIA ---

def salvar_pets(lista_pets):
    lista_dicionarios = [pet.para_dicionario() for pet in lista_pets]
    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(lista_dicionarios, arquivo, ensure_ascii=False, indent=4)
    print("\n[OK] Dados salvos com sucesso!")


def carregar_pets():
    if not os.path.exists(ARQUIVO_JSON):
        return []
    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
            lista_dicionarios = json.load(arquivo)
        return [Pet.criar_de_dicionario(d) for d in lista_dicionarios]
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return []


# --- INTERFACE ---

def main():
    pets = carregar_pets()

    while True:
        print("\n" + "=" * 45)
        print("      SISTEMA PETVILLE V2.0 (ATUALIZADO)")
        print("=" * 45)
        print("1. Cadastrar Pet")
        print("2. Listar Todos")
        print("3. Buscar Pet (Nome)")
        print("4. Check-in/Out e Atualizar Peso")
        print("5. Relatório de Hospedados")
        print("6. Emitir Resumo Individual")
        print("7. SALVAR DADOS")
        print("0. Sair")

        op = input("\nSelecione uma opção: ")

        if op == "1":
            try:
                n = input("Nome: ")
                e = input("Espécie: ")
                i = int(input("Idade: "))
                p = float(input("Peso (kg): "))
                alt = float(input("Altura (m): "))
                nasc = input("Data de Nascimento (dd/mm/aaaa): ")
                d = input("Dono: ")
                v = input("Vacinado? (s/n): ").lower() == 's'

                # Criando o pet com a nova ordem de parâmetros
                novo_pet = Pet(n, e, i, p, d, nasc, alt, v)
                pets.append(novo_pet)
                print("\n[SUCESSO] Pet cadastrado!")
            except ValueError:
                print("\n[ERRO] Entrada inválida. Idade, Peso e Altura devem ser números.")

        elif op == "2":
            print("\n" + "ID  " + "STATUS".ljust(11) + " | " + "NOME".ljust(10) + " | " + "ESPÉCIE".ljust(8))
            print("-" * 60)
            for i, p in enumerate(pets):
                print(f"{i:<3} ", end="")
                p.exibir_dados()

        elif op == "3":
            busca = input("Nome do pet: ").lower()
            encontrados = [p for p in pets if busca in p.nome.lower()]
            if encontrados:
                for p in encontrados:
                    p.exibir_dados()
            else:
                print("Nenhum pet encontrado.")

        elif op == "4":
            nome = input("Nome exato do pet: ")
            encontrado = False
            for p in pets:
                if p.nome.lower() == nome.lower():
                    p.hospedado = not p.hospedado
                    try:
                        p.peso = float(input(f"Peso atual de {p.nome} (kg): "))
                        print(f"\n[OK] Status de {p.nome}: {'HOSPEDADO' if p.hospedado else 'LIBERADO'}")
                    except ValueError:
                        print("[ERRO] Peso inválido. Mantendo peso anterior.")
                    encontrado = True
                    break
            if not encontrado:
                print("Pet não encontrado.")

        elif op == "5":
            print("\nPETS ATUALMENTE HOSPEDADOS:")
            hospedados = [p for p in pets if p.hospedado]
            for p in hospedados:
                p.exibir_dados()
            print(f"\nTotal: {len(hospedados)} pets no hotel.")

        elif op == "6":
            nome = input("Nome do pet para resumo: ")
            encontrado = False
            for p in pets:
                if p.nome.lower() == nome.lower():
                    p.emitir_resumo()
                    encontrado = True
                    break
            if not encontrado:
                print("Pet não encontrado.")

        elif op == "7":
            salvar_pets(pets)

        elif op == "0":
            salvar_pets(pets)
            print("Sistema encerrado. Até logo!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()