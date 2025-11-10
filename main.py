from inicio import iniciar_jogo
from navegador import iniciar_navegador, fechar_navegador
from palavras import capturar_palavras_dia, capturar_celulas, selecionar_palavras
from config import URL
import time

def main():

    driver = iniciar_navegador(URL)

    iniciar_jogo(driver)

    palavras = capturar_palavras_dia(driver)

    celulas_agrupadas = capturar_celulas(driver)

    for grupo, lista in celulas_agrupadas.items():
        selecionar_palavras(driver, lista)
        time.sleep(0.3)

    print(f"[INFO] Palavras do dia: {' '.join(palavras)}")
    print(f"[INFO] Células para serem agrupadas: {' '.join(celulas_agrupadas.keys())}")

    input("Pressione Enter para fechar o navegador...")
    fechar_navegador(driver)

if __name__ == "__main__":
    main()