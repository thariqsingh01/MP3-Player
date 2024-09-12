
#Import Modules
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
import os

#Creating the root window for python mp3 music player
root=Tk()
root.title('Music Player')
root.geometry("1000x700")
root.configure(bg= "#323b95")
root.resizable(False, False)
mixer.init()

def Add_Music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
 
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)
 
def Play_Music():
    Music_Name= Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

#icon
Icon_Image = PhotoImage(file="logo.png")
root.iconphoto(False,Icon_Image)
 
Top_Image = PhotoImage(file="logo.png")
Label(root, image=Top_Image, bg="#0f1a2b").pack()
 
#logo
#logo_Image = PhotoImage(file="logo.png")
#Label(root, image=logo_Image, bg="#0f1a2b").place(x=65, y=115)

# Button
Button_Play = PhotoImage(file="plays.png")
Button(root, image=Button_Play,height= 150, width=300, bg="#0f1a2b", bd=0, command=Play_Music).place(x=0, y=0)
 
Button_Stop = PhotoImage(file="stops.png")
Button(root, image=Button_Stop,height= 150, width=300, bg="#0f1a2b", bd=0, command=mixer.music.stop).place(x=0, y=180)
 
Button_Resume = PhotoImage(file="resumes.png")
Button(root, image=Button_Resume,height= 150, width=300, bg="#0f1a2b", bd=0, command=mixer.music.unpause).place(x=0, y=360)
 
Button_Pause = PhotoImage(file="pauses.png")
Button(root, image=Button_Pause,height= 150, width=300, bg="#0f1a2b", bd=0, command=mixer.music.pause).place(x=0, y=540)
 
#music
Menu = PhotoImage(file="menu.png")
Label(root, image=Menu, bg="#0f1a2b").pack(padx=10, pady=50, side=RIGHT)
 
Frame_Music = Frame(root, bd=2, relief = RIDGE)
Frame_Music.place(x=350, y=200, width=800, height=600)
 
Button(root, text="Add Music", width=15, height=2, font=("times new roman",12,"bold"),fg="Black", bg="#21b3de", command= Add_Music).place(x=350, y=150)
 
Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman",10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)
 
root.mainloop()
