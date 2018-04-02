from Tkinter import *
import ttk
import AppKit


root = Tk()
root.title('Project Navigator')
root.minsize(200,500)
root.tk_setPalette('#ececec')

dialog_frame = ttk.Frame(root)
dialog_frame.pack(padx=20,pady=15,anchor='w')

#Label that reads the name of the workspace
workspace_label = ttk.Label(dialog_frame, text='Workspace X',background='#ececec')
workspace_label.pack()

#Frame to store project name buttons
button_frame = ttk.Frame(root)
button_frame.pack()

#Buttons with available project names
projectA_button = ttk.Button(button_frame,text='Project A')
photo = PhotoImage(file='openFolderIcon.gif')
projectA_button.config(image=photo)
projectA_button.pack(side='right')

#To bring the window on top of other windows
AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)

mainloop()