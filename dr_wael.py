import tkinter as tk
from tkinter import *
from matplotlib.pyplot import get
import pandas as pd
import os

from pyparsing import col
###############################################################################################
# Create a main app
root = Tk()
root.title('Inventory')
root.resizable(width=True,height=True)
labels = Frame(root)
labels.config(bg='#0174DF')
labels1=Frame(root)
labels1.config(bg='#0174DF')
root.geometry("1210x770")
root.config(bg='#0174DF')
################################################################################################
#Functions
g1= StringVar()
g2= StringVar()
g3= StringVar()
g4= StringVar()
g5= StringVar()
g6= StringVar()
g7= StringVar()
g8= StringVar()
x=StringVar()


def show():
    global g , d1 ,ch ,g3
    g=clicked.get()
    ch=["ECG","VENT","Tower"]
    for i in ch :
        if i == g:
            d1= pd.read_csv("I:\yyy\BIO\D_1.csv")
            g1.set(d1[i][0])
            g2.set(d1[i][1])
            g3.set(d1[i][2])
            g4.set(d1[i][3])
            g5.set(d1[i][4])
            g6.set(d1[i][5])
            g7.set(d1[i][6])

###############################################################################################
def on_click(event):
        event.widget.delete(0, tk.END)

def save():
    g=clicked.get()
    ch=["ECG","VENT","Tower"]
    for i in ch :
        if i == g:
            txt_file = open(f"I:\yyy\BIO\{i}.txt","a")
            txt_file.write('Date      :     ' + ent71.get() + '\n')
            txt_file.write('\n')
            txt_file.write('Job done By         ' + ent9.get() + 'at' + ent8.get() + '\n')
            txt_file.write('Problem solved      :     ' + ent91.get() + '\n') 
            txt_file.write('Report     :     ' + ent10.get() + '\n') 
            txt_file.write('Job finished at     :      ' + ent9.get() + '\n') 
            txt_file.write('\n')
            txt_file.write('********************************************************' + '\n') 
            # Close file
            txt_file.close()
 
def hist():
    global p
    g=clicked.get()
    ch=["ECG","VENT","Tower"]
    for i in ch :
        if i == g:
            p = os.startfile(f'I:\yyy\BIO\{i}.txt')
            return p

def avilbale():
    global parts ,v , x
    v=ent11.get()
    parts = ["p_1","p_2","p_3", "p_4", "p_5"]      
    if v in parts:
        x.set("YES")
    else :           
        x.set("NO")

def req():
    global v
    v=ent11.get()
    if v =="NO" :
        noti=Button(root , text="N\no\nt\ni\nf\ni\nc\na\nt\ni\no\nn\ns"  ,command=note,bg="red", width= 3,height=20)
        noti.grid(row=2 ,column=1)


def note():
    pass

################################################################################################    
#GiUI
wrap1 = LabelFrame(root, text="Health Facility",bg='#0174DF')
wrap1.grid(row=0,column=0 , padx=10, pady=1)
lbl1 = Label(wrap1, text="72345", font=('Helvatical bold',15),bg='#0174DF')
lbl1.grid(row=0,column=0 , padx=50, pady=10)
lbl2 = Label(wrap1, text="Benha University Hospital", font=('Helvatical bold',15),bg='#0174DF')
lbl2.grid(row=0,column=1 , padx=50, pady=10)
lbl3 = Label(wrap1, text="Ministry of Health\nDirectorate of Biomedical Engineering\nEqupment card", font=('Helvatical bold',15),bg='#0174DF')
lbl3.grid(row=0,column=2 , padx=50, pady=10)
lbl4 = Label(wrap1, text="Inventory Number\nM15700", font=('Helvatical bold',15),bg='#0174DF')
lbl4.grid(row=0,column=3 , padx=50, pady=1)
################################################################################################
wrap2 = Label(root,bg='#0174DF')
wrap2.grid(row=1,column=0 , padx=10, pady=1)
clicked= StringVar()
clicked.set("Check your Device ")
drop = OptionMenu(wrap2,clicked, "ECG","VENT","Tower")
drop.config(width=20, height=2)
drop.pack(padx=10, pady=10)

####################################################################################################
wrap3 = LabelFrame(labels, text="Equipment Details",bg='#0174DF')
wrap3.grid(row=2, column=0, padx=30 , pady=10)

btn1=Button(wrap3, text="Show details", command=show, width=20 , height=2, font=('Helvatical bold',12))
btn1.grid(row=0,column=0 , padx=50, pady=10)

lbl5= Label(wrap3,text="ID", font=('Helvatical bold',12),bg='#0174DF')
lbl5.grid(row=1,column=0 , padx=20, pady=10)

ent = Entry(wrap3, textvariable=g1, width=30)
ent.grid(row=1,column=1, padx=20, pady=10)

lbl6= Label(wrap3,text="MODEL", font=('Helvatical bold',12),bg='#0174DF')
lbl6.grid(row=2,column=0 , padx=20, pady=10)

ent1 = Entry(wrap3, textvariable=g2, width=30)
ent1.grid(row=2,column=1, padx=20, pady=10)

lbl5= Label(wrap3,text="MANUFACTURER", font=('Helvatical bold',12),bg='#0174DF')
lbl5.grid(row=3,column=0 , padx=20, pady=10)

ent2 = Entry(wrap3, textvariable=g3, width=30)
ent2.grid(row=3,column=1, padx=20, pady=10)

lbl5= Label(wrap3,text="SERIAL NO", font=('Helvatical bold',12),bg='#0174DF')
lbl5.grid(row=4,column=0 , padx=20, pady=10)

ent3 = Entry(wrap3, textvariable=g4, width=30)
ent3.grid(row=4,column=1, padx=20, pady=10)

