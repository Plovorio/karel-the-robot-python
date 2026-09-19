### KAREL THE ROBOT  PYTHON – EDITION ###
### AUTHOR PLOVORIO ###

import PySimpleGUI as sg
from assets import karel_sprites, field_asset, marker_sprites

base_commands = ["STEP", "LEFT_FACE", "PUT-HERE", "TAKE-HERE"]

# DEFAULT
karel_x = 0
karel_y = 9
karel_direction = "right"

field_width = 10
field_height = 10
field = []
markers = {}

for y in range(field_height):
    row = []

    for x in range(field_width):

        if x == karel_x and y == karel_y:
            image = karel_sprites[karel_direction]
        else:
            image = field_asset

        row.append(
            sg.Image(
                filename=image,
                pad=(0, 0),
                key=f"FIELD_{x}_{y}"
            )
        )

    field.append(row)

layout = [
    [sg.Text("Town")],
    [*field],
    [sg.Button(base_commands[0])],
    [sg.Button(base_commands[1])],
    [sg.Button(base_commands[2])],
    [sg.Button(base_commands[3])],
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
                print("Karel se pohnul v ose X o 1!")
                position = (karel_x, karel_y)
                position_old = (old_x, karel_y)

                marker_count = markers.get(position_old, 0)
                if marker_count >= 1:
                        window[f"FIELD_{old_x}_{karel_y}"].update(
                        filename=marker_sprites[marker_count]["field_asset"]
                        )
                else:
                        window[f"FIELD_{old_x}_{karel_y}"].update(
                        filename=field_asset
                        )   

                marker_count = markers.get(position, 0)
                if marker_count >= 1:
                        window[f"FIELD_{karel_x}_{karel_y}"].update(
                        filename=marker_sprites[marker_count][karel_direction]
                        )
                else:
                        window[f"FIELD_{karel_x}_{karel_y}"].update(
                        filename=karel_sprites[karel_direction]
                        )   
             else:
                print(f"Nemůžu učinit {base_commands[0]}, přede mnou je zeď.")


        elif karel_direction == "left":
            if karel_x > 0:
                old_x = karel_x
                karel_x -= 1
                print("Karel se pohnul v ose X o -1!")
                position = (karel_x, karel_y)
                position_old = (old_x, karel_y)
                
                marker_count = markers.get(position_old, 0)
                if marker_count >= 1:
                        window[f"FIELD_{old_x}_{karel_y}"].update(
                        filename=marker_sprites[marker_count]["field_asset"]
                        )
                else:
                        window[f"FIELD_{old_x}_{karel_y}"].update(
                        filename=field_asset
                        )  

                marker_count = markers.get(position, 0)
                if marker_count >= 1:
                        window[f"FIELD_{karel_x}_{karel_y}"].update(
                        filename=marker_sprites[marker_count][karel_direction]
                        )
                else:
                        window[f"FIELD_{karel_x}_{karel_y}"].update(
                        filename=karel_sprites[karel_direction]
                        )            
            else:
                print(f"Nemůžu učinit {base_commands[0]}, přede mnou je zeď.")


        elif karel_direction == "front":
            if karel_y < 9:
                old_y = karel_y
                karel_y += 1
                print("Karel se pohnul v ose Y o 1!")
                position = (karel_x, karel_y)
                position_old = (karel_x, old_y)
                
                marker_count = markers.get(position_old, 0)
                if marker_count >= 1:
                        window[f"FIELD_{karel_x}_{old_y}"].update(
                        filename=marker_sprites[marker_count]["field_asset"]
                        )
                else:
                        window[f"FIELD_{karel_x}_{old_y}"].update(
                        filename=field_asset
                        )  

                marker_count = markers.get(position, 0)
                if marker_count >= 1:
                        window[f"FIELD_{karel_x}_{karel_y}"].update(
                        filename=marker_sprites[marker_count][karel_direction]
                        )
                else:
                        window[f"FIELD_{karel_x}_{karel_y}"].update(
                        filename=karel_sprites[karel_direction]
                        )        
            else:
                print(f"Nemůžu učinit {base_commands[0]}, přede mnou je zeď.")

        elif karel_direction == "back":
            if karel_y > 0:
                old_y = karel_y
                karel_y -= 1
                print("Karel se pohnul v ose Y o -1!")
                position = (karel_x, karel_y)
                position_old = (karel_x, old_y)
                
                marker_count = markers.get(position_old, 0)
                if marker_count >= 1:
                        window[f"FIELD_{karel_x}_{old_y}"].update(
                        filename=marker_sprites[marker_count]["field_asset"]
                        )
                else:
                        window[f"FIELD_{karel_x}_{old_y}"].update(
                        filename=field_asset
                        )  

                marker_count = markers.get(position, 0)
                if marker_count >= 1:
                        window[f"FIELD_{karel_x}_{karel_y}"].update(
                        filename=marker_sprites[marker_count][karel_direction]
                        )
                else:
                        window[f"FIELD_{karel_x}_{karel_y}"].update(
                        filename=karel_sprites[karel_direction]
                        )        
            else:
                print(f"Nemůžu učinit {base_commands[0]}, přede mnou je zeď.")

        else: 
            print("Jiná direction neexistuje :skull: !")

    if event == base_commands[1]:
        if karel_direction == "right":
            karel_direction = "back"
            
            position = (karel_x, karel_y)   
            marker_count = markers.get(position, 0)

            if marker_count >= 1:
                    window[f"FIELD_{karel_x}_{karel_y}"].update(
                    filename=marker_sprites[marker_count][karel_direction]
                    )
            else:
                    window[f"FIELD_{karel_x}_{karel_y}"].update(
                    filename=karel_sprites[karel_direction]
                    )     
            print("Karel se otočil dopředu.")
        elif karel_direction == "back":
            karel_direction = "left"

            position = (karel_x, karel_y)   
            marker_count = markers.get(position, 0)

            if marker_count >= 1:
                    window[f"FIELD_{karel_x}_{karel_y}"].update(
                    filename=marker_sprites[marker_count][karel_direction]
                    )
            else:
                    window[f"FIELD_{karel_x}_{karel_y}"].update(
                    filename=karel_sprites[karel_direction]
                    )    
            print("Karel se otočil vlevo.")
        elif karel_direction == "left":
            karel_direction = "front"

            position = (karel_x, karel_y)   
            marker_count = markers.get(position, 0)

            if marker_count >= 1:
                    window[f"FIELD_{karel_x}_{karel_y}"].update(
                    filename=marker_sprites[marker_count][karel_direction]
                    )
            else:
                    window[f"FIELD_{karel_x}_{karel_y}"].update(
                    filename=karel_sprites[karel_direction]
                    )  
            print("Karel se otočil dozadu.")
        elif karel_direction == "front":
            karel_direction = "right"

            position = (karel_x, karel_y)   
            marker_count = markers.get(position, 0)

            if marker_count >= 1:
                    window[f"FIELD_{karel_x}_{karel_y}"].update(
                    filename=marker_sprites[marker_count][karel_direction]
                    )
            else:
                    window[f"FIELD_{karel_x}_{karel_y}"].update(
                    filename=karel_sprites[karel_direction]
                    )  
            print("Karel se otočil doprava.")
        else:
            print("k tomu nikdy nedojde, leda by nastala chyba v matrixu!")

    if event == base_commands[2]:
        position = (karel_x, karel_y)
        if markers.get(position) != 4:
            markers[position] = markers.get(position, 0) + 1
            marker_count = markers.get(position, 0)
            if marker_count > 0:
                    window[f"FIELD_{karel_x}_{karel_y}"].update(
                    filename=marker_sprites[marker_count][karel_direction]
                    )
        else:
            print("Nemohu položit více jak 4 značky.")

    if event == base_commands[3]:
        position = (karel_x, karel_y)
        if markers.get(position, 0) > 0:
            markers[position] -= 1
            marker_count = markers.get(position, 0)
            if marker_count > 0:
                    window[f"FIELD_{karel_x}_{karel_y}"].update(
                    filename=marker_sprites[marker_count][karel_direction]
                    )
            elif marker_count == 0:
                window[f"FIELD_{karel_x}_{karel_y}"].update(
                filename=karel_sprites[karel_direction]
                )
                del markers[position]

        else:
            print("Na políčku nejsou žádné značky.")
        
    if event == sg.WIN_CLOSED or event == "CLOSE":
        print("Karel The Robot has been closed.")
        break
    print(markers)

window.close()