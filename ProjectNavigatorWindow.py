import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Pango
import sys

data = [["Project A", "Dissector A"],
        ["Project B", "Dissector B"],
        ["Project C", "Dissector C"]]


class ProjectNavigatorWindow(Gtk.ApplicationWindow):

    def __init__(self, app):
        Gtk.Window.__init__(self, title="Project Navigation", application=app)
        self.set_default_size(250, 100)
        self.set_border_width(10)

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

        # the cellrenderer for the column - text
        renderer_data = Gtk.CellRendererText()
        # the column is created
        column_data = Gtk.TreeViewColumn("Project X", renderer_data, text=0)
        # and it is appended to the treeview
        view.append_column(column_data)

        # the books are sortable by author
        column_data.set_sort_column_id(0)

        # add the treeview to the window
        self.add(view)


class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = ProjectNavigatorWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)

'''
app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
'''