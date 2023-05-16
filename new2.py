# librarries used in app
from tkinter import *
import pandas as pd
from PIL import Image, ImageTk
import tkinter.messagebox as box


# the main window
root=Tk()
root.title('find your device')
root.geometry("1285x650")
frame = Frame(root)



def getx_y_V(self):
    df=pd.read_csv('I:\yyy\distance_v.csv' )
    d=df["distance"]

    x=df['distance'][df.index[-1]]

    ind=df.index[df['distance']==x].tolist()
    f=ind[0]

    l=[]
    for i in range(ind[0]+1):
        l.append(d[i])

    l.sort(reverse=True)
    x1=l[-1]
    x11=l[-2]
    x111=l[-3]
    x1111=l[-4]

    ind1=df.index[df['distance']==x1].tolist()
    ind11=df.index[df['distance']==x11].tolist()
    ind111=df.index[df['distance']==x111].tolist()
    ind1111=df.index[df['distance']==x1111].tolist()

    x2=ind1[0]
    x22=ind11[0]
    x222=ind111[0]
    x2222=ind1111[0]

    s1=df['scanner'][df.index[x2]]
    s2=df['scanner'][df.index[x22]]
    s3=df['scanner'][df.index[x222]]
    s4=df['scanner'][df.index[x2222]]


    if f==4 :
       if s1 == 'A' :
          ox= 60
          oy=45
       elif s1 == 'E' and s2=='A' :
          ox=179
          oy=45
       elif s1 == 'E' and s2=='B' :
          ox=298
          oy=45
       elif s1== 'B' and s2== 'E':
          ox=388
          oy=45
       elif s1== 'B' and s2== 'D':
          ox=507
          oy=45
       elif s1== 'D' and s2== 'B':
          ox=597
          oy=45
       elif s1== 'D' and s2== 'C':
          ox=716
          oy=45
       elif s1== 'C' and s2== 'D' and x11 <= 8.499:
          ox=806
          oy=45       
       elif s1== 'C' and s2== 'D' and x11 > 8.499 and x11 <= 13:
          ox=925
          oy=45
       elif s1== 'C' and s2== 'D' and x11 > 13 and x11 < 17:
          ox=1015
          oy=45
       else :
          ox=1150
          oy=45
    elif f < 4 :
        if f < 2 and s1 == 'C':#sec352################
         if x1 < 6 : #1
            ox=926
            oy=122
         elif x1 >6 and x1< 15  and s2 =='D':#4
            ox=1046
            oy=122
        elif  f == 0 and x1 >15 :#3
         ox=1046
         oy=229
        elif  f == 0 and x1 >6 and x1 < 15 :#2 
         ox=926
         oy=229  
        elif f < 2 and (s1=='D' or s1 == 'C') and (s2=='D' or s2 == 'C'):#sec353#################   #3
         ox=806
         oy=229
        elif f < 3 :
         if s1=='D' and s2==' c' and s3=='B' and x1 < 15:   #1
            ox=717
            oy=122    
         elif (s1=='D' or s1=='C' or s1=='B') and (s2=='D' or s2=='C' or s2=='B') and (s3=='D' or s3=='C' or s3=='B') and x1 > 19:  #2 ####Check#####
            ox=717
            oy=229
         elif (s1=='D' or s1=='C') and (s2=='D' or s2=='C') and (s3=='B'):#  4
            ox=806
            oy=122
        elif s1=='B' and (s2=='D' or s2=='C') and (s3=='D' or s3=='C') and s4=='E':#sec354#####################  #1
         ox=507
         oy=122
        elif f<3 and s1=='B' and s2=='D' and x1 > 14 and x11> 33:#2
         ox=507
         oy=229
        elif f<3 and s1=='B' and s2=='D' and x1<14 and x11<33: #3
         ox=597
         oy=229
        elif f<3 and (s1=='B' or s1=='D') and (s2=='B' or s2=='D') and s3=='E': #4
         ox=597
         oy=122

         
    return ox , oy
