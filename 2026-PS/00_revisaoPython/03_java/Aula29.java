import java.util.ArrayList;

// Media da turma //
public class Aula29 {
    public static double calcularMedia(double[] notas) {
        double soma = 0;
        for (double nota : notas) {
            soma += nota;
        }
        return soma / notas.length;
    }

    // Contar Aprovados //
    public static int contarAprovados(double[] notas) {
        int aprovados = 0;
        for (double nota : notas) {
            if (nota >= 6.0) {
                aprovados++;
            }
        }
        return aprovados;
    }
    
    // Catálogo dos Produtos ArrayList//
    public static void adicionarProduto(ArrayList<String> lista, String nome) {
        lista.add(nome);
    }

    public static void listarProdutos(ArrayList<String> lista) {
        for (int i = 0; i < lista.size(); i++) {
            System.out.println((i + 1) + " - " + lista.get(i));
        }
    }

    // Maior Valor com sobrecarga //
    public static int maiorValor(int[] valores) {
        int maior = valores[0];
        for (int valor : valores) {
            if (valor > maior) {
                maior = valor;
            }
        }
        return maior;
    }

    public static int maiorValor(int a, int b) {
        return Math.max(a, b);
    }

    // Boletim com Integrador //
    public static void exibirBoletim(double[] notas) {
        double media = calcularMedia(notas);
        int aprovados = contarAprovados(notas);
        String situacao = (media >= 6.0) ? "APROVADA" : "EM RECUPERAÇÃO";

        System.out.printf("Média: %.2f%n", media);
        System.out.println("Aprovados: " + aprovados);
        System.out.println("Situação: " + situacao);
    }
}