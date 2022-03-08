from selenium import webdriver as wd
import PySimpleGUI as sg

#define the layout
layout = [[sg.Text('Iniciar conversa whatsapp')],
            [sg.Text('Digite o número sem o código do país e DDD'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Window Title', layout)
#read the event
event, values = window.read()
#close the window
window.close()

#get data and open the link
driver = wd.Chrome(executable_path=r"caminho_do_crhome_driver\chromedriver.exe")
driver.get("https://wa.me/5583" + str(values[0]))
