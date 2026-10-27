
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

            Livro livro = dao.buscarLivroPorId(id);

            if (livro != null) {

                System.out.println("Livro encontrado:");

                System.out.println("ID: " + livro.getId());
                System.out.println("Título: " + livro.getTitulo());
                System.out.println("Autor: " + livro.getAutor());
                System.out.println("Ano: " + livro.getAno());

            } else {
                System.out.println("Livro não encontrado.");
            }
        }

        System.out.println("Programa encerrado.");
        entrada.close();
    }
}
