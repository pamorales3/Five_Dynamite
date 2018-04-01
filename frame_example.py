from Tkinter import *
import ttk

root = Tk()

f1 = ttk.Frame(root)
f2 = ttk.Frame(root)

f1.grid(column=0, row=0, sticky="ns")
f2.grid(column=1, row=0, sticky="n")
root.rowconfigure(0, weight=1)

treeview = ttk.Treeview(f1).pack(expand=True, fill='y')
ttk.Button(f2, text="DAT BUTTON IS IN F2").pack()
ttk.Button(f2, text="DAT BUTTON IS IN F2").pack()
ttk.Button(f2, text="DAT BUTTON IS IN F2").pack()

mainloop()