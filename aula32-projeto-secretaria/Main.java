import java.util.ArrayList;
import java.util.Scanner;

/*
 * Disciplina: Programacao
 * Aluno: Yuri
 * Data: 27/08/2026
 * Projeto: Secretaria
 * Arquivo: Main.java
 */

public class Main {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        ArrayList<Aluno> lista = new ArrayList<Aluno>();

        while (true) {
            System.out.println("==========================================");
            System.out.println("   SECRETARIA DO CAMPUS - por Yuri");
            System.out.println("==========================================");
            System.out.println("[1] Cadastrar aluno");
            System.out.println("[2] Listar alunos");
            System.out.println("[3] Buscar por matricula");
            System.out.println("[4] Atualizar curso");
            System.out.println("[5] Remover aluno");
            System.out.println("[6] Relatorio");
            System.out.println("[0] Sair");
            System.out.print("Sua escolha: ");

            String opcao = teclado.nextLine().trim();

            if (opcao.equals("0")) {
                System.out.println("Secretaria encerrada. Ate a proxima!");
                break;

            } else if (opcao.equals("1")) {
                cadastrar(lista, teclado);

            } else if (opcao.equals("2")) {
                listar(lista);

            } else if (opcao.equals("3")) {
                buscar(lista, teclado);

            } else if (opcao.equals("4")) {
                atualizarCurso(lista, teclado);

            } else if (opcao.equals("5")) {
                remover(lista, teclado);

            } else if (opcao.equals("6")) {
                relatorio(lista);

            } else {
                System.out.println(
                    "Opcao invalida! Vale 0, 1, 2, 3, 4, 5 ou 6."
                );
            }

            System.out.println();
        }

        teclado.close();
    }


    // =========================================================
    // 1 - CADASTRAR ALUNO
    // =========================================================

    static void cadastrar(ArrayList<Aluno> lista, Scanner teclado) {

        System.out.println("\n--- CADASTRAR ALUNO ---");

        System.out.print("Nome: ");
        String nome = teclado.nextLine().trim();

        // Verifica se o nome foi preenchido
        if (nome.isEmpty()) {
            System.out.println("Erro: o nome nao pode ficar vazio.");
            return;
        }

        System.out.print("Matricula: ");
        String matricula = teclado.nextLine().trim();

        // Verifica se a matricula foi preenchida
        if (matricula.isEmpty()) {
            System.out.println("Erro: a matricula nao pode ficar vazia.");
            return;
        }

        // Verifica se a matricula ja existe
        if (buscarAluno(lista, matricula) != null) {
            System.out.println("Erro: essa matricula ja esta cadastrada.");
            return;
        }

        System.out.print("Curso: ");
        String curso = teclado.nextLine().trim();

        // Verifica se o curso foi preenchido
        if (curso.isEmpty()) {
            System.out.println("Erro: o curso nao pode ficar vazio.");
            return;
        }

        Aluno novo = new Aluno(nome, matricula, curso);
        lista.add(novo);

        System.out.println(
            "Aluno cadastrado com sucesso: " + novo.getNome()
        );
    }


    // =========================================================
    // 2 - LISTAR ALUNOS
    // =========================================================

    static void listar(ArrayList<Aluno> lista) {

        System.out.println("\n--- LISTA DE ALUNOS ---");

        if (lista.size() == 0) {
            System.out.println("Nenhuma ficha cadastrada ainda.");
            return;
        }

        for (Aluno aluno : lista) {
            System.out.println(
                aluno.getMatricula() + " | " +
                aluno.getNome() + " | " +
                aluno.getCurso()
            );
        }
    }


    // =========================================================
    // 3 - BUSCAR POR MATRICULA
    // =========================================================

    static void buscar(ArrayList<Aluno> lista, Scanner teclado) {

        System.out.println("\n--- BUSCAR ALUNO ---");

        System.out.print("Digite a matricula: ");
        String matricula = teclado.nextLine().trim();

        Aluno aluno = buscarAluno(lista, matricula);

        if (aluno != null) {

            System.out.println("Aluno encontrado!");
            System.out.println("Nome: " + aluno.getNome());
            System.out.println("Matricula: " + aluno.getMatricula());
            System.out.println("Curso: " + aluno.getCurso());

        } else {
            System.out.println(
                "Nenhum aluno encontrado com essa matricula."
            );
        }
    }


    // =========================================================
    // METODO DE BUSCA REUTILIZADO
    // =========================================================

    static Aluno buscarAluno(
        ArrayList<Aluno> lista,
        String matricula
    ) {

        for (Aluno aluno : lista) {

            if (aluno.getMatricula().equals(matricula)) {
                return aluno;
            }
        }

        return null;
    }


    // =========================================================
    // 4 - ATUALIZAR CURSO
    // =========================================================

    static void atualizarCurso(
        ArrayList<Aluno> lista,
        Scanner teclado
    ) {

        System.out.println("\n--- ATUALIZAR CURSO ---");

        System.out.print("Digite a matricula do aluno: ");
        String matricula = teclado.nextLine().trim();

        Aluno aluno = buscarAluno(lista, matricula);

        if (aluno == null) {
            System.out.println("Aluno nao encontrado.");
            return;
        }

        System.out.println("Aluno: " + aluno.getNome());
        System.out.println("Curso atual: " + aluno.getCurso());

        System.out.print("Novo curso: ");
        String novoCurso = teclado.nextLine().trim();

        if (novoCurso.isEmpty()) {
            System.out.println("Erro: o curso nao pode ficar vazio.");
            return;
        }

        aluno.setCurso(novoCurso);

        System.out.println("Curso atualizado com sucesso!");
    }


    // =========================================================
    // 5 - REMOVER ALUNO
    // =========================================================

    static void remover(
        ArrayList<Aluno> lista,
        Scanner teclado
    ) {

        System.out.println("\n--- REMOVER ALUNO ---");

        System.out.print("Digite a matricula do aluno: ");
        String matricula = teclado.nextLine().trim();

        Aluno aluno = buscarAluno(lista, matricula);

        if (aluno == null) {
            System.out.println("Aluno nao encontrado.");
            return;
        }

        System.out.println("Aluno encontrado: " + aluno.getNome());

        System.out.print(
            "Tem certeza que deseja remover? (s/n): "
        );

        String confirmacao = teclado.nextLine().trim();

        if (confirmacao.equalsIgnoreCase("s")) {

            lista.remove(aluno);

            System.out.println("Aluno removido com sucesso.");

        } else {

            System.out.println("Remocao cancelada.");
        }
    }


    // =========================================================
    // 6 - RELATORIO
    // =========================================================

    static void relatorio(ArrayList<Aluno> lista) {

        System.out.println("\n--- RELATORIO ---");

        if (lista.size() == 0) {
            System.out.println("Nenhum aluno cadastrado.");
            return;
        }

        System.out.println("Total de alunos: " + lista.size());

        System.out.println("\nAlunos cadastrados:");

        for (Aluno aluno : lista) {

            System.out.println(
                "- " + aluno.getNome() +
                " | Matricula: " + aluno.getMatricula() +
                " | Curso: " + aluno.getCurso()
            );
        }
    }
}