from abc import ABC, abstractmethod
from curses.textpad import Textbox, rectangle
import curses

class Scene(ABC):
    def __init__(self, logger):
        self.logger = logger

    @abstractmethod
    def display(self, stdscr):
        pass

class MainMenuScene(Scene):

    # The index of the currently selected option
    selection_index = 0

    def display(self, stdscr):

        # Clear the screen
        stdscr.clear()

        # Display the welcome text
        stdscr.addstr(stdscr.getyx()[0], 0, "Welcome to DAWS Industries (TM) Terminal Log")

        # Move the curser down two lines
        stdscr.move(stdscr.getyx()[0] + 2, 0)

        buttons = self.logger.get_buttons()

        # Display all buttons
        for i in range(len(buttons)):
            is_selected = False
            if i == self.selection_index:
                is_selected = True

            button = buttons[i]
            button.display(stdscr, is_selected)

        stdscr.refresh()

        # Wait for user input
        key = stdscr.getch()

        # Check if the down arrow key is pressed
        if key == curses.KEY_DOWN:
            self.selection_index += 1
        elif key == curses.KEY_UP:
            self.selection_index -= 1
        elif key == 10:
            buttons[self.selection_index].on_press()


                
class WriteLogScene(Scene):
    def display(self, stdscr):
        # Clear the screen
        stdscr.clear()

        # Display the welcome text
        stdscr.addstr(stdscr.getyx()[0], 0, "Welcome to DAWS Industries (TM) Terminal Log")

        # Move the curser down two lines
        stdscr.move(stdscr.getyx()[0] + 2, 0)

        width = stdscr.getmaxyx()[1]
        height = stdscr.getmaxyx()[0]

        editwin = curses.newwin(height - 3, width - 3, 2,1)

        rectangle(stdscr, 1, 0, height - 1, width - 2)

        stdscr.refresh()

        box = Textbox(editwin)

        # Let the user edit until Ctrl-G is struck.
        box.edit()

        # Get resulting contents
        message = box.gather()

        self.logger.set_current_scene_index(0)
        
