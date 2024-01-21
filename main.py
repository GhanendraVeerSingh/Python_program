#CREATED BY---- GHANENDRA VEER SINGH
#BTECH II YEAR(COMPUTER SCIENCE AND ENGINEERING)
# DATE--- 12 AUGUST 2019
#!!!! dsyghannu60@gamil.com !!!!
#================================== functionality 0f program ==================================================================

from tkinter import *

def btnclick(numbers):
    global operator
    operator=operator+str(numbers)
    text_input.set(operator)
def btnequal():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
def btnclear():
    global operator
    operator=""
    text_input.set(operator)
    operator=""

#================================== Creation of window =========================================================================    
w=Tk()
w.geometry()
w.title("CALCULATOR")
w.resizable(FALSE,FALSE)   
#================================== Dsigining of calculator =====================================================================

mainframe=Frame(w,bg='cyan',bd=10)
mainframe.grid(row=0,column=0)

operator=""
text_input=StringVar() 
contententry=Entry(mainframe,bd=15,bg='powder blue',insertwidth=5,width=24,font=('arial',18,'bold'),textvariable=text_input)
contententry.grid(row=0,column=0)
contententry.focus()
contentframe=Frame(mainframe,bg='misty rose',bd=25)
contentframe.grid(row=1,column=0)

button7=Button(contentframe,text='7',bg='cyan',bd=9,font=45,fg='black',width=4,height=2,command=lambda :btnclick(7))
button7.grid(row=0,column=0)
button8=Button(contentframe,text='8',bg='cyan',bd=9,font=45,fg='black',height=2,width=4,command=lambda :btnclick(8))
button8.grid(row=0,column=1,padx=3,pady=3)
button9=Button(contentframe,text='9',bg='cyan',bd=9,font=45,fg='black',width=4,height=2,command=lambda :btnclick(9))
button9.grid(row=0,column=2,padx=3,pady=3)
button4=Button(contentframe,text='4',bg='cyan',bd=9,font=45,fg='black',height=2,width=4,command=lambda :btnclick(4))
button4.grid(row=1,column=0)
button5=Button(contentframe,text='5',bg='cyan',bd=9,font=45,fg='black',height=2,width=4,command=lambda :btnclick(5))
button5.grid(row=1,column=1,padx=3,pady=3)
button6=Button(contentframe,text='6',bg='cyan',bd=9,font=45,fg='black',height=2,width=4,command=lambda :btnclick(6))
button6.grid(row=1,column=2,padx=3,pady=3)
button1=Button(contentframe,text='1',bg='cyan',bd=9,font=45,fg='black',height=2,width=4,command=lambda :btnclick(1))
button1.grid(row=2,column=0)
button2=Button(contentframe,text='2',bg='cyan',bd=9,font=45,fg='black',height=2,width=4,command=lambda :btnclick(2))
button2.grid(row=2,column=1,padx=3,pady=3)
button3=Button(contentframe,text='3',bg='cyan',bd=9,font=45,fg='black',height=2,width=4,command=lambda :btnclick(3))
button3.grid(row=2,column=2,padx=3,pady=3)
button0=Button(contentframe,text='0',bg='cyan',bd=9,font=45,fg='black',height=2,width=4,command=lambda :btnclick(0))
button0.grid(row=3,column=0)
buttondec=Button(contentframe,text='.',bg='cyan',bd=9,font=45,fg='black',height=2,width=4,command=lambda :btnclick('.'))
buttondec.grid(row=3,column=1,padx=3,pady=3)
buttonplus=Button(contentframe,text='+',bg='cyan',bd=9,font=45,fg='black',height=2,width=4,command=lambda :btnclick('+'))
buttonplus.grid(row=3,column=2,padx=3,pady=3)
buttonmul=Button(contentframe,text='*',bg='cyan',bd=9,font=45,fg='black',height=2,width=4,command=lambda :btnclick('*'))
buttonmul.grid(row=0,column=3,padx=3,pady=3)
buttondiv=Button(contentframe,text='/',bg='cyan',bd=9,font=45,fg='black',height=2,width=4,command=lambda :btnclick('/'))
buttondiv.grid(row=1,column=3,padx=3,pady=3)
buttonper=Button(contentframe,text='%',bg='cyan',bd=9,font=45,fg='black',height=2,width=4,command=lambda :btnclick('%'))
buttonper.grid(row=2,column=3,padx=3,pady=3)
buttonclear=Button(contentframe,text='C',bg='cyan',bd=9,font=45,fg='black',height=2,width=4,command=btnclear)
buttonclear.grid(row=3,column=3,padx=3,pady=3)
buttonsub=Button(contentframe,text='-',bg='cyan',bd=9,font=45,fg='black',height=2,width=4,command=lambda :btnclick('-'))
buttonsub.grid(row=4,column=3,padx=3,pady=3)
buttonequal=Button(contentframe,text='=',bg='cyan',bd=9,font=45,fg='black',height=2,width=17,command=btnequal)
buttonequal.grid(row=4,column=0,padx=3,pady=3,columnspan=3)
w.mainloop()
#===========================================END OF PROGRAM ============================================================================
