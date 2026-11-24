public class TesteSingleton {

    public static void main(String[] args) {

        ConfiguracaoSistema config1 =
            ConfiguracaoSistema.getInstancia();

        ConfiguracaoSistema config2 =
            ConfiguracaoSistema.getInstancia();

        System.out.println(
            config1 == config2
        );

        config1.setNome("BiblioTech 2026");

        System.out.println(
            config2.getNome()
        );
    }
}
