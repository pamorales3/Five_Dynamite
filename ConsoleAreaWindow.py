import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ConsoleAreaWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Console Area")

        # Creates Big Box
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(box)

        errorLabel = Gtk.Label("No error message to show.")
        box.pack_start(errorLabel, True, True, 0)
    

win = ConsoleAreaWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()