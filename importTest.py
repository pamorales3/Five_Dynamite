from Tkinter import *

#Create window object
window = Tk()
#window.configure(background="blue")
window.title("Project Import")

infoLabel = Label(window, text="Import a project into the current workspace")
infoLabel.grid(row=2, column = 2)

projectLabel = Label(window, text="Project")
projectLabel.grid(row=3, column=1)

project_name = StringVar()
projectEntry = Entry(window, textvariable = project_name)
projectEntry.grid(row=3,column =2)

browseButton = Button(window, text="Browse")
browseButton.grid(row= 3, column = 3)

importButton = Button(window, text="Import",width=6)
importButton.grid(row = 4, column = 2)

cancelButton = Button(window, text="Cancel",width=6)
cancelButton.grid(row = 4, column = 3)


window.mainloop()