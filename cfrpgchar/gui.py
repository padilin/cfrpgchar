import json

import PySimpleGUI as sg
from cfrpgchar.character import CFRPGChar

character_creation = [
    [sg.Text("What is your name?")],
    [sg.Input(key="name")],
    [sg.Checkbox("Can I rage?", key="rage_ability")],
    [sg.Text(size=(40, 1), key="-OUTPUT-")],
    [sg.Button("Submit")],
    [sg.FileBrowse("Load Char", key="loaded_sheet", enable_events=True)]
]

character_stats = [
    [sg.Multiline("", size=(80, 25), key="CharacterStats")],
    [sg.Button("Save"), sg.FileBrowse("Load Char", key="loaded_sheet", enable_events=True)]
]

layout = [
    [sg.Column(character_creation, visible=True, key="cc"), sg.Column(character_stats, visible=False, key="cs")],
    [sg.Button("Quit")]
]


window = sg.Window("Character", layout)
charload = None

while True:
    event, values = window.read()
    print(f"{event} {values}")

    if event == sg.WINDOW_CLOSED or event == "Quit":
        break

    if event == "loaded_sheet":
        with open(values["loaded_sheet"], 'r') as json_file:
            json_data = json.load(json_file)
            charload = CFRPGChar(**json_data)
        window["cc"].update(visible=False)
        window["cs"].update(visible=True)
        window["CharacterStats"].update(f"{charload.name}\nStrength: {charload.strength} \nDex: {charload.dexterity}")

    if event == "Save":
        with open(f"../data/{charload.name}.json", "w") as json_file:
            json.dump(charload.__dict__, json_file)

    if event == "Submit":
        charload = CFRPGChar(values["name"], rage_ability=values["rage_ability"])
        window["cc"].update(visible=False)
        window["cs"].update(visible=True)
        window["CharacterStats"].update(f"{charload.name}\nStrength: {charload.strength} \nDex: {charload.dexterity}")

window.close()
