import curses

def main():

    stdscr=curses.initscr()
    curses.noecho()
    stdscr.keypad(True)

    max_y, max_x = stdscr.getmaxyx()
    window = curses.newwin(19, 46, int((max_y/2)-9), int((max_x/2)-23))
    window_2 = curses.newwin(5, 46, int((max_y/2)+10), int((max_x/2)-23))
    window.keypad(1)
    curses.curs_set(2)

    window.border(0)
    window_2.border(0)

    run_gui = GUI(window, window_2)
    run_gui.render_gui()

    window.noutrefresh()
    window_2.noutrefresh()
    curses.doupdate()


    cursor1 = Cursor(window, window_2)
    cursor1.cursor_set_position()

    running = True
    run_gui.render_massaging('--> ESC zum beenden <--')
    while running:
        key = window.getch()
        if key == 27:
            running = False
            break

    curses.endwin()

class GUI(object):
    def __init__(self, window, window_2):
        self.window = window
        self.window_2 = window_2

    def render_gui(self):
        self.window.addstr(0, 20, 'SUDOKU')

        for y in range(1, 18):
            for x in range(1, 45, 5):
                if (y % 2 != 0) and ((x-1) % 5 == 0) and (x != 1):
                    if ((x-1) == 15) or ((x -1 )== 30):
                        self.window.addstr(y, x-1, '|', curses.A_BOLD)
                    else:
                        self.window.addstr(y, x-1, '|')

                elif (y % 2 == 0) and (x <= 40):
                    if (y % 3 == 0):     
                        self.window.addstr(y, x, '----+', curses.A_BOLD)
                    else:
                        self.window.addstr(y, x, '----+')

                elif (y % 2 == 0) and (x > 40):
                    if (y % 3 == 0):
                        self.window.addstr(y, x, '----', curses.A_BOLD)
                    else:
                        self.window.addstr(y, x, '----')

    def render_massaging(self, massage):
        self.massage = massage
        for y in range (1, 3):
            for x in range (1, 45):
                self.window_2.addstr(y, x, ' ')

        x_write_point = int((46-len(self.massage))/2)
        self.window_2.addstr(1, x_write_point, self.massage)
        self.window_2.noutrefresh()
        curses.doupdate()

class Cursor(object):

    def __init__(self, window, window_2):
        self.x_start = 2
        self.y_start = 1
        self.window = window
        self.window.move(self.y_start, self.x_start)
        curses.curs_set(2)
        self.run_gui = GUI(window, window_2)
        self.run_gui.render_massaging('--> to calc or end press ENTER  <--')


    def cursor_set_position(self):
        
        self.running = True
        self.x_running = self.x_start
        self.y_running = self.y_start
        while self.running == True:

            self.key = self.window.getkey()

            if self.key == '1':
                self.cursor_write()

            if self.key == '2':
                self.cursor_write()

            if self.key == '3':
                self.cursor_write()

            if self.key == '4':
                self.cursor_write()

            if self.key == '5':
                self.cursor_write()

            if self.key == '6':
                self.cursor_write()

            if self.key == '7':
                self.cursor_write()

            if self.key == '8':
                self.cursor_write()

            if self.key == '9':
                self.cursor_write()

            if self.key == '\x7f':
                self.cursor_delete()

            if self.key == '\n':
                self.running = False
                break

            if self.key == 'KEY_DOWN':
                self.y_running = self.y_running + 2

                if self.y_running >= 19:
                    self.y_running = self.y_start

                self.window.move(self.y_running, self.x_running)

            if self.key == 'KEY_UP':
                self.y_running = self.y_running - 2

                if self.y_running <= 0:
                    self.y_running = 0
                    self.y_running = self.y_running + 17
                    
                self.window.move(self.y_running, self.x_running)

            if self.key == 'KEY_LEFT':
                self.x_running = self.x_running - 5

                if self.x_running <= 0:
                    self.x_running = 0
                    self.x_running = self.x_running + 42

                self.window.move(self.y_running, self.x_running)

            if self.key == 'KEY_RIGHT':
                self.x_running = self.x_running + 5

                if self.x_running >= 46:
                    self.x_running = self.x_start

                self.window.move(self.y_running, self.x_running)

    def cursor_write(self):
        self.window.addstr(self.y_running, self.x_running, self.key)
        self.window.move(self.y_running, self.x_running)

    def cursor_delete(self):
        self.window.addstr(self.y_running, self.x_running, ' ')
        self.window.move(self.y_running, self.x_running)


if __name__ == '__main__':
    main()
