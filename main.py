#!/usr/bin/env python

import pygtk
import pango

pygtk.require('2.0')

from utils import *
from lib.apk import *
from menu import *

class ApkViewer(gtk.Window):

    APP_VERSION = 1.0
    APP_NAME = 'ApkViewer'

    def about_info(self, button):
        dialog = gtk.AboutDialog()
        dialog.set_program_name(self.APP_NAME)
        dialog.set_title('About')
        dialog.set_version(str(self.APP_VERSION))
        dialog.set_copyright("(c) Munish Katoch <katochmunish14@gmail.com>")
        dialog.connect("response", lambda d, r: d.destroy())
        dialog.show()

    def open_apk_file(self, button):
        apk_path = ApkViewer.get_apk_path()

        textbuffer = self.main_info_textview.get_buffer()
        start = textbuffer.get_start_iter()
        end = textbuffer.get_end_iter()
        textbuffer.remove_all_tags(start, end)
        textbuffer.set_text('')

        textbuffer = self.permission_textview.get_buffer()
        start = textbuffer.get_start_iter()
        end = textbuffer.get_end_iter()
        textbuffer.remove_all_tags(start, end)
        textbuffer.set_text('')

        textbuffer = self.signature_textview.get_buffer()
        start = textbuffer.get_start_iter()
        end = textbuffer.get_end_iter()
        textbuffer.remove_all_tags(start, end)
        textbuffer.set_text('')

        if apk_path is not '':
            self.set_apk_main_info(apk_path)
            self.set_apk_permission(apk_path)
            self.set_apk_signature(apk_path)

    def save_apk_info_file(self, button):
        apk_path = utils().save_file()
        text = ''
        if apk_path is not '':
            f = open(apk_path, 'w')
            start_iter = self.main_info_textview.get_buffer().get_start_iter()
            end_iter = self.main_info_textview.get_buffer().get_end_iter()
            text = self.main_info_textview.get_buffer().get_text(start_iter, end_iter, True)

            start_iter = self.permission_textview.get_buffer().get_start_iter()
            end_iter = self.permission_textview.get_buffer().get_end_iter()
            text += self.permission_textview.get_buffer().get_text(start_iter, end_iter, True)

            start_iter = self.signature_textview.get_buffer().get_start_iter()
            end_iter = self.signature_textview.get_buffer().get_end_iter()
            text += self.signature_textview.get_buffer().get_text(start_iter, end_iter, True)

            f.write(text)
            f.close()


    @staticmethod
    def get_apk_path():
        path = utils().select_file()
        return path

    def set_apk_main_info(self,path):
        apk_info = APK(path)
        textbuffer = self.main_info_textview.get_buffer()

        # heading
        h_tag = textbuffer.create_tag( size_points=14, weight=pango.WEIGHT_BOLD)

        if (apk_info.is_valid_APK()):
            xml = apk_info.axml
            position = textbuffer.get_end_iter()
            textbuffer.insert_with_tags(position, "Package name:\n", h_tag)
            position = textbuffer.get_end_iter()
            textbuffer.insert(position,str( apk_info.get_package()))

            position = textbuffer.get_end_iter()
            textbuffer.insert_with_tags(position, '\nAPK Version Name: \n', h_tag)
            position = textbuffer.get_end_iter()
            textbuffer.insert(position,str( apk_info.get_androidversion_name()))

            position = textbuffer.get_end_iter()
            textbuffer.insert_with_tags(position, '\nAPK Debuggable flag: \n', h_tag)
            position = textbuffer.get_end_iter()
            textbuffer.insert(position,str( apk_info.get_debuggable_flag()))

            position = textbuffer.get_end_iter()
            textbuffer.insert_with_tags(position, '\n\nAPK Md5: \n', h_tag)
            position = textbuffer.get_end_iter()
            textbuffer.insert(position,str( apk_info.file_md5))

            position = textbuffer.get_end_iter()
            textbuffer.insert_with_tags(position,'\nAPK Target SDK Version: \n', h_tag)
            position = textbuffer.get_end_iter()
            textbuffer.insert(position,str( apk_info.get_target_sdk_version()))

            position = textbuffer.get_end_iter()
            textbuffer.insert_with_tags(position,'\nAPK Libraries Used: \n', h_tag)
            apk_libraries = apk_info.get_libraries()
            for librarie in apk_libraries:
                position = textbuffer.get_end_iter()
                textbuffer.insert(position, str(librarie + '\n'))

            position = textbuffer.get_end_iter()
            textbuffer.insert_with_tags(position,'\nAPK Main Activity: \n', h_tag)
            position = textbuffer.get_end_iter()
            textbuffer.insert(position,str( apk_info.get_main_activity()))

            position = textbuffer.get_end_iter()
            textbuffer.insert_with_tags(position,'\n\nAPK Activities: \n', h_tag)
            apk_activities = apk_info.get_activities()
            for activitie in apk_activities:
                position = textbuffer.get_end_iter()
                textbuffer.insert(position, str(activitie + '\n'))

            position = textbuffer.get_end_iter()
            textbuffer.insert_with_tags(position,'\n\nAPK Services: \n', h_tag)
            apk_services = apk_info.get_services()
            for service in apk_services:
                position = textbuffer.get_end_iter()
                textbuffer.insert(position, str(service + '\n'))

            position = textbuffer.get_end_iter()
            textbuffer.insert_with_tags(position,'\n\nAPK Receivers: \n', h_tag)
            apk_receivers = apk_info.get_receivers()
            for receiver in apk_receivers:
                position = textbuffer.get_end_iter()
                textbuffer.insert(position, str(receiver + '\n'))

            position = textbuffer.get_end_iter()
            textbuffer.insert_with_tags(position,'\n\nAPK Providers: \n', h_tag)
            apk_providers = apk_info.get_providers()
            for provider in apk_providers:
                position = textbuffer.get_end_iter()
                textbuffer.insert(position, str(provider + '\n'))

            position = textbuffer.get_end_iter()
            textbuffer.insert_with_tags(position,'\n\nAPK XML: \n', h_tag)
            position = textbuffer.get_end_iter()
            textbuffer.insert(position,str( xml['AndroidManifest.xml'].buff))

        else:
            position = textbuffer.get_end_iter()
            textbuffer.insert_with_tags(position, "Invalid APK!!!", h_tag)

    def set_apk_permission(self,path):
        apk_info = APK(path)
        apk_permission = ''
        apk_dangerous_permission = ''
        apk_signatureOrSystem_permission = ''
        apk_signature_permission = ''
        apk_normal_permission = ''
        apk_other_permission = ''

        textbuffer = self.permission_textview.get_buffer()
        h_tag = textbuffer.create_tag(size_points=14, weight=pango.WEIGHT_BOLD)

        if (apk_info.is_valid_APK()):
            permission = apk_info.get_details_permissions()
            for p in permission:
                if permission[p][0] == 'dangerous':
                    apk_dangerous_permission += str(p + '  ' + permission[p][2] + '\n')
                elif permission[p][0] == 'signatureOrSystem':
                    apk_signatureOrSystem_permission += str(p + '  ' + permission[p][2] + '\n')
                elif permission[p][0] == 'signature':
                    apk_signature_permission += str(p + '  ' + permission[p][2] + '\n')
                elif permission[p][0] == 'normal':
                    apk_normal_permission += str(p + '  ' + permission[p][2] + '\n')
                else:
                    apk_other_permission += str(p + '  ' + permission[p][2] + '\n')


            if apk_dangerous_permission != '':
                position = textbuffer.get_end_iter()
                textbuffer.insert_with_tags(position, '\n Dangerous permission:  \n', h_tag)

                position = textbuffer.get_end_iter()
                textbuffer.insert(position, apk_dangerous_permission)

            if apk_signatureOrSystem_permission != '':
                position = textbuffer.get_end_iter()
                textbuffer.insert_with_tags(position, '\n signatureOrSystem permission:  \n', h_tag)

                position = textbuffer.get_end_iter()
                textbuffer.insert(position, apk_signatureOrSystem_permission)

            if apk_signature_permission != '':
                position = textbuffer.get_end_iter()
                textbuffer.insert_with_tags(position, '\n signature permission:  \n', h_tag)

                position = textbuffer.get_end_iter()
                textbuffer.insert(position, apk_signature_permission)
            elif apk_normal_permission != '':
                position = textbuffer.get_end_iter()
                textbuffer.insert_with_tags(position, '\n Normal permission:  \n', h_tag)

                position = textbuffer.get_end_iter()
                textbuffer.insert(position, apk_normal_permission)

            if apk_other_permission != '':
                position = textbuffer.get_end_iter()
                textbuffer.insert_with_tags(position, '\n Other permission:  \n', h_tag)

                position = textbuffer.get_end_iter()
                textbuffer.insert(position, apk_other_permission)

        else:
            position = textbuffer.get_end_iter()
            textbuffer.insert_with_tags(position, "Invalid APK!!!", h_tag)

    def set_apk_signature(self,path):
        apk_info = APK(path)
        apk_signature = ' '
        if apk_info.is_valid_APK():
            apk_signature = apk_info.cert_text
            apk_signature = apk_signature.replace('\x00', '').decode('utf-8', 'replace').encode('utf-8')

        else:
            apk_signature = "Invalid APK!!!"

        textbuffer = self.signature_textview.get_buffer()
        textbuffer.set_text(apk_signature)

    def destroy(self, widget, data=None):
        print "destroy signal occurred"
        gtk.main_quit()

    def __init__(self):
        super(ApkViewer, self).__init__()
        self.set_title(self.APP_NAME)
        self.set_size_request(1000, 1000)
        self.set_position(gtk.WIN_POS_CENTER)

        table = gtk.Table(1, 3, False)
        # Create a new notebook, place the position of the tabs
        notebook = gtk.Notebook()
        notebook.set_tab_pos(gtk.POS_TOP)
        table.attach(notebook, 0, 6, 0, 1)
        notebook.show()
        table.show_tabs = True
        table.show_border = True

        # Let's append a bunch of pages to the notebook
        for i in range(3):
            if i == 0:
                bufferf = "Main Info"
                label = gtk.Label(bufferf)
                self.main_info_textview = gtk.TextView()
                textview = self.main_info_textview
                textview.set_wrap_mode(gtk.WRAP_WORD)
                textview.set_editable(False)

            elif i == 1:
                bufferf = "Permission"
                label = gtk.Label(bufferf)
                self.permission_textview = gtk.TextView()
                textview = self.permission_textview
                textview.set_wrap_mode(gtk.WRAP_WORD)
                textview.set_editable(False)
            else:
                bufferf = "Signature"
                label = gtk.Label(bufferf)
                self.signature_textview = gtk.TextView()
                textview = self.signature_textview
                textview.set_wrap_mode(gtk.WRAP_WORD)
                textview.set_editable(False)



            frame = gtk.Frame(bufferf)
            frame.set_border_width(10)
            frame.set_size_request(100, 75)

            sw = gtk.ScrolledWindow()
            sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
            sw.add(textview)
            sw.show()

            frame.add(sw)
            textview.show()

            frame.show()

            label.set_selectable(True)
            # frame.add(label)
            # label.show()

            label = gtk.Label(bufferf)
            notebook.append_page(frame, label)



        notebook.set_current_page(0)

        toolbar = gtk.Toolbar()
        toolbar.set_style(gtk.TOOLBAR_ICONS)
        toolbar.set_orientation(gtk.ORIENTATION_HORIZONTAL)

        openbtn = gtk.ToolButton(gtk.STOCK_OPEN)
        savebtn = gtk.ToolButton(gtk.STOCK_SAVE)
        aboutbtn = gtk.ToolButton(gtk.STOCK_INFO)
        quitbtn = gtk.ToolButton(gtk.STOCK_QUIT)

        toolbar.insert(openbtn, 0)
        toolbar.insert(savebtn, 1)
        toolbar.insert(aboutbtn,2)
        toolbar.insert(quitbtn, 3)

        quitbtn.connect("clicked", gtk.main_quit)
        openbtn.connect("clicked", self.open_apk_file)
        savebtn.connect("clicked", self.save_apk_info_file)
        aboutbtn.connect("clicked", self.about_info)

        vbox = gtk.VBox(False, 2)
        vbox.pack_start(toolbar, False, False, 0)
        vbox.pack_end(table, True, True, 2)

        self.add(vbox)
        self.connect("destroy", gtk.main_quit)

        self.show_all()

ApkViewer()
gtk.main()
