import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class PaletteWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Palette")


    


win = PaletteWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()