from tkinter import *
from tkinter import filedialog
import os

TextFiles = os.listdir('TBN_Bin/TextFiles/')

getTxtFiles = []
for i in TextFiles:
  fileName, fileExtension = os.path.splitext(i)
  if fileExtension == ".txt":
    getTxtFiles.append(i)


root = Tk()
root.geometry("500x250")
root.title("The Better Notepad")
root.iconbitmap='TBN_Bin/logo.ico'

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)

def openFile():
  global file
  root.filename = filedialog.askopenfilename(initialdir="/TBN_Bin/", title="Select a TEXT file", filetypes=(("text files","*.txt"),("all files", "*.*")))
  selectedTextFile = open(root.filename, 'r')
  print(selectedTextFile.read())
#

def saveFile():
  
    
  
openFileButton = Button(root,text="Open File",command=openFile).grid(row=0,column=0,padx=1,pady=1)
saveFileButton = Button(root,text="Save File").grid(row=0,column=1,padx=1,pady=1)
newFileButton = Button(root,text="New File").grid(row=0,column=2,padx=1,pady=1)
settingsButton = Button(root,text="Settings").grid(row=0,column=3,padx=1,pady=1)
textBox = Text(root)
  

textBox.grid(row=1,column=0,columnspan=4)
textBox.insert('1.0',"hi")


root.mainloop()