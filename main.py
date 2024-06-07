from tkinter import *
from tkinter import ttk
from Class.BrowserControl import BrowserControl

root = Tk()
root.title("Camera Swap Configuration")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

TDC = StringVar()
TDC_entry = ttk.Entry(mainframe, width=7, textvariable=TDC)
TDC_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(
    column=3, row=3, sticky=W
)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()


# use after geting GUI set up to take tdc and what cams are needed to be configed
browser_control = BrowserControl()

browser_control.sign_in()

# browser_control.open_service_now()

# browser_control.open_old_vms()

# browser_control.close()
