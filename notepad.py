import tkinter
from tkinter.constants import BOTH, END, RIGHT, Y
import tkinter.messagebox
import tkinter.filedialog,os

if __name__ == '__main__':
   
    
    root=tkinter.Tk()
    root.title("Notepad")


    def cut():
        text.event_generate("<<Cut>>")
    def copy():
        text.event_generate("<<Copy>>")
    def paste():
        text.event_generate("<<Paste>>")
    def about():
        tkinter.messagebox.showinfo("Notepad","Notepad by Aviney")
    def newfile():
        global file
        root.title("Untitled-Notepad")
        file=None
        text.delete(1.0,END)
    def openfile():
        global file
        file= tkinter.filedialog.askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
        if (file is ""):
            file=None
        else:
            root.title(os.path.basename(file) + "-Notepad")
            text.delete(1.0,END)
            data=open(file,"r")
            text.insert(1.0,data.read())
            data.close()
        

    def savefile():
        global file
        
        if (file==None):
            file= tkinter.filedialog.asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])
            if (file is ""):
                file=None
            else:
             datad=open(file,"w")
             datad.write(text.get(1.0,  END))
             datad.close()
             root.title(os.path.basename(file) + "-Notepad")
        else:
             datad=open(file,"w")
             datad.write(text.get(1.0,  END))
             datad.close()

        
    def quitApp():
        root.destroy()
    scroll=tkinter.Scrollbar(root)
    scroll.pack(fill=Y,side=RIGHT)
    root.geometry("644x788")
    file=None
    text=tkinter.Text(root,font="lucida 13",yscrollcommand=scroll.set)
    text.pack(fill=BOTH,expand=True)
    scroll.config(command=text.yview)
    
    #menu
    menu=tkinter.Menu(root)
    m1=tkinter.Menu(menu,tearoff=0)
    m1.add_command(label="New",command=newfile)
    m1.add_command(label="Open",command=openfile)
    m1.add_command(label="Save",command=savefile)
    m1.add_separator()
    m1.add_command(label="Exit",command=quitApp)
    menu.add_cascade(menu=m1,label="File")
   

    m2=tkinter.Menu(menu,tearoff=0)
    m2.add_command(label="Cut",command=cut)
    m2.add_command(label="Copy",command=copy)
    m2.add_command(label="Paste",command=paste)
    menu.add_cascade(menu=m2,label="Edit")

    m3=tkinter.Menu(menu,tearoff=0)
    m3.add_command(label="About Notepad",command=about)
    menu.add_cascade(menu=m3,label="Help")
    
    root.config(menu=menu)



    root.mainloop()
