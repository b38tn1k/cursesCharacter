import curses


class cursedMaze(object):
    def __init__(self, verbose):
        self.verbose = verbose
        self.screen = curses.initscr()
        self.dims = self.screen.getmaxyx()
        curses.curs_set(0)
        self.refresh = self.screen.refresh()
        self.screen.clear()
        self.base_user_input = ' '
        while self.base_user_input != ord('q'):
              self.base_user_input = self.screen.getch()
              self.base_user_input = self.base_user_input
        curses.endwin()
        exit()

maze = cursedMaze(True)
