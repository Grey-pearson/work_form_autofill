import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from BrowserControl import BrowserControl

# root = ttk.Window(themename="solar")
# root.title("VMS-inator")

# TDC = ttk.Entry(bootstyle="success").pack(side=TOP, padx=5, pady=10)
# right_cam = ttk.Checkbutton(bootstyle="success").pack()
# center_cam = ttk.Checkbutton(bootstyle="success").pack()
# left_cam = ttk.Checkbutton(bootstyle="success").pack()


# root.mainloop()


# use after geting GUI set up to take tdc and what cams are needed to be configed
browser_control = BrowserControl()

# cam selection with Checkbutton()

browser_control.sign_in_to_service_now()

# browser_control.open_old_vms()

# browser_control.close()
