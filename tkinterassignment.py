import tkinter
from tkinter import *



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=False,height=False)
        self.master.geometry('{}x{}'.format(600, 250))
        self.master.title('Check files')

        self.txtFile1 = Entry(self.master,text='',width=70)
        self.txtFile1.grid(row=2,column=2,padx=(15,0),pady=(15,0))

        self.txtFile2 = Entry(self.master,text='',width=70)
        self.txtFile2.grid(row=3,column=2,padx=(15,0),pady=(15,0))

        self.browsebtn1 = Button(self.master,text='Browse...',width=15,height=1)
        self.browsebtn1.grid(row=2,column=0,padx=(15,0),pady=(15,0))


        self.browsebtn2 = Button(self.master,text='Browse...',width=15,height=1)
        self.browsebtn2.grid(row=3,column=0,padx=(15,0),pady=(15,0))

        self.checkfiles = Button(self.master,text='Check for files...',width=15,height=2)
        self.checkfiles.grid(row=4,column=0,padx=(15,0),pady=(15,0))

        self.closebtn = Button(self.master,text='Close Program',width=15,height=2)
        self.closebtn.grid(row=4,column=2,padx=(15,0),pady=(15,0),sticky=E)

        







if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
