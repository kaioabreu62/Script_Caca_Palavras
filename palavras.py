from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

def capturar_palavras_dia(driver):
    try:
        elementos_palavras = driver.find_elements(By.CSS_SELECTOR, "span.suggestion")
        palavras_capturadas = [p.text.strip() for p in elementos_palavras if p.text.strip()]
        return palavras_capturadas
    except Exception as e:
        print(f"Não foi possível capturar as palavras do dia", {e})


def capturar_celulas(driver):
    try:
        celulas = driver.find_elements(By.CSS_SELECTOR, ".letter-box text")

        agrupar_palavras = {}
        for celula in celulas:
            classe_palavra = celula.get_attribute("data-id")
            if classe_palavra:
                if classe_palavra not in agrupar_palavras:
                    agrupar_palavras[classe_palavra] = []
                agrupar_palavras[classe_palavra].append(celula)
        
        for grupo, lista in agrupar_palavras.items():
            selecionar_palavras(driver, lista)
            print(f"[INFO] Grupo '{grupo}' contém {len(lista)} células")

        return agrupar_palavras
    
    except Exception as e:
        print(f"Não foi possível capturar o tabuleiro de letras", {e})


def selecionar_palavras(driver, celulas):
    if not celulas:
        print("Não nenhuma seleciona encontrada para ser selecionada.")
        return

    action = ActionChains(driver)

    primeira_celula = celulas[0]
    action.click_and_hold(primeira_celula)

    for letra in celulas[0:]:
        action.move_to_element(letra)
        time.sleep(0.05)

    
    action.release().perform()

    print(f"[INFO] Palavra selecionada: ({len(celulas)} letras)")