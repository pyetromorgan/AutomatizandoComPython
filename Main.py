import pyautogui
import time

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
