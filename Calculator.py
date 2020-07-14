import math
from tkinter import *

def scientificl():
    newWindow = Tk()

    newWindow.title('Calculator!')
    newWindow.resizable(0,0)
    #newWindow.iconbitmap('calculator2.ico')

    ur_menu = Menu(newWindow)
    newWindow.config(menu = ur_menu)
    file_menu = Menu(ur_menu, tearoff = False, background = 'black', foreground = 'white',activebackground = '#00E4FF', activeforeground='black')
    ur_menu.add_cascade(label = 'Styleo', background = '#9C25F3', activebackground = 'black',menu = file_menu)
    #my_menu.add_cascade(label = 'Mode', menu = file_menu)

                                                        
    Variant = Menu(ur_menu, tearoff = False, background = 'black', foreground = 'white',activebackground = '#00E4FF', activeforeground='black')
    ur_menu.add_cascade(label = 'Varianto',background = '#9C25F3', activebackground = 'black',menu = Variant)


    
    #Variant = Menu(my_menu, tearoff = False, background = 'black', foreground = 'white',activebackground = '#00E4FF', activeforeground='black')
    #my_menu.add_cascade(label = 'Variant',background = '#9C25F3', activebackground = 'black',menu = Variant)



    def a():
        file_menu.add_command(label = 'BLACK', command = lambda:[newWindow.destroy(), scientific()])

    def b():
        file_menu.add_command(label = 'LIGHT')
        #def quit():
        #    global calculator
        #   calculator.quit()
    a()
    b()
    #file_menu.add_command(label = 'BLACK')
        #b()
        #file_menu.add_command(label = 'LIGHT')
    Variant.add_command(label = 'Standard', command = lambda:[newWindow.destroy(), light()])
    Variant.add_command(label = 'Scientific')
        #
        #
        #
        #
        #calculator.iconbitmap('./images/calculator2.ico')
        #
    frame=Frame(newWindow)
    frame.configure(bg='white')
    frame.grid(row=0, column=0,columnspan = 6 ,padx=0, pady=0)
        #
    enter2=Entry(frame, width=23, borderwidth=0, font=('Comic San MS',25))
    enter2.configure(justify=RIGHT, width = 39 )
    enter2.configure(bg='white')
    enter2.configure(fg='black')

    enter2.grid(row=0, column=0, columnspan=8, padx=0, pady=0, ipady=8)

    enter=Entry(frame, width=18, borderwidth=0, font=('Comic San MS',45))
    enter.configure(justify=RIGHT, width = 23 )
    enter.configure(bg='white')
    enter.configure(fg='black')
    enter.grid(row=1, column=0, columnspan=8, padx=0, pady=0, ipady=15)

    def buttonClick(number):
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0, str(current) + str(number))

    def dot():
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0, str(current) + '.')

    def add():
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0,str(current) + '+')

    def subtract():
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0,str(current) + '-')

    def multiply():
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0,str(current) + '*') 

    def divide():
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0,str(current) + '/')

    def clear():
        enter.delete(0,END)
        enter2.delete(0,END)

    def equal():

        enter2.insert(0, enter.get())
        result=eval(enter.get())
        enter.delete(0,END)
        resultString = str(result)
        resultLength = len(resultString)

        if resultString[resultLength-2:] =='.0':
            result = str(resultString[:resultLength-2])

        enter.insert(0,result)

    def delete():
        current=len(enter.get())
        last = current - 1
        enter.delete(last, END)

    def percent():
        firstNumber=float(enter.get())
        enter.delete(0,END)
        enter.insert(0,firstNumber / 100)
        enter2.insert(0,f'{firstNumber}/100' )


    def plusMinus():
        current=enter.get()
        plus = current[0:1]
            
        if plus == '0' or plus == '1' or plus == '2' or plus == '3' or plus == '4' or plus == '5' or plus == '6' or plus == '7' or plus == '8' or plus == '9':  
            enter.insert(0,'-')
        else:
            enter.delete(0,1)

    def root():
        current=enter.get()
        enter.delete(0,END)
        root = math.sqrt(float(current))
        enter.insert(0,root)   
        equation = f'√ {current}'
        enter2.insert(0,equation)

    def sin():
        current = enter.get()
        enter.delete(0, END)
        sin = math.sin(float(current))
        enter.insert(0,sin)
        enter2.insert(0, current)

    def cos():
        current = enter.get()
        enter.delete(0, END)
        cos = math.cos(float(current))
        enter.insert(0,cos)
        enter2.insert(0, current)

    def tan():
        current = enter.get()
        enter.delete(0, END)
        tan = math.tan(float(current))
        enter.insert(0,tan)
        enter2.insert(0, current)

    def sinh():
        current = enter.get()
        enter.delete(0, END)
        sinh = math.sinh(float(current))
        enter.insert(0,sinh)
        enter2.insert(0, current)

    def cosh():
        current = enter.get()
        enter.delete(0, END)
        cosh = math.cosh(float(current))
        enter.insert(0,cosh)
        enter2.insert(0, current)

    def tanh():
        current = enter.get()
        enter.delete(0, END)
        tanh = math.tanh(float(current))
        enter.insert(0,tanh)
        enter2.insert(0, current)

    def pi():
        current=enter.get()
        enter.delete(0, END)
        pi = str(math.pi)
        enter.insert(0, str(current) + pi )

    def square():
        current = enter.get()
        enter.delete(0, END)
        square = math.isqrt(current)
        enter.insert(0,pi)
        enter2.insert(0, current)

    def lB():
        current = enter.get()
        enter.delete(0,END)
        enter.insert(0, str(current) + '(' )

    def rB():
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0, str(current) + ')' )

    def e():
        current=enter.get()
        enter.delete(0, END)
        e = str(math.e)
        enter.insert(0, str(current) + e )


    def log():
        current=enter.get()
        enter.delete(0,END)
        log = str(math.log10(float(current)))
        enter.insert(0, log )
        equation = f'log({current})'
        enter2.insert(0,equation)

    one=Button(frame,text=" 1 ",padx=15,pady=15, borderwidth = 0, command=lambda:buttonClick(1))
    one.grid(row=4,column=0)
    one.configure(bg='white',fg='black', font=('Comic San MS',20))

    two=Button(frame, text=" 2 ", padx=15,pady=15, borderwidth = 0, command=lambda:buttonClick(2))
    two.grid(row=4,column=1)
    two.configure(bg='white',fg='black', font=('Comic San MS',20))

    three=Button(frame, text=" 3 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(3))
    three.grid(row=4,column=2)
    three.configure(bg='white',fg='black', font=('Comic San MS',20))

    four=Button(frame, text=" 4 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(4))
    four.grid(row=3,column=0)
    four.configure(bg='white',fg='black', font=('Comic San MS',20))

    five=Button(frame, text=" 5 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(5))
    five.grid(row=3,column=1)
    five.configure(bg='white',fg='black', font=('Comic San MS',20))

    six=Button(frame, text=" 6 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(6))
    six.grid(row=3,column=2)
    six.configure(bg='white',fg='black', font=('Comic San MS',20))

    seven=Button(frame, text=" 7 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(7))
    seven.grid(row=2,column=0)
    seven.configure(bg='white',fg='black', font=('Comic San MS',20))

    eight=Button(frame, text=" 8 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(8))
    eight.grid(row=2,column=1)
    eight.configure(bg='white',fg='black', font=('Comic San MS',20))

    nine=Button(frame, text=" 9 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(9))
    nine.grid(row=2,column=2)
    nine.configure(bg='white',fg='black', font=('Comic San MS',20))

    zero=Button(frame, text=" 0 ",padx=15,pady=15,borderwidth = 0, command=lambda:buttonClick(0))
    zero.grid(row=5,column=0)
    zero.configure(bg='white',fg='black', font=('Comic San MS',20))

    dot=Button(frame, text=" . ",padx=18,pady=15,borderwidth = 0,command=dot)
    dot.grid(row=5,column=2)
    dot.configure(bg='white',fg='black', font=('Comic San MS',20))

    add=Button(frame, text=" + ",padx=20,pady=15,borderwidth = 0, command=add)
    add.grid(row=5,column=3)
    add.configure(bg='white',fg='black', font=('Comic San MS',20))

    subtract=Button(frame, text=" - ",padx=18,pady=15,borderwidth = 0, command=subtract)
    subtract.grid(row=4,column=3)
    subtract.configure(bg='white',fg='black', font=('Comic San MS',20))

    multiply=Button(frame, text=" * ",padx=17,pady=15,borderwidth = 0,command=multiply)
    multiply.grid(row=3,column=3)
    multiply.configure(bg='white',fg='black', font=('Comic San MS',20))

    divide=Button(frame, text=" / ",padx=18,pady=15,borderwidth = 0,command=divide)
    divide.grid(row=3,column=4)
    divide.configure(bg='white',fg='black', font=('Comic San MS',20))

    equalto=Button(frame, text=" = ",padx=18,pady=15,borderwidth = 0,command=equal)
    equalto.grid(row=5,column=4)
    equalto.configure(bg='white',fg='black', font=('Comic San MS',20))

    percent=Button(frame, text=" % ",padx=17,pady=15,borderwidth = 0,command=percent)
    percent.grid(row=4,column=4)
    percent.configure(bg='white',fg='black', font=('Comic San MS',20))

    clear=Button(frame,text="AC",padx=17,pady=15,borderwidth = 0,command=clear)
    clear.grid(row=2,column=4)
    clear.configure(bg= 'white',fg='black', font=('Comic San MS',20))

    delete=Button(frame,text=" C ",padx=16,pady=15,borderwidth = 0,command=delete)
    delete.grid(row=2,column=3)
    delete.configure( bg = 'white',fg = 'black', font=('Comic San MS',20))

    plusMinus=Button(frame, text=" ± ",padx=15,pady=15,borderwidth = 0,command=plusMinus)
    plusMinus.grid(row=5,column=1)
    plusMinus.configure(bg='white',fg='black', font=('Comic San MS',20))

    #========================================Function================================================


    def enterOne(e):
        one['background'] = 'darkslategrey'

    def leaveOne(e):
        one['background'] = 'white'

    one.bind("<Enter>", enterOne)
    one.bind("<Leave>", leaveOne)

    def enterTwo(e):
        two['background'] = 'darkslategrey'

    def leaveTwo(e):
        two['background'] = 'white'

    two.bind("<Enter>", enterTwo)
    two.bind("<Leave>", leaveTwo)

    def enterThree(e):
        three['background'] = 'darkslategrey'

    def leaveThree(e):
        three['background'] = 'white'

    three.bind("<Enter>", enterThree)
    three.bind("<Leave>", leaveThree)

    def enterFour(e):
        four['background'] = 'darkslategrey'

    def leaveFour(e):
        four['background'] = 'white'

    four.bind("<Enter>", enterFour)
    four.bind("<Leave>", leaveFour)

    def enterFive(e):
        five['background'] = 'darkslategrey'

    def leaveFive(e):
        five['background'] = 'white'

    five.bind("<Enter>", enterFive)
    five.bind("<Leave>", leaveFive)

    def enterSix(e):
        six['background'] = 'darkslategrey'

    def leaveSix(e):
        six['background'] = 'white'

    six.bind("<Enter>", enterSix)
    six.bind("<Leave>", leaveSix)

    def enterSeven(e):
        seven['background'] = 'darkslategrey'

    def leaveSeven(e):
        seven['background'] = 'white'

    seven.bind("<Enter>", enterSeven)
    seven.bind("<Leave>", leaveSeven)

    def enterEight(e):
        eight['background'] = 'darkslategrey'

    def leaveEight(e):
        eight['background'] = 'white'

    eight.bind("<Enter>", enterEight)
    eight.bind("<Leave>", leaveEight)

    def enterNine(e):
        nine['background'] = 'darkslategrey'

    def leaveNine(e):
        nine['background'] = 'white'

    nine.bind("<Enter>", enterNine)
    nine.bind("<Leave>", leaveNine)

    def enterZero(e):
        zero['background'] = 'darkslategrey'

    def leaveZero(e):
        zero['background'] = 'white'

    zero.bind("<Enter>", enterZero)
    zero.bind("<Leave>", leaveZero)

    def enterPlusMinus(e):
        plusMinus['background'] = 'darkslategrey'

    def leavePlusMinus(e):
        plusMinus['background'] = 'white'

    plusMinus.bind("<Enter>", enterPlusMinus)
    plusMinus.bind("<Leave>", leavePlusMinus)

    def enterDot(e):
        dot['background'] = 'darkslategrey'

    def leaveDot(e):
        dot['background'] = 'white'

    dot.bind("<Enter>", enterDot)
    dot.bind("<Leave>", leaveDot)

    def enterPlus(e):
        add['background'] = 'darkslategrey'

    def leavePlus(e):
        add['background'] = 'white'

    add.bind("<Enter>", enterPlus)
    add.bind("<Leave>", leavePlus)

    def enterEqualto(e):
        equalto['background'] = 'darkslategrey'

    def leaveEqualto(e):
        equalto['background'] = 'white'

    equalto.bind("<Enter>", enterEqualto)
    equalto.bind("<Leave>", leaveEqualto)

    def enterPercent(e):
        percent['background'] = 'darkslategrey'

    def leavePercent(e):
        percent['background'] = 'white'

    percent.bind("<Enter>", enterPercent)
    percent.bind("<Leave>", leavePercent)

    def enterMinus(e):
        subtract['background'] = 'darkslategrey'

    def leaveMinus(e):
        subtract['background'] = 'white'

    subtract.bind("<Enter>", enterMinus)
    subtract.bind("<Leave>", leaveMinus)

    def enterDivide(e):
        divide['background'] = 'darkslategrey'

    def leaveDivide(e):
        divide['background'] = 'white'

    divide.bind("<Enter>", enterDivide)
    divide.bind("<Leave>", leaveDivide)

    def enterMultiply(e):
        multiply['background'] = 'darkslategrey'

    def leaveMultiply(e):
        multiply['background'] = 'white'

    multiply.bind("<Enter>", enterMultiply)
    multiply.bind("<Leave>", leaveMultiply)

    def enterAC(e):
        clear['background'] = 'darkslategrey'

    def leaveAC(e):
        clear['background'] = 'white'

    clear.bind("<Enter>", enterAC)
    clear.bind("<Leave>", leaveAC)

    def enterDelete(e):
        delete['background'] = 'darkslategrey'

    def leaveDelete(e):
        delete['background'] = 'white'

    delete.bind("<Enter>", enterDelete)
    delete.bind("<Leave>", leaveDelete)

    #============================================BUTTON============================================#

    bracket1=Button(frame,text=" ( ",padx=15,pady=15, borderwidth = 0, command= lB)
    bracket1.grid(row=2,column=5)
    bracket1.configure(bg='white',fg='black', font=('Comic San MS',20))

    bracket2=Button(frame,text=" ) ",padx=15,pady=15, borderwidth = 0, command= rB)
    bracket2.grid(row=2,column=6)
    bracket2.configure(bg='white',fg='black', font=('Comic San MS',20))

    log=Button(frame,text=" log ",padx=15,pady=15, borderwidth = 0, command= log)
    log.grid(row=2,column=7)
    log.configure(bg='white',fg='black', font=('Comic San MS',20))

    sin=Button(frame,text=" sin ",padx=15,pady=15, borderwidth = 0, command = sin)
    sin.grid(row=3,column=5)
    sin.configure(bg='white',fg='black', font=('Comic San MS',20))

    cos=Button(frame,text=" cos ",padx=15,pady=15, borderwidth = 0, command= cos)
    cos.grid(row=3,column=6)
    cos.configure(bg='white',fg='black', font=('Comic San MS',20))

    tan=Button(frame,text=" tan ",padx=15,pady=15, borderwidth = 0, command= tan)
    tan.grid(row=3,column=7)
    tan.configure(bg='white',fg='black', font=('Comic San MS',20))

    sinh=Button(frame,text=" sinh ",padx=15,pady=15, borderwidth = 0, command = sinh)
    sinh.grid(row=4,column=5)
    sinh.configure(bg='white' ,fg='black', font=('Comic San MS',20))

    cosh=Button(frame,text=" cosh ",padx=15,pady=15, borderwidth = 0, command= cosh)
    cosh.grid(row=4,column=6)
    cosh.configure(bg='white',fg='black', font=('Comic San MS',20))

    tanh=Button(frame,text=" tanh ",padx=15,pady=15, borderwidth = 0, command=tanh)
    tanh.grid(row=4,column=7)
    tanh.configure(bg= 'white',fg='black', font=('Comic San MS',20))

    pi=Button(frame,text=" pi ",padx=15,pady=15, borderwidth = 0, command = pi)
    pi.grid(row=5,column=5)
    pi.configure(bg='white',fg='black', font=('Comic San MS',20))

    root=Button(frame,text=" root ",padx=15,pady=15, borderwidth = 0, command = root)
    root.grid(row=5,column=6)
    root.configure(bg='white',fg='black', font=('Comic San MS',20))

    xn=Button(frame,text=" Xn ",padx=15,pady=15, borderwidth = 0, command= square)
    xn.grid(row=5,column=7)
    xn.configure(bg='white',fg='black', font=('Comic San MS',20))




    newWindow.mainloop()
       
def scientific():
    puthiya = Tk()
    puthiya.title('Calculator!')
    puthiya.resizable(0, 0)
    #puthiya.geometry("0+0")
    #puthiya.iconbitmap('calculator2.ico')


    ur_menu = Menu(puthiya)
    puthiya.config(menu = ur_menu)
    file_menu = Menu(ur_menu, tearoff = False, background = 'black', foreground = 'white',activebackground = '#00E4FF', activeforeground='black')
    ur_menu.add_cascade(label = 'Styleo', background = '#9C25F3', activebackground = 'black',menu = file_menu)
    #my_menu.add_cascade(label = 'Mode', menu = file_menu)h

                                                     
    Variant = Menu(ur_menu, tearoff = False, background = 'black', foreground = 'white',activebackground = '#00E4FF', activeforeground='black')
    ur_menu.add_cascade(label = 'Varianto',background = '#9C25F3', activebackground = 'black',menu = Variant)


   

    #Variant = Menu(my_menu, tearoff = False, background = 'black', foreground = 'white',activebackground = '#00E4FF', activeforeground='black')
    #my_menu.add_cascade(label = 'Variant',background = '#9C25F3', activebackground = 'black',menu = Variant)



    def a():
        file_menu.add_command(label = 'BLACK')

    def b():
        file_menu.add_command(label = 'LIGHT', command = lambda:[puthiya.destroy() ,scientificl()])
    #def quit():
    #    global calculator
    #   calculator.quit()
    a()
    b()
    #file_menu.add_command(label = 'BLACK')
    #b()
    #file_menu.add_command(label = 'LIGHT')
    Variant.add_command(label = 'Standard', command = lambda:[puthiya.destroy() ,dark()])
    Variant.add_command(label = 'Scientific')


    
    #calculator.iconbitmap('./images/calculator2.ico')

    frame=Frame(puthiya)
    frame.configure(bg='black')
    frame.grid(row=0, column=0,columnspan = 6 ,padx=0, pady=0)

    enter2=Entry(frame, width=23, borderwidth=0, font=('Comic San MS',25))
    enter2.configure(justify=RIGHT, width = 39 )
    enter2.configure(bg='black')
    enter2.configure(fg='white')

    enter2.grid(row=0, column=0, columnspan=8, padx=0, pady=0, ipady=8)

    enter=Entry(frame, width=18, borderwidth=0, font=('Comic San MS',45))
    enter.configure(justify=RIGHT, width = 23 )
    enter.configure(bg='black')
    enter.configure(fg='white')
    enter.grid(row=1, column=0, columnspan=8, padx=0, pady=0, ipady=15)

    def buttonClick(number):
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0, str(current) + str(number))

    def dot():
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0, str(current) + '.')

    def add():
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0,str(current) + '+')

    def subtract():
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0,str(current) + '-')

    def multiply():
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0,str(current) + '*') 

    def divide():
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0,str(current) + '/')

    def clear():
        enter.delete(0,END)
        enter2.delete(0,END)

    def equal():

        enter2.insert(0, enter.get())
        result=eval(enter.get())
        enter.delete(0,END)
        resultString = str(result)
        resultLength = len(resultString)

        if resultString[resultLength-2:] =='.0':
            result = str(resultString[:resultLength-2])

        enter.insert(0,result)

    def delete():
        current=len(enter.get())
        last = current - 1
        enter.delete(last, END)

    def percent():
        firstNumber=float(enter.get())
        enter.delete(0,END)
        enter.insert(0,firstNumber / 100)
        enter2.insert(0,f'{firstNumber}/100' )


    def plusMinus():
        current=enter.get()
        plus = current[0:1]
            
        if plus == '0' or plus == '1' or plus == '2' or plus == '3' or plus == '4' or plus == '5' or plus == '6' or plus == '7' or plus == '8' or plus == '9':  
            enter.insert(0,'-')
        else:
            enter.delete(0,1)

    def root():
        current=enter.get()
        enter.delete(0,END)
        root = math.sqrt(float(current))
        enter.insert(0,root)   
        equation = f'√ {current}'
        enter2.insert(0,equation)

    def sin():
        current = enter.get()
        enter.delete(0, END)
        sin = math.sin(float(current))
        enter.insert(0,sin)
        enter2.insert(0, current)

    def cos():
        current = enter.get()
        enter.delete(0, END)
        cos = math.cos(float(current))
        enter.insert(0,cos)
        enter2.insert(0, current)

    def tan():
        current = enter.get()
        enter.delete(0, END)
        tan = math.tan(float(current))
        enter.insert(0,tan)
        enter2.insert(0, current)

    def sinh():
        current = enter.get()
        enter.delete(0, END)
        sinh = math.sinh(float(current))
        enter.insert(0,sinh)
        enter2.insert(0, current)

    def cosh():
        current = enter.get()
        enter.delete(0, END)
        cosh = math.cosh(float(current))
        enter.insert(0,cosh)
        enter2.insert(0, current)

    def tanh():
        current = enter.get()
        enter.delete(0, END)
        tanh = math.tanh(float(current))
        enter.insert(0,tanh)
        enter2.insert(0, current)

    def pi():
        current=enter.get()
        enter.delete(0, END)
        pi = str(math.pi)
        enter.insert(0, str(current) + pi )

    def square():
        current = enter.get()
        enter.delete(0, END)
        square = math.isqrt(current)
        enter.insert(0,pi)
        enter2.insert(0, current)

    def lB():
        current = enter.get()
        enter.delete(0,END)
        enter.insert(0, str(current) + '(' )

    def rB():
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0, str(current) + ')' )

    def e():
        current=enter.get()
        enter.delete(0, END)
        e = str(math.e)
        enter.insert(0, str(current) + e )


    def log():
        current=enter.get()
        enter.delete(0,END)
        log = str(math.log10(float(current)))
        enter.insert(0, log )
        equation = f'log({current})'
        enter2.insert(0,equation)

    one=Button(frame,text=" 1 ",padx=15,pady=15, borderwidth = 0, command=lambda:buttonClick(1))
    one.grid(row=4,column=0)
    one.configure(bg='black',fg='white', font=('Comic San MS',20))

    two=Button(frame, text=" 2 ", padx=15,pady=15, borderwidth = 0, command=lambda:buttonClick(2))
    two.grid(row=4,column=1)
    two.configure(bg='black',fg='white', font=('Comic San MS',20))

    three=Button(frame, text=" 3 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(3))
    three.grid(row=4,column=2)
    three.configure(bg='black',fg='white', font=('Comic San MS',20))

    four=Button(frame, text=" 4 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(4))
    four.grid(row=3,column=0)
    four.configure(bg='black',fg='white', font=('Comic San MS',20))

    five=Button(frame, text=" 5 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(5))
    five.grid(row=3,column=1)
    five.configure(bg='black',fg='white', font=('Comic San MS',20))

    six=Button(frame, text=" 6 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(6))
    six.grid(row=3,column=2)
    six.configure(bg='black',fg='white', font=('Comic San MS',20))

    seven=Button(frame, text=" 7 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(7))
    seven.grid(row=2,column=0)
    seven.configure(bg='black',fg='white', font=('Comic San MS',20))

    eight=Button(frame, text=" 8 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(8))
    eight.grid(row=2,column=1)
    eight.configure(bg='black',fg='white', font=('Comic San MS',20))

    nine=Button(frame, text=" 9 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(9))
    nine.grid(row=2,column=2)
    nine.configure(bg='black',fg='white', font=('Comic San MS',20))

    zero=Button(frame, text=" 0 ",padx=15,pady=15,borderwidth = 0, command=lambda:buttonClick(0))
    zero.grid(row=5,column=0)
    zero.configure(bg='black',fg='white', font=('Comic San MS',20))

    dot=Button(frame, text=" . ",padx=18,pady=15,borderwidth = 0,command=dot)
    dot.grid(row=5,column=2)
    dot.configure(bg='black',fg='white', font=('Comic San MS',20))

    add=Button(frame, text=" + ",padx=20,pady=15,borderwidth = 0, command=add)
    add.grid(row=5,column=3)
    add.configure(bg='black',fg='white', font=('Comic San MS',20))

    subtract=Button(frame, text=" - ",padx=18,pady=15,borderwidth = 0, command=subtract)
    subtract.grid(row=4,column=3)
    subtract.configure(bg='black',fg='white', font=('Comic San MS',20))

    multiply=Button(frame, text=" * ",padx=17,pady=15,borderwidth = 0,command=multiply)
    multiply.grid(row=3,column=3)
    multiply.configure(bg='black',fg='white', font=('Comic San MS',20))

    divide=Button(frame, text=" / ",padx=18,pady=15,borderwidth = 0,command=divide)
    divide.grid(row=3,column=4)
    divide.configure(bg='black',fg='white', font=('Comic San MS',20))

    equalto=Button(frame, text=" = ",padx=18,pady=15,borderwidth = 0,command=equal)
    equalto.grid(row=5,column=4)
    equalto.configure(bg='black',fg='white', font=('Comic San MS',20))

    percent=Button(frame, text=" % ",padx=17,pady=15,borderwidth = 0,command=percent)
    percent.grid(row=4,column=4)
    percent.configure(bg='black',fg='white', font=('Comic San MS',20))

    clear=Button(frame,text="AC",padx=17,pady=15,borderwidth = 0,command=clear)
    clear.grid(row=2,column=4)
    clear.configure(bg= 'black',fg='white', font=('Comic San MS',20))

    delete=Button(frame,text=" C ",padx=16,pady=15,borderwidth = 0,command=delete)
    delete.grid(row=2,column=3)
    delete.configure( bg = 'black',fg='white', font=('Comic San MS',20))

    plusMinus=Button(frame, text=" ± ",padx=15,pady=15,borderwidth = 0,command=plusMinus)
    plusMinus.grid(row=5,column=1)
    plusMinus.configure(bg='black',fg='white', font=('Comic San MS',20))

    #========================================Function================================================


    def enterOne(e):
        one['background'] = 'darkslategrey'

    def leaveOne(e):
        one['background'] = 'black'

    one.bind("<Enter>", enterOne)
    one.bind("<Leave>", leaveOne)

    def enterTwo(e):
        two['background'] = 'darkslategrey'

    def leaveTwo(e):
        two['background'] = 'black'

    two.bind("<Enter>", enterTwo)
    two.bind("<Leave>", leaveTwo)

    def enterThree(e):
        three['background'] = 'darkslategrey'

    def leaveThree(e):
        three['background'] = 'black'

    three.bind("<Enter>", enterThree)
    three.bind("<Leave>", leaveThree)

    def enterFour(e):
        four['background'] = 'darkslategrey'

    def leaveFour(e):
        four['background'] = 'black'

    four.bind("<Enter>", enterFour)
    four.bind("<Leave>", leaveFour)

    def enterFive(e):
        five['background'] = 'darkslategrey'

    def leaveFive(e):
        five['background'] = 'black'

    five.bind("<Enter>", enterFive)
    five.bind("<Leave>", leaveFive)

    def enterSix(e):
        six['background'] = 'darkslategrey'

    def leaveSix(e):
        six['background'] = 'black'

    six.bind("<Enter>", enterSix)
    six.bind("<Leave>", leaveSix)

    def enterSeven(e):
        seven['background'] = 'darkslategrey'

    def leaveSeven(e):
        seven['background'] = 'black'

    seven.bind("<Enter>", enterSeven)
    seven.bind("<Leave>", leaveSeven)

    def enterEight(e):
        eight['background'] = 'darkslategrey'

    def leaveEight(e):
        eight['background'] = 'black'

    eight.bind("<Enter>", enterEight)
    eight.bind("<Leave>", leaveEight)

    def enterNine(e):
        nine['background'] = 'darkslategrey'

    def leaveNine(e):
        nine['background'] = 'black'

    nine.bind("<Enter>", enterNine)
    nine.bind("<Leave>", leaveNine)

    def enterZero(e):
        zero['background'] = 'darkslategrey'

    def leaveZero(e):
        zero['background'] = 'black'

    zero.bind("<Enter>", enterZero)
    zero.bind("<Leave>", leaveZero)

    def enterPlusMinus(e):
        plusMinus['background'] = 'darkslategrey'

    def leavePlusMinus(e):
        plusMinus['background'] = 'black'

    plusMinus.bind("<Enter>", enterPlusMinus)
    plusMinus.bind("<Leave>", leavePlusMinus)

    def enterDot(e):
        dot['background'] = 'darkslategrey'

    def leaveDot(e):
        dot['background'] = 'black'

    dot.bind("<Enter>", enterDot)
    dot.bind("<Leave>", leaveDot)

    def enterPlus(e):
        add['background'] = 'darkslategrey'

    def leavePlus(e):
        add['background'] = 'black'

    add.bind("<Enter>", enterPlus)
    add.bind("<Leave>", leavePlus)

    def enterEqualto(e):
        equalto['background'] = 'darkslategrey'

    def leaveEqualto(e):
        equalto['background'] = 'black'

    equalto.bind("<Enter>", enterEqualto)
    equalto.bind("<Leave>", leaveEqualto)

    def enterPercent(e):
        percent['background'] = 'darkslategrey'

    def leavePercent(e):
        percent['background'] = 'black'

    percent.bind("<Enter>", enterPercent)
    percent.bind("<Leave>", leavePercent)

    def enterMinus(e):
        subtract['background'] = 'darkslategrey'

    def leaveMinus(e):
        subtract['background'] = 'black'

    subtract.bind("<Enter>", enterMinus)
    subtract.bind("<Leave>", leaveMinus)

    def enterDivide(e):
        divide['background'] = 'darkslategrey'

    def leaveDivide(e):
        divide['background'] = 'black'

    divide.bind("<Enter>", enterDivide)
    divide.bind("<Leave>", leaveDivide)

    def enterMultiply(e):
        multiply['background'] = 'darkslategrey'

    def leaveMultiply(e):
        multiply['background'] = 'black'

    multiply.bind("<Enter>", enterMultiply)
    multiply.bind("<Leave>", leaveMultiply)

    def enterAC(e):
        clear['background'] = 'darkslategrey'

    def leaveAC(e):
        clear['background'] = 'black'

    clear.bind("<Enter>", enterAC)
    clear.bind("<Leave>", leaveAC)

    def enterDelete(e):
        delete['background'] = 'darkslategrey'

    def leaveDelete(e):
        delete['background'] = 'black'

    delete.bind("<Enter>", enterDelete)
    delete.bind("<Leave>", leaveDelete)

    #============================================BUTTON============================================#

    bracket1=Button(frame,text=" ( ",padx=15,pady=15, borderwidth = 0, command= lB)
    bracket1.grid(row=2,column=5)
    bracket1.configure(bg='black',fg='white', font=('Comic San MS',20))

    bracket2=Button(frame,text=" ) ",padx=15,pady=15, borderwidth = 0, command= rB)
    bracket2.grid(row=2,column=6)
    bracket2.configure(bg='black',fg='white', font=('Comic San MS',20))

    log=Button(frame,text=" log ",padx=15,pady=15, borderwidth = 0, command= log)
    log.grid(row=2,column=7)
    log.configure(bg='black',fg='white', font=('Comic San MS',20))

    sin=Button(frame,text=" sin ",padx=15,pady=15, borderwidth = 0, command = sin)
    sin.grid(row=3,column=5)
    sin.configure(bg='black',fg='white', font=('Comic San MS',20))

    cos=Button(frame,text=" cos ",padx=15,pady=15, borderwidth = 0, command= cos)
    cos.grid(row=3,column=6)
    cos.configure(bg='black',fg='white', font=('Comic San MS',20))

    tan=Button(frame,text=" tan ",padx=15,pady=15, borderwidth = 0, command= tan)
    tan.grid(row=3,column=7)
    tan.configure(bg='black',fg='white', font=('Comic San MS',20))

    sinh=Button(frame,text=" sinh ",padx=15,pady=15, borderwidth = 0, command = sinh)
    sinh.grid(row=4,column=5)
    sinh.configure(bg='black',fg='white', font=('Comic San MS',20))

    cosh=Button(frame,text=" cosh ",padx=15,pady=15, borderwidth = 0, command= cosh)
    cosh.grid(row=4,column=6)
    cosh.configure(bg='black',fg='white', font=('Comic San MS',20))

    tanh=Button(frame,text=" tanh ",padx=15,pady=15, borderwidth = 0, command=tanh)
    tanh.grid(row=4,column=7)
    tanh.configure(bg='black',fg='white', font=('Comic San MS',20))

    pi=Button(frame,text=" pi ",padx=15,pady=15, borderwidth = 0, command = pi)
    pi.grid(row=5,column=5)
    pi.configure(bg='black',fg='white', font=('Comic San MS',20))

    root=Button(frame,text=" root ",padx=15,pady=15, borderwidth = 0, command = root)
    root.grid(row=5,column=6)
    root.configure(bg='black',fg='white', font=('Comic San MS',20))

    xn=Button(frame,text=" Xn ",padx=15,pady=15, borderwidth = 0, command= square)
    xn.grid(row=5,column=7)
    xn.configure(bg='black',fg='white', font=('Comic San MS',20))

def dark():

    calculator = Tk()
    calculator.title("Calculator!")
    #calculator.configure(bg='black')
    calculator.resizable(0, 0)
    #calculator.iconbitmap('calculator2.ico')

    
    ur_menu = Menu(calculator)
    calculator.config(menu = ur_menu)
    file_menu = Menu(ur_menu, tearoff = False, background = 'black', foreground = 'white',activebackground = '#00E4FF', activeforeground='black')
    ur_menu.add_cascade(label = 'Style', background = '#9C25F3', activebackground = 'black',menu = file_menu)
    #my_menu.add_cascade(label = 'Mode', menu = file_menu)h

                                                     
    Variant = Menu(ur_menu, tearoff = False, background = 'black', foreground = 'white',activebackground = '#00E4FF', activeforeground='black')
    ur_menu.add_cascade(label = 'Variant',background = '#9C25F3', activebackground = 'black',menu = Variant)


   

    #Variant = Menu(my_menu, tearoff = False, background = 'black', foreground = 'white',activebackground = '#00E4FF', activeforeground='black')
    #my_menu.add_cascade(label = 'Variant',background = '#9C25F3', activebackground = 'black',menu = Variant)



    def a():
        file_menu.add_command(label = 'BLACK')

    def b():
        file_menu.add_command(label = 'LIGHT', command = lambda:[calculator.destroy() ,light()])
    #def quit():
    #    global calculator
    #   calculator.quit()
    a()
    b()
    #file_menu.add_command(label = 'BLACK')
    #b()
    #file_menu.add_command(label = 'LIGHT')
    Variant.add_command(label = 'Standard')
    Variant.add_command(label = 'Scientific', command = lambda: [calculator.destroy(),scientific()])
    
    frame=Frame(calculator)
    frame.configure(bg='black')
    frame.grid(row=0, column=0, columnspan=6, padx=0, pady=0)

    enter2=Entry(frame, width=23, borderwidth=0, font=('Comic San MS',25))
    enter2.configure(justify=RIGHT)
    enter2.configure(bg='black')
    enter2.configure(fg='white')
    enter2.grid(row=0, column=0, columnspan=5, padx=0, pady=0, ipady=8)

    enter=Entry(frame, width=12, borderwidth=0, font=('Comic San MS',45))
    enter.configure(justify=RIGHT)
    enter.configure(bg='black')
    enter.configure(fg='white')
    enter.grid(row=1, column=0, columnspan=5, padx=0, pady=0, ipady=15)

    def buttonClick(number):
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0, str(current) + str(number))

    def dot():
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0, str(current) + '.')

    def add():
        firstNumberStr=enter.get()
        global firstNumber
        global math
        math='add'
        firstNumber= float(firstNumberStr)
        enter.delete(0,END)

    def subtract():
        firstNumberStr=enter.get()
        global firstNumber
        global math
        math='subtract'
        firstNumber= float(firstNumberStr)
        enter.delete(0,END)

    def multiply():
        firstNumberStr=enter.get()
        global firstNumber
        global math
        math='multiply'
        firstNumber= float(firstNumberStr)
        enter.delete(0,END)

    def divide():
        firstNumberStr=enter.get()
        global firstNumber
        global math
        math='divide'
        firstNumber= float(firstNumberStr)
        enter.delete(0,END)

    def clear():
        enter.delete(0,END)
        enter2.delete(0,END)

    def equal():
        secondNumber=enter.get()
        enter.delete(0,END)

        if math =='add':

            global firstNumber

            firstNumberString = str(firstNumber)
            firstNumberLength = len(firstNumberString)
            if firstNumberString[firstNumberLength-2:] == '.0':
                firstNumber = int(firstNumberString[:firstNumberLength-2])

            entryEquation = enter2.get()
            if len(entryEquation) > 0:
                equation = f' + {secondNumber} '
                enter2.insert(END, equation)
            if len(entryEquation) == 0:
                equation = f'{firstNumber} + {secondNumber}'
                enter2.insert(0, equation)

            result = firstNumber + float(secondNumber)
            resultString = str(result)
            length = len(resultString)
            if resultString[length-2:] == '.0':
                result = int(resultString[:length-2])

            enter.insert(0,result)
    
        if math =='subtract':
            
            #global firstNumber

            firstNumberString = str(firstNumber)
            firstNumberLength = len(firstNumberString)
            if firstNumberString[firstNumberLength-2:] == '.0':
                firstNumber = int(firstNumberString[:firstNumberLength-2])

            entryEquation = enter2.get()
            if len(entryEquation) > 0:
                equation = f' - {secondNumber} '
                enter2.insert(END, equation)
            if len(entryEquation) == 0:
                equation = f'{firstNumber} - {secondNumber}'
                enter2.insert(0, equation)

            result = firstNumber - float(secondNumber)
            resultString = str(result)
            length = len(resultString)
            if resultString[length-2:] == '.0':
                result = int(resultString[:length-2])

            enter.insert(0,result)

        if math =='multiply':
            
            #global firstNumber

            firstNumberString = str(firstNumber)
            firstNumberLength = len(firstNumberString)
            if firstNumberString[firstNumberLength-2:] == '.0':
                firstNumber = int(firstNumberString[:firstNumberLength-2])

            entryEquation = enter2.get()
            if len(entryEquation) > 0:
                equation = f' x {secondNumber} '
                enter2.insert(END, equation)
            if len(entryEquation) == 0:
                equation = f'{firstNumber} x {secondNumber}'
                enter2.insert(0, equation)

            result = firstNumber * float(secondNumber)
            resultString = str(result)
            length = len(resultString)
            if resultString[length-2:] == '.0':
                result = int(resultString[:length-2])

            enter.insert(0,result)

        if math =='divide':
            
            #global firstNumber

            firstNumberString = str(firstNumber)
            firstNumberLength = len(firstNumberString)
            if firstNumberString[firstNumberLength-2:] == '.0':
                firstNumber = int(firstNumberString[:firstNumberLength-2])

            entryEquation = enter2.get()
            if len(entryEquation) > 0:
                equation = f' / {secondNumber} '
                enter2.insert(END, equation)
            if len(entryEquation) == 0:
                equation = f'{firstNumber} / {secondNumber}'
                enter2.insert(0, equation)

            result = firstNumber / float(secondNumber)
            resultString = str(result)
            length = len(resultString)
            if resultString[length-2:] == '.0':
                result = int(resultString[:length-2])

            enter.insert(0,result)

    def delete():
        current=len(enter.get())
        last = current - 1
        enter.delete(last,END)

    def percent():
        firstNumber=float(enter.get())
        enter.delete(0,END)
        enter.insert(0,firstNumber / 100 )

    def plusMinus():
        current=enter.get()
        plus = current[0:1]
        
        if plus == '0' or plus == '1' or plus == '2' or plus == '3' or plus == '4' or plus == '5' or plus == '6' or plus == '7' or plus == '8' or plus == '9':  
            enter.insert(0,'-')
        else:
            enter.delete(0,1)
    
    one=Button(frame,text=" 1 ",padx=15,pady=15, borderwidth = 0, command=lambda:buttonClick(1))
    one.grid(row=4,column=0)
    one.configure(bg='black',fg='white', font=('Comic San MS',20))

    two=Button(frame, text=" 2 ", padx=15,pady=15, borderwidth = 0, command=lambda:buttonClick(2))
    two.grid(row=4,column=1)
    two.configure(bg='black',fg='white', font=('Comic San MS',20))

    three=Button(frame, text=" 3 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(3))
    three.grid(row=4,column=2)
    three.configure(bg='black',fg='white', font=('Comic San MS',20))

    four=Button(frame, text=" 4 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(4))
    four.grid(row=3,column=0)
    four.configure(bg='black',fg='white', font=('Comic San MS',20))

    five=Button(frame, text=" 5 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(5))
    five.grid(row=3,column=1)
    five.configure(bg='black',fg='white', font=('Comic San MS',20))

    six=Button(frame, text=" 6 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(6))
    six.grid(row=3,column=2)
    six.configure(bg='black',fg='white', font=('Comic San MS',20))

    seven=Button(frame, text=" 7 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(7))
    seven.grid(row=2,column=0)
    seven.configure(bg='black',fg='white', font=('Comic San MS',20))

    eight=Button(frame, text=" 8 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(8))
    eight.grid(row=2,column=1)
    eight.configure(bg='black',fg='white', font=('Comic San MS',20))

    nine=Button(frame, text=" 9 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(9))
    nine.grid(row=2,column=2)
    nine.configure(bg='black',fg='white', font=('Comic San MS',20))

    zero=Button(frame, text=" 0 ",padx=15,pady=15,borderwidth = 0, command=lambda:buttonClick(0))
    zero.grid(row=5,column=0)
    zero.configure(bg='black',fg='white', font=('Comic San MS',20))

    dot=Button(frame, text=" . ",padx=18,pady=15,borderwidth = 0,command=dot)
    dot.grid(row=5,column=2)
    dot.configure(bg='black',fg='white', font=('Comic San MS',20))

    add=Button(frame, text=" + ",padx=14,pady=15,borderwidth = 0, command=add)
    add.grid(row=5,column=3)
    add.configure(bg='black',fg='white', font=('Comic San MS',20))

    subtract=Button(frame, text=" - ",padx=18,pady=15,borderwidth = 0, command=subtract)
    subtract.grid(row=4,column=3)
    subtract.configure(bg='black',fg='white', font=('Comic San MS',20))

    multiply=Button(frame, text=" x ",padx=17,pady=15,borderwidth = 0,command=multiply)
    multiply.grid(row=3,column=3)
    multiply.configure(bg='black',fg='white', font=('Comic San MS',20))

    divide=Button(frame, text=" / ",padx=18,pady=15,borderwidth = 0,command=divide)
    divide.grid(row=3,column=4)
    divide.configure(bg='black',fg='white', font=('Comic San MS',20))

    equalto=Button(frame, text=" = ",padx=18,pady=15,borderwidth = 0,command=equal)
    equalto.grid(row=5,column=4)
    equalto.configure(bg='black',fg='white', font=('Comic San MS',20))

    percent=Button(frame, text=" % ",padx=17,pady=15,borderwidth = 0,command=percent)
    percent.grid(row=4,column=4)
    percent.configure(bg='black',fg='white', font=('Comic San MS',20))

    clear=Button(frame, text="AC",padx=17,pady=15,borderwidth = 0,command=clear)
    clear.grid(row=2,column=4)
    clear.configure(bg='black',fg='white', font=('Comic San MS',20))

    delete=Button(frame, text=" C ",padx=16,pady=15,borderwidth = 0,command=delete)
    delete.grid(row=2,column=3)
    delete.configure(bg='black',fg='white', font=('Comic San MS',20))

    plusMinus=Button(frame, text=" ± ",padx=15,pady=15,borderwidth = 0,command=plusMinus)
    plusMinus.grid(row=5,column=1)
    plusMinus.configure(bg='black',fg='white', font=('Comic San MS',20))

    def enterOne(e):
        one['background'] = '#00E0FF'

    def leaveOne(e):
        one['background'] = 'black'

    one.bind("<Enter>", enterOne)
    one.bind("<Leave>", leaveOne)

    def enterTwo(e):
        two['background'] = '#00E0FF'

    def leaveTwo(e):
        two['background'] = 'black'

    two.bind("<Enter>", enterTwo)
    two.bind("<Leave>", leaveTwo)

    def enterThree(e):
        three['background'] = '#00E0FF'

    def leaveThree(e):
        three['background'] = 'black'

    three.bind("<Enter>", enterThree)
    three.bind("<Leave>", leaveThree)

    def enterFour(e):
        four['background'] = '#00E0FF'

    def leaveFour(e):
        four['background'] = 'black'

    four.bind("<Enter>", enterFour)
    four.bind("<Leave>", leaveFour)

    def enterFive(e):
        five['background'] = '#00E0FF'

    def leaveFive(e):
        five['background'] = 'black'

    five.bind("<Enter>", enterFive)
    five.bind("<Leave>", leaveFive)

    def enterSix(e):
        six['background'] = '#00E0FF'

    def leaveSix(e):
        six['background'] = 'black'

    six.bind("<Enter>", enterSix) 
    six.bind("<Leave>", leaveSix)

    def enterSeven(e):
        seven['background'] = '#00E0FF'

    def leaveSeven(e):
        seven['background'] = 'black'

    seven.bind("<Enter>", enterSeven)
    seven.bind("<Leave>", leaveSeven)

    def enterEight(e):
        eight['background'] = '#00E0FF'

    def leaveEight(e):
        eight['background'] = 'black'

    eight.bind("<Enter>", enterEight)
    eight.bind("<Leave>", leaveEight)

    def enterNine(e):
        nine['background'] = '#00E0FF'

    def leaveNine(e):
        nine['background'] = 'black'

    nine.bind("<Enter>", enterNine)
    nine.bind("<Leave>", leaveNine)

    def enterZero(e):
        zero['background'] = '#00E0FF'

    def leaveZero(e):
        zero['background'] = 'black'

    zero.bind("<Enter>", enterZero)
    zero.bind("<Leave>", leaveZero)

    def enterPlusMinus(e):
        plusMinus['background'] = '#00E0FF'

    def leavePlusMinus(e):
        plusMinus['background'] = 'black'

    plusMinus.bind("<Enter>", enterPlusMinus)
    plusMinus.bind("<Leave>", leavePlusMinus)

    def enterDot(e):
        dot['background'] = '#00E0FF'

    def leaveDot(e):
        dot['background'] = 'black'

    dot.bind("<Enter>", enterDot)
    dot.bind("<Leave>", leaveDot)

    def enterPlus(e):
        add['background'] = '#00E0FF'

    def leavePlus(e):
        add['background'] = 'black'

    add.bind("<Enter>", enterPlus)
    add.bind("<Leave>", leavePlus)

    def enterEqualto(e):
        equalto['background'] = '#00E0FF'

    def leaveEqualto(e):
        equalto['background'] = 'black'

    equalto.bind("<Enter>", enterEqualto)
    equalto.bind("<Leave>", leaveEqualto)

    def enterPercent(e):
        percent['background'] = '#00E0FF'

    def leavePercent(e):
        percent['background'] = 'black'

    percent.bind("<Enter>", enterPercent)
    percent.bind("<Leave>", leavePercent)

    def enterMinus(e):
        subtract['background'] = '#00E0FF'

    def leaveMinus(e):
        subtract['background'] = 'black'

    subtract.bind("<Enter>", enterMinus)
    subtract.bind("<Leave>", leaveMinus)

    def enterDivide(e):
        divide['background'] = '#00E0FF'

    def leaveDivide(e):
        divide['background'] = 'black'

    divide.bind("<Enter>", enterDivide)
    divide.bind("<Leave>", leaveDivide)

    def enterMultiply(e):
        multiply['background'] = '#00E0FF'

    def leaveMultiply(e):
        multiply['background'] = 'black'

    multiply.bind("<Enter>", enterMultiply)
    multiply.bind("<Leave>", leaveMultiply)

    def enterAC(e):
        clear['background'] = '#00E0FF'

    def leaveAC(e):
        clear['background'] = 'black'

    clear.bind("<Enter>", enterAC)
    clear.bind("<Leave>", leaveAC)

    def enterDelete(e):
        delete['background'] = '#00E0FF'

    def leaveDelete(e):
        delete['background'] = 'black'

    delete.bind("<Enter>", enterDelete)
    delete.bind("<Leave>", leaveDelete)

    calculator.mainloop()

def light():
    
    Lighto = Tk()
    Lighto.title('Calculator!')
    #calculator.geometry("415x475")
    Lighto.resizable(0, 0)
   # Lighto.configure(width  =  200 , height = 100)
    #Lighto.iconbitmap('')
    
    my_menu = Menu(Lighto)
    Lighto.config(menu = my_menu)
    file_menu = Menu(my_menu, tearoff = False, background = 'black', foreground = 'white',activebackground = '#00E4FF', activeforeground='black')
    my_menu.add_cascade(label = 'Style', background = '#9C25F3', activebackground = 'black',menu = file_menu)
    #my_menu.add_cascade(label = 'Mode', menu = file_menu)

    #file_menu.add_command(label = 'exit' ,command = calculator.quit)


    Variant = Menu(my_menu, tearoff = False, background = 'black', foreground = 'white',activebackground = '#00E4FF', activeforeground='black')
    my_menu.add_cascade(label = 'Variant',background = '#9C25F3', activebackground = 'black',menu = Variant)


    my_menu = Menu(Lighto)
    Lighto.config(menu = my_menu)
    file_menu = Menu(my_menu, tearoff = False, background = 'black', foreground = 'white',activebackground = '#00E4FF', activeforeground='black')
    my_menu.add_cascade(label = 'Style', background = '#9C25F3', activebackground = 'black',menu = file_menu)
    #my_menu.add_cascade(label = 'Mode', menu = file_menu)
        #file_menu.add_command(label = 'exit' ,command = calculator.quit)

    Variant = Menu(my_menu, tearoff = False, background = 'black', foreground = 'white',activebackground = '#00E4FF', activeforeground='black')
    my_menu.add_cascade(label = 'Variant',background = '#9C25F3', activebackground = 'black',menu = Variant)



    def a():
        file_menu.add_command(label = 'BLACK', command = lambda:[Lighto.destroy(),dark()])

    def b():
            file_menu.add_command(label = 'LIGHT')
    #def quit():
    #    global calculator
    #   calculator.quit()
    a()
    b()
    #file_menu.add_command(label = 'BLACK')
    #b()
    #file_menu.add_command(label = 'LIGHT')
    Variant.add_command(label = 'Standard', command = lambda:[light])
    Variant.add_command(label = 'Scientific',command = lambda:[Lighto.destroy() , scientificl()] )



    frame=Frame(Lighto)
    frame.configure(background='white')
    frame.grid(row=0, column=0, columnspan=6, padx=0, pady=0)

    enter2=Entry(frame, width=23, borderwidth=0, font=('Comic San MS',25))
    enter2.configure(justify=RIGHT)
    enter2.configure(bg='white')
    enter2.configure(fg='black')
    enter2.grid(row=0, column=0, columnspan=5, padx=0, pady=0, ipady=8)

    enter=Entry(frame, width=12, borderwidth=0, font=('Comic San MS',45))
    enter.configure(justify=RIGHT)
    enter.configure(bg='white')
    enter.configure(fg='black')
    enter.grid(row=1, column=0, columnspan=5, padx=0, pady=0, ipady=15)



    def buttonClick(number):
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0, str(current) + str(number))

    def dot():
        current=enter.get()
        enter.delete(0,END)
        enter.insert(0, str(current) + '.')

    def add():
        firstNumberStr=enter.get()
        global firstNumber
        global math
        math='add'
        firstNumber= float(firstNumberStr)
        enter.delete(0,END)

    def subtract():
        firstNumberStr=enter.get()
        global firstNumber
        global math
        math='subtract'
        firstNumber= float(firstNumberStr)
        enter.delete(0,END)

    def multiply():
        firstNumberStr=enter.get()
        global firstNumber
        global math
        math='multiply'
        firstNumber= float(firstNumberStr)
        enter.delete(0,END)

    def divide():
        firstNumberStr=enter.get()
        global firstNumber
        global math
        math='divide'
        firstNumber= float(firstNumberStr)
        enter.delete(0,END)

    def clear():
        enter.delete(0,END)
        enter2.delete(0,END)

    def equal():
        secondNumber=enter.get()
        enter.delete(0,END)

        if math =='add':

            global firstNumber

            firstNumberString = str(firstNumber)
            firstNumberLength = len(firstNumberString)
            if firstNumberString[firstNumberLength-2:] == '.0':
                firstNumber = int(firstNumberString[:firstNumberLength-2])

            entryEquation = enter2.get()
            if len(entryEquation) > 0:
                equation = f' + {secondNumber} '
                enter2.insert(END, equation)
            if len(entryEquation) == 0:
                equation = f'{firstNumber} + {secondNumber}'
                enter2.insert(0, equation)

            result = firstNumber + float(secondNumber)
            resultString = str(result)
            length = len(resultString)
            if resultString[length-2:] == '.0':
                result = int(resultString[:length-2])

            enter.insert(0,result)
    
        if math =='subtract':
            
            #global firstNumber

            firstNumberString = str(firstNumber)
            firstNumberLength = len(firstNumberString)
            if firstNumberString[firstNumberLength-2:] == '.0':
                firstNumber = int(firstNumberString[:firstNumberLength-2])

            entryEquation = enter2.get()
            if len(entryEquation) > 0:
                equation = f' - {secondNumber} '
                enter2.insert(END, equation)
            if len(entryEquation) == 0:
                equation = f'{firstNumber} - {secondNumber}'
                enter2.insert(0, equation)

            result = firstNumber - float(secondNumber)
            resultString = str(result)
            length = len(resultString)
            if resultString[length-2:] == '.0':
                result = int(resultString[:length-2])

            enter.insert(0,result)

        if math =='multiply':
            
            #global firstNumber

            firstNumberString = str(firstNumber)
            firstNumberLength = len(firstNumberString)
            if firstNumberString[firstNumberLength-2:] == '.0':
                firstNumber = int(firstNumberString[:firstNumberLength-2])

            entryEquation = enter2.get()
            if len(entryEquation) > 0:
                equation = f' x {secondNumber} '
                enter2.insert(END, equation)
            if len(entryEquation) == 0:
                equation = f'{firstNumber} x {secondNumber}'
                enter2.insert(0, equation)

            result = firstNumber * float(secondNumber)
            resultString = str(result)
            length = len(resultString)
            if resultString[length-2:] == '.0':
                result = int(resultString[:length-2])

            enter.insert(0,result)

        if math =='divide':
            
            #global firstNumber

            firstNumberString = str(firstNumber)
            firstNumberLength = len(firstNumberString)
            if firstNumberString[firstNumberLength-2:] == '.0':
                firstNumber = int(firstNumberString[:firstNumberLength-2])

            entryEquation = enter2.get()
            if len(entryEquation) > 0:
                equation = f' / {secondNumber} '
                enter2.insert(END, equation)
            if len(entryEquation) == 0:
                equation = f'{firstNumber} / {secondNumber}'
                enter2.insert(0, equation)

            result = firstNumber / float(secondNumber)
            resultString = str(result)
            length = len(resultString)
            if resultString[length-2:] == '.0':
                result = int(resultString[:length-2])

            enter.insert(0,result)

    def delete():
        current=len(enter.get())
        last = current - 1
        enter.delete(last,END)

    def percent():
        firstNumber=float(enter.get())
        enter.delete(0,END)
        enter.insert(0,firstNumber / 100 )

    def plusMinus():
        current=enter.get()
        plus = current[0:1]
        
        if plus == '0' or plus == '1' or plus == '2' or plus == '3' or plus == '4' or plus == '5' or plus == '6' or plus == '7' or plus == '8' or plus == '9':  
            enter.insert(0,'-')
        else:
            enter.delete(0,1)
    



    one=Button(frame,text=" 1 ",padx=15,pady=15, borderwidth = 0, command=lambda:buttonClick(1))
    one.grid(row=4,column=0)
    one.configure(bg='white',fg='black', font=('Comic San MS',20))

    two=Button(frame, text=" 2 ", padx=15,pady=15, borderwidth = 0, command=lambda:buttonClick(2))
    two.grid(row=4,column=1)
    two.configure(bg='white',fg='black', font=('Comic San MS',20))

    three=Button(frame, text=" 3 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(3))
    three.grid(row=4,column=2)
    three.configure(bg='white',fg='black', font=('Comic San MS',20))

    four=Button(frame, text=" 4 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(4))
    four.grid(row=3,column=0)
    four.configure(bg='white',fg='black', font=('Comic San MS',20))

    five=Button(frame, text=" 5 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(5))
    five.grid(row=3,column=1)
    five.configure(bg='white',fg='black', font=('Comic San MS',20))

    six=Button(frame, text=" 6 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(6))
    six.grid(row=3,column=2)
    six.configure(bg='white',fg='black', font=('Comic San MS',20))

    seven=Button(frame, text=" 7 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(7))
    seven.grid(row=2,column=0)
    seven.configure(bg='white',fg='black', font=('Comic San MS',20))

    eight=Button(frame, text=" 8 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(8))
    eight.grid(row=2,column=1)
    eight.configure(bg='white',fg='black', font=('Comic San MS',20))

    nine=Button(frame, text=" 9 ",padx=15,pady=15, borderwidth = 0,command=lambda:buttonClick(9))
    nine.grid(row=2,column=2)
    nine.configure(bg='white',fg='black', font=('Comic San MS',20))

    zero=Button(frame, text=" 0 ",padx=15,pady=15,borderwidth = 0, command=lambda:buttonClick(0))
    zero.grid(row=5,column=0)
    zero.configure(bg='white',fg='black', font=('Comic San MS',20))

    dot=Button(frame, text=" . ",padx=18,pady=15,borderwidth = 0,command=dot)
    dot.grid(row=5,column=2)
    dot.configure(bg='white',fg='black', font=('Comic San MS',20))

    add=Button(frame, text=" + ",padx=14,pady=15,borderwidth = 0, command=add)
    add.grid(row=5,column=3)
    add.configure(bg='white',fg='black', font=('Comic San MS',20))

    subtract=Button(frame, text=" - ",padx=18,pady=15,borderwidth = 0, command=subtract)
    subtract.grid(row=4,column=3)
    subtract.configure(bg='white',fg='black', font=('Comic San MS',20))

    multiply=Button(frame, text=" x ",padx=17,pady=15,borderwidth = 0,command=multiply)
    multiply.grid(row=3,column=3)
    multiply.configure(bg='white',fg='black', font=('Comic San MS',20))

    divide=Button(frame, text=" / ",padx=18,pady=15,borderwidth = 0,command=divide)
    divide.grid(row=3,column=4)
    divide.configure(bg='white',fg='black', font=('Comic San MS',20))

    equalto=Button(frame, text=" = ",padx=18,pady=15,borderwidth = 0,command=equal)
    equalto.grid(row=5,column=4)
    equalto.configure(bg='white',fg='black', font=('Comic San MS',20))

    percent=Button(frame, text=" % ",padx=17,pady=15,borderwidth = 0,command=percent)
    percent.grid(row=4,column=4)
    percent.configure(bg='white',fg='black', font=('Comic San MS',20))

    clear=Button(frame, text="AC",padx=17,pady=15,borderwidth = 0,command=clear)
    clear.grid(row=2,column=4)
    clear.configure(bg='white',fg='black', font=('Comic San MS',20))

    delete=Button(frame, text=" C ",padx=16,pady=15,borderwidth = 0,command=delete)
    delete.grid(row=2,column=3)
    delete.configure(bg='white',fg='black', font=('Comic San MS',20))

    plusMinus=Button(frame, text=" ± ",padx=15,pady=15,borderwidth = 0,command=plusMinus)
    plusMinus.grid(row=5,column=1)
    plusMinus.configure(bg='white',fg='black', font=('Comic San MS',20))

    def enterOne(e):
        one['background'] = 'darkslategrey'

    def leaveOne(e):
        one['background'] = 'white'

    one.bind("<Enter>", enterOne)
    one.bind("<Leave>", leaveOne)

    def enterTwo(e):
        two['background'] = 'darkslategrey'

    def leaveTwo(e):
        two['background'] = 'white'

    two.bind("<Enter>", enterTwo)
    two.bind("<Leave>", leaveTwo)

    def enterThree(e):
        three['background'] = 'darkslategrey'

    def leaveThree(e):
        three['background'] = 'white'

    three.bind("<Enter>", enterThree)
    three.bind("<Leave>", leaveThree)

    def enterFour(e):
        four['background'] = 'darkslategrey'

    def leaveFour(e):
        four['background'] = 'white'

    four.bind("<Enter>", enterFour)
    four.bind("<Leave>", leaveFour)

    def enterFive(e):
        five['background'] = 'darkslategrey'

    def leaveFive(e):
        five['background'] = 'white'

    five.bind("<Enter>", enterFive)
    five.bind("<Leave>", leaveFive)

    def enterSix(e):
        six['background'] = 'darkslategrey'

    def leaveSix(e):
        six['background'] = 'white'

    six.bind("<Enter>", enterSix) 
    six.bind("<Leave>", leaveSix)

    def enterSeven(e):
        seven['background'] = 'darkslategrey'

    def leaveSeven(e):
        seven['background'] = 'white'

    seven.bind("<Enter>", enterSeven)
    seven.bind("<Leave>", leaveSeven)

    def enterEight(e):
        eight['background'] = 'darkslategrey'

    def leaveEight(e):
        eight['background'] = 'white'

    eight.bind("<Enter>", enterEight)
    eight.bind("<Leave>", leaveEight)

    def enterNine(e):
        nine['background'] = 'darkslategrey'

    def leaveNine(e):
        nine['background'] = 'white'

    nine.bind("<Enter>", enterNine)
    nine.bind("<Leave>", leaveNine)

    def enterZero(e):
        zero['background'] = 'darkslategrey'

    def leaveZero(e):
        zero['background'] = 'white'

    zero.bind("<Enter>", enterZero)
    zero.bind("<Leave>", leaveZero)

    def enterPlusMinus(e):
        plusMinus['background'] = 'darkslategrey'

    def leavePlusMinus(e):
        plusMinus['background'] = 'white'

    plusMinus.bind("<Enter>", enterPlusMinus)
    plusMinus.bind("<Leave>", leavePlusMinus)

    def enterDot(e):
        dot['background'] = 'darkslategrey'

    def leaveDot(e):
        dot['background'] = 'white'

    dot.bind("<Enter>", enterDot)
    dot.bind("<Leave>", leaveDot)

    def enterPlus(e):
        add['background'] = 'darkslategrey'

    def leavePlus(e):
        add['background'] = 'white'

    add.bind("<Enter>", enterPlus)
    add.bind("<Leave>", leavePlus)

    def enterEqualto(e):
        equalto['background'] = 'darkslategrey'

    def leaveEqualto(e):
        equalto['background'] = 'white'

    equalto.bind("<Enter>", enterEqualto)
    equalto.bind("<Leave>", leaveEqualto)

    def enterPercent(e):
        percent['background'] = 'darkslategrey'

    def leavePercent(e):
        percent['background'] = 'white'

    percent.bind("<Enter>", enterPercent)
    percent.bind("<Leave>", leavePercent)

    def enterMinus(e):
        subtract['background'] = 'darkslategrey'

    def leaveMinus(e):
        subtract['background'] = 'white'

    subtract.bind("<Enter>", enterMinus)
    subtract.bind("<Leave>", leaveMinus)

    def enterDivide(e):
        divide['background'] = 'darkslategrey'

    def leaveDivide(e):
        divide['background'] = 'white'

    divide.bind("<Enter>", enterDivide)
    divide.bind("<Leave>", leaveDivide)

    def enterMultiply(e):
        multiply['background'] = 'darkslategrey'

    def leaveMultiply(e):
        multiply['background'] = 'white'

    multiply.bind("<Enter>", enterMultiply)
    multiply.bind("<Leave>", leaveMultiply)

    def enterAC(e):
        clear['background'] = 'darkslategrey'

    def leaveAC(e):
        clear['background'] = 'white'

    clear.bind("<Enter>", enterAC)
    clear.bind("<Leave>", leaveAC)

    def enterDelete(e):
        delete['background'] = 'darkslategrey'

    def leaveDelete(e):
        delete['background'] = 'white'

    delete.bind("<Enter>", enterDelete)
    delete.bind("<Leave>", leaveDelete)


    Lighto.mainloop()


dark()
