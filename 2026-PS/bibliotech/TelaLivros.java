
import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.nio.file.Path;
import java.util.List;

public class TelaLivros extends JFrame {

    private final LivroDAO dao = new LivroDAO();

    private final DefaultTableModel modelo;
    private final JTable tabela;

    private final JTextField campoId = new JTextField(8);
    private final JTextField campoTitulo = new JTextField(18);
    private final JLabel status = new JLabel("Pronto.");

    public TelaLivros() {
        setTitle("BiblioTech - Consulta e Gestão de Livros");
        setSize(1000, 550);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        setLayout(new BorderLayout(8, 8));

        // Modelo da tabela com a nova coluna Capa
        modelo = new DefaultTableModel(
            new Object[]{
                "ID", "Capa", "Título", "Autor", "Ano"
            }, 0
        ) {
            @Override
            public boolean isCellEditable(int linha, int coluna) {
                return false;
            }
        };

        tabela = new JTable(modelo);

        // Configuração da apresentação das imagens
        tabela.setRowHeight(85);

        tabela.getColumnModel()
            .getColumn(1)
            .setPreferredWidth(90);

        tabela.getColumnModel()
            .getColumn(1)
            .setCellRenderer(
                new javax.swing.table.DefaultTableCellRenderer() {

                    @Override
                    public java.awt.Component getTableCellRendererComponent(
                            JTable tabela,
                            Object valor,
                            boolean selecionada,
                            boolean foco,
                            int linha,
                            int coluna) {

                        JLabel label = new JLabel();

                        label.setHorizontalAlignment(
                            JLabel.CENTER
                        );

                        label.setOpaque(true);

                        label.setBackground(
                            selecionada
                            ? tabela.getSelectionBackground()
                            : tabela.getBackground()
                        );

                        if (valor instanceof ImageIcon) {
                            label.setIcon((ImageIcon) valor);
                        } else {
                            label.setText("Sem capa");
                        }

                        return label;
                    }
                }
            );

        add(new JScrollPane(tabela), BorderLayout.CENTER);

        JPanel controles = new JPanel(new FlowLayout(FlowLayout.LEFT));

        JButton atualizar = new JButton("Atualizar listagem");
        JButton buscar = new JButton("Buscar por ID");
        JButton botaoBuscarTitulo = new JButton("Buscar por título");
        JButton botaoLimpar = new JButton("Limpar");
        JButton mostrarTodos = new JButton("Mostrar todos");
        JButton botaoCapa = new JButton("Selecionar capa");

        controles.add(new JLabel("ID:"));
        controles.add(campoId);
        controles.add(buscar);

        controles.add(new JLabel("Título:"));
        controles.add(campoTitulo);
        controles.add(botaoBuscarTitulo);

        controles.add(botaoLimpar);
        controles.add(atualizar);
        controles.add(mostrarTodos);
        controles.add(botaoCapa);

        add(controles, BorderLayout.NORTH);
        add(status, BorderLayout.SOUTH);

        atualizar.addActionListener(e -> carregarLivros());

        mostrarTodos.addActionListener(e -> {
            campoId.setText("");
            campoTitulo.setText("");
            carregarLivros();
        });

        buscar.addActionListener(e -> buscarLivro());
        botaoBuscarTitulo.addActionListener(e -> buscarPorTitulo());

        campoId.addActionListener(e -> buscarLivro());
        campoTitulo.addActionListener(e -> buscarPorTitulo());

        botaoLimpar.addActionListener(e -> {
            campoId.setText("");
            campoTitulo.setText("");
            carregarLivros();
            status.setText("Campos limpos. Listagem restaurada.");
        });

        botaoCapa.addActionListener(e -> selecionarCapa());

        carregarLivros();
    }

    // Carrega os livros com tratamento de exceção
    private void carregarLivros() {

        try {

            List<Livro> livros =
                dao.listarLivros();

            modelo.setRowCount(0);

            for (Livro livro : livros) {
                adicionarLinha(livro);
            }

            status.setText(
                "Livros encontrados: " + livros.size()
            );

        } catch (PersistenciaException e) {

            status.setText(
                "Erro ao consultar o banco."
            );

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

    // Carrega e redimensiona a imagem da capa
    private ImageIcon carregarMiniatura(String caminho) {

        if (caminho == null || caminho.isBlank()) {
            return null;
        }

        java.io.File arquivo = new java.io.File(caminho);

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

        } catch (java.io.IOException e) {
            return null;
        }
    }

    // Adiciona o livro e sua capa na tabela
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

        status.setText("Livros encontrados pelo título: " + livros.size());

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

        int linhaModelo = tabela.convertRowIndexToModel(linhaSelecionada);
        int idLivro = (int) modelo.getValueAt(linhaModelo, 0);

        JFileChooser seletor = new JFileChooser();

        FileNameExtensionFilter filtro =
            new FileNameExtensionFilter(
                "Imagens (*.jpg, *.jpeg, *.png)",
                "jpg", "jpeg", "png"
            );

        seletor.setFileFilter(filtro);

        int resultado = seletor.showOpenDialog(this);

        if (resultado == JFileChooser.APPROVE_OPTION) {

            File arquivo = seletor.getSelectedFile();
            Path arquivoSelecionado = arquivo.toPath();

            try {

                String caminho = ImagemLivro.salvar(
                    arquivoSelecionado, idLivro
                );

                System.out.println(
                    "Imagem salva em: " + caminho
                );

                boolean atualizado = dao.atualizarCapa(
                    idLivro, caminho
                );

                if (atualizado) {

                    carregarLivros();

                    status.setText(
                        "Capa atualizada para o livro ID: " + idLivro
                    );

                    JOptionPane.showMessageDialog(
                        this,
                        "Capa selecionada e salva com sucesso!"
                    );

                } else {

                    JOptionPane.showMessageDialog(
                        this,
                        "Não foi possível atualizar a capa no banco de dados.",
                        "Erro",
                        JOptionPane.ERROR_MESSAGE
                    );
                }

            } catch (IOException e) {

                JOptionPane.showMessageDialog(
                    this,
                    "Não foi possível salvar a imagem.",
                    "Erro",
                    JOptionPane.ERROR_MESSAGE
                );

                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new TelaLivros().setVisible(true);
        });
    }
}
