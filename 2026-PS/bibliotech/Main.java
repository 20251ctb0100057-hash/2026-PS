/*
 * Disciplina: 2026-PS
 * Projeto   : bibliotech
 * Arquivo   : Main.java
 * Autor     : Yuri
 * Descricao : BiblioTech v0.2 (Aula 37): as classes do diagrama existem
 *             e se apresentam. O menu chega na Aula 39.
 */
public class Main {

    public static void main(String[] args) {

        System.out.println("BiblioTech v0.2 - as classes existem");

        Livro l1 = new Livro("Dom Casmurro", "Machado de Assis", 1899);
        Livro l2 = new Livro("Capitaes da Areia", "Jorge Amado", 1937);

        System.out.println(l1);
        System.out.println(l2);

        l1.emprestar();

        System.out.println("Depois do emprestimo: " + l1);
        System.out.println("Dom Casmurro disponivel? " + l1.estaDisponivel());
    }
}