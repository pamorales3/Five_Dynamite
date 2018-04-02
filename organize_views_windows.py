import Tkinter as tk
import AppKit


class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.pack()
        self.master.title("Organize Views")
        self.master.resizable(False, False)
        self.master.tk_setPalette('#ececec')

        x = (self.master.winfo_screenwidth() - self.master.winfo_reqwidth()) / 2
        y = (self.master.winfo_screenheight() - self.master.winfo_reqheight()) / 3
        # center the frame on the screen
        self.master.geometry("+{}+{}".format(x, y))

        self.master.config(menu=tk.Menu(self))

        window_prompt = tk.Message(self, text="Customize the views", font="System 14 bold", justify='left', aspect=800)
        window_prompt.pack(pady=(15, 0))

        dialog_frame = tk.Frame(self)
        dialog_frame.pack(padx=20, pady=15, anchor='w')

        # Project Navigation
        self.var = tk.IntVar()

        project_nav_label = tk.Label(dialog_frame, text="Project Navigation")
        project_nav_label.grid(row=0, column=0, sticky='w')

        project_nav_hide = tk.Radiobutton(dialog_frame, text="Hide", variable=self.var, value=1,
                                          command=self.project_nav_clicked)
        project_nav_hide.grid(row=0, column=1, sticky='w')

        project_nav_show = tk.Radiobutton(dialog_frame, text="Show", variable=self.var, value=2,
                                          command=self.project_nav_clicked)
        project_nav_show.grid(row=0, column=2, sticky='w')

        # Frame to hold buttons
        button_frame = tk.Frame(self)
        button_frame.pack(padx=15, pady=(0, 15), anchor='e')

        cancel_button = tk.Button(button_frame, text='Cancel', command=self.cancel_clicked)
        cancel_button.pack(side='right')

        import_button = tk.Button(button_frame, text='Confirm', height=1, width=6, command=self.confirm_clicked,
                                  default='active')
        import_button.pack(side='right')

        default_button = tk.Button(button_frame, text="Restore to Default", command=self.default_clicked)
        default_button.pack(side='right')

    def default_clicked(self, event=None):
        print('Default was clicked!')
        self.master.destroy()

    def confirm_clicked(self, event=None):
        print('Confirm was clicked!')
        self.master.destroy()

    def cancel_clicked(self, event=None):
        print('Cancel was clicked!')
        self.master.destroy()

    def project_nav_clicked(self, event=None):
        print("Project Navigation was selected")
        selection = "You selected the option " + str(self.var.get())
        print(selection)


if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    # AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
    app.mainloop()