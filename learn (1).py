# librarries used in app
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

# the main window
root=Tk()
root.title('find your device')
root.geometry("1285x650")
frame = Frame(root)
# from operator import index
# from tkinter import N
# from turtle import clear
# import pandas as pd
# import re
# import numpy as np
# import openpyxl as xl
def distance():
######read the read  data  from received file############
    df=pd.read_csv('I:\yyy\data.csv')
    df.columns=['data']
    df.to_csv('I:\yyy\medata.csv')
    df=pd.read_csv('I:\yyy\medata.csv')
    df=df.tail(70)
    df.to_csv('I:\yyy\meedata.csv')
    print("newdata\n",df)
########split the  data in three columns##############
    df[['scanner','tag','rssi']]=df['data'].str.split("_",expand=True)
    print(df)
    df.to_csv('I:\yyy\endddataa.csv',index=False)
    required_col=['scanner','tag','rssi']
    required_Data=df[required_col]
    required_Data.to_csv('I:\yyy\splitdataa.csv',index=False)
    x_data=pd.read_csv('I:\yyy\splitdataa.csv')
    print(x_data)
##########check if the data in the correct  form#########
    com_data=x_data['scanner']+"_"+x_data['tag']
    print(com_data)
####for tag (V)###########
    x="A_V"
    y1="B_V"
    z="C_V"
    R="D_V"
    F="E_V"
#####for tag (M)#########
    x1=" A_M"
    y2=" B_M"
    z1=" C_M"
    R1=" D_M"
    F1=" E_M"
#####for tag (HMSoft)#########
    x3="A_HMSoft"
    y3="B_HMSoft"
    z3="C_HMSoft"
    R3="D_HMSoft"
    F3="E_HMSoft"
# df['combine']=x_data.str.cat(x_data['scanner','tag'])
    print(df)
    print("check from data for tag V")  
    for i in com_data:
       if i==x:
          print ("it's correct data\n",i)

       elif i== y1:
          print ("it's correct data\n",i)  
       elif i==z:
          print ("it's correct data\n",i)
    
       elif i==R:
          print ("it's correct data\n",i)
       elif i==F:
          print ("it's correct data\n",i) 
       else:

          print("it's  incorrect data\n ",i)
    print("check from data for tag M")      
    for i in com_data:
       if i==x1:
           print ("it's correct data\n",i)

       elif i==y2:
           print ("it's correct data\n",i)  
       elif i==z1:
           print ("it's correct data\n",i)
       elif i==z1:
            print ("it's correct data\n",i) 
       elif i==R1:
            print ("it's correct data\n",i)
       elif i==F1:
           print ("it's correct data\n",i) 
       else:

          print("it's  incorrect data\n ",i)     

    print("check from data for tag HMSOft")
    for i in com_data:
        if i==x3:
           print ("it's correct data\n",i)

        elif i==y3:
            print ("it's correct data\n",i)  
        elif i==z3:
            print ("it's correct data\n",i)
        elif i==z3:
            print ("it's correct data\n",i) 
        elif i==R3:
            print ("it's correct data\n",i)
        elif i==F3:
            print ("it's correct data\n",i) 
        else:

           print("it's  incorrect data\n ",i) 

###########seperation the three tags in different files#############

###########split the first tag (v)in file ###########
    reader= pd.read_csv('I:\yyy\splitdataa.csv')
########determine the index of tag (V)##############
    ind=reader.index[reader['tag'] =='V'].tolist()
    print('V_index=',ind)

    R_list=[]
#########determine the value of RSSI & scanner for tag (V)
######RSSI#########
    for i in ind:
        RSSI=reader.loc[i].at["rssi"]
        R_list.append(RSSI)

    print('V_rssi=',R_list)

    S_list=[]
######SCAnner###############
    for i in ind:
       SC=reader.loc[i].at["scanner"]
       S_list.append(SC)

    print('V_scanner=',S_list)
###########split the second tag (M) in file ###########
    indd=reader.index[reader['tag'] =='M'].tolist()
    print('M_index=',indd)

    RR_list=[]
######RSSI#########
    for i in indd:
        RSSI_1=reader.loc[i].at["rssi"]
        RR_list.append(RSSI_1)

    print('M_rssi=',RR_list)
######SCAnner###############
    SS_list=[]
    for i in indd:
       SCC=reader.loc[i].at["scanner"]
       SS_list.append(SCC)

    print('M_scanner=',SS_list)
    scannerv=S_list
    rssiv=R_list

########determine the index of tag (HMSoft)##############

    inddd=reader.index[reader['tag'] =='HMSoft'].tolist()
    print('HM_index=',inddd)

    RRR_list=[]
