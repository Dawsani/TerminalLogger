from abc import ABC, abstractmethod

class Scene(ABC):
    @abstractmethod
    def display(self, stdscr):
        pass

class MainMenuScene(Scene):
    def display(self, stdscr, buttons, selection_index):
        # Clear the screen
        stdscr.clear()

        # Display the welcome text
        stdscr.addstr(stdscr.getyx()[0], 0, "Welcome to DAWS Industries (TM) Terminal Log")

        # Move the curser down two lines
        stdscr.move(stdscr.getyx()[0] + 2, 0)

        # Display all buttons
        for i in range(len(buttons)):
            is_selected = False
            if i == selection_index:
                is_selected = True

            button = buttons[i]
            button.display(stdscr, is_selected)

        stdscr.refresh()
                
class WriteLogScene(Scene):
    def display(self, stdscr):
        # Clear the screen
        stdscr.clear()

        # Display the welcome text
        stdscr.addstr(stdscr.getyx()[0], 0, "Welcome to DAWS Industries (TM) Terminal Log")

        # Move the curser down two lines
        stdscr.move(stdscr.getyx()[0] + 2, 0)