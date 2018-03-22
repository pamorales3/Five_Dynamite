import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class playground(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Playground")

        # Creates Big Box
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        self.add(box)

        LeftSideBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        LeftSideBox.set_homogeneous(False)

        RightSideBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        RightSideBox.set_homogeneous(False)

        box.pack_start(LeftSideBox, True, True, 5)
        box.pack_start(RightSideBox, True, True, 5)

        table = Gtk.Table(3, 3, True)
        

        button1 = Gtk.Button(label="Button 1")
        button2 = Gtk.Button(label="Button 2")
        button3 = Gtk.Button(label="Button 3")
        button4 = Gtk.Button(label="Button 4")
        button5 = Gtk.Button(label="Button 5")
        button6 = Gtk.Button(label="Button 6")

        table.attach(button1, 0, 1, 0, 1)
        table.attach(button2, 1, 3, 0, 1)
        table.attach(button3, 0, 1, 1, 3)
        table.attach(button4, 1, 3, 1, 2)
        table.attach(button5, 1, 2, 2, 3)
        table.attach(button6, 2, 3, 2, 3)

        RightSideBox.pack_start(table, True, True, 5)

        '''
        # Canvas Box         
        canvasBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        canvasBox.set_homogeneous(False)

        paletteBox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        paletteBox.set_homogeneous(False)

        # Palette - Field
        fieldBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        fieldBox.set_homogeneous(False)

        fieldLeftSide = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        fieldLeftSide.set_homogeneous(False)

        fieldRightSide = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        fieldRightSide.set_homogeneous(False)

        # Palette - Construct
        constructBox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=5)
        constructBox.set_homogeneous(False)

        constructLeftSide = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        constructLeftSide.set_homogeneous(False)

        constructRightSide = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        constructRightSide.set_homogeneous(False)

        # Creates the Field Box
        fieldBox.pack_start(fieldLeftSide, True, True, 5)
        fieldBox.pack_start(fieldRightSide, True, True, 5)
        paletteBox.pack_start(paletteBox, True, True, 5)

        # Creates the Construct Box
        constructBox.pack_start(constructLeftSide, True, True, 5)
        constructBox.pack_start(constructRightSide, True, True, 5)
        paletteBox.pack_start(constructBox, True, True, 5)

        

        # Stores boxes into big box
        box.pack_start(canvasBox, True, True, 5)
        box.pack_start(paletteBox, True, True, 5)


        # Field - Start Field Button
        startFieldButton = Gtk.Button.new_with_label("Start Field")
        fieldLeftSide.pack_start(startFieldButton, True, True, 5)
        '''


win = playground()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
