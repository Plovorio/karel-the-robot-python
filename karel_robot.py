### KAREL THE ROBOT  PYTHON – EDITION ###
### AUTHOR PLOVORIO ###

import PySimpleGUI as sg

base_commands = ["STEP", "LEFT_FACE", "PUT-HERE", "TAKE-HERE"]

# DEFAULT
karel_x = 0
karel_y = 0
karel_direction = "right"

#ASSETS OF ROBOT
karel_sprites = { "right": "assets/sprites/karel_right.png", 
"left": "assets/sprites/karel_left.png", 
"front": "assets/sprites/karel_front.png", 
"back": "assets/sprites/karel_back.png" }

field_width = 10
field_height = 10
field = []

for y in range(field_height):
    row = []

    for x in range(field_width):

        if x == karel_x and y == karel_y:
            image = karel_sprites[karel_direction]
        else:
            image = "assets/field.png"

        row.append(
            sg.Image(
                filename=image,
                pad=(0, 0),
                key=f"FIELD_{x}_{y}"
            )
        )

    field.append(row)
    row = []

layout = [
    [sg.Text("Town")],
    [*field],
    [sg.Button(base_commands[0])],
    [sg.Button(base_commands[1])],
    [sg.Button("CLOSE")]
]

window = sg.Window("Karel The Robot", layout, margins=(10, 10))

while 1:
    event, values = window.read()

    if event == base_commands[0]:
        if karel_direction == "right":
             if karel_x < 9:
                old_x = karel_x
                karel_x += 1

                window[f"FIELD_{old_x}_{karel_y}"].update(
                filename="assets/field.png"
                )

                window[f"FIELD_{karel_x}_{karel_y}"].update(
                filename=karel_sprites[karel_direction]
                )
             else:
                print(f"Nemůžu učinit {base_commands[0]}, přede mnou je zeď.")

             print("Karel se pohnul v ose X o 1!")
        elif karel_direction == "left":
            if karel_x > 0:
                old_x = karel_x
                karel_x -= 1
                window[f"FIELD_{old_x}_{karel_y}"].update(
                filename="assets/field.png"
                )

                window[f"FIELD_{karel_x}_{karel_y}"].update(
                filename=karel_sprites[karel_direction]
                )
            else:
                print(f"Nemůžu učinit {base_commands[0]}, přede mnou je zeď.")

            print("Karel se pohnul v ose X o -1!")
        elif karel_direction == "front":
            if karel_y < 9:
                old_y = karel_y
                karel_y += 1
                window[f"FIELD_{karel_x}_{old_y}"].update(
                    filename="assets/field.png"
                )

                window[f"FIELD_{karel_x}_{karel_y}"].update(
                     filename=karel_sprites[karel_direction]
                )
            else:
                print(f"Nemůžu učinit {base_commands[0]}, přede mnou je zeď.")
            print("Karel se pohnul v ose Y o 1!")
        elif karel_direction == "back":
            if karel_y > 0:
                old_y = karel_y
                karel_y -= 1
                window[f"FIELD_{karel_x}_{old_y}"].update(
                    filename="assets/field.png"
                )

                window[f"FIELD_{karel_x}_{karel_y}"].update(
                    filename=karel_sprites[karel_direction]
                )
            else:
                print(f"Nemůžu učinit {base_commands[0]}, přede mnou je zeď.")
            print("Karel se pohnul v ose Y o -1!")
        else: 
            print("Jiná direction neexistuje :skull: !")

    if event == base_commands[1]:
        if karel_direction == "right":
            karel_direction = "back"
            window[f"FIELD_{karel_x}_{karel_y}"].update(
            filename=karel_sprites[karel_direction]
            )
            print("Karel se otočil dopředu.")
        elif karel_direction == "back":
            karel_direction = "left"
            window[f"FIELD_{karel_x}_{karel_y}"].update(
            filename=karel_sprites[karel_direction]
            )
            print("Karel se otočil vlevo.")
        elif karel_direction == "left":
            karel_direction = "front"
            window[f"FIELD_{karel_x}_{karel_y}"].update(
            filename=karel_sprites[karel_direction]
            )
            print("Karel se otočil dozadu.")
        elif karel_direction == "front":
            karel_direction = "right"
            window[f"FIELD_{karel_x}_{karel_y}"].update(
            filename=karel_sprites[karel_direction]
            )
            print("Karel se otočil doprava.")
        else:
            print("k tomu nikdy nedojde, leda by nastala chyba v matrixu!")

    if event == sg.WIN_CLOSED or event == "CLOSE":
        print("Karel The Robot has been closed.")
        break

window.close()