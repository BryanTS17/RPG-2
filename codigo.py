# Importando as bibliotecas necessárias
import pyautogui  # Para controlar mouse e teclado
import time  # Para adicionar pausas (delays)
import pandas as pd  # Para trabalhar com tabelas (ex: CSV)
import keyboard  # Para digitar textos (permite acentos melhor que o pyautogui)

# Lendo a tabela de produtos do arquivo CSV
tabela = pd.read_csv("Produtos.csv")

# Serve para clicar antes de começar a digitar, se precisar
posicao = [943, 511]


# Espaço reservado para escrever um texto maior (está vazio no momento)
texto_redacao = """
Redes sociais: conexão ou exposição disfarçada?

"""

# Exemplo de texto que será escrito automaticamente
texto = ""


# Função para escrever texto em uma posição específica (clicando antes)
# Usa keyboard.write para suportar acentos
def escrever_com_acento(
    texto, intervalo=0.05, posicao_mouse=posicao, esperar=15
):  # Espera 5 segundos antes de começar (tempo para preparar a tela)
    time.sleep(esperar)
    pyautogui.click(posicao_mouse[0], posicao_mouse[1])  # Clica na posição indicada
    for letra in texto:  # Percorre cada letra do texto
        if keyboard.is_pressed("esc"):
            print("Processo interrompido pelo usuário.")
            break
        keyboard.write(letra)  # Digita a letra
        time.sleep(intervalo)  # Espera um pouquinho (simula digitação humana)

def concluirAula(aulas=10, intervalo=0.3, esperar=10):
    time.sleep(esperar)  # Espera 5 segundos antes de começar
    while aulas >= 0:
        if keyboard.is_pressed("esc"):
            print("Processo interrompido pelo usuário.")
            break
        pyautogui.click(1004, 846)
        time.sleep(intervalo)
        pyautogui.click(1075, 845)
        time.sleep(intervalo)
        pyautogui.click(1171, 214)
        time.sleep(intervalo)
        aulas -= 1

# Função para escrever texto onde o cursor já está ativo
def escrever(texto, intervalo=0.05, esperar=15):
    time.sleep(esperar)  # Espera 5 segundos antes de começar
    for letra in texto:  # Percorre cada letra do texto
        if keyboard.is_pressed("esc"):
            print("Processo interrompido pelo usuário.")
            break
        keyboard.write(letra)  # Digita a letra
        time.sleep(intervalo)  # Tempo entre cada letra


# Função que abre o navegador Opera e entra no link do formulário
def entrarChrome():
    pyautogui.press("win")  # Abre o menu iniciar
    pyautogui.write("opera")  # Digita "opera" para abrir o navegador Opera
    pyautogui.press("enter")  # Pressiona Enter para abrir
    time.sleep(0.3)  # Pequena pausa
    pyautogui.write("https:\\\\dlp.hashtagtreinamentos.com\\python\\intersivao\\login")
    time.sleep(0.3)  # Espera um pouco
    pyautogui.press("enter")  # Pressiona Enter para acessar o link
    cadastrar()  # Chama a função cadastrar para preencher o formulário


# Função que preenche automaticamente os campos de um formulário
def cadastrar():
    for linha in tabela.index:  # Percorre todas as linhas da tabela Produtos.csv
        time.sleep(0.2)  # Pausa entre cada campo

        # Campo código
        pyautogui.press("tab")
        pyautogui.write(tabela.loc[linha, "codigo"])

        # Campo marca
        pyautogui.press("tab")
        pyautogui.write(tabela.loc[linha, "marca"])

        # Campo tipo
        pyautogui.press("tab")
        pyautogui.write(tabela.loc[linha, "tipo"])

        # Campo categoria
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "categoria"]))

        # Campo preço unitário
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))

        # Campo custo
        pyautogui.press("tab")
        pyautogui.write(str(tabela.loc[linha, "custo"]))

        # Campo observações (se não for vazio/nan)
        pyautogui.press("tab")
        if tabela.loc[linha, "obs"] != "nan":
            pyautogui.write(tabela.loc[linha, "obs"])

        # Enviar o formulário
        pyautogui.press("tab")
        pyautogui.press("enter")

        # Rola a página para cima para continuar o cadastro
        pyautogui.scroll(10000)


def autoClick(clicks=100, intervalo=0.1, esperar=10, posicao=posicao):
    time.sleep(esperar)
    while clicks > 0:
        if keyboard.is_pressed("esc"):
            print("Processo interrompido pelo usuário.")
            break
        pyautogui.click(posicao[0], posicao[1])
        clicks -= 1


# Função para descobrir a posição atual do mouse
# Muito útil para configurar onde o clique inicial deve acontecer
def acharPosicao(esperar=5):
    time.sleep(esperar)  # Espera o tempo definido (tempo para você posicionar o mouse)
    posicao = pyautogui.position()  # Captura a posição do mouse
    print(posicao)  # Mostra no console (x, y)


def finalRuinBloodMoney(espera=5, primeiro=200):
    posicao_loja = [207, 95]
    posicao_pena = [180, 658]
    posicao_agulha = [650, 658]
    posicao_martelo = [920, 658]
    posicao_tesoura = [1190, 658]
    posicao_faca = [1460, 658]
    posicao_arma = [1730, 658]

    time.sleep(espera)
    autoClick(clicks=primeiro, intervalo=0.2, esperar=0.2, posicao=posicao)
    if keyboard.is_pressed("esc"):
        return

    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_loja)
    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_loja)
    if keyboard.is_pressed("esc"):
        return
    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_loja)
    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_loja)
    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_loja)

    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_pena)
    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_loja)
    autoClick(clicks=100, intervalo=0.2, esperar=0.2, posicao=posicao)
    if keyboard.is_pressed("esc"):
        return

    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_loja)
    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_agulha)
    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_loja)
    autoClick(clicks=200, intervalo=0.2, esperar=0.2, posicao=posicao)
    if keyboard.is_pressed("esc"):
        return

    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_loja)
    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_martelo)
    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_loja)
    autoClick(clicks=200, intervalo=0.2, esperar=0.2, posicao=posicao)
    if keyboard.is_pressed("esc"):
        return

    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_loja)
    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_tesoura)
    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_loja)
    autoClick(clicks=200, intervalo=0.2, esperar=0.2, posicao=posicao)
    if keyboard.is_pressed("esc"):
        return

    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_loja)
    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_faca)
    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_loja)
    autoClick(clicks=200, intervalo=0.2, esperar=0.2, posicao=posicao)
    if keyboard.is_pressed("esc"):
        return

    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_loja)
    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_arma)
    autoClick(clicks=1, intervalo=0.2, esperar=1, posicao=posicao_loja)
    autoClick(clicks=100, intervalo=0.2, esperar=0.2, posicao=posicao)
    if keyboard.is_pressed("esc"):
        return


# Teste prático: digita o texto definido acima
#escrever(texto_redacao, intervalo=0.1, esperar=5)
#acharPosicao(5)  # Chama a função para descobrir a posição do mouse (tempo para posicionar o mouse)
# Caso queira testar o cadastro automático, basta descomentar a linha abaixo:
# entrarChrome()
concluirAula(15, 0.65, 5)
