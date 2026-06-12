import java.util.Random;
import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        Random random = new Random();

        double total = 0;
        boolean comprando = true;
        String resumo = "";

        while (comprando) {

            System.out.println("\n╔════════════════════════════════════╗");
            System.out.println("║           FAST FOOD IFPR           ║");
            System.out.println("╠════════════════════════════════════╣");
            System.out.println("║  1 - X-Burguer      ..... R$ 18,00 ║");
            System.out.println("║  2 - Pizza          ..... R$ 35,00 ║");
            System.out.println("║  3 - Batata Frita   ..... R$ 12,00 ║");
            System.out.println("║  4 - Refrigerante   ..... R$  8,00 ║");
            System.out.println("║  5 - Sorvete        ..... R$ 10,00 ║");
            System.out.println("║  6 - X-Bacon        ..... R$ 22,00 ║");
            System.out.println("║  7 - Hot Dog        ..... R$ 15,00 ║");
            System.out.println("║  8 - Nuggets        ..... R$ 17,00 ║");
            System.out.println("║  9 - Milk Shake     ..... R$ 14,00 ║");
            System.out.println("║ 10 - Suco Natural   ..... R$  9,00 ║");
            System.out.println("║ 11 - Combo Família  ..... R$ 55,00 ║");
            System.out.println("║ 12 - Torta Doce     ..... R$ 13,00 ║");
            System.out.println("║ 13 - Finalizar Pedido              ║");
            System.out.println("╚════════════════════════════════════╝");

            System.out.print("\nEscolha uma opção: ");
            int opcao = entrada.nextInt();

            String produto = "";
            double preco = 0;

            switch (opcao) {

                case 1:
                    produto = "X-Burguer";
                    preco = 18.0;
                    break;

                case 2:
                    produto = "Pizza";
                    preco = 35.0;
                    break;

                case 3:
                    produto = "Batata Frita";
                    preco = 12.0;
                    break;

                case 4:
                    produto = "Refrigerante";
                    preco = 8.0;
                    break;

                case 5:
                    produto = "Sorvete";
                    preco = 10.0;
                    break;

                case 6:
                    produto = "X-Bacon";
                    preco = 22.0;
                    break;

                case 7:
                    produto = "Hot Dog";
                    preco = 15.0;
                    break;

                case 8:
                    produto = "Nuggets";
                    preco = 17.0;
                    break;

                case 9:
                    produto = "Milk Shake";
                    preco = 14.0;
                    break;

                case 10:
                    produto = "Suco Natural";
                    preco = 9.0;
                    break;

                case 11:
                    produto = "Combo Família";
                    preco = 55.0;
                    break;

                case 12:
                    produto = "Torta Doce";
                    preco = 13.0;
                    break;

                case 13:
                    comprando = false;
                    continue;

                default:
                    System.out.println("\n❌ Opção inválida!");
                    continue;
            }

            System.out.println("\n════════════════════════════════════");
            System.out.println("Produto selecionado: " + produto);
            System.out.printf("Valor unitário: R$ %.2f%n", preco);

            System.out.println("Digite 0 para voltar ao cardápio.");
            System.out.print("Quantidade: ");
            int quantidade = entrada.nextInt();

            if (quantidade == 0) {
                continue;
            }

            double subtotal = preco * quantidade;
            total += subtotal;

            resumo += String.format("%dx %-15s R$ %.2f%n",
                    quantidade, produto, subtotal);

            System.out.println("\n✔ Item adicionado ao pedido!");

            System.out.println("\nDeseja continuar comprando?");
            System.out.println("1 - Sim");
            System.out.println("2 - Finalizar");

            System.out.print("Escolha: ");
            int continuar = entrada.nextInt();

            if (continuar == 2) {
                comprando = false;
            }
        }

        System.out.println("\n╔════════════════════════════════════╗");
        System.out.println("║          RESUMO DO PEDIDO          ║");
        System.out.println("╠════════════════════════════════════╣");

        if (!resumo.isEmpty()) {
            System.out.print(resumo);
        }

        System.out.println("╠════════════════════════════════════╣");
        System.out.printf("TOTAL: R$ %.2f%n", total);
        System.out.println("╚════════════════════════════════════╝");

        System.out.println("\n╔════════════════════════════════════╗");
        System.out.println("║       FORMA DE PAGAMENTO           ║");
        System.out.println("╠════════════════════════════════════╣");
        System.out.println("║ 1 - Dinheiro                       ║");
        System.out.println("║ 2 - Cartão                         ║");
        System.out.println("║ 3 - PIX                            ║");
        System.out.println("╚════════════════════════════════════╝");

        System.out.print("\nEscolha: ");
        int pagamento = entrada.nextInt();

        if (pagamento >= 1 && pagamento <= 3) {

            int numeroPedido = random.nextInt(900) + 100;

            System.out.println("\n╔════════════════════════════════════╗");
            System.out.println("║      PAGAMENTO APROVADO            ║");
            System.out.println("╠════════════════════════════════════╣");
            System.out.printf("║ Pedido Nº %-24d║%n", numeroPedido);
            System.out.println("║ Aguarde a chamada do pedido.       ║");
            System.out.println("╚════════════════════════════════════╝");

        } else {

            System.out.println("\n❌ Forma de pagamento inválida.");
        }

        entrada.close();
    }
}