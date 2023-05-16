from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import *
import pandas as pd
from PIL import Image, ImageTk
import tkinter.messagebox as box
from operator import index
from tkinter import N
from turtle import clear
import pandas as pd
import re
import numpy as np
import openpyxl as xl
import threading
import tkinter as tk
import os
import sys
from new2 import dialog1
import dr_wael 

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Inventory')

        # ========================================================================
        # ============================background image============================
        # ========================================================================
        self.bg_frame = Image.open('images\\bim1.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='both', expand='yes')
        # ====== Login Frame =========================
        self.lgn_frame = Frame(self.window, bg='#040405', width=450, height=600)
        self.lgn_frame.place(x=800, y=70)

        # ========================================================================
        # ========================================================
        # ========================================================================
        self.txt = "WELCOME"
        self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, "bold"), bg="#040405",
                             fg='white',
                             bd=5,
                             relief=FLAT)
        self.heading.place(x=80, y=30, width=300, height=30)

        # ============ Sign In Image =============================================
        # ========================================================================
        self.sign_in_image = Image.open('images\\hyy.png')
        photo = ImageTk.PhotoImage(self.sign_in_image)
        self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.sign_in_image_label.image = photo
        self.sign_in_image_label.place(x=150, y=130)

        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
        self.sign_in_label = Label(self.lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
        self.sign_in_label.place(x=100, y=240)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
        self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.username_label.place(x=80, y=300)

        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"))
        self.username_entry.place(x=90, y=335, width=270)

        self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.username_line.place(x=80, y=359)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
        self.lgn_button = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.lgn_button)
        self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
        self.lgn_button_label.image = photo
        self.lgn_button_label.place(x=90, y=450)
        self.login = Button(self.lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                            bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.top)

        self.login.place(x=20, y=10)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
        self.password_label = Label(self.lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
        self.password_label.place(x=80, y=380)

        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*")
        self.password_entry.place(x=90, y=416, width=244)

        self.password_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
        self.password_line.place(x=80, y=440)
        # ======== Password icon ================
        # self.password_icon = Image.open('images\\password_icon.png')
        # photo = ImageTk.PhotoImage(self.password_icon)
        # self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
        # self.password_icon_label.image = photo
        # self.password_icon_label.place(x=550, y=414)
        # ========= show/hide password ==================================================================
        self.show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

        self.hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=400, y=420)

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=420)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=420)
        self.password_entry.config(show='*')
    
    def show1(self):
       os.system('dr_wael.py')

    def track(self):
        self.t_w1=Toplevel()
        self.t_w1.title("track Window")
        self.t_w1.geometry('1666x1200')
        self.t_w1.resizable(0, 0)
        self.t_w1.state('zoomed')
        self.t_w1.configure(bg='black')
 
        self.my_canvas=Canvas(self.t_w1,bg='black')
        self.my_canvas.config(width=1601, height=712)
        self.my_canvas.place(x=0, y=0)

        self.Label1 = Label(self.my_canvas,text = 'ID:', font=('yu gothic ui', 13, "bold"),fg='black',bd=5,relief=FLAT)
        self.entry = Entry(self.my_canvas,bd =5,relief=FLAT,width=50)

        self.btn2 = Image.open('images\\btn1.png')
        photo = ImageTk.PhotoImage(self.btn1) 
        self.btn2_label = Label(self.t_w1, image=photo, bg='#040405')
        self.btn2_label.image = photo
        self.btn2_label.place(x=1000, y=100)  
        self.btn = Button(self.btn2_label, text = 'Track', font=("yu gothic ui", 13, "bold"), width=20, bd=0,bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command = dialog1)



        # position of widgets
        
        self.Label1.place(x=950, y=30)
        self.entry.place(x=1000, y=35)
        self.btn.place(x=40, y=10)
        

        # image of the plane which used in tracking
        self.image= Image.open('images\\Untitled-111.jpg')
        #Resize the Image using resize method
        resized_image= self.image.resize((1360,780), Image.ANTIALIAS)
        self.new_image= ImageTk.PhotoImage(resized_image)
        self.my_canvas.create_image(0,0, image=self.new_image ,anchor='nw')



    def top(self):

        def part():
         top2=Toplevel()
         top2.title("EQUIPMENT PARTS") 

         def avilbale():
            pass

    
         def req():
            pass

         x=StringVar()
         x.set("YES")
         ent=Entry(top2, borderwidth=5, width=30)  
         ent.grid(row=0, sticky = "nesw")
         btn=Button(top2, text="CHECK IF AVILABLE", command=avilbale, width=30)
         btn.grid(row=1, column=0, padx=30, pady=10)
         lbl = Label(top2, textvariable=x)
         lbl.grid(row=1, column=1, padx=20, pady=10)
         btn1=Button(top2, text="REQUIRE PARTS", command=req, width=30)
         btn1.grid(row=2, column=0, padx=50) 
 #######################################################################




        if self.username_entry.get() =='a' and self.password_entry.get()=='a' :
          self.t_w=Toplevel()
          self.t_w.title("New Window")
          self.t_w.geometry('1166x718')
          self.t_w.resizable(0, 0)
          self.t_w.state('zoomed')
          self.bg_t_w = Image.open('images\\background1.png')
          photo = ImageTk.PhotoImage(self.bg_t_w)
          self.bg_panel1 = Label(self.t_w, image=photo)
          self.bg_panel1.image = photo
          self.bg_panel1.pack(fill='both', expand='yes')
