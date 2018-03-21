import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class DissectorBuilderAreaWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Dissector Builder Area")

        # Creates Big Box
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(self.box)

        # Middle Box
        vbox_middle = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        vbox_middle.set_homogeneous(False)

        # Center Column 1 Box In Middle Box
        vbox_center_1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        vbox_center_1.set_homogeneous(False)

        # Center Column 2 Box In Middle Box
        vbox_center_2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        vbox_center_2.set_homogeneous(False)

        # Stores boxes into big box
        vbox_middle.pack_start(vbox_center_1, True, True, 5)
        vbox_middle.pack_start(vbox_center_2, True, True, 5)
        self.box.pack_start(vbox_middle, True, True, 5)


win = DissectorBuilderAreaWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()