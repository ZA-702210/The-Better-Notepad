#Name: Zubair Azizi
#Date: 01/20/2023
#Purpose: A notepad that can open text files, save them, make new ones, and also clears the notepad


#Imports tkinter for GUI widgets
#Imports filedialog from tkinter for opening the file explorer
from tkinter import *
from tkinter import filedialog


#Creates a parent object for all the tkinter widgets
#Sets the size of the main window
#Sets the icon (doesn't work because of replit)
root = Tk()
root.geometry("500x250")
root.title("The Better Notepad")
root.iconbitmap='/home/runner/typewriter/TBN_Bin/logo.ico'


#Configures weightings of the grid system, and makes it so that the buttons are equally apart
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)


#Open file function
#Filedialog obtains the path
#Rest of the code handles like file given the path of it
def openFile():
  root.filename = filedialog.askopenfilename(title="Select a TEXT file", filetypes=(("text files","*.txt"),("all files", "*.*")))
  selectedTextFile = open(root.filename, 'r')
  print(root.filename)
  textBox.delete('1.0', END)
  textBox.insert(END, selectedTextFile.read())
  selectedTextFile.close()
  print(selectedTextFile.read())
#


#Save file function
#Filedialog obtains the path
#Rest of the code handles like file given the path of it
def saveFile():
  notepadText = textBox.get('1.0','end')
  root.filename = filedialog.asksaveasfilename(initialdir="/home/runner/typewriter/TBN_Bin/TextFiles",title='Choose a location to save',filetypes=(("text files","*.txt"),("all files","*.*")))
  createNewFile = open(root.filename, 'w')
  createNewFile.write(notepadText)
  createNewFile.close()
  
#

  
#New file function
#Filedialog obtains the path
#Rest of the code handles like file given the path of it
def newFile():
  root.filename = filedialog.asksaveasfilename(initialdir="/home/runner/typewriter/TBN_Bin/TextFiles",title='Choose a location to save',filetypes=(("text files","*.txt"),("all files","*.*")))
  createNewFile = open(root.filename, 'w')
  createNewFile.close()
  textBox.delete('1.0', END)

#

  
#Empties a notepad
def clearNotepad():
  textBox.delete('1.0', END)
#


#Creates the buttons
#Attached to the parent; root
#Each button has its own text and padding settings
#Columns puts the buttons at the right spots
openFileButton = Button(root,text="Open File",command=openFile).grid(row=0,column=0,padx=1,pady=1)
saveFileButton = Button(root,text="Save File",command=saveFile).grid(row=0,column=1,padx=1,pady=1)
newFileButton = Button(root,text="New File",command=newFile).grid(row=0,column=2,padx=1,pady=1)
clearNotepadButton = Button(root,text="Clear Notepad",command=clearNotepad).grid(row=0,column=3,padx=1,pady=1)


#Making the textbox and putting it under root
#Configures it under row 1, and spans accross all columns
#Inserts placeholder text on the first row
textBox = Text(root)
textBox.grid(row=1,column=0,columnspan=4)
textBox.insert('1.0',"Placeholder text")


#CRITICAL otherwise it wont update
root.mainloop()