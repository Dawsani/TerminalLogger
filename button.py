from abc import ABC, abstractmethod
import curses

class Button(ABC):

    text = ""

    def __init__(self, text):
        self.text = '[' + text + ']'

    def display(self, stdscr, is_selected):
        if is_selected:
            stdscr.addstr(stdscr.getyx()[0], 0, self.text, curses.A_REVERSE)
        else:
            stdscr.addstr(stdscr.getyx()[0], 0, self.text)
        stdscr.move(stdscr.getyx()[0] + 1, 0)

    @abstractmethod
    def on_press():
        pass

class WriteLogButton(Button):
    def on_press():
        pass

class LogButton(Button):
    def on_press():
        pass