#########determine the value of RSSI & scanner for tag (V)
######RSSI#########
    for i in inddd:
        RSSI=reader.loc[i].at["rssi"]
        RRR_list.append(RSSI)

        print('HM_rssi=',RRR_list)
    SSS_list=[]
######SCAnner###############
    for i in inddd:
       SCCC=reader.loc[i].at["scanner"]
       SSS_list.append(SCCC)

    print('HM_scanner=',SSS_list)
#######convert the list to dataframe for tag(V) and save in file##############
    datav={"scanner":scannerv,"rssi":rssiv}
    dataframe=pd.DataFrame(datav)
    dataframe.to_csv('I:\yyy\datatagv.csv',index=False)
    print("tagv",dataframe)
#######convert the list to dataframe for tag(M) and save in file##############
    scannerm=SS_list
    rssim=RR_list
    datam={"scanner":scannerm,"rssi":rssim}
    dataframe=pd.DataFrame(datam)
    dataframe.to_csv('I:\yyy\datatagm.csv',index=False)
    print("tagm",dataframe)
#######convert the list to dataframe for tag(HMSoft) and save in file##############
    scannerHM=SSS_list
    rssiHM=RRR_list
    dataHMSoft={"scanner":scannerHM,"rssi":rssiHM}
    dataframe=pd.DataFrame(dataHMSoft)
    dataframe.to_csv('I:\yyy\datatagHMSoft.csv',index=False)
    print("tagHMSoft\n",dataframe)


############## make a function to determine replicate scanner for the two tags#############
    def dep_value():
    ############3for scanner A tag v#############
         c=x['scanner'] 
         list_1=x.index[x["scanner"]=="A"].tolist()
         print('scanner_indexA=',list_1)

         z=0
         for i in range(len(c)):
             if c[i]=="A":
                z=list_1[-1]
        #    print("final_index",z)

                a=x.loc[z].at["rssi"]
        #    print("final_rssi",a)  
        
    
##############for scanner B tag v################

         list_2=x.index[x["scanner"]=="B"].tolist()
         print('scanner_indexB=',list_2)
         f=0
         for i in range(len(c)):
             if c[i]=="B":
                f=list_2[-1]
    #  print("final_index",f)

                a2=x.loc[f].at["rssi"]
    #  print("final_rssi",a2)


#################for scanner c tag v#################
         list_3=x.index[x["scanner"]=="C"].tolist()
         print('scanner_indexC=',list_3)
    
         f2=0
         for i in range(len(c)):

            if c[i]=="C":
               f2=list_3[-1]
    #   print("final_index",f2)
               a3=x.loc[f2].at["rssi"]
    #   print("final_rssi",a3)
  
###############for scanner D tag v################
         list_4=x.index[x["scanner"]=="D"].tolist()
         print('scanner_indexD=',list_4)
         f3=0
         for i in range(len(c)):

             if c[i]=="D":
                f3=list_4[-1]
        #   print("final_index",f3)
                a4=x.loc[f3].at["rssi"]
        #   print("final_rssi",a4)
    
#############for scanner E tag v#######################
    
         list_5=x.index[x["scanner"]=="E"].tolist()
         print('scanner_indexE=',list_5)
         f4=0
         for i in range(len(c)):
             if c[i]=="E":
                f4=list_5[-1]
        #    print("final_index",f4)
                a5=x.loc[f4].at["rssi"]
########print the list of last index for each scanner#######
         print ("last index of scanner",z,f,f2,f3,f4)    
############sort the list by small index ################  
         sort_index=z,f,f2,f3,f4
         print("sorted list",sort_index)
         fsrssi=sorted(sort_index)
         print("sorted list with zero value ",fsrssi)
#########remove the zero value from list###############
         for i in fsrssi:
            if i==0:
               fsrssi.remove(i)

         listt2=fsrssi
         for i in fsrssi:
            if i==0:
               fsrssi.remove(i)
               print(fsrssi)  
########print the sorted list without zero value########          
         print("sorted list without zero value ",listt2)

         list_scanner=[]
    
         global scanner1
         global rssi1
         list_rssi=[]
#######determine the value of RSSI&scanner for last index###########    
         for i in listt2:
             v=x.loc[i].at["scanner"]
             list_scanner.append(v)
             print("scanner",list_scanner)
         for i in listt2:
             g=x.loc[i].at["rssi"]
             list_rssi.append(g)
             rssi1=list_rssi
             print("rssi",list_rssi)
             scanner1=list_scanner
    
