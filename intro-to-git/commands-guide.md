
# Comandos Git mais Importantes

Este documento contém os comandos Git essenciais para gerenciamento de repositórios, controle de versão e colaboração em projetos. Esses são os comandos mais comuns que você utilizará ao trabalhar com Git.

---

## **1. Configuração Inicial do Git**

### Verificar a versão do Git instalado
```bash
git --version
```

### Configurar seu nome e email no Git
Esses dados são usados para registrar quem está fazendo os commits no repositório.
```bash
git config --global user.name "Seu Nome"
git config --global user.email "seu.email@example.com"
```

### Verificar as configurações do Git
```bash
git config --list
```

---

## **2. Criar e Gerenciar Repositórios**

### Inicializar um repositório Git local
```bash
git init
```

### Clonar um repositório remoto para o seu computador
```bash
git clone https://github.com/usuario/repositorio.git
```

### Criar uma nova branch
```bash
git branch nome-da-branch
```

### Alternar entre branches
```bash
git checkout nome-da-branch
```

### Criar e alternar para uma nova branch em um comando
```bash
git checkout -b nome-da-branch
```

---

## **3. Trabalhando com Arquivos**

### Verificar o status dos arquivos (quais estão alterados, não comitados, etc.)
```bash
git status
```

### Adicionar arquivos ao controle de versão
Adicionar um arquivo específico:
```bash
git add nome-do-arquivo
```

Adicionar todos os arquivos modificados:
```bash
git add .
```

### Realizar um commit com uma mensagem descritiva
```bash
git commit -m "mensagem de commit"
```

### Verificar os commits feitos no repositório
```bash
git log
```

### Desfazer alterações no arquivo (antes de comitar)
```bash
git checkout -- nome-do-arquivo
```

### Remover um arquivo do repositório
```bash
git rm nome-do-arquivo
```

---

## **4. Trabalhando com Repositórios Remotos**

### Adicionar um repositório remoto
```bash
git remote add origin https://github.com/usuario/repositorio.git
```

### Enviar suas mudanças para o repositório remoto
```bash
git push origin nome-da-branch
```

### Baixar alterações do repositório remoto para o local
```bash
git pull origin nome-da-branch
```

### Verificar os repositórios remotos configurados
```bash
git remote -v
```

---

## **5. Trabalhando com Branches**

### Mesclar (merge) uma branch na branch atual
```bash
git merge nome-da-branch
```

### Excluir uma branch local
```bash
git branch -d nome-da-branch
```

### Excluir uma branch remota
```bash
git push origin --delete nome-da-branch
```

---

## **6. Outras Operações Comuns**

### Criar um "stash" (guardar alterações temporariamente)
```bash
git stash
```

### Aplicar as alterações do stash
```bash
git stash apply
```

### Reverter o último commit (sem perder as alterações)
```bash
git revert HEAD
```

### Atualizar o repositório remoto com alterações locais
```bash
git push --force
```

---

## **7. Finalizando a Colaboração com Pull Requests (GitHub)**

### Criar uma Pull Request
- No GitHub, crie uma Pull Request para mesclar suas alterações de uma branch para outra, geralmente para a `main`.

### Revisar e Mesclar a Pull Request
- Após revisão e aprovação, você pode mesclar a PR para integrar as mudanças no repositório principal.

---

Com esses comandos, você tem as bases para gerenciar seu código com Git de forma eficiente e colaborativa. 🚀
