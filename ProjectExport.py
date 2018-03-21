import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ProjectExport(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Project Export")

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
        label = Gtk.Label("Export a project to the local file system.")
        label.set_justify(Gtk.Justification.CENTER)
        vbox_top.pack_start(label, True, True, 5)

        # Project Name Label
        project = Gtk.Label("Project")
        project.set_justify(Gtk.Justification.RIGHT)
        vbox_center_1.pack_start(project, True, True, 5)

        # Project Name Entry Field
        self.entry = Gtk.Entry()
        self.entry.set_text("Project Name")
        vbox_center_1.pack_start(self.entry, True, True, 5)

        # Project Browse Button
        projectBrowseButton = Gtk.Button.new_with_label("Browse")
        projectBrowseButton.connect("clicked", self.on_project_browse_clicked)
        vbox_center_1.pack_start(projectBrowseButton, True, True, 5)

        # Export File Label
        project = Gtk.Label("To export file")
        project.set_justify(Gtk.Justification.RIGHT)
        vbox_center_2.pack_start(project, True, True, 5)

        # Export File Entry Field
        self.entry = Gtk.Entry()
        self.entry.set_text("Local File System Path")
        vbox_center_2.pack_start(self.entry, True, True, 5)

         # Path Browse Button
        locationBrowseButton = Gtk.Button.new_with_label("Browse")
        locationBrowseButton.connect("clicked", self.on_location_browse_clicked)
        vbox_center_2.pack_start(locationBrowseButton, True, True, 5)

        # Export Button
        exportButton = Gtk.Button.new_with_label("Export")
        exportButton.connect("clicked", self.on_export_clicked)
        vbox_bottom.pack_start(exportButton, True, True, 5)

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

     # Opens a location browser
    def on_location_browse_clicked(self, pathBrowseButton):
        dialog = Gtk.FileChooserDialog("Please choose a directory", self,
            Gtk.FileChooserAction.SELECT_FOLDER,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             "Select", Gtk.ResponseType.OK))
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            print("Folder selected: " + dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()

    # Export button 
    def on_export_clicked(self, importButton):
        print("\"Export\" button was pressed, exporting project")
        self.destroy()

    # Cancel button
    def on_cancel_clicked(self, cancelButton):
        print("\"Cancel\" button was pressed, cancelling export")
        self.destroy()

'''
win = ProjectExport()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
'''
