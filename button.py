from abc import ABC, abstractmethod
import curses

class Button(ABC):
    def __init__(self, text, logger):
        self.text = '[' + text + ']'
        self.logger = logger

    def display(self, stdscr, is_selected):
        if is_selected:
            stdscr.addstr(stdscr.getyx()[0], 0, self.text, curses.A_REVERSE)
        else:
            stdscr.addstr(stdscr.getyx()[0], 0, self.text)
        stdscr.move(stdscr.getyx()[0] + 1, 0)

    @abstractmethod
    def on_press(self):
        pass

class WriteLogButton(Button):
    def on_press(self):
        self.logger.set_current_scene_index(1)

class LogButton(Button):
    def on_press(self):
        pass