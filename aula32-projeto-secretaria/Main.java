import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        ArrayList<Aluno> lista = new ArrayList<Aluno>();

        while (true) {
            System.out.println("==========================================");
            System.out.println("        SECRETARIA DO SEU NOME");
            System.out.println("==========================================");
            System.out.println("[1] Cadastrar aluno");
            System.out.println("[2] Listar alunos");
            System.out.println("[0] Sair");
            System.out.print("Sua escolha: ");

            String opcao = teclado.nextLine().trim();

            if (opcao.equals("0")) {
                System.out.println("Secretaria fechada. Ate a proxima!");
                break;
            } else if (opcao.equals("1")) {
                cadastrar(lista, teclado);
            } else if (opcao.equals("2")) {
                listar(lista);
            } else {
                System.out.println("Opcao invalida! Vale 0, 1 ou 2.");
            }
        }

        teclado.close();
    }

    static void cadastrar(ArrayList<Aluno> lista, Scanner teclado) {
        System.out.print("Nome: ");
        String nome = teclado.nextLine().trim();

        System.out.print("Matricula: ");
        String matricula = teclado.nextLine().trim();

        System.out.print("Curso: ");
        String curso = teclado.nextLine().trim();

        Aluno novo = new Aluno(nome, matricula, curso);
        lista.add(novo);

        System.out.println("Ficha de " + novo.getNome() + " arquivada!");
    }

    static void listar(ArrayList<Aluno> lista) {
        if (lista.size() == 0) {
            System.out.println("Nenhuma ficha cadastrada.");
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
}
