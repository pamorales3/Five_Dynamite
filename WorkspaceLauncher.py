import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class WorkspaceLauncher(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Workspace Launcher")

        # Creates Big Box
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(self.box)

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
        self.box.pack_start(vbox_top, True, True, 5)
        self.box.pack_start(vbox_center, True, True, 5)
        self.box.pack_start(vbox_bottom, True, True, 5)

        # Main Label Area
        label = Gtk.Label("Select a directory as workspace: PDGS uses the workspace \n directory to store projects.")
        label.set_justify(Gtk.Justification.CENTER)
        vbox_top.pack_start(label, True, True, 5)

        # Workspace Label
        workspace = Gtk.Label("Workspace")
        workspace.set_justify(Gtk.Justification.LEFT)
        vbox_center.pack_start(workspace, True, True, 5)

        # Workspace Entry Field
        self.entry = Gtk.Entry()
        self.entry.set_text("Workspace Directory Path")
        vbox_center.pack_start(self.entry, True, True, 5)

        # Browse Button
        browseButton = Gtk.Button.new_with_label("Browse")
        browseButton.connect("clicked", self.on_browse_clicked)
        vbox_center.pack_start(browseButton, True, True, 5)

        # Space Filler Label   ASK ABOUT THIS CORNY THING
        #workspace = Gtk.Label("                             ")
        #workspace.set_justify(Gtk.Justification.RIGHT)
        #vbox_bottom.pack_start(workspace, True, True, 5)

        # Launch Button
        launchButton = Gtk.Button.new_with_label("Launch")
        launchButton.connect("clicked", self.on_launch_clicked)
        vbox_bottom.pack_start(launchButton, True, True, 5)

        # Cancel Button
        cancelButton = Gtk.Button.new_with_label("Cancel")
        cancelButton.connect("clicked", self.on_cancel_clicked)
        vbox_bottom.pack_start(cancelButton, True, True, 5)

    # Opens a file browser
    def on_browse_clicked(self, browseButton):
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

    # Launch button 
    def on_launch_clicked(self, launchButton):
        print("\"Launch\" button was pressed, launching workspace")
        self.destroy()

    # Cancel button
    def on_cancel_clicked(self, cancelButton):
        print("\"Cancel\" button was pressed, cancelling launch")
        self.destroy()


'''
win = WorkspaceLauncher()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
'''