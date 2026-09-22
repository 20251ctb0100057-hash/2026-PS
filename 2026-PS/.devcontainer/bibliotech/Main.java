/*
 * Disciplina: 2026-PS
 * Projeto   : bibliotech
 * Arquivo   : Main.java
 * Autor     : Yuri Gonçalves Leuch
 * Descricao : esqueleto do BiblioTech (Aula 36). Ainda nao faz nada:
 *             so prova que o ambiente compila e roda.
 */

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int opcao = -1;

        System.out.println("=========================================");
        System.out.println("       📚 BiblioTech - Sistema de Gestão ");
        System.out.println("=========================================");

        while (opcao != 0) {
            System.out.println("\n--- MENU PRINCIPAL ---");
            System.out.println("1 - Consultar Disponibilidade de Livro");
            System.out.println("2 - Emprestar Livro");
            System.out.println("3 - Devolver Livro");
            System.out.println("4 - Identificar Leitor");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opção: ");

            if (scanner.hasNextInt()) {
                opcao = scanner.nextInt();
                switch (opcao) {
                    case 1:
                        System.out.println("▶ [1 - Consultar Disponibilidade] - Em construção...");
                        break;
                    case 2:
                        System.out.println("▶ [2 - Emprestar Livro] - Em construção...");
                        break;
                    case 3:
                        System.out.println("▶ [3 - Devolver Livro] - Em construção...");
                        break;
                    case 4:
                        System.out.println("▶ [4 - Identificar Leitor] - Em construção...");
                        break;
                    case 0:
                        System.out.println("Encerrando o sistema BiblioTech. Até logo!");
                        break;
                    default:
                        System.out.println("⚠️ Opção inválida! Escolha um número do menu.");
                        break;
                }
            } else {
                System.out.println("⚠️ Entrada inválida! Digite apenas números.");
                scanner.next();
            }
        }
        scanner.close();
    }
}