#############################################################################################
def getx_y_M(self):
    df1=pd.read_csv('I:\yyy\distance_m.csv' )
    d=df1["distance"]

    x=df1['distance'][df1.index[-1]]

    ind=df1.index[df1['distance']==x].tolist()
    f=ind[0]

    l=[]
    for i in range(ind[0]+1):
        l.append(d[i])

    l.sort(reverse=True)
    x1=l[-1]
    x11=l[-2]
    x111=l[-3]
    x1111=l[-4]

    ind1=df1.index[df1['distance']==x1].tolist()
    ind11=df1.index[df1['distance']==x11].tolist()
    ind111=df1.index[df1['distance']==x111].tolist()
    ind1111=df1.index[df1['distance']==x1111].tolist()

    x2=ind1[0]
    x22=ind11[0]
    x222=ind111[0]
    x2222=ind1111[0]

    s1=df1['scanner'][df1.index[x2]]
    s2=df1['scanner'][df1.index[x22]]
    s3=df1['scanner'][df1.index[x222]]
    s4=df1['scanner'][df1.index[x2222]]


    if f==4 :
       if s1 == 'A' :
          ox= 60
          oy=45
       elif s1 == 'E' and s2=='A' :
          ox=179
          oy=45
       elif s1 == 'E' and s2=='B' :
          ox=298
          oy=45
       elif s1== 'B' and s2== 'E':
          ox=388
          oy=45
       elif s1== 'B' and s2== 'D':
          ox=507
          oy=45
       elif s1== 'D' and s2== 'B':
          ox=597
          oy=45
       elif s1== 'D' and s2== 'C':
          ox=716
          oy=45
       elif s1== 'C' and s2== 'D' and x11 <= 8.499:
          ox=806
          oy=45       
       elif s1== 'C' and s2== 'D' and x11 > 8.499 and x11 <= 13:
          ox=925
          oy=45
       elif s1== 'C' and s2== 'D' and x11 > 13 and x11 < 17:
          ox=1015
          oy=45
       else :
          ox=1150
          oy=45
    elif f < 4 :
        if f < 2 and s1 == 'C':#sec352################
         if x1 < 6 : #1
            ox=926
            oy=122
         elif x1 >6 and x1< 15  and s2 =='D':#4
            ox=1046
            oy=122
        elif  f == 0 and x1 >15 :#3
         ox=1046
         oy=229
        elif  f == 0 and x1 >6 and x1 < 15 :#2 
         ox=926
         oy=229  
        elif f < 2 and (s1=='D' or s1 == 'C') and (s2=='D' or s2 == 'C'):#sec353#################   #3
         ox=806
         oy=229
        elif f < 3 :
         if s1=='D' and s2==' c' and s3=='B' and x1 < 15:   #1
            ox=717
            oy=122    
         elif (s1=='D' or s1=='C' or s1=='B') and (s2=='D' or s2=='C' or s2=='B') and (s3=='D' or s3=='C' or s3=='B') and x1 > 19:  #2 ####Check#####
            ox=717
            oy=229
         elif (s1=='D' or s1=='C') and (s2=='D' or s2=='C') and (s3=='B'):#  4
            ox=806
            oy=122
        elif s1=='B' and (s2=='D' or s2=='C') and (s3=='D' or s3=='C') and s4=='E':#sec354#####################  #1
         ox=507
         oy=122
        elif f<3 and s1=='B' and s2=='D' and x1 > 14 and x11> 33:#2
         ox=507
         oy=229
        elif f<3 and s1=='B' and s2=='D' and x1<14 and x11<33: #3
         ox=597
         oy=229
        elif f<3 and (s1=='B' or s1=='D') and (s2=='B' or s2=='D') and s3=='E': #4
         ox=597
         oy=122

         
    return ox , oy
