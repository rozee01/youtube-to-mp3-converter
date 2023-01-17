import PySimpleGUI as sg
#sg.Window(title="Hello World", layout=[[]], margins=(200, 100)).read()
layout = [[sg.Text("Hello from PySimpleGUI")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Demo", layout, margins=(200,200))

# Create an event loop
while True:
    event, values= window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()