from tkinter import *
from tkinter import filedialog
import os


root = Tk()
root.geometry("500x250")
root.title("The Better Notepad")
root.iconbitmap='TBN_Bin/logo.ico'

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)


def openFile():
  root.filename = filedialog.askopenfilename(title="Select a TEXT file", filetypes=(("text files","*.txt"),("all files", "*.*")))
  selectedTextFile = open(root.filename, 'r')
  print(root.filename)
  print(selectedTextFile.read())
#


def saveFile():
  notepadText = textBox.get('1.0','end')
  root.filename = filedialog.asksaveasfilename(initialdir="/home/runner/typewriter/TBN_Bin/TextFiles",title='Choose a location to save',filetypes=(("text files","*.txt"),("all files","*.*")))
  createNewFile = open(root.filename, 'w')
  createNewFile.write(notepadText)
  createNewFile.close()
  
#


def newFile():
  root.filename = filedialog.asksaveasfilename(initialdir="/home/runner/typewriter/TBN_Bin/TextFiles",title='Choose a location to save',filetypes=(("text files","*.txt"),("all files","*.*")))
  createNewFile = open(root.filename, 'w')
  createNewFile.close()
  textBox.delete('1.0', END)

#


def clearNotepad():
  textBox.delete('1.0', END)
#
  
openFileButton = Button(root,text="Open File",command=openFile).grid(row=0,column=0,padx=1,pady=1)
saveFileButton = Button(root,text="Save File",command=saveFile).grid(row=0,column=1,padx=1,pady=1)
newFileButton = Button(root,text="New File",command=newFile).grid(row=0,column=2,padx=1,pady=1)
clearNotepadButton = Button(root,text="Clear Notepad",command=clearNotepad).grid(row=0,column=3,padx=1,pady=1)


textBox = Text(root)
textBox.grid(row=1,column=0,columnspan=4)
textBox.insert('1.0',"Placeholder text")

root.mainloop()