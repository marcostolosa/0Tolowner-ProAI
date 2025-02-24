# Tolowner ProAI 🚀

Tolowner ProAI é uma ferramenta avançada para automação de testes de penetração, projetada para interagir com máquinas no Hack The Box (HTB) utilizando inteligência artificial. A aplicação combina uma API RESTful com uma interface de usuário intuitiva para facilitar a execução de comandos e a geração de relatórios.

## Funcionalidades 🌟

- **Execução de Comandos**: Execute comandos diretamente no shell e obtenha resultados em tempo real.
- **Gerenciamento de Máquinas HTB**: Inicie e gerencie máquinas no Hack The Box com facilidade.
- **Geração de Relatórios**: Crie relatórios em PDF com os resultados das execuções.
- **Logging Detalhado**: Acompanhe a execução com logs detalhados.
- **Persistência de Dados**: Registre comandos e resultados em um banco de dados.
- **Integração com IA**: Sugestões de comandos e análise de resultados usando modelos de linguagem.
- **Containerização com Docker**: Execute a aplicação e o Kali Linux em contêineres Docker.
- **Configuração de VPN**: Conecte-se a uma VPN usando o Kali Linux.
- **Interface de Usuário com Streamlit**: Uma interface web interativa para facilitar a interação com a aplicação.

## Instalação 🛠️

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/marcostolosa/Tolowner-ProAI.git
   cd Tolowner-ProAI
   ```

2. **Crie um Ambiente Virtual** (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
   ```

3. **Instale as Dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as Variáveis de Ambiente**:
   - Crie um arquivo `.env` na raiz do projeto e adicione suas chaves de API e tokens necessários:
     ```bash
     HTB_TOKEN=your_htb_token
     OPENAI_API_KEY=your_openai_api_key
     ```

5. **Configuração da VPN**:
   - Coloque seu arquivo de configuração da VPN (`vpn_config.ovpn`) na pasta `kali/`.

## Uso 📖

### Executando o Tolowner ProAI

Para executar o Tolowner ProAI, use o seguinte comando:

```bash
docker-compose up --build
```

### Interface de Usuário

A interface do usuário pode ser acessada em `http://localhost:5000`. A partir daí, você pode:

1. **Executar um comando**:
   - Digite um comando na seção "Executar Comando" e clique em "Executar".

2. **Executar um comando no Kali**:
   - Digite um comando na seção "Executar Comando no Kali" e clique em "Executar no Kali".

3. **Sugestão de Comando**:
   - Digite um prompt na seção "Sugestão de Comando" e clique em "Sugerir".

## Contribuição 🤝

Contribuições são bem-vindas! Se você deseja contribuir para o Tolowner ProAI, siga estas etapas:

1. **Fork o repositório**.
2. **Crie uma nova branch**:
   ```bash
   git checkout -b feature/nome-da-sua-feature
   ```
3. **Faça suas alterações e commit**:
   ```bash
   git commit -m "Descrição das suas alterações"
   ```
4. **Envie para o repositório remoto**:
   ```bash
   git push origin feature/nome-da-sua-feature
   ```
5. **Abra um Pull Request**.
