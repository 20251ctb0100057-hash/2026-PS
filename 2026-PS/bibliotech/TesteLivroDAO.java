public class TesteLivroDAO {

    public static void main(String[] args) {

        LivroDAO dao = new LivroDAO();

        boolean resultado = dao.atualizarLivro(
            1,
            "Dom Casmurro Atualizado",
            "Machado de Assis",
            1899
        );

        System.out.println(
            "Livro atualizado: " + resultado
        );
    }
}