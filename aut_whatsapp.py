import PySimpleGUI as sg
import webbrowser as wb

sg.theme('DarkGray')
# define the layout

sg.popup('Tutorial\n\nFill the field with the complete number, only with numbers\n\n'
        'Ex.: Brazil: 5583912344321 > Country cod, DDD, number with 9\n\nEnjoy!')
layout = [[sg.Text('Start WhastApp chat')],
          [sg.Text('Number'), sg.InputText(size=25, key='-num-')],
          [sg.Button('Open chat'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Window Title', layout)

while True:
    # read the event
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    elif values['-num-'] == '':
        sg.popup('Please fill the field!')
    else:
        if values['-num-'].isdigit():
            wb.open("https://wa.me/" +
                    values['-num-'])
        else:
            sg.popup('Please fill the field only with numbers')
# close the window
window.close()
