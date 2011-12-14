import Tkinter
import socket
import Queue
import threading
import sys
import String

class RunClient:
    def main(self):
        if self.existingStartupConf() == true:
            self.readStartupConf()
        else:
            GUI.startupDialog()
            
    def existingStartupConf(self):
        pass

class IRCInstance:
    def __init__(self):
        self.HOST="irc.freenode.net"
        self.PORT=6667
        self.NICK=""
        self.IDENT=""
        self.REALNAME=""
        self.readbuffer=""
        
    def connect(self, address, port):
        self.connection = socket.scoket()
        self.connection.connect(address, port)
        self.connection.send("NICK %s\r\n" % self.NICK)
        self.connection.send("USER %s %s bla :%s\r\n" 
                        % (self.IDENT, self.HOST, self.REALNAME))
        
    def serverSend(self, command, args):
        args = " ".join(args)
        self.connection.send("%s %s" % (command, args))
        
    def channelSend(self, channel, message):
        pass
        
    def processInput(self, line):
        line = line.split(" ")
        if line[0] == "PING":
            self.serverSend("PONG", line[1])
    
    def readSock(self):
        self.readbuffer += self.connection.recv(1024)
        temp = self.readbuffer.split("\n")
        self.readbuffer = temp.pop()
        for line in temp:
            line = line.rstrip()
            self.processInput(line)

class OutputBox(Tkinter.Text):
    def append(self, text):
        self.insert(Tkinter.INSERT, text + "\n")
        
    def __init__(self, master=None):
        Tkinter.Text.__init__(self, master)
        self.pack(fill = "both", side = "top", expand = True)
        self.insert(Tkinter.INSERT, "Welcome to PyRC 0.1a\n")
    
class InputBox(Tkinter.Entry):
    def takeInput(self, event):
        line = self.get()
        if line[0] == "/":
            line = line[1:]
            print line
            line = line.split(" ")
            print line
            self.parseCommand(line[0], line[1:])
        else:
            IRCInstance.send(line)
        self.contents.set("")
        self["textvariable"] = self.contents
    
    def parseCommand(self, command, args):
        if command.lower() == "server":
            if len(args) == 2:
                IRCInstance.connect(args[1], args[2])
            elif len(args) == 1:
                IRCInstance.connect(args[1], 6667)
            else:
                GUI.output_box.append("Invalid Command")
    
    def __init__(self, master=None):
        Tkinter.Entry.__init__(self, master)
        self.pack(fill = "x", side = "bottom")
        self.contents = Tkinter.StringVar()
        self.bind('<Key-Return>',
                  self.takeInput)

class GUI(Tkinter.Frame):
       
    def makeMenuBar(self):
        self.menubar = Tkinter.Menu(self)
        
        self.filemenu = Tkinter.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Open", command=self.hello)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit)
        
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        
    def startupDialog(self):
        pass
        
    def hello(self):
        pass
    
    def __init__(self, master=None):
        Tkinter.Frame.__init__(self, master)
        self.pack()
        self.makeMenuBar()
        master.config(menu=self.menubar)
        GUI.output_box = OutputBox()
        GUI.input_box = InputBox()
        
    
root = Tkinter.Tk()
app = GUI(master=root)
app.mainloop()