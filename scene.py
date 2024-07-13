from abc import ABC, abstractmethod
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

        stdscr.refresh()

        stdscr.getch()