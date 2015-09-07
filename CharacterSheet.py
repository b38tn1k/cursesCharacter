#!/usr/bin/env python
import curses
import pickle


class CharacterSheet(object):
    def __init__(self):
        self.bug = '*'
        self.nav_menu = ["Home", "Stats", "Weapons", "Combat", "Skills",  "Damage", "Notes","Benefits", "Gear", "Help","Armor", "Network", "Spells", "Companion", "Finance"]
        self.help = [['Help', '', 0], ['Quit', 'q', 1], ['Nav Up', 'k', 1], ['Nav Down', 'j',1], ['Nav Left', 'h', 1], ['Nav Right', 'l', 1], ['Edit Item', 'i', 1], ['New Item', 'n', 1], ['Delete Item', 'x', 1], ['Save', 'w', 1], ['Indent', 'tab', 1]]
        self.load_character('character_sheet')
        self.base_user_input = ''
        self.screen = curses.initscr()
        self.dims = self.screen.getmaxyx()
        sub_menu= self.home
        cursor = 1
        column = 1
        self.menu(sub_menu, cursor, column)
        indentation = 0
        while self.base_user_input != ord('q'):
            self.base_user_input = self.screen.getch()
            self.base_user_input = self.base_user_input
            if self.base_user_input == ord('1'):
                    sub_menu= self.home
            if self.base_user_input == ord('2'):
                sub_menu= self.stats
            if self.base_user_input == ord('3'):
                sub_menu = self.weapons
            if self.base_user_input == ord('4'):
                sub_menu = self.combat
            if self.base_user_input == ord('5'):
                sub_menu = self.skills
            if self.base_user_input == ord('6'):
                sub_menu = self.damage
            if self.base_user_input == ord('7'):
                sub_menu = self.notes
            if self.base_user_input == ord('8'):
                sub_menu = self.benefits
            if self.base_user_input == ord('9'):
                sub_menu = self.gear
            if self.base_user_input == ord('0'):
                sub_menu = self.help
            if self.base_user_input == ord('!'):
                sub_menu = self.armor
            if self.base_user_input == ord('@'):
                sub_menu = self.connections
            if self.base_user_input == ord('#'):
                sub_menu = self.spells
            if self.base_user_input == ord('$'):
                sub_menu = self.companion
            if self.base_user_input == ord('%'):
                sub_menu = self.finance
            if self.base_user_input == ord('j'):
                cursor += 1
            if self.base_user_input == ord('k'):
                cursor -= 1
            if self.base_user_input == ord('l'):
                column = int(self.dims[1]/2) + 1
            if self.base_user_input == ord('h'):
                column = 1
            if self.base_user_input == ord('w'):
                self.save_character('character_sheet')
            if self.base_user_input == ord('n'):
                self.add_item(sub_menu, cursor, indentation)
                cursor += 1
            if self.base_user_input == ord('x'):
                self.remove_item(sub_menu, cursor)
            if self.base_user_input == ord('i'):
                self.bug = '>'
                self.edit_item(sub_menu, cursor, column)
            if self.base_user_input == ord('\t'):
                indentation += 1
                self.indent_item(sub_menu, cursor, indentation)
            if cursor <= 0:
                cursor += len(sub_menu)-1
            if cursor >= len(sub_menu):
                cursor = 1
            self.menu(sub_menu, cursor, column)
        # self.save_character('character_sheet')
        curses.endwin()
        exit()

    def indent_item(self, sub_menu, cursor, indentation):
        sub_menu[cursor][2] = indentation%3+1
        self.screen.refresh()

    def remove_item(self, sub_menu, cursor):
        if len(sub_menu) != 1:
            sub_menu.pop(cursor)
            self.screen.refresh()

    def add_item(self, sub_menu, cursor, indentation):
        sub_menu.insert(cursor+1, ['New Item', '', indentation%3+1])
        self.screen.refresh()

    def edit_item(self, sub_menu, cursor, column):
        self.screen.refresh()
        self.menu(sub_menu, cursor, column) # blocks i character
        y = cursor + 2
        if column == 1:
            x = 3
            sub_menu[cursor][0] = self.get_input(sub_menu[cursor][0], y, x)
        else:
            x = int(3 + self.dims[1]/2)
            sub_menu[cursor][1] = self.get_input(sub_menu[cursor][1], y, x)
        self.bug = '*'
        self.screen.refresh()

    def get_input(self, prompt_string, y, x):
        # self.screen.addstr(2, 2, prompt_string.upper())
        # self.screen.refresh()
        input = self.screen.getstr(y, x, 60)
        return input

    def save_character(self, file_name):
        # dumb
        for facet in (self.home, self.stats, self.weapons, self.combat, self.skills, self.damage, self.notes, self.benefits, self.gear, self.armour, self.connections, self.spells, self.companion, self.finance):
            for characteristic in facet:
                for field in characteristic:
                    if not field.isdigit():
                        field = field.upper()
        file_object = open(file_name, 'wb')
        pickle.dump(self.home, file_object)
        pickle.dump(self.stats, file_object)
        pickle.dump(self.weapons, file_object)
        pickle.dump(self.combat, file_object)
        pickle.dump(self.skills, file_object)
        pickle.dump(self.damage, file_object)
        pickle.dump(self.notes, file_object)
        pickle.dump(self.benefits, file_object)
        pickle.dump(self.gear, file_object)
        pickle.dump(self.armor, file_object)
        pickle.dump(self.connections, file_object)
        pickle.dump(self.spells, file_object)
        pickle.dump(self.companion, file_object)
        pickle.dump(self.finance, file_object)
        file_object.close()

    def load_character(self, file_name):
        # Load a Synapse for reuse
        file_object = open(file_name, 'r')
        self.home = pickle.load(file_object)
        self.stats = pickle.load(file_object)
        self.weapons = pickle.load(file_object)
        self.combat = pickle.load(file_object)
        self.skills = pickle.load(file_object)
        self.damage = pickle.load(file_object)
        self.notes = pickle.load(file_object)
        self.benefits = pickle.load(file_object)
        self.gear = pickle.load(file_object)
        self.armor = pickle.load(file_object)
        self.connections = pickle.load(file_object)
        self.spells = pickle.load(file_object)
        self.companion = pickle.load(file_object)
        self.finance = pickle.load(file_object)
        file_object.close()

    def menu(self, menu_item, cursor, column):
        # MAIN MENU
        curses.curs_set(0)
        self.screen.refresh()
        self.screen.clear()
        x = 2
        rows = 5
        space = self.dims[1]/5
        y = self.dims[0] - 4
        for j, nav_item in enumerate(self.nav_menu[:10]):
            if j < rows:
                self.screen.addstr(y, x+space*j, ' {!s}: {!s}'.format(j+1, nav_item.upper()))
            else:
                if j == 9:
                    self.screen.addstr(y+1, x+space*(j-rows), ' 0: {!s}'.format(nav_item.upper()))
                else:
                    self.screen.addstr(y+1, x+space*(j-rows), ' {!s}: {!s}'.format(j+1, nav_item.upper()))
        y = self.dims[0] - 2
        for j, nav_item in enumerate(self.nav_menu[10:]):
            self.screen.addstr(y, x+space*j, '^{!s}: {!s}'.format(j+1, nav_item.upper()))
        x = 3
        y = 1
        for j, stat in enumerate(menu_item):
            if j == 0:
                self.screen.addstr(1, x, stat[0].upper())
            else:
                if j == cursor:
                    self.screen.addstr(cursor+2, column, self.bug)
                self.screen.addstr(j+2, x*stat[2], '{!s}:'.format(stat[0].upper()))
                self.screen.addstr(j+2, int(x+self.dims[1]/2), '{!s}'.format(stat[1].upper()))

    def new(self):
                self.home = [['Home', '', 0],['Name', 'Set Character Name', 1],['Sex', 'Set Character Sex', 1],['Defining Chacteristics', 'Set Defining Characteristics', 1],['Weight', 'Set Character Weight', 1],['Height', 'Set Character Height', 1],['Archetype', 'Set Character Archetype',1],['Race', 'Set Character Race',1],['Careers', 'Set Character Careers',1],['Faith', 'Set Character Faith',1],['Player', 'Set Character Player',1],['Level', 'Set Level',1]]
                self.weapons = [['Weapons', '', 0],['Ranged Weapons', '',1],['Weapon One', 'Set Weapon Name', 2],['AMMO', '', 3],['RNG', '', 3],['RAT', '', 3],['POW', '', 3],['Notes', '',3],['Weapon Two', 'Set Weapon Name', 2],['AMMO', '', 3],['RNG', '', 3],['RAT', '', 3],['POW', '', 3],['Notes', '',3],['Melee Weapons', '',1],['Weapon One', 'Set Weapon Name', 2], ['MAT', '', 3],['P+S', '', 3],['Notes', '',3],['Weapon Two', 'Set Weapon Name', 2],['MAT', '', 3],['P+S', '', 3],['Notes', '',3]]
                self.stats = [['Stats', '', 0], ['PHY', '', 1], ['MAX', '', 1], ['SPD', '', 2],['MAX', '', 2],['STR', '', 2],['MAX', '', 2],['AGI', '', 1], ['MAX', '', 1],['PRW', '', 2],['MAX', '', 2],['POI', '', 2],['MAX', '', 2],['INT', '', 1],['MAX', '', 1],['ARC', '', 2],['MAX', '', 2],['PER', '', 2],['MAX', '', 2],['Willpower', '', 1]]
                self.combat =[['Combat', '', 0], self.stats[3], ['AGI', '', 1], self.stats[17]]
                self.damage = [['Damage', '', 0]]
                self.skills = [['Skills', '', 0]]
                self.notes = [['Notes', '', 0]]
                self.benefits = [['Benefits', '', 0]]
                self.gear = [['Gear', '', 0]]
                self.armor = [['Armor', '', 0]]
                self.connections = [['Network', '', 0]]
                self.spells = [['Spells', '', 0]]
                self.companion = [['companion', '', 0]]
                self.finance = [['Finance', '', 0]]
                self.save_character('character')


character = CharacterSheet()
character.show()
