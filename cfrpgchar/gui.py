import PySimpleGUI as sg
from cfrpgchar.character import CFRPGChar

character_creation = [
    [sg.Text("What is your name?")],
    [sg.Input(key="name")],
    [sg.Checkbox("Can I rage?", key="rage_ability")],
    [sg.Text(size=(40, 1), key="-OUTPUT-")],
    [sg.Button("Submit")],
]

character_stats = [
    [sg.Multiline("", size=(80, 25), key="CharacterStats")]
]

layout = [
    [sg.Column(character_creation, visible=True, key="cc"), sg.Column(character_stats, visible=False, key="cs")],
    [sg.Button("Quit")]
]


window = sg.Window("Character", layout)
while True:
    event, values = window.read()
    charload = None

    if event == sg.WINDOW_CLOSED or event == "Quit":
        break

    if event == "Submit":
        charload = CFRPGChar(values["name"], rage_ability=values["rage_ability"])
        window["cc"].update(visible=False)
        window["cs"].update(visible=True)
        window["CharacterStats"].update(f"{charload.name}\nStrength: {charload.strength} \nDex: {charload.dexterity}")

window.close()
