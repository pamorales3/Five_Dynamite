import Tkinter as tk
import ttk
import AppKit

class ListApp(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title('Raw Data Area')
        self.pack(fill='both',expand=True)
        self.master.minsize(800,200)

        #tk.Label(self, text="This is a listbox").pack()

        list_items = ["0000   00 1c 26 26 66 a2 00 0e  8e 04 d0 9e 08 00 45 00    ..&&f... ......E.",
                      '0010   00 99 00 00 40 00 40 11  b8 e6 c0 a8 00 01 c0 a8    ....@.@. ........',
                      '0020   00 1c 00 35 f5 98 00 85  98 5a cf 1f 81 80 00 01    ...5.... .Z......',
                      '0030   00 06 00 00 00 00 03 77  77 77 03 63 6e 6e 03 63    .......w ww.cnn.c',
                      '0040   6f 6d 00 00 01 00 01 c0  0c 00 01 00 01 00 00 00    om...... ........']

        self.listbox = tk.Listbox(self, selectmode='extended', bg='white')
        self.listbox.pack(fill='both',expand=True)

        for l in list_items:
            self.listbox.insert('end', l)


if __name__ == '__main__':
    #info = AppKit.NSBundle.mainBundle().infoDictionary()
    #info['LSUIElement']=True
    root = tk.Tk()
    app=ListApp(root)
    AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
    app.mainloop()