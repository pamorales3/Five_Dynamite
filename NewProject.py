import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class NewProject(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="New Project")

        # Creates Big Box
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(box)

        # Top Box         
        vbox_top = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        vbox_top.set_homogeneous(False)

        # Middle 1 Box
        vbox_center_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        vbox_center_1.set_homogeneous(False)

        # Middle 2 Box
        vbox_center_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        vbox_center_2.set_homogeneous(False)

        # Bottom Box
        vbox_bottom = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        vbox_bottom.set_homogeneous(False)
        
        # Stores boxes into big box
        box.pack_start(vbox_top, True, True, 5)
        box.pack_start(vbox_center_1, True, True, 5)
        box.pack_start(vbox_center_2, True, True, 5)
        box.pack_start(vbox_bottom, True, True, 5)

        # Main Label Area
        label = Gtk.Label("Create a new project.")
        label.set_justify(Gtk.Justification.CENTER)
        vbox_top.pack_start(label, True, True, 5)

        # Project Name Label
        workspace = Gtk.Label("Project Name")
        workspace.set_justify(Gtk.Justification.RIGHT)
        vbox_center_1.pack_start(workspace, True, True, 5)

        # Project Name Entry Field
        self.entry = Gtk.Entry()
        self.entry.set_text("Project Name")
        vbox_center_1.pack_start(self.entry, True, True, 5)

        # Description Label
        description = Gtk.Label("Description")
        workspace.set_justify(Gtk.Justification.RIGHT)
        vbox_center_2.pack_start(description, True, True, 5)

        # Description Entry Field
        self.entry = Gtk.Entry()
        self.entry.set_text("Description")
        vbox_center_2.pack_start(self.entry, True, True, 5)

        # Create Button
        createButton = Gtk.Button.new_with_label("Create")
        createButton.connect("clicked", self.on_create_clicked)
        vbox_bottom.pack_start(createButton, True, True, 5)

        # Cancel Button
        cancelButton = Gtk.Button.new_with_label("Cancel")
        cancelButton.connect("clicked", self.on_cancel_clicked)
        vbox_bottom.pack_start(cancelButton, True, True, 5)


    # Create Button 
    def on_create_clicked(self, createButton):
        print("\"Create\" button was pressed, creating new project")
        self.destroy()

    # Cancel Button
    def on_cancel_clicked(self, cancelButton):
        print("\"Cancel\" button was pressed, new project creation")
        self.destroy()

'''
win = NewProject()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
'''