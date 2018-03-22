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



# List of tuples for each packet stream, containing the number, time, source, destination, protocol, and info
packets_list = [("366", "11.767290", "192.168.0.31", "192.168.0.28", "SNMP", "get-response SNMPv2-SMI::enterprises.11.2.3.9.4.2.1.4.1.5.7.1"),
                ("367", "11.768865", "192.168.0.28", "192.168.0.31", "SNMP", "get-request SNMPv2-SMI::enterprises.11.2.3.9.4.2.1.4.1.5.8.1"),
                ("369", "11.775952", "192.168.0.31", "192.168.0.28", "SNMP", "get-response SNMPv2-SMI::enterprises.11.2.3.9.4.2.1.4.1.5.8.1"),
                ("381", "12.286091", "192.168.0.1", "192.168.0.1", "DNS", "Standard query A www.cnn.com"),
                ("384", "12.311862", "192.168.0.1", "192.168.0.28", "DNS", "Standard query response A 64.236.91.21 A 64.236.91.23 A 64.23"),
                ("385", "12.312727", "192.168.0.28", "64.236.91.21", "TCP", "56606 > http [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=2"),
                ("386", "12.361495", "64.236.91.21", "192.168.0.28", "TCP", "http > 56606 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1460"),
                ("387", "12.361583", "192.168.0.28", "64.236.91.21", "TCP", "56606 > http [ACK] Seq=1 Ack=1 Win=17520 Len=0"),
                ("388", "12.361805", "192.168.0.28", "64.236.91.21", "HTTP", "GET / HTTP/1.1"),
                ("389", "12.413166", "64.236.91.21", "192.168.0.28", "TCP", "http > 56606 [ACK] Seq=1 Ack=845 Win=6960 Len=0"),
                ("390", "12.413611", "64.236.91.21", "192.168.0.28", "TCP", "[TCP segment of a reassembled PDU]"),
                ("391", "12.414386", "64.236.91.21", "192.168.0.28", "TCP", "[TCP segment of a reassembled PDU]")]

data = [["User Datagram Protocol, Src Port: domain (53), Dst Port: 62872 (82672)", "Other Info", "Other Info"],
        ["Domain Name System (response)", "[Request In: 381]", "[Time: 0.025771000 seconds]", "[Transaction ID: 0xcf1f]"],
        ["Flags: 0x8180 (Standard query response, No error", "Other Info"]]


# List of tuples for the raw data
data_list = [("0000", "00 1c 26 26 66 a2 00 0e", "8e 04 d0 9e 08 00 45 00", "..&&f...  ......E."),
                ("0010", "00 99 00 00 40 00 40 11", "b8 e6 c0 a8 00 01 c0 a8" , "....@.@.  ........"),
                ("0020", "00 1c 00 35 f5 98 00 85", "98 5a cf 1f 81 80 00 01", "...5....  .z......"),
                ("0030", "00 06 00 00 00 00 03 77", "77 77 03 63 6e 6e 03 63", ".......w  ww.cnn.c"),
                ("0040", "6f 6d 00 00 01 00 01 c0", "0c 00 01 00 01 00 00 00", "om......  ........"),
                ("0050", "b7 00 04 40 ec 5b 15 c0", "0c 00 01 00 01 00 00 00", "...@.[..  ........"),
                ("0060", "b7 00 04 40 ec 5b 17 c0", "0c 00 01 00 01 00 00 00", "...@.[...  ........"),
                ("0070", "b7 00 04 40 ec 10 14 c0", "0c 00 01 00 01 00 00 00", "...@....  ........"),]