########call the function and convert the list of last value of RSSI for tag (V) into dataframe######   
    x=pd.read_csv('I:\yyy\datatagv.csv')
    job1=dep_value()
    dataa={"scanner":scanner1,"rssi":rssi1}
    dataaframefinal=pd.DataFrame(dataa)
    dataaframefinal.to_csv('I:\yyy\Finaltagv.csv',index=False)
    print("VVVVVVVVVVV\n",dataaframefinal)
    print("#######done#############")
#######calculate the distance for tag(V) first tag########
    df=pd.read_csv('I:\yyy\Finaltagv.csv')
    measured_rssi=-59
    rssi_now1=df['rssi']
    w1=(10)*(2.486)

    for i in rssi_now1:
       global y
       y=(-59-(rssi_now1))
       d=(y/w1)
       dis1=10**(d)
       print("dis of tag v\n",dis1)
       first={"scanner":scanner1,"distance":dis1}
       distance=pd.DataFrame(first)
       distance.to_csv('I:\yyy\distance_v.csv',index=False)
       print(distance)
########convert the list of last value of RSSI for tag (M) into dataframe#############
    x=pd.read_csv('I:\yyy\datatagm.csv')
    job2=dep_value()   
    print("scanner1",scanner1) 
    dataa={"scanner":scanner1,"rssi":rssi1}
    dataaframefinal=pd.DataFrame(dataa)
    dataaframefinal.to_csv('I:\yyy\Finaltagm.csv',index=False)
    print("MMMMMMMMMMMM",dataaframefinal)

#########calculate distance for tag (M) second tag ######################
    print("#########done#############")
    df=pd.read_csv('I:\yyy\Finaltagm.csv')
    measured_rssi=-59
    rssi_now2=df['rssi']
    w2=(10)*(2.486)
    for i in rssi_now2:
       global f
       f=(-59-(rssi_now2))
       dd=(f/w2)
       dis2=10**(dd)
       print("dis of tag M\n",dis2)

    second={"scanner":scanner1,"distance":dis2}
    distance=pd.DataFrame(second)
    distance.to_csv('I:\yyy\distance_m.csv',index=False)
    print(distance)
########call the function and convert the list of last value of RSSI for tag (HMSoft) into dataframe####   
    x=pd.read_csv('I:\yyy\datatagHMSoft.csv')
    job3=dep_value()
    dataa={"scanner":scanner1,"rssi":rssi1}
    dataaframefinal=pd.DataFrame(dataa)
    dataaframefinal.to_csv('I:\yyy\FinaltagHMSoft.csv',index=False)
    print("HMSoft\n",dataaframefinal)
    print("#######done#############")
#######calculate the distance for tag(HMSoft) first tag########
    df=pd.read_csv('I:\yyy\FinaltagHMSoft.csv')
    measured_rssi=-59
    rssi_now3=df['rssi']
    w3=(10)**(2.486)

    for i in rssi_now3:
        global a
        a=(-59-(rssi_now3))
        ddd=(a/w3)
        dis3=10**(ddd)
        print("dis of tag HMSoft\n",dis3)
    third={"scanner":scanner1,"distance":dis3}
    distance=pd.DataFrame(third)
    distance.to_csv('I:\yyy\distance_hmsoft.csv',index=False)


final=distance()




def getx_y_V():
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
          oy=285
       elif s1 == 'E' and s2=='B' :
          ox=298
          oy=285
       elif s1== 'B' and s2== 'E':
          ox=388
          oy=285
       elif s1== 'B' and s2== 'D':
          ox=507
          oy=285
       elif s1== 'D' and s2== 'B':
          ox=597
          oy=285
       elif s1== 'D' and s2== 'C':
          ox=716
          oy=285
       elif s1== 'C' and s2== 'D' and x11 <= 8.499:
          ox=806
          oy=285       
       elif s1== 'C' and s2== 'D' and x11 > 8.499 and x11 <= 13:
          ox=925
          oy=285
       elif s1== 'C' and s2== 'D' and x11 > 13 and x11 < 17:
          ox=1015
          oy=285
       else :
          ox=1150
          oy=285
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
         if s1=='D' and s2=='C' and s3=='B' and x1 < 15:   #1
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
def getx_y_M():
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
          oy=285
       elif s1 == 'E' and s2=='A' :
          ox=179
          oy=285
       elif s1 == 'E' and s2=='B' :
          ox=298
          oy=285
       elif s1== 'B' and s2== 'E':
          ox=388
          oy=285
       elif s1== 'B' and s2== 'D':
          ox=507
          oy=285
       elif s1== 'D' and s2== 'B':
          ox=597
          oy=285
       elif s1== 'D' and s2== 'C':
          ox=716
          oy=285
       elif s1== 'C' and s2== 'D' and x11 <= 8.499:
          ox=806
          oy=285       
       elif s1== 'C' and s2== 'D' and x11 > 8.499 and x11 <= 13:
          ox=925
          oy=285
       elif s1== 'C' and s2== 'D' and x11 > 13 and x11 < 17:
          ox=1015
          oy=285
       else :
          ox=1150
          oy=285
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
def getx_y_HM():
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
          oy=285
       elif s1 == 'E' and s2=='A' :
          ox=179
          oy=285
       elif s1 == 'E' and s2=='B' :
          ox=298
          oy=285
       elif s1== 'B' and s2== 'E':
          ox=388
          oy=285
       elif s1== 'B' and s2== 'D':
          ox=507
          oy=285
       elif s1== 'D' and s2== 'B':
          ox=597
          oy=285
       elif s1== 'D' and s2== 'C':
          ox=716
          oy=285
       elif s1== 'C' and s2== 'D' and x11 <= 8.499:
          ox=806
          oy=285       
       elif s1== 'C' and s2== 'D' and x11 > 8.499 and x11 <= 13:
          ox=925
          oy=285
       elif s1== 'C' and s2== 'D' and x11 > 13 and x11 < 17:
          ox=1015
          oy=285
       else :
          ox=1150
          oy=285
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
########################################################################################
def refresh():
  my_canvas.delete('all')
