
# Como Adicionar Seu Nome ao Arquivo `introduction.md` no Repositório Público Usando o VS Code

### **Objetivo**
Neste guia, você aprenderá como **adicionar seu nome** ao arquivo **`introduction.md`** de forma simples e rápida, utilizando o **VS Code**. Como o repositório é **público**, você fará isso usando o processo de **fork + Pull Request (PR)**, pois **não somos colaboradores** do repositório original.

---

### **O Que É um Fork e uma Pull Request?**

Como o repositório é **público**, qualquer pessoa pode **clonar** o repositório, mas apenas quem tem **permissões de colaboração** pode **editar diretamente** a branch `main` do repositório. Isso significa que, como **não somos colaboradores**, você precisará fazer um **fork** do repositório.

1. **Fork**: Fazer um fork significa criar uma **cópia do repositório** sob a sua própria conta do GitHub. Com isso, você poderá editar a cópia do repositório.
2. **Pull Request (PR)**: Após fazer suas alterações no repositório **forkado**, você criará uma **Pull Request** para enviar suas mudanças de volta ao repositório original. Eu (ou o responsável pelo repositório) revisarei e, se estiver tudo certo, mesclarei suas alterações com a `main` do repositório original.

---

### **Passo 1: Clonar o Repositório no VS Code**

1. **Abra o VS Code** no seu computador.
2. **Clone o repositório**:
   - No **VS Code**, clique em **View** > **Command Palette** (ou pressione `Ctrl+Shift+P` no Windows/Linux, `Cmd+Shift+P` no macOS).
   - Digite **Git: Clone** e cole o link do repositório:
   
     [https://github.com/thiagoturini/learn-git](https://github.com/thiagoturini/learn-git)

   - Escolha um diretório onde o repositório será clonado.
   - O VS Code abrirá automaticamente a pasta do repositório.

---

### **Passo 2: Criar um Fork do Repositório**

1. **Acesse o repositório no GitHub**: [https://github.com/thiagoturini/learn-git](https://github.com/thiagoturini/learn-git)
2. No canto superior direito do repositório, clique em **Fork** para criar uma cópia do repositório sob a sua conta do GitHub.
3. Após criar o **fork**, você verá o repositório agora disponível na sua conta do GitHub.
4. **Clone o repositório forkado**:
   - No VS Code, use o comando **Git: Clone** e cole o link do repositório **forkado** (será algo como `https://github.com/seu-usuario/learn-git.git`).

---

### **Passo 3: Adicionar Seu Nome no Arquivo `introduction.md`**

1. **Abra o arquivo `introduction.md`** no VS Code.
2. **Adicione seu nome** na lista de alunos, no formato:
   
   ```markdown
   - Seu Nome
   ```
   
   Exemplo:
   ```markdown
   ### Lista de Alunos
   - João Silva
   ```

3. **Salve o arquivo** (`Ctrl + S` ou `Cmd + S` no macOS).

---

### **Passo 4: Criar uma Nova Branch para Suas Alterações**

1. **Crie uma nova branch** para suas alterações (não trabalhe na `main`):
   - No VS Code, abra o **Source Control** (controle de versão).
   - No terminal integrado, crie uma nova branch:
   
     ```bash
     git checkout -b adicionar-nome
     ```

2. Faça o **commit** das alterações:
   
   ```bash
   git add introduction.md
   git commit -m "Adiciona nome de João Silva na lista de alunos"
   ```

---

### **Passo 5: Enviar Suas Alterações para o Repositório Forkado**

1. **Faça o push** da sua nova branch para o repositório **forkado** no GitHub:
   
   ```bash
   git push origin adicionar-nome
   ```

---

### **Passo 6: Criar uma Pull Request (PR) no GitHub**

1. Acesse seu **repositório forkado** no GitHub.
2. Você verá uma notificação dizendo algo como "Compare & Pull Request" para a branch que você acabou de enviar.
3. Clique em **"Compare & Pull Request"**.
4. Preencha o título e a descrição da PR. Exemplo:
   - **Título**: "Adiciona nome de João Silva na lista de alunos"
   - **Descrição**: "Este PR adiciona o nome de João Silva à lista de alunos no arquivo `introduction.md`."
5. Clique em **Create Pull Request** para criar a PR.

---

### **Passo 7: Aguardar Revisão e Merge**

- Uma vez que você tenha criado a Pull Request, **eu (ou o responsável pelo repositório)** revisarei suas alterações.
- Se tudo estiver correto, a PR será **mesclada** com a `main` do repositório original.
- Se houver algum problema, o responsável pode pedir para ajustar algo antes de mesclar.

---

### **Resumo dos Passos**

1. **Clonar o repositório** no VS Code.
2. **Fazer um fork** do repositório para sua conta no GitHub.
3. **Criar uma nova branch** no VS Code para suas alterações.
4. **Adicionar seu nome** ao arquivo `introduction.md` e **commit**.
5. **Enviar suas alterações** para o GitHub com `git push`.
6. **Criar uma Pull Request (PR)** no GitHub.
7. **Aguardar revisão e merge** da PR.

---

### **Dúvidas ou Problemas?**

Se você encontrar algum problema ou tiver dúvidas durante o processo, não hesite em perguntar. Estamos aqui para garantir que o aprendizado seja o mais fluido possível!

---
