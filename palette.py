import Tkinter as tk
import AppKit

class Palette(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.pack()
        self.master.title("Palette")
        self.master.tk_setPalette('#ececec')
        self.master.minsize(300, 500)

        #A frame to put more widgets on
        component_frame = tk.Frame(self,highlightbackground = 'blue', highlightcolor='blue',highlightthickness=1)
        component_frame.pack(fill='both',expand=True)

        field_frame = tk.Frame(component_frame, width=200,height=300,highlightbackground = 'green', highlightcolor='green',highlightthickness=1)
        field_frame.pack(padx=10,pady=15,anchor='center')

        self.folder_image = tk.PhotoImage(file="open_folder_icon.gif")
        self.folder_image = self.folder_image.subsample(10, 10)

        folder_label = tk.Label(field_frame, image=self.folder_image)
        folder_label.grid(row=0,column=0)

        field_label = tk.Label(field_frame,text="Field", font='System 14 bold')
        field_label.grid(row=0,column=1)

        startfield_button = tk.Button(field_frame,text='Start Field')
        startfield_button.grid(row=1,column=0)

        fieldbyte1_button = tk.Button(field_frame,text='Field 1 Byte')
        fieldbyte1_button.grid(row =1, column=1)

        fieldbyte2_button = tk.Button(field_frame,text='Field 2 Byte')
        fieldbyte2_button.grid(row=2,column=0)

        fieldbyte4_button = tk.Button(field_frame,text='Field 4 Byte')
        fieldbyte4_button.grid(row=2,column=1)

        fieldbyte8_button = tk.Button(field_frame, text='Field 8 Byte')
        fieldbyte8_button.grid(row=3, column=0)

        fieldbyte16_button = tk.Button(field_frame, text='Field 16 Byte')
        fieldbyte16_button.grid(row=3, column=1)

        fieldbyte8b_button = tk.Button(field_frame, text='Field 8 Byte')
        fieldbyte8b_button.grid(row=4, column=0)

        fieldbyte16b_button = tk.Button(field_frame, text='Field 16 Byte')
        fieldbyte16b_button.grid(row=4, column=1)

        fieldVar_button = tk.Button(field_frame, text='Field (Var size)')
        fieldVar_button.grid(row=5, column=0)

        endField_button = tk.Button(field_frame, text='End Field')
        endField_button.grid(row=5, column=1)

        refList_button = tk.Button(field_frame, text='Reference List')
        refList_button.grid(row=6, column=0)

        packetInfo_button = tk.Button(field_frame, text='Packet Info')
        packetInfo_button.grid(row=6, column=1)

        construct_frame = tk.Frame(component_frame, highlightbackground = 'green', highlightcolor='green',highlightthickness=1)
        construct_frame.pack(padx=20,pady=15,anchor='center')

        construct_label = tk.Label(construct_frame,text='Construct',font='System 14 bold')
        construct_label.grid(row=0,column=0)









if __name__ == '__main__':
    root = tk.Tk()
    palette = Palette(root)
    AppKit.NSApplication.sharedApplication().activateIgnoringOtherApps_(True)
    palette.mainloop()