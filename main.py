# Importar bibliotecas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service         # Para criar o serviço do ChromeDriver
from selenium.webdriver.chrome.options import Options         # Para configurar o navegador
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import os
from pathlib import Path
import random
import time
from datetime import datetime, timedelta
import schedule

APPDATA = os.path.expanduser('~')

contatos = ['⛑ Segurança EPD-MS ⛑']  # Nome exato do grupo
mensagens_seguranca_campo = [
    "Senhores, bom dia! \nUse sempre os EPIs — sua segurança vem em primeiro lugar! \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
    "Senhores, bom dia! \nNão existe serviço tão urgente que não possa ser feito com segurança.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
    "Senhores, bom dia! \nCarro limpo e organizado é ambiente seguro.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
    "Senhores, bom dia! \nNão corra riscos desnecessários. Pare e pense!  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
    "Senhores, bom dia! \nComunique situações de risco — prevenir é sempre o melhor caminho.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
    "Senhores, bom dia! \nA pressa é inimiga da segurança. Faça com calma e atenção.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
    "Senhores, bom dia! \nVerifique seus equipamentos antes de iniciar o trabalho.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
    "Senhores, bom dia! \nTrabalhe com foco: sua vida vale mais que qualquer tarefa.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
    "Senhores, bom dia! \nSegurança é um valor. Pratique todos os dias!  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
    "Senhores, bom dia! \nSua atitude segura protege você e quem está ao seu lado.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
    "Senhores, bom dia! \nMantenha distância segura de veículos em movimento.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
    "Senhores, bom dia! \nEm caso de acidente, comunique imediatamente!  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
    "Senhores, bom dia! \nNão arrisque! Afinal, você é a ferramenta mais importante da empresa.  \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
    "Senhores, bom dia! \nUse o trabalho para cuidar da sua família e não para se afastar.   \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
    "Senhores, bom dia! \nNão esqueçam de se hidratar.   \nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos"
    "Senhores, bom dia! \nUm segundo de descuido pode custar uma vida inteira\nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
    "Senhores, bom dia! \nA prevenção é a melhor forma de proteção\nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
    "Senhores, bom dia! \nSegurança começa com você!\nÓtimo dia para todos",
    "Senhores, bom dia! \nEPI não é enfeite. Use corretamente!\nNão se esqueçam da APR e os Checklist, ok? \nÓtimo dia para todos",
    "Senhores, bom dia! \nTrabalhar seguro é um sinal de inteligência. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nNão espere um acidente acontecer para mudar sua postura. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nUm ambiente seguro é um ambiente produtivo. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nLembre-se de reportar qualquer risco identificado. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nPrevenir é um ato de respeito com os colegas. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nA maioria dos acidentes são causados por comportamento inseguro, então não se esqueça de sempre agir com segurança. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nO corpo dá sinais: se está cansado ou não está bem, pare e comunique. Sua segurança em primeiro lugar \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nNão se esqueça dos 5s. Então separe o essencial do desnecessário e elimine o que não é necessário. Deixe seu carro organizado, afinal, ele é seu ambiente de trabalho principal. Mantenha seu carro limpo. Crie padrões para organização e limpeza.\n E sempre se lembre de manter a disciplina, seguindo os padrões e promovendo organização e limpeza, isso pode ajudar a melhorar sua saúde. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nVocê voltar para casa no fim do dia sempre vai ser a meta mais importante. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nA vida não tem botão de reinício. Previna-se. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nTrabalho seguro é sinal de profissionalismo. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nPequenas ações fazem grandes diferenças na segurança. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nNegligência é o caminho mais rápido para um acidente. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nNão se arrisque, siga o procedimento! \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nSegurança não combina com improviso. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nUm acidente pode ter consequências para toda a vida. Tome cuidado. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nNão corra riscos, trabalhe com consciência. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nDireção defensiva é uma técnica de condução que visa evitar acidentes, mesmo diante de ações incorretas de outros motoristas e condições adversas da estrada. Envolve a antecipação de situações perigosas e a adoção de medidas para minimizar riscos.\nNão se esqueça disso, pode salvar sua vida e a de outras pessoas. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nA segurança é individual, mas o impacto é coletivo. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nResponsabilidade se pratica, não se terceiriza. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nFaça certo, mesmo quando ninguém está olhando. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nA cultura de segurança começa com pequenos hábitos e cuidados. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nFale! Segurança também se constrói com diálogo. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nNenhuma meta é mais importante que sua vida. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nIsso pode salvar sua vida: \nA identificação de riscos é o processo de identificar, reconhecer e descrever riscos ou oportunidades que possam afetar os objetivos de uma organização ou projeto. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nUma cultura de segurança, com a participação ativa de todos, é essencial para garantir a prevenção de acidentes e doenças ocupacionais. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nA segurança do trabalho não se limita à prevenção de acidentes, mas também inclui a promoção da saúde e do bem-estar de todos \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nA cultura de prevenção é um conjunto de valores, crenças e comportamentos que promovem a segurança e a saúde no trabalho. Faça também a sua parte! \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos",
    "Senhores, bom dia! \nA participação ativa dos trabalhadores no processo de segurança é fundamental para garantir que as medidas de segurança sejam eficazes e que haja uma cultura de prevenção. \nNão se esqueçam da APR e os Checklist, ok?\nÓtimo dia para todos"
]
options = Options()         # Configurar opções do navegador
service = Service(ChromeDriverManager().install())          # Criar o serviço, usando o ChromeDriverManager para baixar o ChromeDriver certo
options.add_argument(f"user-data-dir={APPDATA}\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

# Navegar até o web whats
driver = webdriver.Chrome(service=service, options=options)
driver.get('https://web.whatsapp.com/')
time.sleep(30)

# Buscar contatos/grupos
def buscar_contato(contato):
    time.sleep(3)  # aguarda o WhatsApp carregar
    campo_pesquisa = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    time.sleep(1)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem_grupo(mensagem):
    try:
        # Buscar todos os campos contenteditable (textos onde se pode digitar)
        campos_editaveis = driver.find_elements(By.XPATH, '//div[@contenteditable="true"]')
        if not campos_editaveis:
            print("Nenhum campo de digitação encontrado.")
            return

        campo_mensagem = campos_editaveis[-1]  # O último normalmente é o campo de digitação
        campo_mensagem.click()
        time.sleep(1)
        campo_mensagem.send_keys(mensagem)
        time.sleep(1)
        campo_mensagem.send_keys(Keys.ENTER)
        print("Mensagem enviada com sucesso!")
    except NoSuchElementException:
        print("Erro: campo de mensagem não encontrado.")
    except Exception as e:
        print(f"Erro ao tentar enviar mensagem: {e}")


schedule.every().day.at("08:00").do(enviar_mensagem_grupo)

print("Automação iniciada para envio de mensagens de segurança no grupo.")
buscar_contato(contatos[0])
mensagem = random.choice(mensagens_seguranca_campo)  # Escolhe uma mensagem aleatória
enviar_mensagem_grupo(mensagem)  # Passa a mensagem diretamente
print(f"Mensagem enviada ao grupo '{contatos}': {mensagem}")

# Espera alguns segundos e fecha o navegador
time.sleep(5)
driver.quit()

while True:
    schedule.run_pending()
    time.sleep(60)