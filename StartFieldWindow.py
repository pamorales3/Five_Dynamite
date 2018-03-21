import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class StartFieldWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Start Field [Protocol Name]")

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

        # Protocol Name Label
        protocolNameLabel = Gtk.Label("Protocol Name")
        protocolNameLabel.set_justify(Gtk.Justification.CENTER)
        vbox_center_1.pack_start(protocolNameLabel, True, True, 5)

        # Protocol Name Entry 
        protocolNameEntry = Gtk.Entry()
        vbox_center_2.pack_start(protocolNameEntry, True, True, 5)


        # Protocol Description Label
        protocolDescriptionLabel = Gtk.Label("Protocol Description")
        protocolDescriptionLabel.set_justify(Gtk.Justification.CENTER)
        vbox_center_1.pack_start(protocolDescriptionLabel, True, True, 5)

        # Protocol Description Entry 
        protocolDescriptionEntry = Gtk.Entry()
        vbox_center_2.pack_start(protocolDescriptionEntry, True, True, 5)    


        # Dependent Protocol Name Label
        protocolProtoNameLabel = Gtk.Label("Dependent Protocol Name")
        protocolProtoNameLabel.set_justify(Gtk.Justification.CENTER)
        vbox_center_1.pack_start(protocolProtoNameLabel, True, True, 5)

        # Dependent Protocol Name Entry 
        protocolProtoNameEntry = Gtk.Entry()
        vbox_center_2.pack_start(protocolProtoNameEntry, True, True, 5)   
        

        # Dependency Pattern Label
        dependencyPatLabel = Gtk.Label("Dependency Pattern")
        dependencyPatLabel.set_justify(Gtk.Justification.CENTER)
        vbox_center_1.pack_start(dependencyPatLabel, True, True, 5)

        # Dependency Pattern Entry 
        dependencyPatEntry = Gtk.Entry()
        dependencyPatEntry.set_text("(Integer/Range/String)")
        vbox_center_2.pack_start(dependencyPatEntry, True, True, 5)  



win = StartFieldWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()