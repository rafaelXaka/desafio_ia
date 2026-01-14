# 🏦 Sistema de Triagem Inteligente de E-mails - AUTO_MAIL AI

Este projeto é uma solução digital desenvolvida para automatizar a leitura, classificação e resposta de e-mails em larga escala para empresas do setor financeiro. O objetivo principal é otimizar o fluxo de trabalho da equipe, separando demandas críticas (**Produtivas**) de mensagens irrelevantes (**Improdutivas**).

---

## 🚀 Funcionalidades

- **Classificação Automática:** Utiliza IA para identificar se um e-mail requer ação (suporte, dúvidas, solicitações) ou se é apenas informativo/agradecimento.
- **Sugestão de Resposta:** Gera automaticamente uma resposta contextualizada e profissional para cada e-mail processado.
- **Interface Responsiva:** Design moderno focado em UX/UI, adaptável a dispositivos móveis e desktops.
- **Segurança de Dados:** Implementação de variáveis de ambiente para proteção de chaves de API.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python 3.14+
- **Framework Web:** Flask (Backend)
- **Inteligência Artificial:** OpenAI API (Modelo GPT-4o-mini)
- **Interface:** HTML5, CSS3 (Modern SaaS Design) e Bootstrap 5
- **Hospedagem:** Render.com (Web Service)
- **Gestão de Dependências:** Pip & Requirements.txt

---

## 📦 Como Executar o Projeto Localmente

Siga os passos abaixo para rodar a aplicação em sua máquina:

1. **Clonar o repositório:**
   ```bash
   git clone github.com
   cd seu-repositorio
   Use o código com cuidado.
   ```

Configurar o Ambiente Virtual (Opcional, mas recomendado):
bash
python -m venv venv
source venv/bin/activate # No Windows: venv\Scripts\activate
Use o código com cuidado.

Instalar Dependências:
bash
pip install -r requirements.txt
Use o código com cuidado.

Configurar Variáveis de Ambiente:
Crie um arquivo .env na raiz do projeto e adicione sua chave da OpenAI:
env
OPENAI_API_KEY=sua_chave_aqui
Use o código com cuidado.

Iniciar a Aplicação:
bash
python app.py
Use o código com cuidado.

Acesse no navegador: http://127.0.0.1:5000
📂 Estrutura do Projeto
text
├── app.py # Lógica do Backend e Integração com IA
├── static/ # Arquivos de estilização (CSS)
├── templates/ # Interface Web (HTML/Jinja2)
├── requirements.txt # Bibliotecas necessárias
├── .env # Variáveis sensíveis (não enviado ao GitHub)
└── README.md # Documentação do projeto
Use o código com cuidado.

🧠 Decisões Técnicas
Separação de Preocupações: O CSS foi desacoplado do HTML para facilitar a manutenção e garantir um código limpo.
UX/UI Design: Optou-se por um layout Clean/Corporate utilizando a fonte Inter, visando a seriedade exigida pelo setor bancário em 2026.
Prompt Engineering: Foi utilizado um System Prompt estruturado para garantir que a IA responda estritamente no formato necessário para o parse do sistema, reduzindo erros de processamento.
🎥 Vídeo Demonstrativo
Confira o funcionamento da aplicação e a explicação técnica completa através deste link: [LINK_VIDEO]
Desenvolvido por Rafael Cardozo da Silva como parte do Desafio para estágio na AutoU.
