import pyautogui
import time
import pandas

url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.PAUSE = 3
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(url)
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=691, y=411)
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345testador2")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)
tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=692, y=293)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(5000)


