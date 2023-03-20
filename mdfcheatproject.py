import os
import pyautogui
import pytesseract
import webbrowser

# Configurez le chemin vers l'exécutable Tesseract
pytesseract.pytesseract.tesseract_cmd = "pathto/Tesseract-OCR/tesseract.exe"

# Coordonnées de la zone de capture d'écran (à adapter en fonction de votre écran)
x, y, largeur, hauteur = 700, 340, 500, 300

# Prendre une capture d'écran de la zone définie
screenshot = pyautogui.screenshot(region=(x, y, largeur, hauteur))

# Reconnaissance de texte (OCR) à partir de la capture d'écran
texte = pytesseract.image_to_string(screenshot, lang='fra')
texte = texte.replace("\n", " ")

print(texte)
url = f"https://www.google.com/search?q={texte}"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:/Program Files/Google/Chrome/Application/chrome.exe"))
webbrowser.get('chrome').open(url)