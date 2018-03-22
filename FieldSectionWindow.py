import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

(TARGET_ENTRY_TEXT, TARGET_ENTRY_PIXBUF) = range(2)
(COLUMN_TEXT, COLUMN_PIXBUF) = range(2)

DRAG_ACTION = Gdk.DragAction.COPY

class DragDropWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Drag and Drop Demo")

        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,spacing=12)
        self.add(hbox)

        constructs = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6) 
        dropArea = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)


        hbox.pack_start(dropArea, True, True, 5)
        hbox.pack_start(constructs, True, True, 5)

        label = Gtk.Label("Drop Something Here!")
        label.set_justify(Gtk.Justification.CENTER)
        dropArea.pack_start(label, True, True, 5)

        
        button = Gtk.Button.new_with_label("Hello")                                  # Button for constructs box

        button.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)       # Sets constructs box as source
        dropArea.drag_dest_set(Gtk.DestDefaults.ALL, [], DRAG_ACTION)                # Sets dropArea box as destination

        button.connect("drag-data-get", self.on_drag_data_get)                       # Handles drag function
        dropArea.connect("drag-data-received", self.on_drag_data_received)           # Handles drop function

        constructs.pack_start(button, True, True, 5)


    def on_drag_data_get(self, widget, drag_context, data, info, time):
        print("Hello There!")

        


    def on_drag_data_received(self, widget, drag_context, x, y, data, info, time):
        print("             ")
        




    #self.enable_model_drag_source(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
    #self.connect("drag-data-get", self.on_drag_data_get)
    #self.connect("drag-data-received", self.on_drag_data_received)


win = DragDropWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()