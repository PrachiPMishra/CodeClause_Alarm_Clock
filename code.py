#importing libraries
from tkinter import *
import datetime as d
import time as t
import winsound as w

def alarm(setAlarmTimer):  
    while True:  
        t.sleep(1)
        actualTime = d.datetime.now()  
        currentTime = actualTime.strftime("%H:%M:%S")  
        print("Current Time: ",currentTime)  
        if currentTime==setAlarmTimer:  
            print("***ALARM RINGING***")
            for _ in range(70):
                w.Beep(1300,300)
            break 
    

def getAlarmTime():  
    if int(h.get())>=0 and int(h.get())<10:
        ht="0"+h.get()
    else:
        ht=h.get()
    if int(m.get())>=0 and int(m.get())<10:
        mt="0"+m.get()
    else:
        mt=m.get()
    if int(s.get())>=0 and int(s.get())<10:
        st="0"+s.get()
    else:
        st=s.get()
    alarmSetTime = ht+":"+mt+":"+st
    print(alarmSetTime)
    alarm(alarmSetTime)  

clock=Tk()
clock.title("Alarm Clock")  
clock.geometry("550x300")  
clock.config(bg="#CDCDFD")
hms=Label(clock, text="HOUR\t       MIN\t            SEC ",font=20,fg='black',bg="#CDCDFD").place(x=220,y=50)
set_time=Label(clock, text="SET TIME: ",font=20,bg='#9A79B6',fg='black').place(x=60,y=100)
h=StringVar()  
m=StringVar()  
s=StringVar() 
hour=Spinbox(clock,
             from_=00,
             to=23,
             font=15,
             width=7,
             justify='center'
             ,wrap=True,
             textvariable=h,
             ).place(
                    x=200,
                    y=100)
min=Spinbox(clock,
             from_=00,
             to=59,
             font=15,
             width=7,
             justify='center'
             ,wrap=True,
             textvariable=m,
             ).place(
                    x=300,
                    y=100)
sec=Spinbox(clock,
             from_=00,
             to=59,
             font=15,
             width=7,
             justify='center'
             ,wrap=True,
             textvariable=s,
             ).place(
                    x=400,
                    y=100)
submit= Button(clock,text="SET ALARM",fg="white",bg="#4E1F78",font=20,command = getAlarmTime).place(x=275,y=150)
warning=Label(clock, text="(Set the Time in 24-hour format)",font=20,fg='black',bg="#CDCDFD").place(x=200,y=230)
clock.mainloop()
