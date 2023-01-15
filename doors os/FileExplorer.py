from tkinter import *
from tkinter import filedialog
import os

def openFile():
    filepath = filedialog.askopenfilename(initialdir='/Users/black/OneDrive/Desktop/doors os/user/data/',
                                           title='Open Files',
                                           filetypes= (('text files', '*.txt'),
                                           ('python files', '*.py'),
                                           ('executable files', '*.exe'),
                                           ('all files', '*.*')))
    os.startfile(filepath)

window = Tk()
button = Button(text='Open',command=openFile)
button.pack()
window.mainloop()