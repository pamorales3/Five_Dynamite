import Tkinter as tk
import AppKit

class App(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.pack()
        self.master.title("Workspace Launcher")
        self.master.resizable(False,False)
        self.master.tk_setPalette('#ececec')

        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth())/2
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight())/3
        #center the frame on the screen
        self.master.geometry("+{}+{}".format(x,y))

        self.master.config(menu=tk.Menu(self))

        window_prompt = tk.Message(self, text="Select a directory as a workspace: PDGS uses "
                                              "the workspace directory to store projects.",
                                   font="System 14 bold", justify='left',aspect=800)
        window_prompt.pack(pady=(15,0))

        dialog_frame = tk.Frame(self)
        dialog_frame.pack(padx=20,pady=15,anchor='w')

        workspace_label = tk.Label(dialog_frame,text="Workspace",font='System 14 bold')
        workspace_label.grid(row=0,column=0,sticky='w')

        workspace_path_entry = tk.Entry(dialog_frame,background="white",width=24)
        workspace_path_entry.grid(row=0,column=1,sticky='w')

        browse_project_button = tk.Button(dialog_frame,text='Browse')
        browse_project_button.grid(row=0,column=2,sticky='w')

        #frame for Import and Cancel Buttons
        button_frame = tk.Frame(self)
        button_frame.pack(padx=15,pady=(0,15),anchor='e')

        cancel_button = tk.Button(button_frame,text='Cancel', command=self.cancel_clicked)
        cancel_button.pack(side='right')

        launch_button = tk.Button(button_frame,text='Launch',height = 1,width=6,command=self.launch_clicked,default='active')
        launch_button.pack(side='right')

    def cancel_clicked(self, event=None):
        print('Cancel was clicked!')
        self.master.destroy()

    def launch_clicked(self,event=None):
        print('Launch was clicked!')
        self.master.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
    app.mainloop()