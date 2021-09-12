from tkinter import *

window=Tk()
window.geometry('312x500')
window.resizable(0,0)
window.title("Calculator")



def btnClick(values):
    global btnValue
    btnValue= btnValue +str(values)
    inputText.set(btnValue)

def clrBtn():
    global btnValue
    btnValue=""
    inputText.set(btnValue)

def eqlbtn():
    global btnValue
    result = str(eval(btnValue)) # 'eval':This function is used to evaluates the string expression directly
    inputText.set(result)
    btnValue = ""

btnValue=""

inputText=StringVar()

inputFrame=Frame(window,width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
inputFrame.pack(side=TOP)

inputField = Entry(inputFrame, font=('arial', 18, 'bold'), textvariable=inputText, width=50, bg="#eee", bd=0, justify=RIGHT)
inputField.grid(row=0,column=0)
inputField.pack(ipady=10)

btnsFrame=Frame(window,width=312,height=272.5)
btnsFrame.pack()

button9 = Button(btnsFrame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btnClick(9)).grid(row = 1, column = 0, padx = 1, pady = 1)
button8=Button(btnsFrame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btnClick(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
button7=Button(btnsFrame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btnClick(7)).grid(row = 1, column = 2, padx = 1, pady = 1)
button6=Button(btnsFrame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btnClick(6)).grid(row = 2, column = 0, padx = 1, pady = 1)
button5=Button(btnsFrame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btnClick(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
button4=Button(btnsFrame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btnClick(4)).grid(row = 2, column = 2, padx = 1, pady = 1)
button3=Button(btnsFrame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btnClick(3)).grid(row = 3, column = 0, padx = 1, pady = 1)
button2=Button(btnsFrame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btnClick(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
button1=Button(btnsFrame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btnClick(1)).grid(row = 3, column = 2, padx = 1, pady = 1)
button0=Button(btnsFrame, text = "0", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btnClick(0)).grid(row = 4, column = 1, padx = 1, pady = 1)
buttonplus=Button(btnsFrame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btnClick('+')).grid(row = 1, column = 3, padx = 1, pady = 1)
buttonminus=Button(btnsFrame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btnClick('-')).grid(row = 2, column = 3, padx = 1, pady = 1)
buttondivide=Button(btnsFrame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btnClick('/')).grid(row = 3, column = 3, padx = 1, pady = 1)
buttonmutiply=Button(btnsFrame, text = "x", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btnClick('*')).grid(row = 4, column = 3, padx = 1, pady = 1)
buttonclear=Button(btnsFrame, text = "C", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: clrBtn()).grid(row = 4, column = 0, padx = 1, pady = 1)
buttonmequals=Button(btnsFrame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: eqlbtn()).grid(row = 4, column = 2, padx = 1, pady = 1)


window.mainloop()