###########################################################################################
def getx_y_HM(self):
    df2=pd.read_csv('I:\yyy\distance_hmsoft.csv' )
    d=df2["distance"]

    x=df2['distance'][df2.index[-1]]

    ind=df2.index[df2['distance']==x].tolist()
    f=ind[0]

    l=[]
    for i in range(ind[0]+1):
        l.append(d[i])

    l.sort(reverse=True)
    x1=l[-1]
    x11=l[-2]
    x111=l[-3]
    x1111=l[-4]

    ind1=df2.index[df2['distance']==x1].tolist()
    ind11=df2.index[df2['distance']==x11].tolist()
    ind111=df2.index[df2['distance']==x111].tolist()
    ind1111=df2.index[df2['distance']==x1111].tolist()

    x2=ind1[0]
    x22=ind11[0]
    x222=ind111[0]
    x2222=ind1111[0]

    s1=df2['scanner'][df2.index[x2]]
    s2=df2['scanner'][df2.index[x22]]
    s3=df2['scanner'][df2.index[x222]]
    s4=df2['scanner'][df2.index[x2222]]


    if f==4 :
       if s1 == 'A' :
          ox= 60
          oy=45
       elif s1 == 'E' and s2=='A' :
          ox=179
          oy=45
       elif s1 == 'E' and s2=='B' :
          ox=298
          oy=45
       elif s1== 'B' and s2== 'E':
          ox=388
          oy=45
       elif s1== 'B' and s2== 'D':
          ox=507
          oy=45
       elif s1== 'D' and s2== 'B':
          ox=597
          oy=45
       elif s1== 'D' and s2== 'C':
          ox=716
          oy=45
       elif s1== 'C' and s2== 'D' and x11 <= 8.499:
          ox=806
          oy=45       
       elif s1== 'C' and s2== 'D' and x11 > 8.499 and x11 <= 13:
          ox=925
          oy=45
       elif s1== 'C' and s2== 'D' and x11 > 13 and x11 < 17:
          ox=1015
          oy=45
       else :
          ox=1150
          oy=45
    elif f < 4 :
        if f < 2 and s1 == 'C':#sec352################
         if x1 < 6 : #1
            ox=926
            oy=122
         elif x1 >6 and x1< 15  and s2 =='D':#4
            ox=1046
            oy=122
        elif  f == 0 and x1 >15 :#3
         ox=1046
         oy=229
        elif  f == 0 and x1 >6 and x1 < 15 :#2 
         ox=926
         oy=229  
        elif f < 2 and (s1=='D' or s1 == 'C') and (s2=='D' or s2 == 'C'):#sec353#################   #3
         ox=806
         oy=229
        elif f < 3 :
         if s1=='D' and s2==' c' and s3=='B' and x1 < 15:   #1
            ox=717
            oy=122    
         elif (s1=='D' or s1=='C' or s1=='B') and (s2=='D' or s2=='C' or s2=='B') and (s3=='D' or s3=='C' or s3=='B') and x1 > 19:  #2 ####Check#####
            ox=717
            oy=229
         elif (s1=='D' or s1=='C') and (s2=='D' or s2=='C') and (s3=='B'):#  4
            ox=806
            oy=122
        elif s1=='B' and (s2=='D' or s2=='C') and (s3=='D' or s3=='C') and s4=='E':#sec354#####################  #1
         ox=507
         oy=122
        elif f<3 and s1=='B' and s2=='D' and x1 > 14 and x11> 33:#2
         ox=507
         oy=229
        elif f<3 and s1=='B' and s2=='D' and x1<14 and x11<33: #3
         ox=597
         oy=229
        elif f<3 and (s1=='B' or s1=='D') and (s2=='B' or s2=='D') and s3=='E': #4
         ox=597
         oy=122

         
    return ox , oy
# function used in tracking 
def dialog1(self):

    ID=self.entry.get()
    
    if (ID == '123' ):
         #  function to creat a circle in its position 
        def create_circle(x, y, r, canvasName): #center coordinates, radius
          x0 = x - r
          y0 = y - r
          x1 = x + r
          y1 = y + r
          return canvasName.create_oval((x0, y0, x1, y1), width=5,fill='blue')
        q=getx_y_V(self)
        x=q[0]
        y=q[1]
        create_circle(x, y, 15, my_canvas)

    elif (ID == '456' ):
         #  function to creat a circle in its position 
        def create_circle(x, y, r, canvasName): #center coordinates, radius
          x0 = x - r
          y0 = y - r
          x1 = x + r
          y1 = y + r
          return canvasName.create_oval((x0, y0, x1, y1), width=5,fill='blue' )
        q1=getx_y_M(self)
        xq=q1[0]
        yq=q1[1]
        create_circle(xq, yq, 15, my_canvas)
    elif (ID == '789' ):
        #  function to creat a circle in its position 
        def create_circle(x, y, r, canvasName): #center coordinates, radius
          x0 = x - r
          y0 = y - r
          x1 = x + r
          y1 = y + r
          return canvasName.create_oval((x0, y0, x1, y1), width=5,fill='blue' )
        q2=getx_y_HM(self)
        xq1=q2[0]
        yq1=q2[1]
        create_circle(xq1, yq1, 15, my_canvas)     
    elif (ID == '' ):
        def create_circle(x, y, r, canvasName): #center coordinates, radius
          x0 = x - r
          y0 = y - r
          x1 = x + r
          y1 = y + r
          return canvasName.create_oval((x0, y0, x1, y1), width=5,fill='red' )     
        q=getx_y_V(self)
        xq2=q[0]
        yq2=q[1]
        create_circle(xq2, yq2, 15, my_canvas)
        q1=getx_y_M(self)
        xq=q1[0]
        yq=q1[1]
        create_circle(xq, yq, 15, my_canvas)  
        q2=getx_y_HM(self)
        xq1=q2[0]
        yq1=q2[1]
        create_circle(xq1, yq1, 15, my_canvas)                     
    else:
        box.showinfo('info','Invalid ID,Please re-enter a valid ID')

