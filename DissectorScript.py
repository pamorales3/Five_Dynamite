import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class DissectorScript(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Dissector Script")

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

        # Middle 3 Box
        vbox_center_3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        vbox_center_3.set_homogeneous(False)

        # Bottom Box
        vbox_bottom = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        vbox_bottom.set_homogeneous(False)

        # Dissector Format Combo Box
        name_store = Gtk.ListStore(str) 
        format_store = ["Format 1", "Format 2", "Format 3"]
        for f in format_store:
            name_store.append([f])

        
        # Stores boxes into big box
        box.pack_start(vbox_top, True, True, 5)
        box.pack_start(vbox_center_1, True, True, 5)
        box.pack_start(vbox_center_2, True, True, 5)
        box.pack_start(vbox_center_3, True, True, 5)
        box.pack_start(vbox_bottom, True, True, 5)

        # Main Label Area
        label = Gtk.Label("Generate a custom dissector from a selected project.")
        label.set_justify(Gtk.Justification.CENTER)
        vbox_top.pack_start(label, True, True, 5)

        # Project Name Label
        project = Gtk.Label("Project")
        project.set_justify(Gtk.Justification.RIGHT)
        vbox_center_1.pack_start(project, True, True, 5)

        # Project Name Entry Field
        entry = Gtk.Entry()
        entry.set_text("Project Name")
        vbox_center_1.pack_start(entry, True, True, 5)

        # Project Browse Button
        projectBrowseButton = Gtk.Button.new_with_label("Browse")
        projectBrowseButton.connect("clicked", self.on_project_browse_clicked)
        vbox_center_1.pack_start(projectBrowseButton, True, True, 5)

        # Dissector Format Label
        dissectorFormat = Gtk.Label("Dissector Format")
        dissectorFormat.set_justify(Gtk.Justification.RIGHT)
        vbox_center_2.pack_start(dissectorFormat, True, True, 5)

        # Dissector Format Combo Box
        format_combo = Gtk.ComboBox.new_with_model(name_store)
        format_combo.connect("changed", self.on_dissector_format_changed)
        renderer_text = Gtk.CellRendererText()
        format_combo.pack_start(renderer_text, True)
        format_combo.add_attribute(renderer_text, "text", 0)
        vbox_center_2.pack_start(format_combo, True, True, 5)

        # Save Location Label
        saveLocation = Gtk.Label("Save Location")
        saveLocation.set_justify(Gtk.Justification.RIGHT)
        vbox_center_3.pack_start(saveLocation, True, True, 5)

        # Save Location  Entry Field
        saveLoc = Gtk.Entry()
        saveLoc.set_text("Local File System Path")
        vbox_center_3.pack_start(saveLoc, True, True, 5)

        # Save Location Browse Button
        locationBrowseButton = Gtk.Button.new_with_label("Browse")
        locationBrowseButton.connect("clicked", self.on_location_browse_clicked)
        vbox_center_3.pack_start(locationBrowseButton, True, True, 5)

        # Generate Button
        generateButton = Gtk.Button.new_with_label("Generate")
        generateButton.connect("clicked", self.on_generate_clicked)
        vbox_bottom.pack_start(generateButton, True, True, 5)

        # Generate Button
        cancelButton = Gtk.Button.new_with_label("Cancel")
        cancelButton.connect("clicked", self.on_cancel_clicked)
        vbox_bottom.pack_start(cancelButton, True, True, 5)



    # Opens a file browser
    def on_project_browse_clicked(self, projectBrowseButton):
        dialog = Gtk.FileChooserDialog("Please choose a directory", self,
            Gtk.FileChooserAction.OPEN,
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

    # Opens a location browser
    def on_location_browse_clicked(self, projectBrowseButton):
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

    def on_dissector_format_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            format = model[tree_iter][0]
            print("Selected: format=%s" % format)

    # Generate Button 
    def on_generate_clicked(self, generateButton):
        print("\"Generate\" button was pressed, generating dissector")
        self.destroy()

    # Cancel Button
    def on_cancel_clicked(self, cancelButton):
        print("\"Cancel\" button was pressed, cancelling dissector generation")
        self.destroy()


'''
win = DissectorScript()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
'''