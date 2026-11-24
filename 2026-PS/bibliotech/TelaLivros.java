import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardCopyOption;
import java.util.List;

public class TelaLivros extends JFrame {

    private final LivroDAO dao = new LivroDAO();

    private final DefaultTableModel modelo;
    private final JTable tabela;

    private final JTextField campoId = new JTextField(8);
    private final JTextField campoTitulo = new JTextField(18);
    private final JLabel status = new JLabel("Pronto.");

    private final Color AZUL_ESCURO = new Color(20, 35, 60);
    private final Color AZUL = new Color(37, 99, 235);
    private final Color AZUL_CLARO = new Color(239, 246, 255);
    private final Color FUNDO = new Color(245, 247, 250);
    private final Color TEXTO = new Color(40, 50, 65);

    public TelaLivros() {

        setTitle("BiblioTech - Consulta e Gestão de Livros");
        setSize(1100, 650);
        setMinimumSize(new Dimension(900, 550));
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

        getContentPane().setBackground(FUNDO);
        setLayout(new BorderLayout());

        modelo = new DefaultTableModel(
            new Object[]{"ID", "Capa", "Título", "Autor", "Ano"}, 0
        ) {
            @Override
            public boolean isCellEditable(int linha, int coluna) {
                return false;
            }
        };

        tabela = new JTable(modelo);

        configurarTabela();

        JPanel principal = new JPanel(new BorderLayout(0, 15));
        principal.setBackground(FUNDO);
        principal.setBorder(
            BorderFactory.createEmptyBorder(18, 22, 10, 22)
        );

        principal.add(criarCabecalho(), BorderLayout.NORTH);
        principal.add(criarAreaTabela(), BorderLayout.CENTER);

        add(principal, BorderLayout.CENTER);
        add(criarRodape(), BorderLayout.SOUTH);

        tabela.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                if (e.getClickCount() == 2) {
                    abrirDetalhesLivro();
                }
            }
        });

        carregarLivros();
    }

    private JPanel criarCabecalho() {

        JPanel painel = new JPanel(new BorderLayout(0, 15));
        painel.setBackground(FUNDO);

        JPanel cabecalho = new JPanel(new BorderLayout());
        cabecalho.setBackground(AZUL_ESCURO);
        cabecalho.setBorder(
            BorderFactory.createEmptyBorder(20, 25, 20, 25)
        );

        JLabel titulo = new JLabel("BiblioTech");
        titulo.setFont(new Font("SansSerif", Font.BOLD, 27));
        titulo.setForeground(Color.WHITE);

        JLabel subtitulo = new JLabel(
            "CONSULTA E GERENCIAMENTO DE LIVROS"
        );
        subtitulo.setFont(new Font("SansSerif", Font.PLAIN, 11));
        subtitulo.setForeground(new Color(190, 205, 225));

        JPanel textos = new JPanel();
        textos.setLayout(new BoxLayout(textos, BoxLayout.Y_AXIS));
        textos.setOpaque(false);
        textos.add(titulo);
        textos.add(Box.createVerticalStrut(5));
        textos.add(subtitulo);

        cabecalho.add(textos, BorderLayout.WEST);

        JLabel identificacao = new JLabel("CATÁLOGO");
        identificacao.setFont(new Font("SansSerif", Font.BOLD, 12));
        identificacao.setForeground(new Color(180, 205, 255));

        cabecalho.add(identificacao, BorderLayout.EAST);

        painel.add(cabecalho, BorderLayout.NORTH);
        painel.add(criarPainelControles(), BorderLayout.CENTER);

        return painel;
    }

    private JPanel criarPainelControles() {

        JPanel painel = new JPanel(new BorderLayout(10, 10));
        painel.setBackground(Color.WHITE);
        painel.setBorder(
            BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(new Color(225, 230, 238)),
                BorderFactory.createEmptyBorder(15, 15, 15, 15)
            )
        );

        JPanel pesquisas = new JPanel(
            new FlowLayout(FlowLayout.LEFT, 10, 5)
        );
        pesquisas.setBackground(Color.WHITE);

        JLabel labelId = new JLabel("ID:");
        JLabel labelTitulo = new JLabel("Título:");

        estilizarLabel(labelId);
        estilizarLabel(labelTitulo);

        estilizarCampo(campoId);
        estilizarCampo(campoTitulo);

        JButton buscar = criarBotao("Buscar por ID", AZUL);
        JButton buscarTitulo = criarBotao("Buscar por título", AZUL);

        pesquisas.add(labelId);
        pesquisas.add(campoId);
        pesquisas.add(buscar);
        pesquisas.add(Box.createHorizontalStrut(15));
        pesquisas.add(labelTitulo);
        pesquisas.add(campoTitulo);
        pesquisas.add(buscarTitulo);

        JPanel acoes = new JPanel(
            new FlowLayout(FlowLayout.LEFT, 10, 5)
        );
        acoes.setBackground(Color.WHITE);

        JButton limpar = criarBotao(
            "Limpar", new Color(100, 116, 139)
        );

        JButton atualizar = criarBotao(
            "Atualizar listagem", AZUL
        );

        JButton mostrarTodos = criarBotao(
            "Mostrar todos", new Color(16, 140, 105)
        );

        JButton selecionarCapa = criarBotao(
            "Selecionar capa", new Color(124, 58, 237)
        );

        JButton detalhes = criarBotao(
            "Ver detalhes", new Color(14, 116, 144)
        );

        acoes.add(limpar);
        acoes.add(atualizar);
        acoes.add(mostrarTodos);
        acoes.add(selecionarCapa);
        acoes.add(detalhes);

        painel.add(pesquisas, BorderLayout.NORTH);
        painel.add(acoes, BorderLayout.CENTER);

        buscar.addActionListener(e -> buscarLivro());
        buscarTitulo.addActionListener(e -> buscarPorTitulo());

        campoId.addActionListener(e -> buscarLivro());
        campoTitulo.addActionListener(e -> buscarPorTitulo());

        limpar.addActionListener(e -> {
            campoId.setText("");
            campoTitulo.setText("");
            carregarLivros();
            status.setText("Campos limpos. Listagem restaurada.");
        });

        atualizar.addActionListener(e -> carregarLivros());

        mostrarTodos.addActionListener(e -> {
            campoId.setText("");
            campoTitulo.setText("");
            carregarLivros();
        });

        selecionarCapa.addActionListener(e -> selecionarCapa());

        detalhes.addActionListener(e -> abrirDetalhesLivro());

        return painel;
    }

    private JPanel criarAreaTabela() {

        JPanel painel = new JPanel(new BorderLayout(0, 10));
        painel.setBackground(FUNDO);

        JLabel titulo = new JLabel("  Livros cadastrados");
        titulo.setFont(new Font("SansSerif", Font.BOLD, 17));
        titulo.setForeground(AZUL_ESCURO);

        JScrollPane scroll = new JScrollPane(tabela);
        scroll.setBorder(
            BorderFactory.createLineBorder(new Color(220, 226, 235))
        );
        scroll.getViewport().setBackground(Color.WHITE);

        painel.add(titulo, BorderLayout.NORTH);
        painel.add(scroll, BorderLayout.CENTER);

        return painel;
    }

    private void configurarTabela() {

        tabela.setRowHeight(90);
        tabela.setFont(new Font("SansSerif", Font.PLAIN, 13));
        tabela.setForeground(TEXTO);
        tabela.setBackground(Color.WHITE);
        tabela.setSelectionBackground(new Color(219, 234, 254));
        tabela.setSelectionForeground(AZUL_ESCURO);
        tabela.setGridColor(new Color(230, 235, 242));
        tabela.setShowVerticalLines(false);
        tabela.setShowHorizontalLines(true);
        tabela.setIntercellSpacing(new Dimension(0, 1));
        tabela.setFillsViewportHeight(true);
        tabela.setAutoCreateRowSorter(true);

        tabela.getTableHeader().setFont(
            new Font("SansSerif", Font.BOLD, 13)
        );
        tabela.getTableHeader().setBackground(AZUL_ESCURO);
        tabela.getTableHeader().setForeground(Color.WHITE);
        tabela.getTableHeader().setPreferredSize(
            new Dimension(0, 42)
        );
        tabela.getTableHeader().setReorderingAllowed(false);

        tabela.getColumnModel().getColumn(0).setPreferredWidth(55);
        tabela.getColumnModel().getColumn(1).setPreferredWidth(100);
        tabela.getColumnModel().getColumn(2).setPreferredWidth(350);
        tabela.getColumnModel().getColumn(3).setPreferredWidth(280);
        tabela.getColumnModel().getColumn(4).setPreferredWidth(80);

        tabela.getColumnModel().getColumn(1).setCellRenderer(
            new DefaultTableCellRenderer() {

                @Override
                public Component getTableCellRendererComponent(
                    JTable tabela, Object valor,
                    boolean selecionada, boolean foco,
                    int linha, int coluna
                ) {

                    JLabel label = new JLabel();
                    label.setHorizontalAlignment(JLabel.CENTER);
                    label.setVerticalAlignment(JLabel.CENTER);
                    label.setOpaque(true);

                    label.setBackground(
                        selecionada
                        ? tabela.getSelectionBackground()
                        : (linha % 2 == 0 ? Color.WHITE : AZUL_CLARO)
                    );

                    if (valor instanceof ImageIcon) {
                        label.setIcon((ImageIcon) valor);
                        label.setText("");
                    } else {
                        label.setIcon(null);
                        label.setText("Sem capa");
                        label.setForeground(new Color(140, 150, 165));
                        label.setFont(
                            new Font("SansSerif", Font.ITALIC, 11)
                        );
                    }

                    return label;
                }
            }
        );

        DefaultTableCellRenderer renderizador =
            new DefaultTableCellRenderer() {

                @Override
                public Component getTableCellRendererComponent(
                    JTable tabela, Object valor,
                    boolean selecionada, boolean foco,
                    int linha, int coluna
                ) {

                    Component componente =
                        super.getTableCellRendererComponent(
                            tabela, valor, selecionada, foco,
                            linha, coluna
                        );

                    componente.setBackground(
                        selecionada
                        ? tabela.getSelectionBackground()
                        : (linha % 2 == 0 ? Color.WHITE : AZUL_CLARO)
                    );

                    componente.setForeground(TEXTO);

                    setBorder(
                        BorderFactory.createEmptyBorder(5, 12, 5, 12)
                    );

                    return componente;
                }
            };

        for (int i = 0; i < tabela.getColumnCount(); i++) {
            if (i != 1) {
                tabela.getColumnModel()
                    .getColumn(i)
                    .setCellRenderer(renderizador);
            }
        }
    }

    private JPanel criarRodape() {

        JPanel painel = new JPanel(new BorderLayout());
        painel.setBackground(AZUL_ESCURO);
        painel.setBorder(
            BorderFactory.createEmptyBorder(12, 22, 12, 22)
        );

        status.setFont(new Font("SansSerif", Font.PLAIN, 12));
        status.setForeground(Color.WHITE);

        painel.add(status, BorderLayout.WEST);

        JLabel rodape = new JLabel("BiblioTech");
        rodape.setFont(new Font("SansSerif", Font.BOLD, 12));
        rodape.setForeground(new Color(190, 205, 225));

        painel.add(rodape, BorderLayout.EAST);

        return painel;
    }

    private JButton criarBotao(String texto, Color cor) {

        JButton botao = new JButton(texto);
        botao.setFont(new Font("SansSerif", Font.BOLD, 12));
        botao.setForeground(Color.WHITE);
        botao.setBackground(cor);
        botao.setFocusPainted(false);
        botao.setBorderPainted(false);
        botao.setOpaque(true);
        botao.setCursor(new Cursor(Cursor.HAND_CURSOR));
        botao.setBorder(
            BorderFactory.createEmptyBorder(10, 14, 10, 14)
        );

        return botao;
    }

    private void estilizarCampo(JTextField campo) {

        campo.setFont(new Font("SansSerif", Font.PLAIN, 13));
        campo.setForeground(TEXTO);
        campo.setBackground(Color.WHITE);
        campo.setCaretColor(AZUL);

        campo.setBorder(
            BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(
                    new Color(205, 215, 230)
                ),
                BorderFactory.createEmptyBorder(8, 9, 8, 9)
            )
        );
    }

    private void estilizarLabel(JLabel label) {
        label.setFont(new Font("SansSerif", Font.BOLD, 12));
        label.setForeground(TEXTO);
    }

    private void carregarLivros() {

        modelo.setRowCount(0);

        try {

            List<Livro> livros = dao.listarLivros();

            for (Livro livro : livros) {
                adicionarLinha(livro);
            }

            status.setText(
                "Livros encontrados: " + livros.size()
            );

        } catch (PersistenciaException e) {

            status.setText("Erro ao consultar o banco.");

            System.err.println(e.getMessage());
            e.printStackTrace();

            JOptionPane.showMessageDialog(
                this,
                "Não foi possível carregar os livros. " +
                "Verifique a conexão com o MariaDB.",
                "Erro de conexão",
                JOptionPane.ERROR_MESSAGE
            );
        }
    }

    private ImageIcon carregarMiniatura(String caminho) {

        if (caminho == null || caminho.isBlank()) {
            return null;
        }

        File arquivo = new File(caminho);

        if (!arquivo.isFile()) {
            return null;
        }

        try {

            java.awt.image.BufferedImage imagem =
                javax.imageio.ImageIO.read(arquivo);

            if (imagem == null) {
                return null;
            }

            Image reduzida = imagem.getScaledInstance(
                55, 75, Image.SCALE_SMOOTH
            );

            return new ImageIcon(reduzida);

        } catch (IOException e) {
            return null;
        }
    }

    private void adicionarLinha(Livro livro) {

        modelo.addRow(new Object[]{
            livro.getId(),
            carregarMiniatura(livro.getCapa()),
            livro.getTitulo(),
            livro.getAutor(),
            livro.getAno()
        });
    }

    private void buscarLivro() {

        String texto = campoId.getText().trim();

        if (texto.isEmpty()) {
            JOptionPane.showMessageDialog(
                this, "Informe um ID para buscar."
            );
            return;
        }

        int id;

        try {

            id = Integer.parseInt(texto);

            if (id <= 0) {
                throw new IllegalArgumentException(
                    "O ID deve ser positivo."
                );
            }

        } catch (NumberFormatException e) {

            JOptionPane.showMessageDialog(
                this,
                "Informe um número inteiro válido."
            );

            return;

        } catch (IllegalArgumentException e) {

            JOptionPane.showMessageDialog(
                this,
                e.getMessage()
            );

            return;
        }

        Livro livro = dao.buscarLivroPorId(id);
        modelo.setRowCount(0);

        if (livro == null) {
            status.setText("Nenhum livro encontrado para o ID " + id);
            JOptionPane.showMessageDialog(this, "Livro não encontrado.");
        } else {
            adicionarLinha(livro);
            status.setText("Livro encontrado pelo ID: " + id);
        }
    }

    private void buscarPorTitulo() {

        String titulo = campoTitulo.getText().trim();

        if (titulo.isEmpty()) {
            JOptionPane.showMessageDialog(
                this,
                "Informe o título do livro.",
                "Campo obrigatório",
                JOptionPane.WARNING_MESSAGE
            );
            return;
        }

        List<Livro> livros = dao.buscarLivrosPorTitulo(titulo);
        modelo.setRowCount(0);

        for (Livro livro : livros) {
            adicionarLinha(livro);
        }

        status.setText(
            "Livros encontrados pelo título: " + livros.size()
        );

        if (livros.isEmpty()) {
            JOptionPane.showMessageDialog(this, "Nenhum livro encontrado.");
        }
    }

    // Seleciona e salva uma imagem para a capa do livro
    private void selecionarCapa() {

        int linhaSelecionada = tabela.getSelectedRow();

        if (linhaSelecionada == -1) {
            JOptionPane.showMessageDialog(
                this,
                "Selecione um livro na tabela primeiro.",
                "Aviso",
                JOptionPane.WARNING_MESSAGE
            );
            return;
        }

        int linhaModelo =
            tabela.convertRowIndexToModel(linhaSelecionada);

        int id = (int) modelo.getValueAt(linhaModelo, 0);

        JFileChooser seletor = new JFileChooser();

        FileNameExtensionFilter filtro =
            new FileNameExtensionFilter(
                "Imagens (*.jpg, *.jpeg, *.png)",
                "jpg", "jpeg", "png"
            );

        seletor.setFileFilter(filtro);

        int resultado = seletor.showOpenDialog(this);

        if (resultado != JFileChooser.APPROVE_OPTION) {
            return;
        }

        File arquivo = seletor.getSelectedFile();
        String nome = arquivo.getName();
        int ponto = nome.lastIndexOf(".");

        if (ponto == -1) {
            JOptionPane.showMessageDialog(
                this,
                "Arquivo sem extensão válida.",
                "Imagem inválida",
                JOptionPane.WARNING_MESSAGE
            );
            return;
        }

        String extensao =
            nome.substring(ponto + 1).toLowerCase();

        if (!extensao.matches("jpg|jpeg|png")) {
            JOptionPane.showMessageDialog(
                this,
                "Selecione uma imagem JPG, JPEG ou PNG."
            );
            return;
        }

        try {

            Path pasta = Path.of("imagens", "livros");
            Files.createDirectories(pasta);

            String nomeArquivo = "livro_" + id + "." + extensao;
            Path destino = pasta.resolve(nomeArquivo);

            Files.copy(
                arquivo.toPath(),
                destino,
                StandardCopyOption.REPLACE_EXISTING
            );

            boolean atualizado =
                dao.atualizarCapa(id, destino.toString());

            if (atualizado) {

                carregarLivros();

                status.setText(
                    "Capa atualizada para o livro ID: " + id
                );

                JOptionPane.showMessageDialog(
                    this,
                    "Capa salva na pasta imagens/livros!"
                );

            } else {

                JOptionPane.showMessageDialog(
                    this,
                    "Não foi possível atualizar a capa no banco.",
                    "Erro",
                    JOptionPane.ERROR_MESSAGE
                );
            }

        } catch (IOException e) {

            JOptionPane.showMessageDialog(
                this,
                "Erro ao copiar a imagem: " + e.getMessage(),
                "Erro",
                JOptionPane.ERROR_MESSAGE
            );

            e.printStackTrace();
        }
    }

    // =====================================================
    // SEGUNDA TELA: DETALHES DO LIVRO
    // =====================================================

    private void abrirDetalhesLivro() {

        int linhaSelecionada = tabela.getSelectedRow();

        if (linhaSelecionada == -1) {
            JOptionPane.showMessageDialog(
                this,
                "Selecione um livro na tabela primeiro.",
                "Nenhum livro selecionado",
                JOptionPane.WARNING_MESSAGE
            );
            return;
        }

        int linhaModelo =
            tabela.convertRowIndexToModel(linhaSelecionada);

        int id = (int) modelo.getValueAt(linhaModelo, 0);

        Livro livro = dao.buscarLivroPorId(id);

        if (livro == null) {
            JOptionPane.showMessageDialog(
                this, "Não foi possível encontrar esse livro."
            );
            return;
        }

        JFrame janela = new JFrame("BiblioTech - Detalhes do Livro");

        janela.setSize(720, 480);
        janela.setMinimumSize(new Dimension(650, 430));
        janela.setLocationRelativeTo(this);
        janela.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        janela.setLayout(new BorderLayout());

        Color fundo = new Color(245, 247, 250);
        Color azul = new Color(20, 35, 60);

        janela.getContentPane().setBackground(fundo);

        JPanel cabecalho = new JPanel(new BorderLayout());
        cabecalho.setBackground(azul);
        cabecalho.setBorder(
            BorderFactory.createEmptyBorder(22, 28, 22, 28)
        );

        JLabel titulo = new JLabel("Detalhes do livro");
        titulo.setFont(new Font("SansSerif", Font.BOLD, 25));
        titulo.setForeground(Color.WHITE);

        JLabel subtitulo = new JLabel(
            "INFORMAÇÕES COMPLETAS DA OBRA"
        );
        subtitulo.setFont(new Font("SansSerif", Font.PLAIN, 11));
        subtitulo.setForeground(new Color(190, 205, 225));

        JPanel textos = new JPanel();
        textos.setLayout(new BoxLayout(textos, BoxLayout.Y_AXIS));
        textos.setOpaque(false);
        textos.add(titulo);
        textos.add(Box.createVerticalStrut(5));
        textos.add(subtitulo);

        cabecalho.add(textos, BorderLayout.WEST);

        JPanel conteudo = new JPanel(new BorderLayout(30, 10));
        conteudo.setBackground(Color.WHITE);
        conteudo.setBorder(
            BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(
                    new Color(225, 230, 238)
                ),
                BorderFactory.createEmptyBorder(25, 25, 25, 25)
            )
        );

        JLabel capa = new JLabel();
        capa.setHorizontalAlignment(JLabel.CENTER);
        capa.setVerticalAlignment(JLabel.CENTER);
        capa.setPreferredSize(new Dimension(190, 270));
        capa.setOpaque(true);
        capa.setBackground(new Color(239, 246, 255));

        ImageIcon imagem = carregarCapaGrande(livro.getCapa());

        if (imagem != null) {
            capa.setIcon(imagem);
        } else {
            capa.setText("Sem capa disponível");
            capa.setFont(
                new Font("SansSerif", Font.ITALIC, 12)
            );
            capa.setForeground(new Color(130, 145, 165));
        }

        JPanel painelCapa = new JPanel(new BorderLayout());
        painelCapa.setBackground(Color.WHITE);
        painelCapa.add(capa, BorderLayout.CENTER);

        JPanel informacoes = new JPanel();
        informacoes.setLayout(
            new BoxLayout(informacoes, BoxLayout.Y_AXIS)
        );
        informacoes.setBackground(Color.WHITE);

        JLabel identificacao = new JLabel(
            "LIVRO Nº " + livro.getId()
        );
        identificacao.setFont(
            new Font("SansSerif", Font.BOLD, 12)
        );
        identificacao.setForeground(new Color(37, 99, 235));

        JLabel nomeLivro = new JLabel(livro.getTitulo());
        nomeLivro.setFont(
            new Font("SansSerif", Font.BOLD, 23)
        );
        nomeLivro.setForeground(azul);

        JLabel linha = new JLabel(
            "________________________________"
        );
        linha.setForeground(new Color(220, 226, 235));

        JLabel autor = criarInformacao(
            "AUTOR", livro.getAutor()
        );

        JLabel ano = criarInformacao(
            "ANO DE PUBLICAÇÃO",
            String.valueOf(livro.getAno())
        );

        JLabel idLivro = criarInformacao(
            "IDENTIFICADOR",
            String.valueOf(livro.getId())
        );

        informacoes.add(identificacao);
        informacoes.add(Box.createVerticalStrut(18));
        informacoes.add(nomeLivro);
        informacoes.add(Box.createVerticalStrut(15));
        informacoes.add(linha);
        informacoes.add(Box.createVerticalStrut(20));
        informacoes.add(autor);
        informacoes.add(Box.createVerticalStrut(20));
        informacoes.add(ano);
        informacoes.add(Box.createVerticalStrut(20));
        informacoes.add(idLivro);

        conteudo.add(painelCapa, BorderLayout.WEST);
        conteudo.add(informacoes, BorderLayout.CENTER);

        JPanel rodape = new JPanel(
            new FlowLayout(FlowLayout.RIGHT)
        );
        rodape.setBackground(fundo);
        rodape.setBorder(
            BorderFactory.createEmptyBorder(5, 20, 15, 20)
        );

        JButton fechar = criarBotao(
            "Voltar ao catálogo", AZUL
        );

        fechar.addActionListener(e -> janela.dispose());

        rodape.add(fechar);

        JPanel centro = new JPanel(new BorderLayout(0, 15));
        centro.setBackground(fundo);
        centro.setBorder(
            BorderFactory.createEmptyBorder(20, 25, 5, 25)
        );

        centro.add(conteudo, BorderLayout.CENTER);

        janela.add(cabecalho, BorderLayout.NORTH);
        janela.add(centro, BorderLayout.CENTER);
        janela.add(rodape, BorderLayout.SOUTH);

        janela.setVisible(true);
    }

    // Carrega uma capa em tamanho maior
    private ImageIcon carregarCapaGrande(String caminho) {

        if (caminho == null || caminho.isBlank()) {
            return null;
        }

        File arquivo = new File(caminho);

        if (!arquivo.isFile()) {
            return null;
        }

        try {

            java.awt.image.BufferedImage imagem =
                javax.imageio.ImageIO.read(arquivo);

            if (imagem == null) {
                return null;
            }

            int larguraOriginal = imagem.getWidth();
            int alturaOriginal = imagem.getHeight();

            double escala = Math.min(
                180.0 / larguraOriginal,
                260.0 / alturaOriginal
            );

            int largura = (int) (larguraOriginal * escala);
            int altura = (int) (alturaOriginal * escala);

            Image reduzida = imagem.getScaledInstance(
                largura, altura, Image.SCALE_SMOOTH
            );

            return new ImageIcon(reduzida);

        } catch (IOException e) {
            return null;
        }
    }

    // Cria os campos de informação da segunda tela
    private JLabel criarInformacao(String rotulo, String valor) {

        JLabel label = new JLabel(
            "<html><b>" + rotulo + "</b><br><br>"
            + valor + "</html>"
        );

        label.setFont(new Font("SansSerif", Font.PLAIN, 14));
        label.setForeground(new Color(55, 65, 80));

        return label;
    }

    public static void main(String[] args) {

        SwingUtilities.invokeLater(() -> {
            new TelaLivros().setVisible(true);
        });
    }
}