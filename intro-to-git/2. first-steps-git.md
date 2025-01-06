
# Guia Detalhado: Configurando Git, GitHub e VS Code

Este guia apresenta os passos necessários para configurar o Git, conectar ao GitHub, e integrar com o VS Code, incluindo o login e autenticação.

---

1. **Verificar Instalação do Git**
   Certifique-se de que o Git está instalado no seu sistema:
   ```bash
   git --version
   ```

   - Se o Git não estiver instalado, faça o download em [git-scm.com](https://git-scm.com) e siga as instruções para instalação.

2. **Configurar o Git Localmente**
   Configure seu nome e email para associar os commits ao seu perfil:
   ```bash
   git config --global user.name "Seu Nome"
   git config --global user.email "seu.email@example.com"
   ```

   Para verificar as configurações realizadas:
   ```bash
   git config --list
   ```

3. **Fazer Login no GitHub**
   Utilize o GitHub CLI para autenticar no GitHub diretamente do terminal:

   - Certifique-se de que o GitHub CLI está instalado:
     ```bash
     gh --version
     ```

     - Se não estiver instalado, siga as instruções em [cli.github.com](https://cli.github.com).

   - Execute o comando para autenticar:
     ```bash
     gh auth login
     ```

   - Escolha as opções:
     - Tipo de conta: **GitHub.com**.
     - Método de autenticação: **Login via navegador**.
     - Siga as instruções exibidas no terminal e no navegador.

   - Verifique se a autenticação foi concluída com sucesso:
     ```bash
     gh auth status
     ```

4. **Integrar com o VS Code**
   - Certifique-se de que o VS Code está instalado. Faça o download em [code.visualstudio.com](https://code.visualstudio.com) se necessário.
   - Abra o VS Code e instale a extensão **GitHub Pull Requests and Issues**:
     - No VS Code, vá para a aba **Extensões** (ícone de quadrados empilhados).
     - Pesquise por **GitHub Pull Requests and Issues** e clique em **Instalar**.

   - Configure o VS Code para usar o Git como controle de versão:
     - No terminal integrado do VS Code, execute:
       ```bash
       git --version
       ```

   - Faça login no GitHub pelo VS Code:
     - Clique no ícone do **GitHub** no canto inferior esquerdo.
     - Siga as instruções para conectar sua conta do GitHub ao VS Code.

5. **Testando a Conexão com o GitHub**
   - No terminal do VS Code, execute o seguinte comando para verificar os remotos configurados:
     ```bash
     git remote -v
     ```

     - Se não houver nenhum repositório configurado, você verá uma saída vazia.

   - Crie ou clone um repositório:
     - Para criar um repositório:
       ```bash
       gh repo create nome-do-repositorio --public
       ```

     - Para clonar um repositório existente:
       ```bash
       git clone https://github.com/seu-usuario/seu-repositorio.git
       ```

   - Verifique se o repositório foi configurado corretamente:
     ```bash
     git remote -v
     ```

---

Agora você está pronto para começar a usar o Git, GitHub e VS Code integrados! 🚀
