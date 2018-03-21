import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject
import time

class SaveProject(Gtk.Dialog):

    def __init__(self, parent):
        Gtk.Dialog.__init__(self, "Save Project", parent, 0,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OK, Gtk.ResponseType.OK))

        self.set_default_size(250, 200)

class SaveProject(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Save Project")

        self.set_border_width(6)

        label = Gtk.Label("The project is saving.")
        quitLabel = Gtk.Label("Close window when saving has completed so data is not lost.")

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(self.box)

        self.progressbar = Gtk.ProgressBar()

        self.box.pack_start(label, True, True, 5)
        self.box.pack_start(quitLabel, True, True, 5)
        self.box.pack_start(self.progressbar, True, True, 5)
       
        self.timeout_id = GObject.timeout_add(50, self.on_timeout, None)
        self.activity_mode = False

    def on_timeout(self, user_data):
        """
        Update value on the progress bar
        """
        if self.activity_mode:
            self.progressbar.pulse()
        else:
            new_value = self.progressbar.get_fraction() + 0.03

            self.progressbar.set_fraction(new_value)

        # As this is a timeout function, return True so that it
        # continues to get called

        return True

'''
win = SaveProject()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
'''