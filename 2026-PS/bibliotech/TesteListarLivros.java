
import java.util.List;

public class TesteListarLivros {

    public static void main(String[] args) {

        LivroDAO dao = new LivroDAO();
        List<Livro> livros = dao.listarLivros();

        System.out.println("=== LIVROS PUBLICADOS A PARTIR DE 2000 ===");

        boolean encontrou = false;

        for (Livro livro : livros) {
            if (livro.getAno() >= 2000) {

                System.out.println(
                    livro.getId() + " - "
                    + livro.getTitulo() + " - "
                    + livro.getAutor() + " ("
                    + livro.getAno() + ")"
                );

                encontrou = true;
            }
        }

        if (!encontrou) {
            System.out.println(
                "Nenhum livro publicado a partir de 2000 foi encontrado."
            );
        }
    }
}
