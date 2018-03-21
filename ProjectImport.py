import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ProjectImport(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Project Import")

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
        label = Gtk.Label("Import a project into the current workspace.")
        label.set_justify(Gtk.Justification.CENTER)
        vbox_top.pack_start(label, True, True, 5)

        # Project Name Label
        project = Gtk.Label("Project")
        project.set_justify(Gtk.Justification.RIGHT)
        vbox_center.pack_start(project, True, True, 5)

        # Project Name Entry Field
        self.entry = Gtk.Entry()
        self.entry.set_text("Project Name")
        vbox_center.pack_start(self.entry, True, True, 5)

        # Browse Button
        projectBrowseButton = Gtk.Button.new_with_label("Browse")
        projectBrowseButton.connect("clicked", self.on_project_browse_clicked)
        vbox_center.pack_start(projectBrowseButton, True, True, 5)

        # Import Button
        importButton = Gtk.Button.new_with_label("Import")
        importButton.connect("clicked", self.on_import_clicked)
        vbox_bottom.pack_start(importButton, True, True, 5)

        # Cancel Button
        cancelButton = Gtk.Button.new_with_label("Cancel")
        cancelButton.connect("clicked", self.on_cancel_clicked)
        vbox_bottom.pack_start(cancelButton, True, True, 5)


    # Opens a file browser
    def on_project_browse_clicked(self, projectBrowseButton):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
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

    # Import button 
    def on_import_clicked(self, importButton):
        print("\"Import\" button was pressed, importing project")
        self.destroy()

    # Cancel button
    def on_cancel_clicked(self, cancelButton):
        print("\"Cancel\" button was pressed, cancelling import")
        self.destroy()

'''
win = ProjectImport()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
'''