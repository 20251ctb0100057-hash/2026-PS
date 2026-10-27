
/*
 * Disciplina: 2026-PS
 * Projeto   : bibliotech
 * Arquivo   : Livro.java
 * Autor     : Yuri Gonçalves Leuch
 * Descricao : Representa um livro do sistema BiblioTech.
 */

public class Livro {

    private int id;
    private String titulo;
    private String autor;
    private int ano;
    private boolean disponivel;

    // Construtor original
    public Livro(String titulo, String autor, int ano) {
        this.id = 0;
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.disponivel = true;
    }

    // Construtor com ID, utilizado nas consultas ao banco
    public Livro(int id, String titulo, String autor, int ano) {
        this.id = id;
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.disponivel = true;
    }

    // Getters
    public int getId() {
        return id;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public int getAno() {
        return ano;
    }

    // Setters
    public void setId(int id) {
        this.id = id;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    // Verifica se o livro está disponível
    public boolean estaDisponivel() {
        return disponivel;
    }

    // Mantém compatibilidade com códigos que usam isDisponivel()
    public boolean isDisponivel() {
        return disponivel;
    }

    // Empresta o livro
    public boolean emprestar() {
        if (disponivel) {
            disponivel = false;
            return true;
        }

        return false;
    }

    // Devolve o livro
    public boolean devolver() {
        if (!disponivel) {
            disponivel = true;
            return true;
        }

        return false;
    }

    @Override
    public String toString() {
        String status = disponivel ? "disponível" : "emprestado";

        return id + " - " + titulo + " (" + autor + ", " + ano
                + ") - " + status;
    }
}
