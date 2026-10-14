public class TesteRequisitos {

    private static int passaram = 0;
    private static int falharam = 0;

    private static void verificar(String requisito, boolean condicao) {
        if (condicao) {
            passaram++;
            System.out.println("OK      " + requisito);
        } else {
            falharam++;
            System.out.println("FALHOU  " + requisito);
        }
    }

    public static void main(String[] args) {
        Biblioteca biblioteca = new Biblioteca();

        biblioteca.cadastrarLivro(
            new Livro("Dom Casmurro", "Machado de Assis", 1));
        biblioteca.cadastrarLivro(
            new Livro("Capitaes de Areia", "Jorge Amado", 2));

        biblioteca.cadastrarLeitor(
            new Leitor("Pedro Alves", "2026010", 1));
        biblioteca.cadastrarLeitor(
            new Leitor("Ana Lima", "2026011", 2));

        Livro dom = biblioteca.buscarLivro("Dom Casmurro");
        Leitor pedro = biblioteca.buscarLeitor("2026010");

        verificar("RF01 livro cadastrado aparece na busca",
            dom != null);

        verificar("RF02 leitor cadastrado aparece na busca",
            pedro != null);

        verificar("RF03 livro novo esta disponivel",
            dom != null && dom.estaDisponivel());

        verificar("RF03 titulo fora do acervo nao e encontrado",
            biblioteca.buscarLivro("O Cortico") == null);

        verificar("RF05 emprestimo de livro disponivel e aceito",
            biblioteca.emprestar("Dom Casmurro", "2026010"));

        verificar("RF05 livro emprestado fica indisponivel",
            !dom.estaDisponivel());

        verificar("RF05 leitor passa a ter 1 livro em maos",
            pedro.getLivrosEmMaos() == 1);

        verificar("RF05 livro emprestado e recusado para outro leitor",
            !biblioteca.emprestar("Dom Casmurro", "2026011"));

        verificar("RF05 leitor no limite e recusado",
            !biblioteca.emprestar("Capitaes de Areia", "2026010"));

        verificar("RF04 devolucao de emprestimo ativo e aceita",
            biblioteca.devolver("Dom Casmurro"));

        verificar("RF04 livro devolvido volta a ficar disponivel",
            dom.estaDisponivel());

        verificar("RF04 segunda devolucao e recusada",
            !biblioteca.devolver("Dom Casmurro"));

        System.out.println();
        System.out.println(passaram + " passaram, "
            + falharam + " falharam.");
    }
}