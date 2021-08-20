#Creating GUI with tkinter
import tkinter
from tkinter import *
import chatgui
from chatgui import *



def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Helvetica", 12, "bold italic"))
    
        res = chatbot_response(msg)
        ChatLog.insert(END, "AI: " + res + '\n\n')

            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
 

base = Tk()
base.title("Exception Processing Chatbot")
base.geometry("520x500")
base.resizable(width=TRUE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="100", font=("Helvetica", 12, "bold italic"),)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="arrow")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Helvetica", 12, "bold italic"), text="ASK", width="10", height=3,
                    bd=0, bg="#BA2317", activebackground="#E84D41",fg='#ffffff',
                    command= send )

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font=("Helvetica", 12, "bold italic"))



#Place all components on the screen
#scrollbar.place(x=376,y=6, height=386)
scrollbar.pack(side=RIGHT,fill=Y)
ChatLog.place(x=6,y=6, height=386, width=500)
EntryBox.place(x=128, y=401, height=90, width=500)
SendButton.place(x=6, y=401, height=90)

base.mainloop()
