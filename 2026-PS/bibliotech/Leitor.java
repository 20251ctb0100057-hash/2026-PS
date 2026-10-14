/*
 * Disciplina: 2026-PS
 * Projeto   : bibliotech
 * Arquivo   : Leitor.java
 * Autor     : Yuri
 * Descricao : Leitor E UM TIPO DE Usuario: herda nome, matricula e entrar().
 */

public class Leitor extends Usuario {

    private int limiteEmprestimos;
    private int livrosEmMaos;

    public Leitor(String nome, String matricula, int limiteEmprestimos) {
        super(nome, matricula);
        this.limiteEmprestimos = limiteEmprestimos;
        this.livrosEmMaos = 0;
    }

    public int getLimiteEmprestimos() {
        return limiteEmprestimos;
    }

    public int getLivrosEmMaos() {
        return livrosEmMaos;
    }

    // Verifica se o leitor ainda pode pegar livros
    public boolean podePegarEmprestado() {
        return livrosEmMaos < limiteEmprestimos;
    }

    // Registra que o leitor pegou um livro
    public void pegouLivro() {
        livrosEmMaos++;
    }

    // Registra que o leitor devolveu um livro
    public void devolveuLivro() {
        if (livrosEmMaos > 0) {
            livrosEmMaos--;
        }
    }

    @Override
    public String toString() {
        return "Leitor " + getNome() +
                " (" + getMatricula() + ") - " +
                livrosEmMaos + " de " +
                limiteEmprestimos + " livros";
    }
}