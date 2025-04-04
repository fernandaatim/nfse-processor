# NFSe Processor

Projeto desenvolvido para automatizar um processo interno da área de Controladoria da Robert Bosch. O processo original era totalmente manual, envolvendo o download das Notas Fiscais, renomeação de acordo com padrões específicos e armazenamento em pastas organizadas por mês (referente ao mês anterior ao atual). 
Existem algumas particularidades para as Notas Fiscais de cada portal (Joinville e Campinas).

## ⚠️ Aviso de Confidencialidade

Este projeto foi desenvolvido com base em documentos públicos (Notas Fiscais eletrônicas) e **não expõe dados sigilosos, internos ou estratégicos da empresa**. 
Toda a automação depende de arquivos locais fornecidos pelo usuário, e **não há conexão com sistemas internos ou informações confidenciais da Robert Bosch**.

## Resultados Obtidos

### Redução de Tempo
  - NFSe de Campinas: *Redução de aproximadamente **1h15min para alguns segundos** no processo de renomeação e organização das notas.
  - NFSe de Joinville: Redução de cerca de **2 horas para segundos**, eliminando a necessidade de baixar cada NF individualmente e realizar separações manuais.

### Redução de Erros
  - Padronização automáticas conforme regras específicas por localidade.
  - Eliminação de erros de digitação e organizaçao incorreta dos arquivos.

### Confiabilidade e Reprodutibilidade
  - Processo pode ser executado por qualquer outra pessoa da equipe, mantendo os mesmos padrões e resultados.
  - Garante a consistência no arquivamento mensal das notas fiscais.

## Funcionalidades

- **Separação das notas (`split_pdf`)**: Para as NFs de Joinville, realiza a separação dos documentos que são baixados em um único PDF.
- **Extração de dados (`extract_data`)**: Extrai informações específicas das NFs de Joinville e Campinas para facilitar a identificação.
- **Renomear PDF (`rename_pdf`)**: Renomeia cada PDF conforme o padrão de nomenclatura definido para cada localidade.
- **Converter PDF para XML (`convert_pdf_to_xml`)**: Para as NFs de Campinas, realiza a conversão para o formato XML.
- **Compactar pasta de arquivos (`zip_folder`)**: Compacta todas as NFs de Campinas em uma pasta com nome padronizado.

## Tecnologias

- Python 3.x
- Flet Desktop
- pdfminer.six
- Bibliotecas padrão do Python

**Todas as dependências estão listadas no arquivo requirements.txt.**

## Como executar o Projeto

**1. Clone o repositório:**
   ```
   git clone https://github.com/fernandaatim/nfse-processor.git
   cd nfse-processor
   ```
   
**2. (Opcional) Crie um ambiente virtual:**
   ```
   python -m venv venv
   ```
   
**3. Ative o ambiente virtual:**
   ```
   Windows: venv\Scripts\activate
   Linux/macOS: source venv/bin/activate
   ```
   
**4. Instale as dependências:**
   ```
   pip install -r requirements.txt
   ```
   
**5. Execute a aplicação:**
   ```
   py src/main.py
   ```

## Como gerar o Executável

No console (na mesma linha), execute:
```
flet pack src/main.py --name "NFSe Processor" --add-data "src/interface/assets/;interface/assets"
--icon "src/interface/assets/icons/icon_bosch.ico"
```

## Licença

Este projeto é de **uso interno**, e **não deve ser comercializado ou redistribuído** sem autorização prévia.
Todos os direitos relacionados à marca **Robert Bosch** são reservados à própria empresa.
