import PySimpleGUI as sg
import webbrowser as wb

sg.theme('DarkGray')
# define the layout

layout = [[sg.Text('Start WhastApp chat')],
          [sg.Text(
              'Country code', size=14), sg.InputText(size=5, key='-cod-')],
          [sg.Text(
              'DDD',  size=14), sg.InputText(size=5, key='-ddd-')],
          [sg.Text(
              'Number'), sg.InputText(size=15, key='-num-')],
          [sg.Button('Open chat'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Window Title', layout)

while True:
    # read the event
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    elif values['-cod-'] == '' or values['-ddd-'] == '' or values['-num-'] == '':
        sg.popup('Please fill all the fields!')
    else:
        if values['-cod-'].isdigit() and values['-ddd-'].isdigit() and values['-num-'].isdigit():
            wb.open("https://wa.me/" +
                    values['-cod-'] + values['-ddd-'] + values['-num-'])
        else:
            sg.popup('Please fill the fields only with numbers')
# close the window
window.close()
