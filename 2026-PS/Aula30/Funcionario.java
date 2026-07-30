public class Main {

    // --- 1. ENTIDADE FUNCIONARIO (Inner Class) ---
    static class Funcionario {
        // Atributos privados (Encapsulamento)
        private String matricula; // Ex: MA1015 (Iniciais + Dia)
        private String nome;
        private double salario;   // Ex: R$ 1500.00
        private String cargo;
        private boolean ativo;

        // Construtor principal
        public Funcionario(String matricula, String nome, double salario, String cargo, boolean ativo) {
            if (!validarMatricula(matricula) || !validarNome(nome) || !validarSalario(salario)) {
                System.out.println("❌ Dados inválidos para cadastro!");
                return;
            }
            this.matricula = matricula;
            this.nome = nome;
            this.salario = salario;
            this.cargo = cargo;
            this.ativo = ativo;
        }

        // Desafio Complementar 1: Construtor alternativo (menos parâmetros)
        public Funcionario(String matricula, String nome, double salario) {
            this(matricula, nome, salario, "Analista Junior", true);
        }

        // --- VALIDAÇÕES (3 regras) ---
        private boolean validarMatricula(String matricula) {
            return matricula != null && !matricula.trim().isEmpty() && matricula.length() >= 4;
        }

        private boolean validarNome(String nome) {
            return nome != null && !nome.trim().isEmpty();
        }

        private boolean validarSalario(double salario) {
            return salario > 0;
        }

        // --- GETTERS E SETTERS ---
        public String getNome() { return nome; }
        public double getSalario() { return salario; }
        public boolean isAtivo() { return ativo; }

        public void setNome(String nome) {
            if (validarNome(nome)) {
                this.nome = nome;
                System.out.println("✅ Nome alterado para: " + nome);
            } else {
                System.out.println("❌ Alteração recusada: Nome não pode ser vazio!");
            }
        }

        // --- COMPORTAMENTOS DA ENTIDADE (Regras de negócio) ---
        public boolean aplicarAumento(double percentual) {
            if (percentual <= 0) {
                System.out.println("❌ Alteração recusada: Percentual deve ser maior que zero!");
                return false;
            }
            this.salario += this.salario * (percentual / 100);
            System.out.println("✅ Aumento de " + percentual + "% aplicado! Novo Salário: R$" + this.salario);
            return true;
        }

        public boolean inativar() {
            if (!this.ativo) {
                System.out.println("❌ Falha: O funcionário já está inativo!");
                return false;
            }
            this.ativo = false;
            System.out.println("✅ Funcionário " + this.nome + " inativado com sucesso!");
            return true;
        }

        // Desafio Complementar 2: Resumo textual do objeto
        public String obterResumo() {
            return "ID: " + matricula + " | Nome: " + nome + " | Cargo: " + cargo + 
                   " | Salario: R$" + salario + " | Ativo: " + (ativo ? "Sim" : "Não");
        }
    }

    // --- 2. EXECUÇÃO DOS CASOS DE TESTE (Main) ---
    public static void main(String[] args) {
        
        System.out.println("\n--- Teste 1: Criar objetos com dados válidos ---");
        // Personalização: Iniciais "MA" e dia do nascimento "15"
        Funcionario f1 = new Funcionario("MA1015", "Mateus Silva", 1500.00, "Desenvolvedor", true);
        Funcionario f2 = new Funcionario("MA1016", "Mariana Costa", 2515.00, "Gerente", true);
        Funcionario f3 = new Funcionario("MA1017", "Marcio Souza", 1500.15); // Construtor reduzido

        System.out.println(f1.obterResumo());
        System.out.println(f2.obterResumo());
        System.out.println(f3.obterResumo());

        System.out.println("\n--- Teste 2: Atribuir texto vazio a campo obrigatório ---");
        f1.setNome(""); // Deve recusar

        System.out.println("\n--- Teste 3: Atribuir número negativo a campo restrito ---");
        f1.aplicarAumento(-15.0); // Deve recusar

        System.out.println("\n--- Teste 4: Executar comportamento permitido ---");
        f1.aplicarAumento(15.0); // Aumento válido de 15%

        System.out.println("\n--- Teste 5: Executar comportamento impossível ---");
        f2.inativar(); // 1ª vez: Sucesso
        f2.inativar(); // 2ª vez: Deve falhar (já está inativo)

        System.out.println("\n=================================");
        System.out.println("--- ESTADO FINAL DOS OBJETOS ---");
        System.out.println("=================================");
        System.out.println(f1.obterResumo());
        System.out.println(f2.obterResumo());
        System.out.println(f3.obterResumo());
    }
}