import os
import platform
import subprocess
import pygtk
pygtk.require('2.0')
import gtk

import time

class utils:

    def select_file(self):
        file_path = ''
        if gtk.pygtk_version < (2, 3, 90):
            print "PyGtk 2.3.90 or later required for this example"
            raise SystemExit

        dialog = gtk.FileChooserDialog("Open..",
                                       None,
                                       gtk.FILE_CHOOSER_ACTION_OPEN,
                                       (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                        gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)

        filter = gtk.FileFilter()
        filter.set_name("All files")
        filter.add_pattern("*.apk")
        dialog.add_filter(filter)

        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            print dialog.get_filename(), 'selected'
            file_path = dialog.get_filename()
        elif response == gtk.RESPONSE_CANCEL:
            print 'Closed, no files selected'
        dialog.destroy()

        return file_path

    def save_file(self):
        file_path = ''
        # Check for new pygtk: this is new class in PyGtk 2.4
        if gtk.pygtk_version < (2, 3, 90):
            print "PyGtk 2.3.90 or later required for this example"
            raise SystemExit

        dialog = gtk.FileChooserDialog("Save..",
                                       None,
                                       gtk.FILE_CHOOSER_ACTION_SAVE,
                                       (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                        gtk.STOCK_SAVE, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)

        filter = gtk.FileFilter()
        filter.set_name("All files")
        dialog.add_filter(filter)

        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            print dialog.get_filename(), 'selected'
            file_path = dialog.get_filename()
        elif response == gtk.RESPONSE_CANCEL:
            print 'Closed, no files selected'
        dialog.destroy()

        return file_path
