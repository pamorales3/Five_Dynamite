import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import MenuSection
import sys

import WorkspaceLauncher
import NewProject
import DissectorScript
import ProjectImport
import ProjectExport
import PCAP
import OrganizeViews
import SaveProject


# a Gtk ApplicationWindow


class MyWindow(Gtk.ApplicationWindow):
    # constructor: the title is "Welcome to GNOME" and the window belongs
    # to the application app

    def __init__(self, app):
        Gtk.Window.__init__(self, title="", application=app)

         # Creates Big Box
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(box)

        titleBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        titleBox.set_homogeneous(False)

        buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        buttonBox.set_homogeneous(False)

        box.pack_start(titleBox, True, True, 5)
        box.pack_start(buttonBox, True, True, 5)

        titleLabel = Gtk.Label("Protocol Dissector Generator System")
        titleBox.pack_start(titleLabel, True, True, 5)
        titleLabel.set_markup("<span color='orange'><b><big>Protocol Dissector Generator System</big></b></span>")
        

        # Create Project Button
        createProjectButton = Gtk.Button.new_with_label("Create Project")
        createProjectButton.connect("clicked", self.on_create_project_clicked)
        buttonBox.pack_start(createProjectButton, True, True, 5)

        # Save Project Button
        saveProjectButton = Gtk.Button.new_with_label("Save Project")
        saveProjectButton.connect("clicked", self.on_save_project_clicked)
        buttonBox.pack_start(saveProjectButton, True, True, 5)

        # Close Project Button
        closeProjectButton = Gtk.Button.new_with_label("Close Project")
        closeProjectButton.connect("clicked", self.on_close_project_clicked)
        buttonBox.pack_start(closeProjectButton, True, True, 5)

        # Switch Workspace Button
        switchWorkspaceButton = Gtk.Button.new_with_label("Switch Workspace")
        switchWorkspaceButton.connect("clicked", self.on_workspace_button_clicked)
        buttonBox.pack_start(switchWorkspaceButton, True, True, 5)

        # Import Project Button
        importProjectButton = Gtk.Button.new_with_label("Import Project")
        importProjectButton.connect("clicked", self.on_import_button_clicked)
        buttonBox.pack_start(importProjectButton, True, True, 5)

        # Export Project Button
        exportProjectButton = Gtk.Button.new_with_label("Export Project")
        exportProjectButton.connect("clicked", self.on_export_button_clicked)
        buttonBox.pack_start(exportProjectButton, True, True, 5)    

        # Generate Dissector Script Button
        generateDSButton = Gtk.Button.new_with_label("Generate Dissector Script")
        generateDSButton.connect("clicked", self.on_generateDS_button_clicked)
        buttonBox.pack_start(generateDSButton, True, True, 5)

        # Organize Views Button
        organizeViewsButton = Gtk.Button.new_with_label("Organize Views")
        organizeViewsButton.connect("clicked", self.on_organize_views_button_clicked)
        buttonBox.pack_start(organizeViewsButton, True, True, 5)

        # Open PCAP Button
        openPCAPButton = Gtk.Button.new_with_label("Open PCAP")
        openPCAPButton.connect("clicked", self.on_open_pcap_button_clicked)
        buttonBox.pack_start(openPCAPButton, True, True, 5)


    def on_save_project_clicked(self, saveProjectButton):
        win = SaveProject.SaveProject()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    def on_close_project_clicked(self, closeProjectButton):
        print("Closing Project")

    def on_workspace_button_clicked(self, switchWorkspaceButton):
        win = WorkspaceLauncher.WorkspaceLauncher()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    def on_create_project_clicked(self, createProjectButton):
        win = NewProject.NewProject()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    def on_generateDS_button_clicked(self, generateDSButton):
        win = DissectorScript.DissectorScript()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    def on_import_button_clicked(self, importProjectButton):
        win = ProjectImport.ProjectImport()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()

    def on_export_button_clicked(self, exportProjectButton):
        win = ProjectExport.ProjectExport()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()
    
    def on_organize_views_button_clicked(self, organizeViewsButton):
        win = OrganizeViews.OrganizeViews()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()
    
    def on_open_pcap_button_clicked(self, openPCAPButton):
        win = PCAP.PCAP()
        win.connect("destroy", Gtk.main_quit)
        win.show_all()
        Gtk.main()





class MyApplication(Gtk.Application):
    # constructor of the Gtk Application

    def __init__(self):
        Gtk.Application.__init__(self)

    # create and activate a MyWindow, with self (the MyApplication) as
    # application the window belongs to.
    # Note that the function in C activate() becomes do_activate() in Python
    def do_activate(self):
        win = MyWindow(self)
        # show the window and all its content
        # this line could go in the constructor of MyWindow as well
        win.show_all()

    # start up the application
    # Note that the function in C startup() becomes do_startup() in Python
    def do_startup(self):
        Gtk.Application.do_startup(self)

# create and run the application, exit with the value returned by
# running the program
app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)














'''
class ProtocolDissectorGeneratorSystem(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="")
        
        # Creates Big Box
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(self.box)

        # Title Box         
        title_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        title_box.set_homogeneous(False)

        # Menu Section Box
        menuSection_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        menuSection_box.set_homogeneous(False)

        # Project Navigator Box
        pn_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        pn_box.set_homogeneous(False)

        # Dissector Builder Area Box
        dba_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        dba_box.set_homogeneous(False)

        # Bottom View Windows
        vw_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        vw_box.set_homogeneous(False)

        self.box.pack_start(title_box, True, True, 5)
        self.box.pack_start(menuSection_box, True, True, 5)
        self.box.pack_start(pn_box, True, True, 5)
        self.box.pack_start(dba_box, True, True, 5)
        self.box.pack_start(vw_box, True, True, 5)


        # Title Label
        titleLabel = Gtk.Label("Protocol Dissector Generator System")
        titleLabel.set_justify(Gtk.Justification.CENTER)
        title_box.pack_start(titleLabel, True, True, 5)

        # Menu Section 
        #self.menu_Section(self.box)
        group = Gtk.WindowGroup()
        group.add_window(MenuSection.MenuSection())
        #menuSection_box.pack_start(group, True, True, 5)
        


    def menu_Section(self, box):
        win = MenuSection.MenuSection()
        win.connect("destroy", Gtk.main_quit)
        box.pack_start(win, True, True, 5)
        win.show_all()
        #Gtk.main()
        #return win



win = ProtocolDissectorGeneratorSystem()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
'''