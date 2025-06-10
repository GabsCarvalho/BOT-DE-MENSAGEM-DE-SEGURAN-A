# 🛡️ Bot de Envio Automático de Mensagens de Segurança via WhatsApp

Este projeto é um **bot automatizado em Python com Selenium** que envia mensagens de conscientização sobre segurança do trabalho para grupos do WhatsApp Web.

---

## 📌 Funcionalidades

* Conecta-se ao **WhatsApp Web** automaticamente.
* Procura pelo(s) grupo(s) especificado(s) no WhatsApp.
* Envia uma **mensagem aleatória de segurança** para cada grupo.
* Utiliza uma base extensa de mensagens pré-definidas com foco em **EPIs, comportamento seguro, prevenção de acidentes e cultura de segurança**.

---

## ⚙️ Tecnologias Utilizadas

* [Python](https://www.python.org/)
* [Selenium](https://www.selenium.dev/)
* [WebDriver Manager](https://pypi.org/project/webdriver-manager/)
* WhatsApp Web

---

## 🔧 Pré-requisitos

* Python 3.7 ou superior
* Google Chrome instalado
* Instalar as dependências:

```bash
pip install selenium webdriver-manager schedule
```

---

## 🚀 Como Usar

1. **Clone o repositório** ou copie os arquivos do projeto.
2. **Edite a lista de contatos/grupos** no código:

   ```python
   contatos = ['⛑ Segurança EPD-MS ⛑']
   ```
3. **(Opcional)** Personalize a lista de mensagens em `mensagens_seguranca_campo`.
4. **Execute o script**:

```bash
python seu_script.py
```

5. O navegador será aberto automaticamente e **aguardará 30 segundos** para que você escaneie o QR Code do WhatsApp Web.
6. Após o login, o bot buscará o(s) grupo(s) e enviará uma mensagem aleatória de segurança.

---

## 🗓️ Agendamento Automático (Opcional)

O projeto usa a biblioteca `schedule`, permitindo o envio de mensagens de forma automatizada em horários programados. Exemplo de uso:

```python
schedule.every().day.at("07:00").do(enviar_mensagem)
```

---

## ⚠️ Avisos Importantes

* O WhatsApp pode detectar automações e restringir o uso. **Evite uso excessivo** ou fora dos termos de uso.
* Mantenha o Chrome aberto e autenticado no WhatsApp Web para funcionamento contínuo.
* O caminho de perfil do Chrome precisa estar correto para preservar o login:

  ```python
  options.add_argument(f"user-data-dir={APPDATA}\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
  ```