lbl5= Label(wrap3,text="START CONTRACT", font=('Helvatical bold',12),bg='#0174DF')
lbl5.grid(row=5,column=0 , padx=20, pady=10)

ent4 = Entry(wrap3, textvariable=g5, width=30)
ent4.grid(row=5,column=1, padx=20, pady=10)

lbl5= Label(wrap3,text="END CONTRACT", font=('Helvatical bold',12),bg='#0174DF')
lbl5.grid(row=6,column=0 , padx=20, pady=10)

ent5 = Entry(wrap3, textvariable=g6, width=30)
ent5.grid(row=6,column=1, padx=20, pady=10)

lbl5= Label(wrap3,text="PRICE", font=('Helvatical bold',12),bg='#0174DF')
lbl5.grid(row=7,column=0 , padx=20, pady=10)

ent6 = Entry(wrap3, textvariable=g7, width=30)
ent6.grid(row=7,column=1, padx=20, pady=10)
# ########################################################################################################
wrapm = Label(labels,bg='#0174DF')
wrapm.grid(row=2, column=1, padx=30 , pady=10)

wrap4 = LabelFrame(wrapm, text="MAINTENANCE",width=300,bg='#0174DF')
wrap4.grid(row=0, column=0, padx=0 , pady=10)

lble = Label(wrap4, text="TECH NAME", font=('Helvatical bold',12),bg='#0174DF')
lble.grid(row=0, column=0, padx=50, pady=10)  

ent7=Entry(wrap4, borderwidth=5, width=30)  
ent7.grid(row=0, column=1, padx=50, pady=10) 
ent7.insert(0,"Enter your name:") 
ent7.bind("<Button-1>", on_click)

lbl1 = Label(wrap4, text="DATE", font=('Helvatical bold',12),bg='#0174DF')
lbl1.grid(row=1, column=0, padx=20, pady=10)

ent71=Entry(wrap4, borderwidth=5, width=30)  
ent71.grid(row=1, column=1, padx=20, pady=10) 
ent71.insert(0,"Enter date DD/MM/YYYY")
ent71.bind("<Button-1>", on_click) 

lble1 = Label(wrap4, text="JOB BEGIN", font=('Helvatical bold',12),bg='#0174DF')
lble1.grid(row=2, column=0, padx=20, pady=10)

ent8=Entry(wrap4, borderwidth=5, width=30)  
ent8.grid(row=2, column=1, padx=20, pady=10) 
ent8.insert(0,"Enter date ,Time of beginning:")
ent8.bind("<Button-1>", on_click) 

lble2 = Label(wrap4, text="JOB END", font=('Helvatical bold',12),bg='#0174DF')
lble2.grid(row=3, column=0, padx=20, pady=10)

ent9=Entry(wrap4, borderwidth=5, width=30)  
ent9.grid(row=3, column=1, padx=20, pady=10) 
ent9.insert(0,"Enter date ,Time of ending:") 
ent9.bind("<Button-1>", on_click)   

lble21 = Label(wrap4, text="PROBLEM", font=('Helvatical bold',12))
lble21.grid(row=4, column=0, padx=20, pady=10)

ent91=Entry(wrap4, borderwidth=5, width=30)  
ent91.grid(row=4, column=1, padx=20, pady=10) 
ent91.insert(0,"what is the problem?") 
ent91.bind("<Button-1>", on_click)  

lble22 = Label(wrap4, text="SOLVED !", font=('Helvatical bold',12),bg='#0174DF')
lble22.grid(row=5, column=0, padx=20, pady=10)

ent92=Entry(wrap4, borderwidth=5, width=30)  
ent92.grid(row=5, column=1, padx=20, pady=10) 
ent92.insert(0,"YES or NO !") 
ent92.bind("<Button-1>", on_click)   

lble3 = Label(wrap4, text="TECH REPORT", font=('Helvatical bold',12),bg='#0174DF')
lble3.grid(row=6, column=0, padx=20, pady=10)  

ent10=Entry(wrap4, borderwidth=5, width=30)  
ent10.grid(row=6, column=1, padx=20, pady=10) 
ent10.insert(0,"Enter your notes:") 
ent10.bind("<Button-1>", on_click)

btn1=Button(wrap4, text="SAVE", command=save , width=20)
btn1.grid(row=7, column=0, padx=30, pady=10)

btn2=Button(wrap4, text="HISTORY", command=hist , width=20)
btn2.grid(row=7, column=1, padx=30, pady=10)
# # ##########################################################################################################
wrap5 = LabelFrame(wrapm, text="Parts", width=300,bg='#0404B4')
wrap5.grid(row=1, column=0, padx=0 , pady=10)

ent11=Entry(wrap5, borderwidth=5, width=30)  
ent11.grid(row=0, sticky = "nesw", padx=20, pady=10 )
ent11.insert(0,"Check parts needed:") 
ent11.bind("<Button-1>", on_click)  

btn=Button(wrap5, text="AVILABLE !", command=avilbale, width=10 , font=('Helvatical bold',12))
btn.grid(row=1, column=0)

lbl = Label(wrap5, textvariable= x , font=('Helvatical bold',12) , width=10,bg='#0404B4')
lbl.grid(row=1, column=1, padx=5, pady=10)

btn1=Button(wrap5, text="REQUIRE PARTS", command=req, width=15 , font=('Helvatical bold',12))
btn1.grid(row=1, column=2,  padx=5, pady=10)

######################################################################################################
# Gridding Main Frames
root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 1)
root.grid_columnconfigure(0, weight = 1)
##########################################################
labels.grid(row = 2, column = 0, sticky = "nesw")
labels1.grid(row = 2, column = 1, sticky = "nesw")
######################################################################################################
root.mainloop()