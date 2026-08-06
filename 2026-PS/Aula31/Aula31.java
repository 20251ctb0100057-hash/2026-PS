/*Yuri Gonçalves Leuch
Exercicios com java: Menor valor, Maior valor, Contar acima e Soma - Float, int, double

 Para o Double e Float, é só substituir o int pelo nome deles, ou seja, ao inves de int contarAcima, basta colocar double contarAcima, ou float. Escolhi fazer o for da maneira mais rapida, e nao na tradicional.
*/
    // 1 - Calcula Soma

    int calculaSoma(int[] num) {

        int soma = 0;

        for (int n : num) {
            soma += n;
        }

        return soma;
    }

    // 2 - Calcula Média

     int calculaMedia(int[] num) {

        int soma = 0;

        for (int n : num) {
            soma += n;
        }

        return soma / num.length;
    }

    // 3 - Menor Valor
    int menorValor(int[] num) {

        int menor = num[0];

        for (int n : num) {
            if (n < menor) {
                menor = n;
            }
        }

        return menor;
    }

    // 4 - Maior Valor
    int maiorValor(int[] num) {

        int maior = num[0];

        for (int n : num) {
            if (n > maior) {
                maior = n;
            }
        }

        return maior;
    }

    // 5 - Contar Acima
    int contarAcima(int[] num, int limite) {

        int contador = 0;

        for (int n : num) {
            if (n > limite) {
                contador++;
            }
        }

        return contador;
    }

}

