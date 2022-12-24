from tkinter import *
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
currentRow=-1

root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=1)
root.columnconfigure(3,weight=1)
#root.columnconfigure(4,weight=5)
#root.rowconfigure(0,weight=4)
#root.rowconfigure(1,weight=0)

openFileButton = Button(root,text="Open File").grid(row=0,column=0,padx=1,pady=1)
saveFileButton = Button(root,text="Save File").grid(row=0,column=1,padx=1,pady=1)
newFileButton = Button(root,text="New File").grid(row=0,column=2,padx=1,pady=1)
settingsButton = Button(root,text="Settings").grid(row=0,column=3,padx=1,pady=1)
textBox = Text(root).grid(row=1,column=0,columnspan=4)

#Creating Labels
#myLabel = Label(root, text="damn")
#myLabel1 = Label(root, text="loser")

#Creating Buttons
#def func():
  #global currentRow
  #myLabel = Label(root, text="i pressed a button").grid(row=currentRow+1)
  #currentRow = currentRow+1

#myButton = Button(root, text="New File", padx=50, pady=50, command=func, fg='blue',bg='red',)

#Put onto screen
#myButton.grid(row=currentRow+1,column=1)
#currentRow = currentRow+1

#myLabel.grid(row=0,column=1)
#myLabel1.grid(row=0,column=0)
#myButton.grid(row=1,column=0)

root.mainloop()