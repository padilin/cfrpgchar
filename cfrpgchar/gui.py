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


character_landing = sg.Window("Character Landing", character_creation)
character_stats_active = False

character_loaded = None


def open_character_sheet(character_loaded):
    character_stats_active = True
    character_landing.hide()

    character_stats = [
        [sg.Text(character_loaded.character_sheet_header(), size=(5, 5), key="CharHeader")],
        [sg.VPush(), sg.Multiline(character_loaded.character_sheet_base_abilities(), size=(80, 25), key="CharBaseAbility")],
        [sg.Button("Save"), sg.FileBrowse("Load Char", key="load_sheet", enable_events=True)],
        [sg.Button("Close", key="close_sheet")]
    ]
    character_stats = sg.Window("Character Stats", character_stats, element_justification='c')
    while True:
        event2, values2 = character_stats.Read()
        if event2 == "close_sheet" or event2 == "Exit":
            character_stats.Close()
            character_stats_active = False
            character_landing.UnHide()
            break

        if event1 == "Save":
            with open(f"../data/{character_loaded.name}.json", "w") as json_file:
                json.dump(character_loaded.__dict__, json_file)

        if event1 == "load_sheet":
            with open(values1["load_sheet"], 'r') as json_file:
                json_data = json.load(json_file)
                character_loaded = CFRPGChar(**json_data)
                character_stats["CharHeader"].update(character_loaded.character_sheet_header())
                character_stats["CharBaseAbility"].update(character_loaded.character_sheet_base_abilities())

    character_stats.Close()


while True:
    event1, values1= character_landing.Read()
    if event1 == sg.WINDOW_CLOSED or event1 == "Quit":
        break

    if event1 == "loaded_sheet":
        with open(values1["loaded_sheet"], 'r') as json_file:
            json_data = json.load(json_file)
            character_loaded = CFRPGChar(**json_data)
        open_character_sheet(character_loaded)

    if event1 == "Submit":
        character_loaded = CFRPGChar(values1["name"], rage_ability=values1["rage_ability"])
        open_character_sheet(character_loaded)

character_landing.close()
