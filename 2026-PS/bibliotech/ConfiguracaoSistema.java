public final class ConfiguracaoSistema {

    private static final ConfiguracaoSistema
        INSTANCIA = new ConfiguracaoSistema();

    private String nome = "BiblioTech";

    private ConfiguracaoSistema() {
    }

    public static ConfiguracaoSistema
            getInstancia() {

        return INSTANCIA;
    }

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }
}