def refresh():
  my_canvas.delete('all')
#   my_canvas.pack(anchor='sw', fill='both',expand=1)
  my_canvas.create_image(0,0 , image=image ,anchor='nw')
  

def show():
    top=Toplevel()
    global g 
    g=clicked.get()
    top.title(g)
    if g == "ECG1":
         lble = Label(top, text="ID", font=('Helvatical bold',10))
         lble.grid(row=0, column=0) 
         ent1=Entry(top, borderwidth=5)  
         ent1.grid(row=0, column=1) 
         ent1.insert(0,"123456789") 
         ent1.config(state= "disabled")
         lble1 = Label(top, text="MANUFACTURER", font=('Helvatical bold',10))
         lble1.grid(row=1, column=0)  
         ent2=Entry(top, borderwidth=5)  
         ent2.grid(row=1, column=1) 
         ent2.insert(0,"Philips") 
         ent2.config(state= "disabled")
         lble2 = Label(top, text="MODEL", font=('Helvatical bold',10))
         lble2.grid(row=2, column=0)  
         ent3=Entry(top, borderwidth=5)  
         ent3.grid(row=2, column=1) 
         ent3.insert(0,"NESTRO") 
         ent3.config(state= "disabled")
         lble3 = Label(top, text="SERIAL NO", font=('Helvatical bold',10))
         lble3.grid(row=3, column=0)  
         ent4=Entry(top, borderwidth=5)  
         ent4.grid(row=3, column=1) 
         ent4.insert(0,"1601") 
         ent4.config(state= "disabled")
         lble4 = Label(top, text="START CONTRACT", font=('Helvatical bold',10))
         lble4.grid(row=4, column=0)  
         ent5=Entry(top, borderwidth=5)  
         ent5.grid(row=4, column=1) 
         ent5.insert(0,"01/06/2012") 
         ent5.config(state= "disabled")
         lble5 = Label(top, text="END CONTRACT", font=('Helvatical bold',10))
         lble5.grid(row=5, column=0)  
         ent6=Entry(top, borderwidth=5)  
         ent6.grid(row=5, column=1) 
         ent6.insert(0,"01/06/2022") 
         ent6.config(state= "disabled")
         lble6 = Label(top, text="PRICE", font=('Helvatical bold',10))
         lble6.grid(row=6, column=0)  
         ent7=Entry(top, borderwidth=5)  
         ent7.grid(row=6, column=1) 
         ent7.insert(0,"50000$") 
         ent7.config(state= "disabled")
    elif g == "ECG2":
        pass
    elif g == "ECG3":
        pass 
    elif g == "VENT1":
        pass 
    else:
        pass
###############################################################################################
def edit():
    top1=Toplevel()
    g1=clicked.get()
    top1.title(f"MAINTENANCE OF {g1}") 
 ########################################################################
 #Functions 
    def on_click(event):
         event.widget.delete(0, tk.END)

    def save():
        pass

    def hist():
        pass
    
 #######################################################################
    lble = Label(top1, text="TECH NAME", font=('Helvatical bold',10))
    lble.grid(row=0, column=0)  
    ent=Entry(top1, borderwidth=5, width=30)  
    ent.grid(row=0, column=1) 
    ent.insert(0,"Enter your name:") 
    ent.bind("<Button-1>", on_click)
    lble1 = Label(top1, text="JOB BEGIN", font=('Helvatical bold',10))
    lble1.grid(row=1, column=0)  
    ent1=Entry(top1, borderwidth=5, width=30)  
    ent1.grid(row=1, column=1) 
    ent1.insert(0,"Enter date ,Time of beginning:")
    ent1.bind("<Button-1>", on_click) 
    lble2 = Label(top1, text="JOB END", font=('Helvatical bold',10))
    lble2.grid(row=2, column=0)  
    ent2=Entry(top1, borderwidth=5, width=30)  
    ent2.grid(row=2, column=1) 
    ent2.insert(0,"Enter date ,Time of ending:") 
    ent2.bind("<Button-1>", on_click)   
    lble3 = Label(top1, text="TECH REPORT", font=('Helvatical bold',10))
    lble3.grid(row=3, column=0)  
    ent3=Entry(top1, borderwidth=5, width=30)  
    ent3.grid(row=3, column=1) 
    ent3.insert(0,"Enter your notes:") 
    ent3.bind("<Button-1>", on_click)
    btn1=Button(top1, text="SAVE", command=save)
    btn1.grid(row=4, column=0, padx=30, pady=10)
    btn2=Button(top1, text="HISTORY", command=hist)
    btn2.grid(row=4, column=1, padx=30, pady=10)

