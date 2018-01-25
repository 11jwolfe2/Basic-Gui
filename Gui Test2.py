try:
    # Linux/Raspberry Pi
	from tkinter import *
except ImportError:
    # Windows
    from Tkinter import *
    
import time
from datetime import datetime
today = datetime.today()
root = Tk()
root.title("time and date test")

class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)            
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom


#root.geometry('')
#Layout
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.configure(background='black')
frame = Frame(root)
frame.place(relx=.04, rely=.21)
date1 = Label(frame, font=('times', 180, 'bold'), bg='black', fg='white')
clock = Label(frame, font=('times', 150, 'bold'), bg='black', fg='white')
date1.grid(row=1, column=1, columnspan=1, rowspan=1, sticky=W+E+N+S)
clock.grid(row=2, column=1, columnspan=1, rowspan=1, sticky=W+E+N+S)

#Veriables
time1 = ''
date2 = ''
month_text = ''
app=FullScreenApp(root)
#root.attributes("-fullscreen", True)
#Functions
def tick():
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%I:%M:%S %p') # more information on function at https://docs.python.org/3.0/library/datetime.html#strftime-behavior
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clock.after(200, tick)
def date_display():
	date2 = today.strftime('%B %d, %Y')
	date1.config(text=date2)
	clock.after(200, date_display)

#Code	
date_display()	
tick()
root.mainloop(  )