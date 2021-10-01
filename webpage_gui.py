import tkinter
from tkinter import *
from tkinter import filedialog
import webbrowser


def html(self):
    header = self.header_text.get() #grabs the value stored in the second text box and stores it in variable header
    f = open("text.html", "w") #opens an html file or creates one if that file doesnt exist and overwrites its content
    x=("""<html> 
         <body> 
            <h1>
              {} 
           </h1>
         </body> 
    </html> """.format(header))# assiging html structure to x with a wild card for the content of <h1> use format to fill  the wild card
    f.write(x) #write the contents of variable x to the document
    f.close() # close the doc
    webbrowser.open("text.html") #open file in web browser
    


class WebpageGUI:
    def __init__(self, master): 
        self.master = master
        master.title("Webpage Creator") #set title of tkinter window

        self.lblHeader = Label(master, text="Set header")   #create label for the text entry line
        self.lblHeader.grid(row=2,column=0,padx=(15,0))

        self.file_button = Button(master, text="Create web page", command = lambda: html(self),width=12,height=2) #this button will trigger the html function
        self.file_button.grid(row=3,column=1,padx=(15,15),pady=(15,15))

        self.header_text = StringVar()

        self.txtHeader = Entry(self.master, text=self.header_text,width=30) #create the entry line for the user to type in their own header content. assign this 
        self.txtHeader.grid(row=2,column=1,padx=(15,15))                    #line's text to = self.header_text so that when we click the webpage button
                                                                            #the html func will be able to get() the values stored in that variable
                                                                


if __name__ == '__main__':
    root = Tk()
    my_gui = WebpageGUI(root)
    root.mainloop()
