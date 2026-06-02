import java.util.Scanner;

public class CardapioRestaurante {

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);

        String[] itens = {
            "X-Burguer",
            "Pizza",
            "Suco Natural",
            "Café",
            "Salada"
        };

        double[] precos = {
            18.00,
            35.00,
            8.00,
            5.00,
            12.50
        };

        System.out.println("#######################");
        System.out.println("     RESTAURANTE DELÍCIAS");
        System.out.println("#######################");
        for (int i = 0; i < itens.length; i++) {
            System.out.printf("%d - %-15s R$ %.2f\n", i + 1, itens[i], precos[i]);
        }
        System.out.println("#######################");

        System.out.print("Escolha uma opção: ");
        int opcao = entrada.nextInt();

        if (opcao >= 1 && opcao <= itens.length) {
            String itemEscolhido = itens[opcao - 1];
            double precoItem = precos[opcao - 1];

            System.out.print("Quantos " + itemEscolhido + " deseja? ");
            int quantidade = entrada.nextInt();

            double total = precoItem * quantidade;

            System.out.println("#######################");
            System.out.println("Resumo do pedido:");
            System.out.printf("%d x %s - R$ %.2f cada\n", quantidade, itemEscolhido, precoItem);
            System.out.printf("TOTAL: R$ %.2f\n", total);
            System.out.println("#######################");

        } else {
            System.out.println("Opção inválida.");
        }
        entrada.close();
    }
}