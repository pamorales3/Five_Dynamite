import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class FieldWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Field [Abbreviation]")

        # Creates Big Box
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(self.box)

        # Middle Box
        vbox_middle = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        vbox_middle.set_homogeneous(False)

        # Center Column 1 Box In Middle Box
        vbox_center_1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        vbox_center_1.set_homogeneous(False)

        # Center Column 2 Box In Middle Box
        vbox_center_2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        vbox_center_2.set_homogeneous(False)

        # Stores boxes into big box
        vbox_middle.pack_start(vbox_center_1, True, True, 5)
        vbox_middle.pack_start(vbox_center_2, True, True, 5)

        self.box.pack_start(vbox_middle, True, True, 5)

        # Name Label
        nameLabel = Gtk.Label("Name")
        nameLabel.set_justify(Gtk.Justification.CENTER)
        vbox_center_1.pack_start(nameLabel, True, True, 5)

        # Name Entry 
        nameEntry = Gtk.Entry()
        vbox_center_2.pack_start(nameEntry, True, True, 5)


        # Abbreviation Label
        abbreviationLabel = Gtk.Label("Abbreviation")
        abbreviationLabel.set_justify(Gtk.Justification.CENTER)
        vbox_center_1.pack_start(abbreviationLabel, True, True, 5)

        # Abbreviation Entry 
        abbreviationEntry = Gtk.Entry()
        vbox_center_2.pack_start(abbreviationEntry, True, True, 5)


        # Description Label
        descriptionLabel = Gtk.Label("Description")
        descriptionLabel.set_justify(Gtk.Justification.CENTER)
        vbox_center_1.pack_start(descriptionLabel, True, True, 5)

        # Description Entry 
        descriptionEntry = Gtk.Entry()
        vbox_center_2.pack_start(descriptionEntry, True, True, 5)


        # Reference List Label
        refListLabel = Gtk.Label("Reference List")
        refListLabel.set_justify(Gtk.Justification.CENTER)
        vbox_center_1.pack_start(refListLabel, True, True, 5)

        # Reference List Combo Box
        referenceList_store = Gtk.ListStore(str)
        referenceList = ["Reference List 1", "Reference List 2", "Reference List 3",
                         "Reference List 4", "Reference List 5"]

        for lists in referenceList:
            referenceList_store.append([lists])

        refList_combo = Gtk.ComboBox.new_with_model(referenceList_store)
        refList_combo.connect("changed", self.on_refList_combo_changed)
        renderer_text = Gtk.CellRendererText()
        refList_combo.pack_start(renderer_text, True)
        refList_combo.add_attribute(renderer_text, "text", 0)
        vbox_center_2.pack_start(refList_combo, False, False, True)


        # Data Type Label
        dataTypeLabel = Gtk.Label("Data Type")
        dataTypeLabel.set_justify(Gtk.Justification.CENTER)
        vbox_center_1.pack_start(dataTypeLabel, True, True, 5)

        # Data Type Combo Box
        dataType_store = Gtk.ListStore(str)
        dataType = ["Data Type 1", "Data Type 2", "Data Type 3",
                         "Data Type 4", "Data Type 5"]

        for dt in dataType:
            dataType_store.append([dt])

        dataType_combo = Gtk.ComboBox.new_with_model(dataType_store)
        dataType_combo.connect("changed", self.on_dataType_combo_changed)
        renderer_text = Gtk.CellRendererText()
        dataType_combo.pack_start(renderer_text, True)
        dataType_combo.add_attribute(renderer_text, "text", 0)
        vbox_center_2.pack_start(dataType_combo, False, False, True)


        # Base Label
        baseLabel = Gtk.Label("Base")
        baseLabel.set_justify(Gtk.Justification.CENTER)
        vbox_center_1.pack_start(baseLabel, True, True, 5)  

        # Base Combo Box
        base_store = Gtk.ListStore(str)
        base = ["Base 1", "Base 2", "Base 3", "Base 4", "Base 5"]

        for b in base:
            base_store.append([b])

        base_combo = Gtk.ComboBox.new_with_model(base_store)
        base_combo.connect("changed", self.on_base_combo_changed)
        renderer_text = Gtk.CellRendererText()
        base_combo.pack_start(renderer_text, True)
        base_combo.add_attribute(renderer_text, "text", 0)
        vbox_center_2.pack_start(base_combo, False, False, True)     


        # Mask Label
        maskLabel = Gtk.Label("Mask")
        maskLabel.set_justify(Gtk.Justification.CENTER)
        vbox_center_1.pack_start(maskLabel, True, True, 5)   

        # Mask Entry 
        maskEntry = Gtk.Entry()
        vbox_center_2.pack_start(maskEntry, True, True, 5)


        # Value Constraint Label 
        valueConLabel = Gtk.Label("Value Constraint")
        valueConLabel.set_justify(Gtk.Justification.CENTER)
        vbox_center_1.pack_start(valueConLabel, True, True, 5)  

        # Value Constraint Entry
        valueConEntry = Gtk.Entry()
        vbox_center_2.pack_start(valueConEntry, True, True, 5)


        # Required Label 
        requiredLabel = Gtk.Label("Required")
        requiredLabel.set_justify(Gtk.Justification.CENTER)
        vbox_center_1.pack_start(requiredLabel, True, True, 5)  

        # Required Entry
        requiredEntry = Gtk.Entry()
        vbox_center_2.pack_start(requiredEntry, True, True, 5)

    # Reference List Combo Box
    def on_refList_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            lists = model[tree_iter][0]
            print("Selected: reference list = %s" % lists)

    # Data Type Combo Box
    def on_dataType_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            dataType = model[tree_iter][0]
            print("Selected: data type = %s" % dataType)

    # Base Combo Box
    def on_base_combo_changed(self, combo):
        tree_iter = combo.get_active_iter()
        if tree_iter is not None:
            model = combo.get_model()
            base = model[tree_iter][0]
            print("Selected: base = %s" % base)


'''
win = FieldWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
'''