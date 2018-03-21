import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# List of tuples for the raw data
data_list = [("0000", "00 1c 26 26 66 a2 00 0e", "8e 04 d0 9e 08 00 45 00", "..&&f...  ......E."),
                ("0010", "00 99 00 00 40 00 40 11", "b8 e6 c0 a8 00 01 c0 a8" , "....@.@.  ........"),
                ("0020", "00 1c 00 35 f5 98 00 85", "98 5a cf 1f 81 80 00 01", "...5....  .z......"),
                ("0030", "00 06 00 00 00 00 03 77", "77 77 03 63 6e 6e 03 63", ".......w  ww.cnn.c"),
                ("0040", "6f 6d 00 00 01 00 01 c0", "0c 00 01 00 01 00 00 00", "om......  ........"),
                ("0050", "b7 00 04 40 ec 5b 15 c0", "0c 00 01 00 01 00 00 00", "...@.[..  ........"),
                ("0060", "b7 00 04 40 ec 5b 17 c0", "0c 00 01 00 01 00 00 00", "...@.[...  ........"),
                ("0070", "b7 00 04 40 ec 10 14 c0", "0c 00 01 00 01 00 00 00", "...@....  ........"),]

class RawDataAreaWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Raw Data Area")
        self.set_border_width(10)

        #Setting up the self.grid in which the elements are to be positioned
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_row_homogeneous(True)
        self.add(self.grid)

        #Creating the ListStore model
        self.data_listStore = Gtk.ListStore(str, str, str, str)
        for data in data_list:
            self.data_listStore.append(list(data))
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

win = RawDataAreaWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()