######################################################################################################
          self.lgn_frame1 = LabelFrame(self.t_w, width=450, height=600, bg="#040405")
          self.lgn_frame1.place(x=15, y=30)
          lbl1 = Label(self.lgn_frame1, text="72345", font=('yu gothic ui', 21, "bold"), bg="#040405",fg='white',bd=5,relief=FLAT)
          lbl1.pack(side=LEFT, padx=20, pady=10)
          lbl2 = Label(self.lgn_frame1, text="Benha University Hospital", font=('yu gothic ui', 21, "bold"), bg="#040405",fg='white',bd=5,relief=FLAT)
          lbl2.pack(side=LEFT, padx=20, pady=10)
          lbl3 = Label(self.lgn_frame1, text="Ministry of Health\nDirectorate of Biomedical Engineering\nEqupment card", font=('yu gothic ui', 21, "bold"), bg="#040405",fg='white',bd=5,relief=FLAT)
          lbl3.pack(side=LEFT, padx=20, pady=10)
          lbl4 = Label(self.lgn_frame1, text="Inventory Number\nM15700", font=('yu gothic ui', 21, "bold"), bg="#040405",fg='white',bd=5,relief=FLAT)
          lbl4.pack(side=LEFT, padx=20, pady=1)
##########################################################################################################
          self.wrap2 = LabelFrame(self.t_w, width=450, height=600, bg="#040405")
          self.wrap2.place(x=450, y=190)
          # create a combobox
          self.selected_month = tk.StringVar()
          self.drop = ttk.Combobox(self.wrap2, textvariable=self.selected_month ,width=30 , height=1, font=('yu gothic ui', 21, "bold"))
          # get first 3 letters of every month name
          self.drop['values'] = ['ECG','VENT','Tower']
          # prevent typing a value
          self.drop['state'] = 'readonly'
          # place the widget
          self.drop.pack(fill=tk.X, padx=5, pady=5)
################################################################################################################
          self.wrap3 = Frame(self.t_w, bg='#040405', width=360, height=180)
          self.wrap3.place(x=560, y=350)

          self.btn1 = Image.open('images\\btn1.png')
          photo = ImageTk.PhotoImage(self.btn1)  
          self.btn1_label = Label(self.wrap3, image=photo, bg='#040405')
          self.btn1_label.image = photo
          self.btn1_label.place(x=25, y=20)                 
          self.butn1=Button(self.btn1_label, text='MAINTENANCE', font=("yu gothic ui", 13, "bold"), width=20, bd=0,bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.show1)
          self.butn1.place(x=40, y=10)

          self.btn2 = Image.open('images\\btn1.png')
          photo = ImageTk.PhotoImage(self.btn1)  
          self.btn2_label = Label(self.wrap3, image=photo, bg='#040405')
          self.btn2_label.image = photo
          self.btn2_label.place(x=25, y=100)                 
          self.butn2=Button(self.btn2_label, text='Tracking', font=("yu gothic ui", 13, "bold"), width=20, bd=0,bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=self.track)
          self.butn2.place(x=40, y=10)
###########################################################################################################
  



def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()