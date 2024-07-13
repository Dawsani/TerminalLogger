import curses
from button import Button, WriteLogButton, LogButton
from scene import Scene, MainMenuScene, WriteLogScene

logs = ["1/1/00 - Test", "1/2/00 - New Test!"]

class Logger:

    # Set the current scene index to 0 (main menu)
    current_scene_index = 0

    def __init__(self):
        self.scenes = self.setup_scenes()
        self.buttons = self.setup_buttons()

    def get_buttons(self):
        return self.buttons

    def setup_scenes(self):
        scenes = []

        # Create the main menu
        main_menu_scene = MainMenuScene(self)
        write_log_scene = WriteLogScene(self)

        # Add scenes to the array
        scenes.append(main_menu_scene)
        scenes.append(write_log_scene)

        return scenes

    def setup_buttons(self):
        # Define the buttons array
        buttons = []

        # Create the "new log" button
        write_log_button = WriteLogButton("CREATE NEW LOG", self)
        buttons.append(write_log_button)

        # Create a button for each existing log
        for log in logs:
            new_button = LogButton(log, self)
            buttons.append(new_button)

        return buttons
    
    def set_current_scene_index(self, index):
        self.current_scene_index = index

    def main(self, stdscr):

        quit_program = False

        while not quit_program:
            self.scenes[self.current_scene_index].display(stdscr)
                

logger = Logger()        
curses.wrapper(logger.main)
