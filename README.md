# 📟 Calculadora DevOps em Python

Este projeto foi desenvolvido como parte da atividade prática do grupo
**Exploradores DevOps** na disciplina de **Engenharia de Software**.  
O objetivo é aplicar o uso de **CI/CD com GitHub Actions** em um projeto real e
simples: uma calculadora com operações matemáticas e trigonométricas feitas em
**Python**.

---

## ✨ Funcionalidades

- ✅ Operações matemáticas:
  - Soma
  - Subtração
  - Multiplicação
  - Divisão
  - Raiz quadrada
  - Potência
- ✅ Operações trigonométricas:
  - Seno
  - Cosseno
  - Tangente
- ✅ Interface de terminal (`main.py`)
- ✅ Testes automatizados com `pytest`
- ✅ Integração Contínua com **GitHub Actions** (`python.yml`)

---

## ▶️ Como executar o projeto localmente

### 🔧 Pré-requisitos

- Python 3 instalado
- Git
- Recomendado: ambiente virtual

### 📥 Clonar o repositório

```bash
git clone https://github.com/CorinaPC/DevOps
cd DevOps

## ▶️ Rodar o programa principal

python main.py

## 🧪 Rodar os testes

pip install pytest
pytest test_app.py

## ⚙️ Integração Contínua com GitHub Actions
# O projeto possui um pipeline automatizado localizado em:

.github/workflows/python.yml

# Esse workflow executa:

- ✅ Verificação da estrutura mínima do projeto

- ✅ Validação do arquivo README.md

- ✅ Busca por arquivos indesejados (.log, .DS_Store)

- ✅ Execução dos testes com pytest

# A pipeline roda automaticamente a cada push ou pull request para a branch main.
# 🔗 Veja os resultados na aba Actions

## 📂 Estrutura do Projeto

-  DevOps/
-  ├── app.py              # Funções matemáticas e trigonométricas
-  ├── main.py             # Interface para entrada de dados do usuário
-  ├── test_app.py         # Arquivo com testes unitários
-  ├── README.md           # Este documento
-  └── .github/
-      └── workflows/
-          └── python.yml  # Workflow do GitHub Actions (CI)

## 👥 Integrantes do grupo

- Silney Jr.
- Corina.
- Lowreen Almeida.
- Daniel.
- Jhenyffe Maçal.
- Luis Fernando.
- Victor Alcântara.

## 📝 Licença

Este projeto está licenciado sob a Licença MIT – veja o arquivo
[LICENSE](LICENSE) para mais detalhes.
