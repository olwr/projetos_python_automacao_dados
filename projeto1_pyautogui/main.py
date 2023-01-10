import pyautogui
import pyperclip
import time
import pandas as pd

pyautogui.PAUSE = 1.5

# Passo 1: Entrar no sistema (no nosso caso, entrar no link)

#abrir navegador
pyautogui.alert("Program running, press okay and don't do anything")
pyautogui.press('winleft')
pyautogui.write('firefox')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')

#entrar no link
pyperclip.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')

time.sleep(5)

# Passo 2: Navegar até o local do relatório (entrar na pasta Exportar)
pyautogui.click(x=367, y=288, clicks=2)
time.sleep(5)

# Passo 3: Fazer o download do relatório
pyautogui.click(clicks=1, button='right')
pyautogui.click(x=496, y=758)
time.sleep(5)

# Passo 4: Calcular os indicadores
tabela = pd.read_excel(r'C:\Users\OLIWER\Downloads\Vendas - Dez.xlsx')
print(tabela)
faturamento = tabela['Valor Final'].sum()
quantidade = tabela['Quantidade'].sum()

# Passo 5: Entrar no email
pyautogui.press('winleft')
pyautogui.write('mail')
pyautogui.press('enter')
time.sleep(3)

# Passo 6: Enviar por e-mail o resultado
pyautogui.click(x=82, y=103)
time.sleep(3)

pyautogui.write('benites.olivr@gmail.com') #escreve o destinatário
pyautogui.press('tab') #seleciona o email
pyautogui.press('tab', presses=2) #pula para o campo de assunto
pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey('ctrl', 'v') #escreve o assunto
pyautogui.press('tab') #pula para o corpo do email

texto = f'''
Prezados, bom dia

O faturamento de ontem foi de: R${faturamento:,.2f}
A quantidade de produtos foi de: {quantidade:,}

Abs
Oliwer'''

pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')

#enviar com hotkey
pyautogui.hotkey('ctrl', 'enter')

#DONE!!!
pyautogui.alert("All Done!")