import java.util.Scanner;

public class TesteBuscarLivro {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        LivroDAO dao = new LivroDAO();

        System.out.println("=== BUSCAR LIVRO ===");

        int id = -1;

        while (id != 0) {

            System.out.print("\nInforme o ID (0 para sair): ");
            id = entrada.nextInt();

            if (id == 0) {
                break;
            }

            String livro = dao.buscarLivroPorId(id);

            if (livro != null) {
                System.out.println("Livro encontrado:");
                System.out.println(livro);
            } else {
                System.out.println("Livro não encontrado.");
            }
        }

        System.out.println("Programa encerrado.");
        entrada.close();
    }
}