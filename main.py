#text to speech converter

import tkinter as tk
from tkinter import *
import pyttsx3
engine =pyttsx3.init()

def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop

root=Tk()
textv=StringVar()

obj=Label(root,text="Text to speech",font=20,bd=1)
obj.pack(fill="both",expand="yes",padx=10,pady=10)

lb1=Label(obj,text="Text",font=20)
lb1.pack(side=tk.LEFT,padx=5)

text =Entry(obj,textvariable=textv,font=30,width=25,bd=2)
text.pack(side=tk.LEFT,padx=10)

btn=Button(obj,text="Speak",font=20,bg="black",fg="white",command=speaknow)
btn.pack(side=tk.LEFT,padx=10)

root.title("Text to Speech")
root.geometry("400x200")
root.resizable(False,False)
root.mainloop()
