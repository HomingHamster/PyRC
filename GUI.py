from Tkinter import *

class GUI(Frame):
    def __init__(self, master=Tk()):
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
        
        ServerList()
        
        
       
    def menuBar(self):
        menubar = Menu(self)
        
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.quit())
        filemenu.add_command(label="Exit", command=None)
        
        menubar.add_cascade(label="File", menu=filemenu)
        return menubar
        
class ServerList(Frame):
    def __init__(self, master=Toplevel()):
        Frame.__init__(self, master)
        serverListFrame = Frame(self)
        scrollbar = Scrollbar(serverListFrame, orient=VERTICAL)
        serverListbox = Listbox(serverListFrame, yscrollcommand=scrollbar.set)
        serverListbox.pack(fill=BOTH, side=LEFT, expand=1)
        scrollbar.config(command=serverListbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        serverListFrame.pack(fill=BOTH, expand=1)
        
        buttonFrame = Frame(self)
        connectButton = Button(buttonFrame, text="Connect", command=self.connect())
        connectButton.pack(side=LEFT)
        addServerButton = Button(buttonFrame, text="Add Server", command=self.addServer())
        addServerButton.pack(side=LEFT)
        editServerButton = Button(buttonFrame, text="Edit Server", command=self.editServer())
        editServerButton.pack(side=LEFT)
        deleteServerButton = Button(buttonFrame, text="Delete Server", command=self.deleteServer())
        deleteServerButton.pack(side=LEFT)
        buttonFrame.pack()
        
        self.pack(fill=BOTH, expand=1)
    def connect(self):
        pass
    def addServer(self):
        pass
    def editServer(self):
        pass
    def deleteServer(self):
        pass
        
class NewServerDialog(Frame):
    def __init__(self, master=Toplevel()):
        
        
        
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
    app = GUI()
    app.mainloop()