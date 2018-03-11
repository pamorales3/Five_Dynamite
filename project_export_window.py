import Tkinter as tk
import AppKit

class App(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.pack()
        self.master.title("Project Export")
        self.master.resizable(False,False)
        self.master.tk_setPalette('#ececec')

        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth())/2
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight())/3
        #center the frame on the screen
        self.master.geometry("+{}+{}".format(x,y))

        self.master.config(menu=tk.Menu(self))

        window_prompt = tk.Message(self,text="Export a project to the local file system",
                                   font="system 14 bold",justify='left',aspect=800)
        window_prompt.pack(pady=(15,0))

        dialog_frame = tk.Frame(self)
        dialog_frame.pack(padx=20,pady=15,anchor='w')

        project_label = tk.Label(dialog_frame,text='Project',font="System 14 bold")
        project_label.grid(row=0,column=0,sticky='w')

        project_name_entry = tk.Entry(dialog_frame,background='white',width=24)
        project_name_entry.grid(row=0,column=1,sticky='w')

        to_export_label = tk.Label(dialog_frame,text="To export file", font = "System 14 bold")
        to_export_label.grid(row = 1,column = 0, sticky = 'w')

        to_export_entry = tk.Entry(dialog_frame,background = 'white',width=24)
        to_export_entry.grid(row=1,column=1,sticky = 'w')

        #frame for export and cancel buttons
        button_frame = tk.Frame(self)
        button_frame.pack(padx=15,pady=(0,15),anchor='e')

        cancel_button = tk.Button(button_frame,text='Cancel', command=self.cancel_clicked)
        cancel_button.pack(side='right')

        export_button = tk.Button(button_frame,text='Export', command=self.export_clicked, default='active')
        export_button.pack(side='right')

    def cancel_clicked(self,event=None):
        print('Cancel was clicked!')
        self.master.destroy()

    def export_clicked(self,event=None):
        print('Export was clicked!')



if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
    app.mainloop()

