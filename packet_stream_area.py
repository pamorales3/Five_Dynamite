from Tkinter import *
import ttk

root = Tk()
root.title('Packet Stream Area')
root.minsize(800,200)
treeview = ttk.Treeview(root)
treeview.pack(fill='both',expand=True)

# List of tuples for each packet stream, containing the number, time, source, destination, protocol, and info
packets_list = [("366", "11.767290", "192.168.0.31", "192.168.0.28", "SNMP", "get-response SNMPv2-SMI::enterprises.11.2.3.9.4.2.1.4.1.5.7.1"),
                ("367", "11.768865", "192.168.0.28", "192.168.0.31", "SNMP", "get-request SNMPv2-SMI::enterprises.11.2.3.9.4.2.1.4.1.5.8.1"),
                ("369", "11.775952", "192.168.0.31", "192.168.0.28", "SNMP", "get-response SNMPv2-SMI::enterprises.11.2.3.9.4.2.1.4.1.5.8.1"),
                ("381", "12.286091", "192.168.0.1", "192.168.0.1", "DNS", "Standard query A www.cnn.com"),
                ("384", "12.311862", "192.168.0.1", "192.168.0.28", "DNS", "Standard query response A 64.236.91.21 A 64.236.91.23 A 64.23"),
                ("385", "12.312727", "192.168.0.28", "64.236.91.21", "TCP", "56606 > http [SYN] Seq=0 Win=8192 Len=0 MSS=1460 WS=2"),
                ("386", "12.361495", "64.236.91.21", "192.168.0.28", "TCP", "http > 56606 [SYN, ACK] Seq=0 Ack=1 Win=8192 Len=0 MSS=1460"),
                ("387", "12.361583", "192.168.0.28", "64.236.91.21", "TCP", "56606 > http [ACK] Seq=1 Ack=1 Win=17520 Len=0"),
                ("388", "12.361805", "192.168.0.28", "64.236.91.21", "HTTP", "GET / HTTP/1.1"),
                ("389", "12.413166", "64.236.91.21", "192.168.0.28", "TCP", "http > 56606 [ACK] Seq=1 Ack=845 Win=6960 Len=0"),
                ("390", "12.413611", "64.236.91.21", "192.168.0.28", "TCP", "[TCP segment of a reassembled PDU]"),
                ("391", "12.414386", "64.236.91.21", "192.168.0.28", "TCP", "[TCP segment of a reassembled PDU]")]

treeview['columns'] = ('No.','Time','Source','Destination','Protocol','Info')

#set up heading and column for the parent tree view: No.
treeview.heading('No.',text='No.',anchor='w')
treeview.column('No.',anchor='w', width=75)

#set up heading and column for 'Time'
treeview.heading('Time', text='Time')
treeview.column('Time',anchor='w',width=100)

#set up heading and column for 'Source'
treeview.heading('Source', text='Source')
treeview.column('Source',anchor='w',width=100)

#set up heading and column for 'Destination'
treeview.heading('Destination', text='Destination')
treeview.column('Destination',anchor='w',width=100)

#set up heading and column for 'Protocol'
treeview.heading('Protocol', text='Protocol')
treeview.column('Protocol',anchor='w',width=100)

#set up heading and column for 'Info'
treeview.heading('Info', text='Info')
treeview.column('Info',anchor='w',width=400)

#Make this treeview into a grid
#treeview.grid(sticky = (N,S,E,W))
#Configure row and column sizes
#root.grid_rowconfigure(0, weight=1)
#root.grid_columnconfigure(0, weight=1)

#populate table

#this should fill out the first row on the table, but it doesn't
#treeview.insert('','end',values=(packets_list[0])

#Comment line 59 and uncomment lines 62 and 63. I get weird error :(
for packet in packets_list:
    treeview.insert('','end',values=((packet[0]),(packet[1]),(packet[2]),(packet[3]),(packet[4]),(packet[5])))



mainloop()