def part():
    top2=Toplevel()
    top2.title("EQUIPMENT PARTS") 
    #########################################################
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

################################################################################################    
#GiUI
wrap1 = LabelFrame(frame, text="Health Facility")
wrap1.pack(fill="both", padx=10, pady=1)
lbl1 = Label(wrap1, text="72345", font=('Helvatical bold',15))
lbl1.pack(side=LEFT, padx=20, pady=10)
lbl2 = Label(wrap1, text="Benha University Hospital", font=('Helvatical bold',15))
lbl2.pack(side=LEFT, padx=20, pady=10)
lbl3 = Label(wrap1, text="Ministry of Health\nDirectorate of Biomedical Engineering\nEqupment card", font=('Helvatical bold',15))
lbl3.pack(side=LEFT, padx=20, pady=10)
lbl4 = Label(wrap1, text="Inventory Number\nM15700", font=('Helvatical bold',15))
lbl4.pack(side=LEFT, padx=20, pady=1)
################################################################################################
wrap2 = LabelFrame(frame, text="Equipment Details")
wrap2.pack(fill="both", padx=10, pady=1)
clicked= StringVar()
clicked.set("Check your Device ")
drop = OptionMenu(wrap2,clicked, "ECG1","ECG2","ECG3","VENT1","VENT2")
drop.config(width=20, height=2)
drop.pack(side=LEFT, padx=10, pady=10)
btn1=Button(wrap2, text="Show details", command=show, width=20 , height=2, font=('Helvatical bold',12))
btn1.pack(side=LEFT, padx=20, pady=10)
btn2=Button(wrap2, text="MAINTENANCE", command=edit, width=20 , height=2, font=('Helvatical bold',12))
btn2.pack(side=LEFT, padx=20, pady=10)
btn3=Button(wrap2, text="PARTS", command=part, width=20 , height=2, font=('Helvatical bold',12))
btn3.pack(side=LEFT, padx=20, pady=10)
#####################################################################################################
wrap3 = LabelFrame(frame)
wrap3.pack()
Label1 = Label(wrap3,text = 'ID:')
entry = Entry(wrap3,bd =5)
btn = Button(wrap3, text = 'Track',command = dialog1)
btn2 = Button(wrap3, text = 'REFRESH',command = refresh)
my_canvas=Canvas(root,bg='white')

# position of widgets
frame.pack(padx=100,pady = 19)
Label1.pack(side = LEFT ,padx=15,pady= 5)
entry.pack(side = LEFT ,padx=15, pady=5)
btn.pack(side = LEFT , padx =5)
btn2.pack(side = LEFT , padx =5)
my_canvas.pack(anchor='sw', fill='both',expand=1)

# image of the plane which used in tracking
image= Image.open("I:/yyy/sc1.jpg")
image= ImageTk.PhotoImage(image)
my_canvas.create_image(0,0 , image=image ,anchor='nw')

# def create_circle(x, y, r, canvasName): #center coordinates, radius
#    x0 = x - r
#    y0 = y - r
#    x1 = x + r
#    y1 = y + r
#    return canvasName.create_oval((x0, y0, x1, y1), width=1,fill='green')
# create_circle(10, 85, 10, my_canvas)
# create_circle(453, 85, 10, my_canvas)
# create_circle(875, 85, 10, my_canvas)
# create_circle(250, 10, 10, my_canvas)
# create_circle(660, 10, 10, my_canvas)

# run GUI until user close it
mainloop()


