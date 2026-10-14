/*
 * Disciplina: 2026-PS
 * Projeto   : bibliotech
 * Arquivo   : Livro.java
 * Autor     : Yuri Gonçalves Leuch
 * Descricao : Representa um livro do sistema BiblioTech.
 */

public class Livro {

    private String titulo;
    private String autor;
    private int ano;
    private boolean disponivel;

    // Construtor
    public Livro(String titulo, String autor, int ano) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
        this.disponivel = true;
    }

    // Getters
    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }

    public int getAno() {
        return ano;
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
        String status = disponivel ? "disponivel" : "emprestado";

        return titulo + " (" + autor + ", " + ano + ") - " + status;
    }
}