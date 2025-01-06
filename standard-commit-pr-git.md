
# Padrão para Mensagens de Commit e Pull Requests

Para manter a consistência e clareza, siga o formato de mensagem para **commits** e **Pull Requests (PRs)**.

## **1. Padrão de Mensagens de Commit**

As mensagens de commit devem ser curtas, claras e descritivas. Siga este padrão:

| Tipo de Commit | Exemplo de Mensagem de Commit                          | Descrição                                                   |
|-----------------|--------------------------------------------------------|-------------------------------------------------------------|
| **feat**        | `feat: adiciona nova funcionalidade de login`          | Para adicionar uma nova funcionalidade ou feature.          |
| **fix**         | `fix: corrige bug no formulário de cadastro`           | Para corrigir erros ou bugs no código.                      |
| **docs**        | `docs: atualiza documentação do processo de integração` | Para mudanças na documentação, como arquivos README.        |
| **style**       | `style: ajusta a formatação do código sem alterar a lógica` | Para ajustes no estilo do código, como formatação.           |
| **refactor**    | `refactor: melhora a eficiência do algoritmo de busca`  | Para mudanças que melhoram o código sem adicionar ou corrigir funcionalidades. |
| **test**        | `test: adiciona testes unitários para o modelo de usuário` | Para adição ou alteração de testes.                         |

## **2. Padrão de Mensagens de Pull Request (PR)**

As mensagens de PR devem incluir o que foi feito, por que foi feito e qual o impacto das mudanças. A estrutura recomendada é:

| Título da PR                             | Descrição Detalhada                                     |
|------------------------------------------|---------------------------------------------------------|
| `feat: adiciona login via GitHub`        | **O que foi feito?**: Adicionada funcionalidade de login via GitHub.<br>**Por que?**: Para permitir que os usuários façam login usando suas credenciais do GitHub.<br>**Impacto**: A nova funcionalidade não altera as funcionalidades anteriores e não gera impacto em outras áreas do código. |
| `fix: corrige erro de cálculo no relatório de vendas` | **O que foi feito?**: Corrigido o erro que causava cálculos incorretos.<br>**Por que?**: Para garantir a precisão dos relatórios financeiros.<br>**Impacto**: Corrige um erro crítico que afetava apenas os relatórios de vendas.  |
| `docs: atualiza README com instruções de uso`  | **O que foi feito?**: Atualização do README para incluir novas instruções.<br>**Por que?**: Para garantir que as instruções de uso estejam atualizadas.<br>**Impacto**: Nenhuma alteração no código, apenas documentação. |

---