#   my_canvas.pack(anchor='sw', fill='both',expand=1)
  my_canvas.create_image(0,0 , image=image ,anchor='nw')
# function used in tracking 
def dialog1():
    threading.Timer(10.0, dialog1).start()
    distance()
    ID=entry.get()
    
    if (ID == '123' ):
         #  function to creat a circle in its position 
        def create_circle(x, y, r, canvasName): #center coordinates, radius
          x0 = x - r
          y0 = y - r
          x1 = x + r
          y1 = y + r
          return canvasName.create_oval((x0, y0, x1, y1), width=5,fill='blue')
        q=getx_y_V()
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
        q1=getx_y_M()
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
        q2=getx_y_HM()
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
        q=getx_y_V()
        xq2=q[0]
        yq2=q[1]
        create_circle(xq2, yq2, 15, my_canvas)
        q1=getx_y_M()
        xq=q1[0]
        yq=q1[1]
        create_circle(xq, yq, 15, my_canvas)  
        q2=getx_y_HM()
        xq1=q2[0]
        yq1=q2[1]
        create_circle(xq1, yq1, 15, my_canvas)                     
    else:
        box.showinfo('info','Invalid ID,Please re-enter a valid ID')
    # # refresh()
    # threading.Timer(10.0, refresh).start()


  

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
# wrap1 = LabelFrame(frame, text="Health Facility")
# wrap1.pack(fill="both", padx=10, pady=1)
# lbl1 = Label(wrap1, text="72345", font=('Helvatical bold',15))
# lbl1.pack(side=LEFT, padx=20, pady=10)
# lbl2 = Label(wrap1, text="Benha University Hospital", font=('Helvatical bold',15))
# lbl2.pack(side=LEFT, padx=20, pady=10)
# lbl3 = Label(wrap1, text="Ministry of Health\nDirectorate of Biomedical Engineering\nEqupment card", font=('Helvatical bold',15))
# lbl3.pack(side=LEFT, padx=20, pady=10)
# lbl4 = Label(wrap1, text="Inventory Number\nM15700", font=('Helvatical bold',15))
# lbl4.pack(side=LEFT, padx=20, pady=1)
################################################################################################
# wrap2 = LabelFrame(frame, text="Equipment Details")
# wrap2.pack(fill="both", padx=10, pady=1)
# clicked= StringVar()
# clicked.set("Check your Device ")
# drop = OptionMenu(wrap2,clicked, "ECG1","ECG2","ECG3","VENT1","VENT2")
# drop.config(width=20, height=2)
# drop.pack(side=LEFT, padx=10, pady=10)
# btn1=Button(wrap2, text="Show details", command=show, width=20 , height=2, font=('Helvatical bold',12))
# btn1.pack(side=LEFT, padx=20, pady=10)
# btn2=Button(wrap2, text="MAINTENANCE", command=edit, width=20 , height=2, font=('Helvatical bold',12))
# btn2.pack(side=LEFT, padx=20, pady=10)
# btn3=Button(wrap2, text="PARTS", command=part, width=20 , height=2, font=('Helvatical bold',12))
# btn3.pack(side=LEFT, padx=20, pady=10)
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
image= Image.open("I:\yyy/Untitled-111.jpg")
resized_image= image.resize((1280,700), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
my_canvas.create_image(0,0 , image=new_image ,anchor='nw')

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


