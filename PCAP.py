import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class PCAP(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="PCAP")

        # Creates Big Box
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(box)

        # Top Box         
        vbox_top = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        vbox_top.set_homogeneous(False)

        # Middle Box
        vbox_center = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        vbox_center.set_homogeneous(False)

        # Bottom Box
        vbox_bottom = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        vbox_bottom.set_homogeneous(False)

        # Stores boxes into big box
        box.pack_start(vbox_top, True, True, 5)
        box.pack_start(vbox_center, True, True, 5)
        box.pack_start(vbox_bottom, True, True, 5)

        # Main Label Area
        label = Gtk.Label("Open a PCAP file")
        label.set_justify(Gtk.Justification.CENTER)
        vbox_top.pack_start(label, True, True, 5)

        # PCAP Name Label
        pcapName = Gtk.Label("PCAP Name")
        pcapName.set_justify(Gtk.Justification.RIGHT)
        vbox_center.pack_start(pcapName, True, True, 5)

        # PCAP Name Entry Field
        self.entry = Gtk.Entry()
        self.entry.set_text("PCAP File")
        vbox_center.pack_start(self.entry, True, True, 5)

        # Browse Button
        pcapBrowseButton = Gtk.Button.new_with_label("Browse")
        pcapBrowseButton.connect("clicked", self.on_pcap_browse_clicked)
        vbox_center.pack_start(pcapBrowseButton, True, True, 5)

        # Open Button
        openButton = Gtk.Button.new_with_label("Open")
        openButton.connect("clicked", self.on_open_clicked)
        vbox_bottom.pack_start(openButton, True, True, 5)

        # Cancel Button
        cancelButton = Gtk.Button.new_with_label("Cancel")
        cancelButton.connect("clicked", self.on_cancel_clicked)
        vbox_bottom.pack_start(cancelButton, True, True, 5)


    # Opens a PCAP file browser
    def on_pcap_browse_clicked(self, projectBrowseButton):
        dialog = Gtk.FileChooserDialog("Please choose a PCAP file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            print("File selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    # Open button 
    def on_open_clicked(self, openButton):
        print("\"Open\" button was pressed, opening PCAP file")
        self.destroy()

    # Cancel button
    def on_cancel_clicked(self, cancelButton):
        print("\"Cancel\" button was pressed, cancelling PCAP file opening")
        self.destroy()

'''
win = PCAP()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
'''
