/*
 * Disciplina: 2026-PS
 * Projeto   : bibliotech
 * Arquivo   : Bibliotecario.java
 * Autor     : seu nome
 * Descricao : Bibliotecario E UM TIPO DE Usuario, com a matricula funcional.
 */
public class Bibliotecario extends Usuario {

    private String matriculaFuncional;

    public Bibliotecario(String nome, String matricula, String matriculaFuncional) {
        super(nome, matricula);
        this.matriculaFuncional = matriculaFuncional;
    }

    public String getMatriculaFuncional() {
        return matriculaFuncional;
    }

    // OPERACAO DA CAIXA: consultarAcervo(). Em construcao: o acervo
    // de livros so existe a partir da Aula 39. Por enquanto, sempre pode.
    public boolean consultarAcervo() {
        return true;
    }

    public String toString() {
        return "Bibliotecario(a) " + getNome() + " (" + getMatricula()
               + ", funcional " + matriculaFuncional + ")";
    }
}