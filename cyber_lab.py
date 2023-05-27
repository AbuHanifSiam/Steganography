from tkinter import*
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os
from stegano import lsb # pip install stegano

#creating a lab or design where we will do our work
root = Tk()
root.title("Steganography - Hide a Seecret Text Message in an Image")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.configure(bg="#6B3E8F")

#creating lab done
###################################################
def insertimage():
      global filename
      filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",
                                            filetype=(("PNG file","*.png"),
                                                      ("JPG file","*.jpg"),("All file","*")))
      
      img = Image.open(filename)
      img = img.resize((280,200)) # we need to resize our image to set into the frame. 
                                  #Frame means the box where we show this image
      img = ImageTk.PhotoImage(img)
      lbl.configure(image=img)
      lbl.image=img
      lbl.place(x=5,y=5)
       
def encrypt():
      global secret
      message = text1.get(1.0,END)
      secret = lsb.hide(str(filename),message)
      
       
def save():
      secret.save(input("Enter your file name(add **.png** after your file name): "))

def decrypt():
      clear_message = lsb.reveal(filename)
      text1.delete(1.0,END)
      text1.insert(END,clear_message)

###################################################
#icon
image_icon = PhotoImage(file="icon.gif")
root.iconphoto(False,image_icon)

###################################################
#logo
logo = PhotoImage(file ="logo.png")
Label(root,image=logo,bg="#6B3E8F").place(x=0,y=0) # set the logo where to show

Label(root,text="WELCOME TO CYBER LAB",font = "COLETTE 20 bold",bg="#4a355b",fg="#e2d6e6").place(x=185,y=5)

####################################################
#first Frame
frame1= Frame(root,bd=3,bg="#e2d6e6",width=300,height=200,relief=GROOVE)
frame1.place(x=25,y=150)

lbl=Label(frame1,bg="#e2d6e6")
lbl.place(x=40,y=10)
####################################################
#second frame
frame2 = Frame(root,bd=3,width=300,height=200,bg="#e2d6e6",relief=GROOVE)
frame2.place(x=370,y=150)

#creating text box to write text
text1 = Text(frame2,font="COLETTE 15",bg="#e2d6e6",fg="#4a355b",relief = GROOVE)
text1.place(x=0,y=0,width=300,height=250)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=300,y=0,height=255)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

####################################################
#third frame
frame3 = Frame(root,bd=3,bg ="#e2d6e6", width=300,height=80,relief=GROOVE)
frame3.place(x=25,y=400)

Button(frame3,text="Insert Image",width=10,height=1,font="COLETTE 14 bold",command = insertimage).place(x=0,y=30)
Button(frame3,text="Save Image",width=10,height=1,font="COLETTE 14 bold",command = save).place(x=165,y=30)
Label(frame3,text="Picture,Image,Photo File",bg="#e2d6e6",fg="#6b3e8f",font="COLETTE 12 bold").place(x=0,y=0)

####################################################
#fourth frame
frame4 = Frame(root,bd=3,bg ="#e2d6e6", width=300,height=80,relief=GROOVE)
frame4.place(x=370,y=400)

Button(frame4,text="Encrypt ",width=10,height=1,font="COLETTE 14 bold",command = encrypt).place(x=0,y=30)
Button(frame4,text="Decrypt",width=10,height=1,font="COLETTE 14 bold",command = decrypt).place(x=165,y=30)
Label(frame4,text="Picture,Image,Photo File",bg="#e2d6e6",fg="#6b3e8f",font="COLETTE 12 bold").place(x=0,y=0)



root.mainloop()
