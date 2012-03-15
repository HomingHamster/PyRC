from Tkinter import *

class GUI(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.config(menu=self.menuBar())
        self.createWidgets()
        self.pack(fill=BOTH, expand=1)
        
        

    def createWidgets(self):
        serverListFrame = Frame()
        scrollbar = Scrollbar(serverListFrame, orient=VERTICAL)
        serverListbox = Listbox(serverListFrame, yscrollcommand=scrollbar.set)
        scrollbar.config(command=serverListbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        serverListbox.pack(side=LEFT, fill=Y, expand=1)
        
        serverListFrame.pack(side=LEFT, fill=Y)
        
        conversationFrame = Frame(self)
        outputBox = OutputBox(conversationFrame)
        outputBox.pack(fill=BOTH, expand=1)
        InputBox(conversationFrame)
        conversationFrame.pack(fill=BOTH, expand=1)
        
        listFrame = Frame()
        scrollbar = Scrollbar(listFrame, orient=VERTICAL)
        listbox = Listbox(listFrame, yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox.pack(side=LEFT, fill=Y, expand=1)
        
        listFrame.pack(side=RIGHT, fill=Y)
        
        serverListbox.insert(END, "a list entry")
        
        
       
    def menuBar(self):
        menubar = Menu(self)
        
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.quit())
        filemenu.add_command(label="Exit", command=None)
        
        menubar.add_cascade(label="File", menu=filemenu)
        return menubar
        
class OutputBox(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.outputBox = Text(self)
        self.scrollbar = Scrollbar(self)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        
        self.outputBox.configure(wrap=WORD,
                        yscrollcommand=self.scrollbar.set)
        
        self.outputBox.pack(fill = "both", side = "top", expand = True)
        self.outputBox.insert(INSERT, "Welcome to PyRC 0.1a\n")
        
        self.scrollbar.config(command=self.outputBox.yview)
        
    def append(self, text):
        self.outputBox.insert(INSERT, text + "\n")
        
class InputBox(Entry):
    def takeInput(self, event):
        line = self.get()
        if line[0] == "/":
            line = line[1:]
            print line
            line = line.split(" ")
            print line
            self.parseCommand(line[0], line[1:])
        else:
            GUI.irc_instance.send(line)
        self.contents.set("")
        self["textvariable"] = self.contents
    
    
    def __init__(self, master=None):
        Entry.__init__(self, master)
        self.pack(fill=X, side=BOTTOM)
        self.contents = StringVar()
        self.bind('<Key-Return>',
                  self.takeInput)
		
if __name__ == '__main__':
    root=Tk()
    app = GUI(master=root)
    app.mainloop()