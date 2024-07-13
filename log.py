import curses
from button import Button, WriteLogButton, LogButton
from scene import Scene, MainMenuScene, WriteLogScene

logs = ["1/1/00 - Test", "1/2/00 - New Test!"]

def setup_scenes():
    scenes = []

    # Create the main menu
    main_menu_scene = MainMenuScene()
    write_log_scene = WriteLogScene()

    # Add scenes to the array
    scenes.append(main_menu_scene)
    scenes.append(write_log_scene)

    return scenes

def setup_buttons():
    # Define the buttons array
    buttons = []

    # Create the "new log" button
    write_log_button = WriteLogButton("CREATE NEW LOG")
    buttons.append(write_log_button)

    # Create a button for each existing log
    for log in logs:
        new_button = LogButton(log)
        buttons.append(new_button)

    return buttons

def main(stdscr):

    scenes = setup_scenes()
    buttons = setup_buttons()

    # Set the current scene index to 0 (main menu)
    current_scene_index = 0

    scenes[current_scene_index].display(stdscr, buttons)
            

if __name__ == "__main__":
    curses.wrapper(main)
