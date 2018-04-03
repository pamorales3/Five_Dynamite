import Tkinter as tk
import ttk

class OutputView(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self, master)
        notebook = ttk.Notebook(self.master)
        notebook.pack()
        dissected_stream_frame = ttk.Frame(notebook)
        notebook.add(dissected_stream_frame, text="Dissected Stream Area")
        tk.Button(dissected_stream_frame, text="click me").pack()


if __name__ == '__main__':
    root = tk.Tk()
    OutputView = OutputView(root)
    OutputView.mainloop()