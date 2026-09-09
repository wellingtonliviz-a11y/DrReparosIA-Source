# 🔧 Dr Reparos IA — Source Code

Código-fonte público do **Dr Reparos IA**, projeto desenvolvido para aplicar tecnologia à solução de problemas reais de manutenção residencial.

O projeto nasceu da minha experiência prática com manutenção residencial e evoluiu de um protótipo em Python executado no terminal para uma aplicação web com **Flask**, posteriormente integrada a um aplicativo **Android**.

> Este repositório é uma versão pública destinada à apresentação técnica e portfólio.

---

## 🚀 Aplicação funcionando

🌐 **Web:** https://drreparosia.onrender.com

📱 **Android:**  
https://github.com/wellingtonliviz-a11y/DrReparosIA-Android

---

## 🎯 Objetivo do projeto

O Dr Reparos IA busca auxiliar pessoas sem conhecimento técnico a identificar problemas residenciais e seguir um fluxo orientado para encontrar possíveis causas e soluções.

A aplicação trabalha com três possibilidades de atendimento:

- 🔍 Diagnóstico guiado
- 📹 Videochamada com especialista
- 🛠️ Solicitação de atendimento presencial

---

## 🧠 Funcionalidades implementadas

- Diagnóstico guiado de problemas residenciais
- Identificação de modelos de válvulas de descarga
- Diagnóstico de caixa acoplada
- Substituição de sifão
- Troca de engate flexível
- Reparo de registro de pressão
- Orientações para instalação de chuveiro
- Upload de imagens
- Orientações de segurança
- Lista de materiais e ferramentas
- Passo a passo para execução do reparo
- Integração com links de produtos recomendados
- Rotas para videochamada e atendimento presencial
- Estrutura preparada para evolução da integração com IA

---

## 🛠️ Tecnologias

- Python
- Flask
- HTML5
- CSS3
- Jinja2
- Git / GitHub
- Render
- Gunicorn
- Kotlin
- Android Studio
- Android WebView

---

## 🏗️ Estrutura do projeto

```text
DrReparosIA-Source/
│
├── app.py
├── catalogo.py
├── diagnostico.py
├── orcamento.py
├── teste_ia.py
├── requirements.txt
├── render.yaml
├── .env.example
├── .gitignore
│
├── templates/
│   └── interfaces HTML da aplicação
│
└── static/
    └── imagens e recursos estáticos

```

### Arquivos principais

**`app.py`**  
Aplicação Flask principal, contendo rotas, controle de sessões, upload de imagens e lógica dos módulos de diagnóstico.

**`catalogo.py`**  
Centraliza produtos, modelos de válvulas e links utilizados pelos diagnósticos.

**`diagnostico.py`**  
Protótipo inicial desenvolvido em Python para validar o fluxo de diagnóstico antes da implementação da interface web.

**`templates/`**  
Interfaces HTML renderizadas pelo Flask.

**`static/`**  
Recursos visuais utilizados pela aplicação.

---

## 📈 Evolução do projeto

O desenvolvimento começou com um fluxo simples executado pelo terminal utilizando `print()` e `input()`.

A partir desse protótipo, o projeto evoluiu para uma aplicação web utilizando Flask:

**Python → Flask → HTML/CSS → Deploy em nuvem → Android WebView**

Essa evolução permitiu transformar a ideia inicial em uma aplicação funcional acessível pela web e por dispositivos Android.

---

## 🔐 Segurança

Credenciais e variáveis sensíveis não são armazenadas no código-fonte público.

O projeto utiliza variáveis de ambiente para configurações como:

```text
FLASK_SECRET_KEY
OPENAI_API_KEY
```

O arquivo `.env` é ignorado pelo Git através do `.gitignore`.

O arquivo `.env.example` demonstra apenas a estrutura esperada das variáveis.

---

## 🔮 Próximas evoluções

- Integração de IA ao fluxo de diagnóstico
- Análise de imagens enviadas pelo usuário
- Ampliação da base de problemas residenciais
- Evolução da experiência no aplicativo Android
- Melhorias na arquitetura e organização dos módulos
- Expansão dos fluxos de atendimento

---

## 👨‍💻 Desenvolvedor

**Wellington Liviz**

Profissional com experiência em Tecnologia da Informação, atualmente cursando **Tecnologia em Inteligência Artificial**.

Também cursei **3 semestres de Análise e Desenvolvimento de Sistemas** e venho aprofundando meus conhecimentos em desenvolvimento de software através de projetos práticos envolvendo Python, Flask, Android e aplicações web.

**LinkedIn:**  
https://www.linkedin.com/in/wellington-liviz-567001249/

**GitHub:**  
https://github.com/wellingtonliviz-a11y
