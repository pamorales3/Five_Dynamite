import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class PacketInfoFieldWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Packet Information")

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

        # Bottom Box
        vbox_bottom = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        vbox_bottom.set_homogeneous(False)

        # Stores boxes into big box
        vbox_middle.pack_start(vbox_center_1, True, True, 5)
        vbox_middle.pack_start(vbox_center_2, True, True, 5)
        self.box.pack_start(vbox_middle, True, True, 5)
        self.box.pack_start(vbox_bottom, True, True, 5)

         # Value Label
        valueLabel = Gtk.Label("Value")
        valueLabel.set_justify(Gtk.Justification.CENTER)
        vbox_center_1.pack_start(valueLabel, True, True, 5)

        # Text Description Label
        textDescriptionLabel = Gtk.Label("Text Description")
        textDescriptionLabel.set_justify(Gtk.Justification.CENTER)
        vbox_center_2.pack_start(textDescriptionLabel, True, True, 5)


        # Value Entry Field
        valueEntry = Gtk.Entry()
        vbox_center_1.pack_start(valueEntry, True, True, 5)

        # Text Description Entry Field
        textDescriptionEntry = Gtk.Entry()
        vbox_center_2.pack_start(textDescriptionEntry, True, True, 5)


        # Empty Label
        emptyLabel = Gtk.Label("                    ")
        emptyLabel.set_justify(Gtk.Justification.RIGHT)
        vbox_bottom.pack_start(emptyLabel, True, True, 5)

        # Empty Label
        emptyLabel = Gtk.Label("                    ")
        emptyLabel.set_justify(Gtk.Justification.RIGHT)
        vbox_bottom.pack_start(emptyLabel, True, True, 5)

        # Add Button
        addButton = Gtk.Button.new_with_label("(+)")
        addButton.connect("clicked", self.on_add_button_clicked)
        vbox_bottom.pack_start(addButton, True, True, 5)


    def on_add_button_clicked(self, button):
        print("\"Add\" button was pressed, adding another field.")

win = PacketInfoFieldWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()