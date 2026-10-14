/*
 * Disciplina: 2026-PS
 * Projeto   : bibliotech
 * Arquivo   : Emprestimo.java
 * Descricao : Representa um empréstimo realizado no sistema BiblioTech.
 * Autor     : Yuri Gonçalves Leuch
 */

public class Emprestimo {

    private Livro livro;
    private Leitor leitor;
    private boolean ativo;

    // Construtor
    public Emprestimo(Livro livro, Leitor leitor) {

        if (livro == null || leitor == null) {
            throw new IllegalArgumentException(
                    "Livro e leitor sao obrigatorios."
            );
        }

        this.livro = livro;
        this.leitor = leitor;
        this.ativo = false;
    }

    // Retorna o leitor
    public Leitor getLeitor() {
        return leitor;
    }

    // Retorna o livro
    public Livro getLivro() {
        return livro;
    }

    // Verifica se o empréstimo está ativo
    public boolean estaAtivo() {
        return ativo;
    }

    // Alias para manter compatibilidade com outros códigos
    public boolean isAtivo() {
        return ativo;
    }

    // Realiza o empréstimo
    public boolean realizarEmprestimo() {

        if (ativo) {
            return false;
        }

        if (!livro.isDisponivel()) {
            return false;
        }

        if (!leitor.podePegarEmprestado()) {
            return false;
        }

        if (!livro.emprestar()) {
            return false;
        }

        leitor.pegouLivro();
        ativo = true;

        return true;
    }

    // Registra a devolução
    public boolean registrarDevolucao() {

        if (!ativo) {
            return false;
        }

        if (!livro.devolver()) {
            return false;
        }

        leitor.devolveuLivro();
        ativo = false;

        return true;
    }

    // Alias para compatibilidade
    public void finalizarEmprestimo() {
        registrarDevolucao();
    }

    @Override
    public String toString() {

        String estado = ativo ? "Ativo" : "Finalizado";

        return "Leitor: " + leitor.getNome() +
                "\nLivro: " + livro.getTitulo() +
                "\nEstado do empréstimo: " + estado;
    }
}