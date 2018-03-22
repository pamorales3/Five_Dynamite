import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class OrganizeViews(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Organize Views")

        # Creates Big Box
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(self.box)

        # Top Box         
        vbox_top = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        vbox_top.set_homogeneous(False)

        # Hide and Show Box 
        vbox_hsTop = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)

        # Middle Box
        vbox_middle = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        vbox_middle.set_homogeneous(False)

        # Center Column 1 Box In Middle Box
        vbox_center_1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        vbox_center_1.set_homogeneous(False)

        # Center Column 2 Box In Middle Box
        vbox_center_2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        vbox_center_2.set_homogeneous(False)

        # Center Column 3 Box In Middle Box
        vbox_center_3 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        vbox_center_3.set_homogeneous(False)

        # Bottom Box
        vbox_bottom = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        vbox_bottom.set_homogeneous(False)
        
        # Stores boxes into big box
        vbox_middle.pack_start(vbox_center_1, True, True, 5)
        vbox_middle.pack_start(vbox_center_2, True, True, 5)
        vbox_middle.pack_start(vbox_center_3, True, True, 5)
        self.box.pack_start(vbox_top, True, True, 5)
        self.box.pack_start(vbox_hsTop, True, True, 5)
        self.box.pack_start(vbox_middle, True, True, 5)
        self.box.pack_start(vbox_bottom, True, True, 5)

        # Main Label Area
        label = Gtk.Label("Customize the views.")
        label.set_justify(Gtk.Justification.CENTER)
        vbox_top.pack_start(label, True, True, 5)

        # Empty Label
        emptyLabel = Gtk.Label("                               ")
        emptyLabel.set_justify(Gtk.Justification.CENTER)
        vbox_hsTop.pack_start(emptyLabel, True, True, 5)

        # Hide Label
        hideLabel = Gtk.Label("Hide")
        hideLabel.set_justify(Gtk.Justification.CENTER)
        vbox_hsTop.pack_start(hideLabel, True, True, 5)

        # Show Label
        showLabel = Gtk.Label("Show")
        showLabel.set_justify(Gtk.Justification.CENTER)
        vbox_hsTop.pack_start(showLabel, True, True, 5)


        # Project Navigation Label
        projectLabel = Gtk.Label("Project Navigation")
        projectLabel.set_justify(Gtk.Justification.RIGHT)
        vbox_center_1.pack_start(projectLabel, True, True, 5)

        # Project Navigation Show Radio Button
        projectShowButton = Gtk.RadioButton.new_with_label_from_widget(None, "")
        projectShowButton.set_label("")
        projectShowButton.connect("toggled", self.on_project_nav_toggled, "Show")
        vbox_center_3.pack_start(projectShowButton, False, False, 5)

        # Project Navigation Hide Radio Button 
        projectHideButton = Gtk.RadioButton.new_from_widget(projectShowButton)
        projectHideButton.connect("toggled", self.on_project_nav_toggled, "Hide")
        vbox_center_2.pack_start(projectHideButton, False, False, 8)

        

        # Dissector Building Area Label
        dissectorBLabel = Gtk.Label("Dissector Building Area")
        dissectorBLabel.set_justify(Gtk.Justification.RIGHT)
        vbox_center_1.pack_start(dissectorBLabel, True, True, 5)

        # Dissector Building Area Show Radio Button
        dissectorBAShowButton = Gtk.RadioButton.new_with_label_from_widget(None, "")
        dissectorBAShowButton.set_label("")
        dissectorBAShowButton.connect("toggled", self.on_dissector_builder_toggled, "Show")
        vbox_center_3.pack_start(dissectorBAShowButton, False, False, 5)

        # Dissector Building Area Hide Radio Button 
        dissectorBAHideButton = Gtk.RadioButton.new_from_widget(dissectorBAShowButton)
        dissectorBAHideButton.connect("toggled", self.on_dissector_builder_toggled, "Hide")
        vbox_center_2.pack_start(dissectorBAHideButton, False, False, 7)



        # Palette Label
        paletteLabel = Gtk.Label("Palette")
        paletteLabel.set_justify(Gtk.Justification.RIGHT)
        vbox_center_1.pack_start(paletteLabel, True, True, 5)

        # Palette Show Radio Button
        paletteShowButton = Gtk.RadioButton.new_with_label_from_widget(None, "") 
        paletteShowButton.set_label("")
        paletteShowButton.connect("toggled", self.on_palette_toggled, "Show")
        vbox_center_3.pack_start(paletteShowButton, False, False, 5)

        # Palette Hide Radio Button 
        paletteHideButton = Gtk.RadioButton.new_from_widget(paletteShowButton)
        paletteHideButton.connect("toggled", self.on_palette_toggled, "Hide")
        vbox_center_2.pack_start(paletteHideButton, False, False, 7)

        
        # Packet Stream Area Label
        packetSALabel = Gtk.Label("Packet Stream Area")
        packetSALabel.set_justify(Gtk.Justification.RIGHT)
        vbox_center_1.pack_start(packetSALabel, True, True, 5)

        # Packet Stream Area Show Radio Button
        packetSAShowButton = Gtk.RadioButton.new_with_label_from_widget(None, "")
        packetSAShowButton.set_label("")
        packetSAShowButton.connect("toggled", self.on_packet_stream_toggled, "Show")
        vbox_center_3.pack_start(packetSAShowButton, False, False, 5)

        # Packet Stream Area Hide Radio Button 
        packetSAHideButton = Gtk.RadioButton.new_from_widget(packetSAShowButton)
        packetSAHideButton.connect("toggled", self.on_packet_stream_toggled, "Hide")
        vbox_center_2.pack_start(packetSAHideButton, False, False, 5)
        

        # Dissected Stream Area Label
        dissectedSALabel = Gtk.Label("Dissected Stream Area")
        dissectedSALabel.set_justify(Gtk.Justification.RIGHT)
        vbox_center_1.pack_start(dissectedSALabel, True, True, 5)

        # Dissected Stream Area Show Radio Button
        dissectedSAShowButton = Gtk.RadioButton.new_with_label_from_widget(None, "")
        dissectedSAShowButton.set_label("")
        dissectedSAShowButton.connect("toggled", self.on_dissected_stream_toggled, "Show")
        vbox_center_3.pack_start(dissectedSAShowButton, False, False, 5)

        # Dissected Stream Area Hide Radio Button 
        dissectedSAHideButton = Gtk.RadioButton.new_from_widget(dissectedSAShowButton)
        dissectedSAHideButton.connect("toggled", self.on_dissected_stream_toggled, "Hide")
        vbox_center_2.pack_start(dissectedSAHideButton, False, False, 10)
        
        
        # Raw Data Area Label
        rawDALabel = Gtk.Label("Raw Data Area")
        rawDALabel.set_justify(Gtk.Justification.RIGHT)
        vbox_center_1.pack_start(rawDALabel, True, True, 5)

        # Raw Data Area Show Radio Button
        rawDAShowButton = Gtk.RadioButton.new_with_label_from_widget(None, "")
        rawDAShowButton.set_label("")
        rawDAShowButton.connect("toggled", self.on_raw_data_toggled, "Show")
        vbox_center_3.pack_start(rawDAShowButton, False, False, 5)

        # Raw Data Area Hide Radio Button 
        rawDAHideButton = Gtk.RadioButton.new_from_widget(rawDAShowButton)
        rawDAHideButton.connect("toggled", self.on_raw_data_toggled, "Hide")
        vbox_center_2.pack_start(rawDAHideButton, False, False, 3)

        
        # Console Area Label
        consoleAreaLabel = Gtk.Label("Console Area")
        consoleAreaLabel.set_justify(Gtk.Justification.RIGHT)
        vbox_center_1.pack_start(consoleAreaLabel, True, True, 5)

        # Console Area Show Radio Button
        consoleAreaShowButton = Gtk.RadioButton.new_with_label_from_widget(None, "")
        consoleAreaShowButton.set_label("")
        consoleAreaShowButton.connect("toggled", self.on_console_area_toggled, "Show")
        vbox_center_3.pack_start(consoleAreaShowButton, False, False, 5)

        # Console Area Hide Radio Button 
        consoleAreaHideButton = Gtk.RadioButton.new_from_widget(consoleAreaShowButton)
        consoleAreaHideButton.connect("toggled", self.on_console_area_toggled, "Hide")
        vbox_center_2.pack_start(consoleAreaHideButton, False, False, 12)
        


        # Restore to Default Button
        defaultButton = Gtk.Button.new_with_label("Restore to Default")
        defaultButton.connect("clicked", self.on_default_toggled, projectShowButton, 
                              dissectorBAShowButton, paletteShowButton, packetSAShowButton,dissectedSAShowButton,
                              rawDAShowButton, consoleAreaShowButton)
        vbox_bottom.pack_start(defaultButton, True, True, 5)

        # Confirm Button
        confirmButton = Gtk.Button.new_with_label("Open")
        confirmButton.connect("clicked", self.on_confirm_clicked)
        vbox_bottom.pack_start(confirmButton, False, False, 5)

        # Cancel Button
        cancelButton = Gtk.Button.new_with_label("Cancel")
        cancelButton.connect("clicked", self.on_cancel_clicked)
        vbox_bottom.pack_start(cancelButton, False, False, 5)
        

    def on_project_nav_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Project Navigation", name, "was turned", state)


    def on_dissector_builder_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Dissector Builder Area", name, "was turned", state)


    def on_palette_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Palette", name, "was turned", state)


    def on_packet_stream_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Packet Stream Area", name, "was turned", state)


    def on_dissected_stream_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Dissected Stream Area", name, "was turned", state)


    def on_raw_data_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Raw Data Area", name, "was turned", state)

    
    def on_console_area_toggled(self, button, name):
        if button.get_active():
            state = "on"
        else:
            state = "off"
        print("Console Area", name, "was turned", state)


    # Restore to Default Button
    def on_default_toggled(self, button, projectShowButton, 
                              dissectorBAShowButton, paletteShowButton, packetSAShowButton,dissectedSAShowButton,
                              rawDAShowButton, consoleAreaShowButton): 

        projectShowButton.set_active(True) 
        dissectorBAShowButton.set_active(True) 
        paletteShowButton.set_active(True)
        packetSAShowButton.set_active(True)
        dissectedSAShowButton.set_active(True)
        rawDAShowButton.set_active(True)
        consoleAreaShowButton.set_active(True)
        

    # Confirm Button
    def on_confirm_clicked(self, button):
        print("\"Confirm\" button was pressed, confirming windows")
        self.destroy()

    # Cancel Button
    def on_cancel_clicked(self, button):
        print("\"Cancel\" button was pressed, cancelling views")
        self.destroy()
        

'''
win = OrganizeViews()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
'''