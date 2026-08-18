import javax.swing.*;  // biblioteca para criar janelas
import java.io.*;      // biblioteca para ler arquivos

public class LeitorCodigoFonte extends JFrame {  // janela principal

    public LeitorCodigoFonte() throws Exception {

        // cria o campo de texto que vai exibir o conteudo do arquivo
        JTextArea textArea = new JTextArea();

        // abre uma janela para o usuario escolher o arquivo
        JFileChooser chooser = new JFileChooser();

        // define a pasta inicial como a pasta onde o programa esta rodando
        chooser.setCurrentDirectory(new File(System.getProperty("user.dir")));

        chooser.showOpenDialog(null);  // null significa que nao tem janela pai

        // pega o arquivo que o usuario selecionou
        File arquivo = chooser.getSelectedFile();

        // cria um leitor de texto para o arquivo
        BufferedReader reader = new BufferedReader(new FileReader(arquivo));

        // le o conteudo do arquivo e joga no campo de texto
        textArea.read(reader, null);

        // fecha o leitor apos terminar a leitura
        reader.close();

        // adiciona barra de rolagem ao campo de texto e coloca na janela
        add(new JScrollPane(textArea));

        // define o tamanho da janela
        setSize(700, 500);

        // fecha o programa quando a janela for fechada
        setDefaultCloseOperation(EXIT_ON_CLOSE);

        // torna a janela visivel
        setVisible(true);
    }

    // metodo principal que inicia o programa
    public static void main(String[] args) throws Exception {
        new LeitorCodigoFonte();
    }
}