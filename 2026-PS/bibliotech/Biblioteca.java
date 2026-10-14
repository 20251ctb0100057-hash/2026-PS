import java.util.ArrayList;

public class Biblioteca {

    private ArrayList<Livro> livros;
    private ArrayList<Leitor> leitores;
    private ArrayList<Emprestimo> emprestimos;

    public Biblioteca() {
        this.livros = new ArrayList<Livro>();
        this.leitores = new ArrayList<Leitor>();
        this.emprestimos = new ArrayList<Emprestimo>();
    }

    // Cadastra um livro
    public void cadastrarLivro(Livro livro) {
        if (livro != null) {
            livros.add(livro);
        }
    }

    // Cadastra um leitor
    public void cadastrarLeitor(Leitor leitor) {
        if (leitor != null) {
            leitores.add(leitor);
        }
    }

    // Lista todos os livros
    public void listarAcervo() {
        for (int i = 0; i < livros.size(); i++) {
            System.out.println(livros.get(i));
        }
    }

    // Retorna o acervo como texto
    public String obterAcervoComoTexto() {

        String texto = "";

        for (int i = 0; i < livros.size(); i++) {
            texto += livros.get(i).toString();

            if (i < livros.size() - 1) {
                texto += "\n";
            }
        }

        return texto;
    }

    // Busca um livro pelo título
    public Livro buscarLivro(String titulo) {

        for (int i = 0; i < livros.size(); i++) {

            Livro livro = livros.get(i);

            if (livro.getTitulo().equals(titulo)) {
                return livro;
            }
        }

        return null;
    }

    // Busca um leitor pela matrícula
    public Leitor buscarLeitor(String matricula) {

        for (int i = 0; i < leitores.size(); i++) {

            Leitor leitor = leitores.get(i);

            if (leitor.getMatricula().equals(matricula)) {
                return leitor;
            }
        }

        return null;
    }

    // Realiza um empréstimo
    public boolean emprestar(String titulo, String matricula) {

        Livro livro = buscarLivro(titulo);
        Leitor leitor = buscarLeitor(matricula);

        // Se livro ou leitor não existem
        if (livro == null || leitor == null) {
            return false;
        }

        Emprestimo novo = new Emprestimo(livro, leitor);

        // Tenta realizar o empréstimo
        if (!novo.realizarEmprestimo()) {
            return false;
        }

        emprestimos.add(novo);

        return true;
    }

    // Registra uma devolução pelo título do livro
    public boolean devolver(String titulo) {

        for (int i = 0; i < emprestimos.size(); i++) {

            Emprestimo e = emprestimos.get(i);

            if (e.estaAtivo()
                    && e.getLivro().getTitulo().equals(titulo)) {

                return e.registrarDevolucao();
            }
        }

        return false;
    }

    // Lista os empréstimos
    public void listarEmprestimos() {

        for (int i = 0; i < emprestimos.size(); i++) {
            System.out.println(emprestimos.get(i));
        }
    }
}