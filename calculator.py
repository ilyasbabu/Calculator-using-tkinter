from tkinter import *

window=Tk()
window.geometry('500x500')

textDisplay=Text(window,height=4,width=40)

button9=Button(window,text=9,width=8,height=2)
button8=Button(window,text=8,width=8,height=2)
button7=Button(window,text=7,width=8,height=2)
plusbutton=Button(window,text='+',width=8,height=2)
button6=Button(window,text=6,width=8,height=2)
button5=Button(window,text=5,width=8,height=2)
button4=Button(window,text=4,width=8,height=2)
minusbutton=Button(window,text='+',width=8,height=2)
button3=Button(window,text=3,width=8,height=2)
button2=Button(window,text=2,width=8,height=2)
button1=Button(window,text=1,width=8,height=2)
mulbutton=Button(window,text='+',width=8,height=2)
button0=Button(window,text=0,width=16,height=2)
equalbutton=Button(window,text="=",width=16,height=2)


textDisplay.grid(row=0,column=0,columnspan=3)
button9.grid(row=1,column=0)
button8.grid(row=1,column=1)
button7.grid(row=1,column=2)
button6.grid(row=2,column=0)
button5.grid(row=2,column=1)
button4.grid(row=2,column=2)
button3.grid(row=3,column=0)
button2.grid(row=3,column=1)
button1.grid(row=3,column=2)
button0.grid(row=4,column=0,columnspan=2)
equalbutton.grid(row=4,column=2,columnspan=2)
plusbutton.grid(row=1,column=3)
minusbutton.grid(row=1,column=3)
mulbutton.grid(row=1,column=3)


window.mainloop()