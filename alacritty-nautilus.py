#!/usr/bin/env python3

from gi import require_version
require_version('Gtk', '3.0')
require_version('Nautilus', '4.0')

from gi.repository import Nautilus, GObject
import os, subprocess

PROCESSNAME = 'alacritty'

class AlacrittyExtension(Nautilus.MenuProvider, GObject.GObject):
    def __init__(self):
        pass

    def launch_alacritty(self, menu: Nautilus.MenuItem, files):
        path = ''
        args = '--working-directory'

        for file in files:
            dirpath = file.get_location().get_path()
            if os.path.isdir(dirpath) and os.path.exists(dirpath):
                path = dirpath

        subprocess.Popen([PROCESSNAME, args, path], shell=False)

    def get_file_items(self, *args):
        files = args[-1]
        item = Nautilus.MenuItem(
            name="AlacrittyOpen",
            label="Open in Terminal",
            tip="Open the current directory in Terminal"
        )
        item.connect('activate', self.launch_alacritty, files)
        return [item]

    def get_background_items(self, *args):
        file_ = args[-1]
        item = Nautilus.MenuItem(
            name="AlacrittyOpenBackGround",
            label="Open in Terminal",
            tip="Open the current directory in Terminal"
        )
        item.connect('activate', self.launch_alacritty, [file_])
        return [item]
