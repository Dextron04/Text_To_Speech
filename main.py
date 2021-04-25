import pyttsx3 as pi
from tkinter import *

root = Tk()
root.geometry('350x300')
root.configure(bg='black')
root.title("Text to Speech")

Label(root, text = "Text to speech", font = 'arial 20 bold', bg = 'black').pack()
Label(text ="Tushin's text to speech", font = 'arial 15 bold', bg ='black' , width = '20').pack(side = 'bottom')

Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='black').place(x=20,y=60)
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20, y= 100)

def Text_To_Speech():
    Message = entry_field.get()
    engine = pi.init()
    engine.setProperty('rate', 130)
    engine.setProperty('voice', 20)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(Message)
    engine.runAndWait()

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_To_Speech ,width = '4').place(x=25,y=140)

Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)

Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)

root.mainloop()

