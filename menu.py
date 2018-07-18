import pygtk

import gtk

pygtk.require('2.0')

class menu(gtk.Window):
    def init_menu(self):
        # ---------- MENU BAR-------------#
        menu_bar = gtk.MenuBar()
        # Devices Menu option
        self.menu = gtk.Menu()

        root_menu = gtk.MenuItem("Open APK")
        root_menu.show()
        root_menu.set_submenu(self.menu)
        menu_bar.append(root_menu)


        # Insert menu option
        self.quit = gtk.Menu()
        root_menu = gtk.MenuItem("Quit")
        root_menu.show()
        root_menu.set_submenu(self.quit)
        menu_bar.append(root_menu)

        menu_bar.show()
        return menu_bar;
