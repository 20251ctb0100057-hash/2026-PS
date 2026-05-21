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

    def exibir_dados(self):
        status = "Hospedado" if self.hospedado else "Livre"
        vacina = "Vacinado" if self.vacinado else "Não Vacinado"

        print(
            f"[{status:9}] "
            f"{self.nome:10} | "
            f"{self.especie:8} | "
            f"Peso: {self.peso:>4}kg | "
            f"{vacina:12} | "
            f"Dono: {self.dono}"
        )

    def emitir_resumo(self):
        print("-" * 30)
        print(f"RESUMO DO PET: {self.nome.upper()}")
        print(f"Responsável: {self.dono}")
        print(f"Espécie: {self.especie} | Idade: {self.idade} anos")
        print(f"Status Atual: {'Hospedado' if self.hospedado else 'Não está no hotel'}")
        print("-" * 30)

    def para_dicionario(self):
        return {
            "nome": self.nome,
            "especie": self.especie,
            "idade": self.idade,
            "peso": self.peso,
            "dono": self.dono,
            "vacinado": self.vacinado,
            "hospedado": self.hospedado
        }

    @staticmethod
    def criar_de_dicionario(dados):
        return Pet(
            dados["nome"],
            dados["especie"],
            dados["idade"],
            dados["peso"],
            dados["dono"],
            dados["vacinado"],
            dados["hospedado"]
        )


# --- FUNÇÕES DE PERSISTÊNCIA ---

def salvar_pets(lista_pets):

    lista_dicionarios = []

    for pet in lista_pets:
        lista_dicionarios.append(pet.para_dicionario())

    with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
        json.dump(lista_dicionarios, arquivo, ensure_ascii=False, indent=4)

    print("\n[OK] Dados salvos em JSON.")


def carregar_pets():

    if not os.path.exists(ARQUIVO_JSON):
        return []

    with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
        lista_dicionarios = json.load(arquivo)

    lista_pets = []

    for dados in lista_dicionarios:
        pet = Pet.criar_de_dicionario(dados)
        lista_pets.append(pet)

    return lista_pets


# --- INTERFACE ---

def main():

    pets = carregar_pets()

    while True:

        print("\n" + "=" * 40)
        print("      SISTEMA PETVILLE V2.0")
        print("=" * 40)

        print("1. Cadastrar Pet")
        print("2. Listar Todos")
        print("3. Buscar Pet (Nome)")
        print("4. Check-in/Out e Atualizar Peso")
        print("5. Relatório de Hospedados")
        print("6. Emitir Resumo Individual")
        print("7. SALVAR DADOS")
        print("0. Sair")

        op = input("\nSelecione: ")

        if op == "1":

            n = input("Nome: ")
            e = input("Espécie: ")
            i = int(input("Idade: "))
            p = float(input("Peso: "))
            d = input("Dono: ")

            v = input("Vacinado? (s/n): ").lower() == 's'

            pets.append(Pet(n, e, i, p, d, v))

            print("\nPet cadastrado com sucesso!")

        elif op == "2":

            print("\nLISTAGEM GERAL:")

            for i, p in enumerate(pets):
                print(f"{i} - ", end="")
                p.exibir_dados()

        elif op == "3":

            busca = input("Nome do pet: ").lower()

            encontrados = [
                p for p in pets
                if busca in p.nome.lower()
            ]

            if encontrados:
                for p in encontrados:
                    p.exibir_dados()
            else:
                print("Nenhum pet encontrado.")

        elif op == "4":

            nome = input("Nome do pet: ")

            encontrado = False

            for p in pets:

                if p.nome.lower() == nome.lower():

                    p.hospedado = not p.hospedado

                    p.peso = float(
                        input(f"Peso atual de {p.nome}: ")
                    )

                    print(f"Dados de {p.nome} atualizados!")

                    encontrado = True
                    break

            if not encontrado:
                print("Pet não encontrado.")

        elif op == "5":

            print("\nPETS HOSPEDADOS:")

            hospedados = [
                p for p in pets
                if p.hospedado
            ]

            for p in hospedados:
                p.exibir_dados()

            print(f"Total: {len(hospedados)} pets no hotel.")

        elif op == "6":

            nome = input("Nome para resumo: ")

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

            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()