class ProtocolDissectorGeneratorSystem(Gtk.Window):
    # constructor: the title is "Welcome to GNOME" and the window belongs
    # to the application app

    def __init__(self):
        Gtk.Window.__init__(self, title="")

        proj = [["Project A", "Dissector A"],
                ["Project B", "Dissector B"],
                ["Project C", "Dissector C"]]

         # Creates Big Box
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(box)

        # Creates a box for the Title
        titleBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        titleBox.set_homogeneous(False)

        # Creates a box for the Menu Section
        buttonBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        buttonBox.set_homogeneous(False)

        # Creates a box for the middle area that will hold 
        # project nav and builder area boxes
        middleBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        middleBox.set_homogeneous(False)

        # Creates a box for the Project Navigation
        projNavBox = Gtk.Box(False, 0)
        projNavBox.set_size_request(100,400)
        projNavBox.set_homogeneous(False)

        # Creates a box for the Buildera Area 
        builderAreaBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        builderAreaBox.set_homogeneous(False)

        # Creates a box for the Canvas Box
        canvasBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)   
        canvasBox.set_homogeneous(False)

        # Creates a box for the Palette Box
        paletteBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        paletteBox.set_homogeneous(False)

        # Stores the canvas and palette into the builder area box
        builderAreaBox.pack_start(canvasBox, True, True, 0)
        builderAreaBox.pack_start(paletteBox, True, True, 0)

        # Stores the project navigation and builder area into the middle box
        middleBox.pack_start(projNavBox, True, True, 0)
        middleBox.pack_start(builderAreaBox, True, True, 0)


        box.pack_start(titleBox, False, False, 0)
        box.pack_start(buttonBox, False, False, 0)
        box.pack_start(middleBox, False, False, 0)
        

        titleLabel = Gtk.Label("Protocol Dissector Generator System")
        titleBox.pack_start(titleLabel, True, True, 5)
        titleLabel.set_markup("<span color='orange'><b><big>Protocol Dissector Generator System</big></b></span>")
        


        '''
        ////////////////////////////////////////////////////////////////////////////////////
        /                                  MENU SECTION                                    /
        ////////////////////////////////////////////////////////////////////////////////////
        '''   
        # Create Project Button
        createProjectButton = Gtk.Button.new_with_label("Create Project")
        createProjectButton.connect("clicked", self.on_create_project_clicked)
        buttonBox.pack_start(createProjectButton, True, True, 0)

        # Save Project Button
        saveProjectButton = Gtk.Button.new_with_label("Save Project")
        saveProjectButton.connect("clicked", self.on_save_project_clicked)
        buttonBox.pack_start(saveProjectButton, True, True, 0)

        # Close Project Button
        closeProjectButton = Gtk.Button.new_with_label("Close Project")
        closeProjectButton.connect("clicked", self.on_close_project_clicked)
        buttonBox.pack_start(closeProjectButton, True, True, 0)

        # Switch Workspace Button
        switchWorkspaceButton = Gtk.Button.new_with_label("Switch Workspace")
        switchWorkspaceButton.connect("clicked", self.on_workspace_button_clicked)
        buttonBox.pack_start(switchWorkspaceButton, True, True, 0)

        # Import Project Button
        importProjectButton = Gtk.Button.new_with_label("Import Project")
        importProjectButton.connect("clicked", self.on_import_button_clicked)
        buttonBox.pack_start(importProjectButton, True, True, 5)

        # Export Project Button
        exportProjectButton = Gtk.Button.new_with_label("Export Project")
        exportProjectButton.connect("clicked", self.on_export_button_clicked)
        buttonBox.pack_start(exportProjectButton, True, True, 0)    

        # Generate Dissector Script Button
        generateDSButton = Gtk.Button.new_with_label("Generate Dissector Script")
        generateDSButton.connect("clicked", self.on_generateDS_button_clicked)
        buttonBox.pack_start(generateDSButton, True, True, 0)

        # Organize Views Button
        organizeViewsButton = Gtk.Button.new_with_label("Organize Views")
        organizeViewsButton.connect("clicked", self.on_organize_views_button_clicked)
        buttonBox.pack_start(organizeViewsButton, True, True, 0)

        # Open PCAP Button
        openPCAPButton = Gtk.Button.new_with_label("Open PCAP")
        openPCAPButton.connect("clicked", self.on_open_pcap_button_clicked)
        buttonBox.pack_start(openPCAPButton, True, True, 0)


        '''
        ////////////////////////////////////////////////////////////////////////////////////
        /                                  PROJECT NAVIGATION                              /
        ////////////////////////////////////////////////////////////////////////////////////
        '''     
        # the data are stored in the model
        # create a treestore with one column
        store = Gtk.TreeStore(str)
        for i in range(len(proj)):
            
            piter = store.append(None, [proj[i][0]])
            # append the data as children of the projects
            j = 1
            while j < len(proj[i]):
                store.append(piter, [proj[i][j]])
                j += 1
   
        # the treeview shows the model
        # create a treeview on the model store
        view = Gtk.TreeView()
        view.set_hover_expand(True)
        view.set_enable_tree_lines(True)
        view.set_hover_selection(True)
        view.set_model(store)

        # the cellrenderer for the column - text
        renderer_data = Gtk.CellRendererText()
        # the column is created
        column_data = Gtk.TreeViewColumn("Project X", renderer_data, text=0)
        # and it is appended to the treeview
        view.append_column(column_data)

        # the books are sortable by author
        column_data.set_sort_column_id(0)

        projNavBox.pack_start(view, False, False, 0)


        '''
        ////////////////////////////////////////////////////////////////////////////////////
        /                                  Dissector Builder Area                          /
        ////////////////////////////////////////////////////////////////////////////////////
        '''
        table = Gtk.Table(16, 2, True)
        
        fieldLabel = Gtk.Label("Field")
        button1 = Gtk.Button(label="Start Label")
        button2 = Gtk.Button(label="Field (1 byte)")
        button3 = Gtk.Button(label="Field (2 byte)")
        button4 = Gtk.Button(label="Field (4 byte)")
        button5 = Gtk.Button(label="Field (8 byte)")
        button6 = Gtk.Button(label="Field (16 byte)")
        button7 = Gtk.Button(label="Field (32 byte)")
        button8 = Gtk.Button(label="Field (64 byte)")
        button9 = Gtk.Button(label="Field (Var size)")
        button10 = Gtk.Button(label="End Field")
        button11 = Gtk.Button(label="Reference List")
        button12 = Gtk.Button(label="Packet Info.")

        constructLabel = Gtk.Label("Construct")
        button13 = Gtk.Button(label="Expression")
        button14 = Gtk.Button(label="Connector")
        button15 = Gtk.Button(label="<")
        button16 = Gtk.Button(label=">")
        button17 = Gtk.Button(label="<=")
        button18 = Gtk.Button(label=">=")
        button19 = Gtk.Button(label="==")
        button20 = Gtk.Button(label="~=")
        button21 = Gtk.Button(label="And")
        button22 = Gtk.Button(label="Or")
        button23 = Gtk.Button(label="Not")
        button24 = Gtk.Button(label="Operand")



        table.attach(fieldLabel, 0, 2, 0, 1) # Field Label
        table.attach(button1, 0, 1, 1, 2)   # Start Label
        table.attach(button2, 1, 2, 1, 2)   # Field (1 byte)
        table.attach(button3, 0, 1, 2, 3)   # Field (2 byte)
        table.attach(button4, 1, 2, 2, 3)   # Field (4 byte)
        table.attach(button5, 0, 1, 3, 4)   # Field (8 byte)
        table.attach(button6, 1, 2, 3, 4)   # Field (16 byte)
        table.attach(button7, 0, 1, 4, 5)   # Field (32 byte)
        table.attach(button8, 1, 2, 4, 5)   # Field (64 byte)
        table.attach(button9, 0, 1, 5, 6)   # Field (Var size)
        table.attach(button10, 1, 2, 5, 6)  # End Field
        table.attach(button11, 0, 1, 6, 7)  # Reference List
        table.attach(button12, 1, 2, 6, 7)  # Packet Info.

        table.attach(constructLabel, 0, 2, 7, 8)  # Construct Label
        table.attach(button13, 0, 2, 8, 9)        # Expression 
        table.attach(button14, 0, 2, 9, 10)       # Connector
        table.attach(button15, 0, 1, 10, 11)      # <
        table.attach(button16, 1, 2, 10, 11)      # >
        table.attach(button17, 0, 1, 11, 12)      # <=
        table.attach(button18, 1, 2, 11, 12)      # >=
        table.attach(button19, 0, 1, 12, 13)      # ==
        table.attach(button20, 1, 2, 12, 13)      # ~=
        table.attach(button21, 0, 1, 13, 14)      # And
        table.attach(button22, 1, 2, 13, 14)      # Or
        table.attach(button23, 0, 1, 14, 15)      # Not
        table.attach(button24, 0, 2, 15, 16)      # Operand


        paletteBox.pack_start(table, True, True, 0)

        '''
        ////////////////////////////////////////////////////////////////////////////////////
        /                                  PACKET STREAM AREA                              /
        ////////////////////////////////////////////////////////////////////////////////////
        '''
        areaViews = Gtk.Notebook()
        self.add(areaViews)

        packetStreamBox = Gtk.Box(spacing=10)
        packetStreamBox.set_homogeneous(True)
        packetStreamBox.set_border_width(10)
        #Setting up the self.grid in which the elements are to be positioned
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        #Creating the ListStore model
        self.packet_listStore = Gtk.ListStore(str, str, str, str, str, str)
        for packet in packets_list:
            self.packet_listStore.append(list(packet))
        self.current_filter_language = None

        # Creating the filter, feeding it with the liststore model
        self.language_filter = self.packet_listStore.filter_new()

        # Creating the treeview and adding the columns
        self.treeview = Gtk.TreeView.new_with_model(self.language_filter)
        for i, column_title in enumerate(["No.", "Time", "Source", "Destination", "Protocol", "Info"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)


        # Setting up the layout, putting the treeview in a scrollwindow
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)

        self.scrollable_treelist.add(self.treeview)

        self.show_all()
        packetStreamBox.add(self.grid)

        areaViews.append_page(packetStreamBox, Gtk.Label('Packet Stream Area View'))

        '''
         ////////////////////////////////////////////////////////////////////////////////////
         /                                  DISSECTED STREAM AREA                           /
         ////////////////////////////////////////////////////////////////////////////////////
        '''

        dissectedStreamBox = Gtk.Box(spacing=10)
        dissectedStreamBox.set_homogeneous(True)
        dissectedStreamBox.set_border_width(10)

        #Setting up the self.grid in which the elements are to be positioned
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)        

         # the data are stored in the model
        # create a treestore with one column
        store = Gtk.TreeStore(str)
        for i in range(len(data)):
            # the iter piter is returned when appending the author
            piter = store.append(None, [data[i][0]])
            # append the data as children of the author
            j = 1
            while j < len(data[i]):
                store.append(piter, [data[i][j]])
                j += 1


        # the treeview shows the model
        # create a treeview on the model store
        view = Gtk.TreeView()
        view.set_hover_expand(True)
        view.set_enable_tree_lines(True)
        view.set_hover_selection(True)
        view.set_model(store)

        # Setting up the layout, putting the treeview in a scrollwindow
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)

        self.scrollable_treelist.add(view)


        # the cellrenderer for the column - text
        renderer_data = Gtk.CellRendererText()
        # the column is created
        column_data = Gtk.TreeViewColumn("Data", renderer_data, text=0)
        # and it is appended to the treeview
        view.append_column(column_data)

        # the books are sortable by author
        column_data.set_sort_column_id(0)

        dissectedStreamBox.add(self.grid)
        areaViews.append_page(dissectedStreamBox, Gtk.Label('Dissected Stream Area View'))


        '''
         ////////////////////////////////////////////////////////////////////////////////////
         /                                  RAW DATA WINDOW                                 /
         ////////////////////////////////////////////////////////////////////////////////////
        '''

        rawDataBox = Gtk.Box(spacing=10)
        rawDataBox.set_homogeneous(True)
        rawDataBox.set_border_width(10)
        #Setting up the self.grid in which the elements are to be positioned
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        #Creating the ListStore model
        self.data_listStore = Gtk.ListStore(str, str, str, str)
        for d in data_list:
            self.data_listStore.append(list(d))
        self.current_filter_language = None

        # Creating the filter, feeding it with the liststore model
        self.language_filter = self.data_listStore.filter_new()

        # Creating the treeview and adding the columns
        self.treeview = Gtk.TreeView.new_with_model(self.language_filter)
        for i, column_title in enumerate(["", "", "", ""]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, renderer, text=i)
            self.treeview.append_column(column)


        # Setting up the layout, putting the treeview in a scrollwindow
        self.scrollable_treelist = Gtk.ScrolledWindow()
        self.scrollable_treelist.set_vexpand(True)
        self.grid.attach(self.scrollable_treelist, 0, 0, 8, 10)
        
        self.scrollable_treelist.add(self.treeview)

        self.show_all()
        rawDataBox.add(self.grid)

        areaViews.append_page(rawDataBox, Gtk.Label('Raw Data Area'))

        '''
        ////////////////////////////////////////////////////////////////////////////////////
        /                                  CONSOLE WINDOW                                  /
        ////////////////////////////////////////////////////////////////////////////////////
        '''

        consoleBox = Gtk.Box(spacing=10)
        consoleBox.set_homogeneous(False)
        consoleBox.set_border_width(10)
        consoleBox.add(Gtk.Label('No error message to show'))
        areaViews.append_page(consoleBox, Gtk.Label('Console Area'))

        box.pack_start(areaViews, False, False, 5)


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

    
win = ProtocolDissectorGeneratorSystem()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
