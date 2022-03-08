import PySimpleGUI as sg
import webbrowser as wb

#define the layout
layout = [[sg.Text('Iniciar conversa whatsapp')],
            [sg.Text('Digite o número sem o código do país, apenas com o DDD'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Window Title', layout)
#read the event
event, values = window.read()
#close the window
window.close()

wb.open("https://wa.me/5583" + str(values[0]))
