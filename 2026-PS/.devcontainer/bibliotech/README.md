# 🎯 BiblioTech — Gestão Bibliotecária

## Seção 1: Apresentação do Projeto & Visão Geral
O **BiblioTech** é um sistema projetado para gerenciar operações essenciais de uma biblioteca, automatizando a consulta de disponibilidade, o registro de empréstimos, devoluções e a identificação dos usuários leitores.

- **Cliente:** Bibliotecas escolares, universitárias ou comunitárias.
- **Problema:** Controle manual passível de erros na entrega, falta de verificação rápida do acervo e ausência de histórico centralizado de empréstimos.
- **Público-alvo:** Leitores (estudantes/comunidade) e Bibliotecários (gestores do acervo).

![Casos de Uso](docs/casos-de-uso.svg)
![Diagrama de Classes](docs/classes.svg)

---

## Seção 2: Histórias de Usuário (HU) e Requisitos Funcionais (RF)

### Histórias de Usuário (HU)
| ID | Como [Papel] | Eu quero [Ação] | Para que [Benefício] |
|---|---|---|---|
| HU01 | Leitor | Consultar a disponibilidade de um livro | Saber se posso realizá-lo o empréstimo imediatamente |
| HU02 | Bibliotecário | Registrar o empréstimo de um livro para um leitor | Garantir que a obra esteja associada a um leitor identificado |
| HU03 | Bibliotecário | Registrar a devolução de um livro | Atualizar o status da obra e verificar devoluções em atraso |

### Requisitos Funcionais (RF)
| ID | Descrição | Origem / Veio da |
|---|---|---|
| RF01 | O sistema deve permitir a consulta da disponibilidade dos livros do acervo. | HU01 |
| RF02 | O sistema deve permitir ao bibliotecário registrar empréstimos vinculando o leitor ao livro. | HU02 |
| RF03 | O sistema deve obrigatoriamente identificar o leitor ao realizar um empréstimo («include»). | HU02 |
| RF04 | O sistema deve registrar a devolução e calcular eventuais atrasos. | HU03 |
| RF06 | O sistema deve emitir um comprovante/notificação digital de renovação ou devolução. | Solicitado pelo cliente / Regra de Negócio |

---

## Seção 3: Decisão da Ligação Bibliotecario–Emprestimo

- **Multiplicidade definida:** `Bibliotecario (1) <---> (0..*) Emprestimo`
- **Justificativa:** Cada registro de empréstimo deve ser processado e atrelado a exatamente **1** Bibliotecário responsável pela operação no sistema. Por outro lado, um Bibliotecário pode realizar nenhum (**0**) ou múltiplos (*****) empréstimos ao longo da sua rotina de trabalho.

---

## Seção 4: Diagrama de Classes (Mermaid)

```mermaid
classDiagram
    class Usuario {
        +String nome
        +String matricula
        +entrar() boolean
    }

    class Leitor {
        +int limiteEmprestimos
        +podePegarEmprestado()
    }

    class Bibliotecario {
        +String matriculaFuncional
        +consultarAcervo() boolean
    }

    class Livro {
        +String titulo
        +String autor
        +int ano
        +estaDisponivel()
    }

    class Emprestimo {
        +Data dataRetirada
        +Data dataDevolucao
        +calcularDevolucao()
        +estaAtrasado()
    }

    Usuario <|-- Leitor
    Usuario <|-- Bibliotecario
    Leitor "1" -- "0..*" Emprestimo : realiza
    Bibliotecario "1" -- "0..*" Emprestimo : registra
    Livro "1" -- "0..*" Emprestimo : composto por