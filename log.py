import curses


logs = ["1/1/00 - Test", "1/2/00 - New Test!"]

def display_menu(stdscr):
    # Clear screen
    stdscr.clear()

    stdscr.addstr(stdscr.getyx()[0], 0, "Welcome to DAWS Industries (TM) Terminal Log", curses.color_pair(1))
    stdscr.move(stdscr.getyx()[0] + 1, 0)

    stdscr.addstr(stdscr.getyx()[0] + 1, 0, "[WRITE NEW LOG]", curses.color_pair(1))
    stdscr.move(stdscr.getyx()[0] + 2, 0)
    
    for i in range(len(logs)):
        log = '[' + logs[i] + ']'
        stdscr.addstr(stdscr.getyx()[0] + i, 0, log, curses.color_pair(1))

    stdscr.refresh()


def main(stdscr):
    # Initialize curses and set the color scheme
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    # Use the color pair for the background
    stdscr.bkgd(' ', curses.color_pair(1))

    display_menu(stdscr)

    # Wait for a key press
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
