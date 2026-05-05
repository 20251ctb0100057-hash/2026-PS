'''
======================
# ARQUIVO   : pet.py
# Disciplina: Programação de Sistemas
# Aula      : Aula 20 - Por que POO?
# Autor     : Yuri
# Conceitos : Classe, objeto, atributos, métodos, encapsulamento
# Atividade : Classe Pet
'''

class Pet:
    # Esta classe representa em Pet em um sistema simples de hotel para pets.
    # Em vez de guardar dados do pet em um dicionário solto, como fazíamos na programação estruturada,
    # agora agrupamos os dados e comportamentos dentro de uma classe

    def __init__(self, nome, especie, idade, raca, peso, dono, vacinado):
        # Método construtor para inicializar os atributos do pet
        # Executado automaticamente quando criamos um novo pet
        # Ex: pet1 = Pet("Rex", "Cachorro", 5)
        # Parâmetros
        # - nome: nome do pet 
        # - especie: espécie do pet
        # - idade: idade do pet

        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.raca = raca
        self.peso = peso
        self.dono = dono
        self.vacinado = vacinado
        self.hospedado = False  # Atributo para indicar se o pet está hospedado ou não

    # ==================
    # ATIVIDADE 1
    # Adicione pelo menos 3 novos atributoss para o pet.
    # Sugestões: raça, peso, cor, dono, etc.
    # SE VOCE ADICIONAR NOVOS ATRIBUTOR, TAMBEM PRECISARÁ ALTERAR OS PARÂMETROS DO MÉTODO __init__
    def exibir_dados(self):
        # Método para exibir os dados do pet
        print("\n--- Dados do Pet ---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade} anos")
        print(f"Raça: {self.raca}")
        print(f"Peso: {self.peso} kg")
        print(f"Dono: {self.dono}")
        print(f"Vacinado: {'Sim' if self.vacinado else 'Não'}")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")

    def registrar_entrada(self):
        '''
        Registra a entrada do pet no hotel. Verifica se o pet já está hospedado para evitar duplicidade.
        ATIVIDADE: Melhore este metodo para verificar se o pet ja esta hospedado. Se ja estiiver, mostre uma mensagem avisando.
        '''
        if self.hospedado:
            print(f"{self.nome} já está hospedado no hotel.")
        else:
            self.hospedado = True
            print(f"{self.nome} foi registrado para hospedagem.")

    def registrar_saida(self):
        '''
        Registra a saída do pet do hotel.
        ATIVIDADE: Melhore este método para verificar se o pet realmente está hospedado.
        Se o pet não estiver hospedado, mostre uma mensagem avisando.
        '''
        if not self.hospedado:
            print(f"{self.nome} não está hospedado no hotel.")
        else:
            self.hospedado = False
            print(f"{self.nome} saiu do hotel.")

    def calcular_diaria(self):
        '''
        Calcula o valor da diaria do pet
        ATIVIDADE: Melhore este metodo para verificar se o pet realmente está hospedado.
        Se não estiver, mostre uma mensagem avisando.
        Sugestao:
        - Pet com idade até 3 anos: R$50,00
        - Pet com idade entre 4 e 10 anos: R$60,00
        - Pet com idade acima de 10 anos: R$75,00
        '''
        if not self.hospedado:
            print(f"{self.nome} não está hospedado no hotel.")
            return None

        if self.idade <= 3:
            return 45.00
        elif self.idade <= 10:
            return 100.00
        else:
            return 150.00

    def verificar_vacinacao(self):
        '''
        Verifica se o pet está vacinado.
        ATIVIDADE: Melhore este método para verificar se o pet realmente está hospedado.
        Se não estiver, mostre uma mensagem avisando.
        '''
        if not self.hospedado:
            print(f"{self.nome} não está hospedado no hotel.")
            return

        if self.vacinado:
            print(f"{self.nome} está vacinado.")
        else:
            print(f"{self.nome} não está vacinado.")

    def atualizar_peso(self, novo_peso):
        '''
        Atualiza o peso do pet.
        ATIVIDADE: 
        Para este metoodo funcionar, voce precisa criar um atributo chamado self.peso no método __init__ e inicializa-lo com o valor do peso do pet.
        O metodo deve receber um novo peso e atualizar o valor antigo
        '''
        self.peso = novo_peso
        print(f"O peso de {self.nome} foi atualizado para {self.peso} kg.")

    def emitir_resumo(self):
        '''
        Exibe um resumo geral do pet
        ATIVIDADE:
        Crie uma mensagem organiada contendo:
        - Nome do pet
        - Espécie
        - Idade
        - Raça
        - Peso
        - Status de vacinação
        - Status de hospedagem
        Este método deve usar informaçõe dos atributos e tambem pode chamar outros metodos, como calcular_diaria().
        '''
        print("\n--- Resumo do Pet ---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade} anos")
        print(f"Raça: {self.raca}")
        print(f"Peso: {self.peso} kg")
        print(f"Dono: {self.dono}")
        print(f"Vacinado: {'Sim' if self.vacinado else 'Não'}")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")
        if self.hospedado:
            diaria = self.calcular_diaria()
            if diaria is not None:
                print(f"Valor da diária: R${diaria:.2f}")

'''
# ==============================
# TESTES DE CLASSE
# ==============================
# Depois de completar a classe, crie pelo menos 3 objetos Pet.
#
# Exemplo: 
# pet1 = Pet("Rex", "Cachorro", 5)
#
# Atenção
# Se voce adicionou novos atributos no método __init__, lembre-se de passar os valores corretos ao criar os objetos.
'''
'''
ATIVIDADE FINAL:
cRIE MAIS DOIS PETS E TESTE TODOS OS METODOS IMPLEMENTADOS
'''
pet1 = Pet("nobru🐶", "Cachorro", 5, "Labrador", 22.5, "ana", True)
pet2 = Pet("Yuri", "Gato", 2, "Siamês", 4.2, "Maria Eduarda", True)
pet3 = Pet("Fernando🐶", "Cachorro", 11, "Vira-lata", 18.0, "Ana", False)

pet1.exibir_dados()
pet1.registrar_entrada()
pet1.verificar_vacinacao()
print("Diária:", pet1.calcular_diaria())
pet1.atualizar_peso(23.0)
pet1.emitir_resumo()

pet3.exibir_dados()
pet3.verificar_vacinacao()
pet3.registrar_entrada()
pet3.registrar_saida()

pet2.exibir_dados()
pet2.registrar_entrada()
pet2.verificar_vacinacao()
print("Diária:", pet2.calcular_diaria())
pet2.atualizar_peso(4.5)
pet2.emitir_resumo()
