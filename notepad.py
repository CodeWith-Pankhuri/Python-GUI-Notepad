from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file=None
    TextArea.delete(1.0,END) # 1.0 means 1st line 0th character.It takes one by one character till end.

def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()

def saveFile():
    global file
    if file == None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",
                               filetypes=[("All Files","*.*"),("Text Document","*.txt")])
        if file=="":
            file=None
        else:
            #Save as a new file-
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            root.title(os.path.basename(file)+" - Notepad")
            print("File Saving") # For Checking file is saved or not
    else:
        # Again save the existing file-
        f=open(file,"w")
        f.write(TextArea.get(1.0, END))
        f.close()

def cut():
    TextArea.event_generate("<<Cut>>") # Tkinter built-in event handling method
def copy():
    TextArea.event_generate("<<Copy>>") # No need to write logic of these events-It works internally.
def paste():
    TextArea.event_generate("<<Paste>>")

def about():
    showinfo("Notepad", "Notepad made by Pankhuri")


if __name__ == '__main__':

    #Basic window setup-
    root=Tk()
    root.geometry("600x500")
    root.wm_iconbitmap("notepad.ico")
    root.title("Untitled - Notepad")

    #Add text area-
    TextArea=Text(root, font=("lucida", 13))
    TextArea.pack(fill=BOTH,expand=1)
    file=None

    # Creating Menu bars-
    menubar=Menu(root)

    # Sub menu-File
    fileMenu=Menu(menubar,tearoff=False)
    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open",command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=fileMenu)

    # Sub menu- Edit
    editMenu=Menu(menubar,tearoff=False)
    editMenu.add_command(label="Cut",command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    menubar.add_cascade(label="Edit", menu=editMenu)

    # Sub menu- Help
    helpMenu=Menu(menubar,tearoff=False)
    helpMenu.add_command(label="About Notepad",command=about)
    menubar.add_cascade(label="Help", menu=helpMenu)

    root.config(menu=menubar)

   # Adding Scroll bar on right side-
    scroll=Scrollbar(TextArea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=TextArea.yview)  # 1st step
    TextArea.config(yscrollcommand=scroll.set) # 2nd step for adding scrollbar in GUI

    root.mainloop()




