'''
Use the module tkinter to make a graphical program where the user can play
Tic-Tac-Toe against a friend, or against a computer.
The program must
•notice when the game is over;
•know whose turn it is;
•be playable with only a mouse;
•not let anyone do an illegal move.
'''



import tkinter as tk
import tkinter.messagebox
from tkinter.tix import COLUMN

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("300x400")

def Friends():

    root.destroy()
    
    wndo=tk.Tk()
    wndo.title('Tic Tac Toe')
    fm=tk.Frame(master=wndo)
    fm.pack(pady=10)

    lbl=tk.Label(master=fm,text="Tic Tac Toe",font=("Cambria", 20))
    lbl.pack()

    mf = tk.Frame(master=wndo,border=2,relief=tk.SUNKEN,bg='#1bfaaa')
    mf.pack()

    fm1=tk.Frame(master=wndo,borderwidth=2,relief=tk.SUNKEN,bg='blue')
    fm1.pack(padx=10,pady=10)

    btn1=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : btnclick(1))
    btn1.grid(row=0,column=0,padx=5,pady=5)

    btn2=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : btnclick(2))
    btn2.grid(row=0,column=1,padx=5,pady=5)

    btn3=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : btnclick(3))
    btn3.grid(row=0,column=2,padx=5,pady=5)

    btn4=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : btnclick(4))
    btn4.grid(row=1,column=0,padx=5,pady=5)

    btn5=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : btnclick(5))
    btn5.grid(row=1,column=1,padx=5,pady=5)

    btn6=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : btnclick(6))
    btn6.grid(row=1,column=2,padx=5,pady=5)

    btn7=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : btnclick(7))
    btn7.grid(row=2,column=0,padx=5,pady=5)

    btn8=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : btnclick(8))
    btn8.grid(row=2,column=1,padx=5,pady=5)

    btn9=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : btnclick(9))
    btn9.grid(row=2,column=2,padx=5,pady=5)

    fm2=tk.Frame(master=wndo,border=2,relief=tk.SUNKEN,bg='#dadec3')
    fm2.pack()
    lbl1=tk.Label(master=fm2,text="Player 1 --> X\nPlayer 2 --> O",width=10)
    lbl1.grid(row=0,column=0,padx=5)
    btn_restart=tk.Button(master=fm2,text="Restart",width=10,height=3,relief=tk.GROOVE,command=lambda: restartbtn())
    btn_restart.grid(row=0,column=1,padx=10,pady=10)
    lbl2=tk.Label(master=fm2,text='Player-1 Turn',bg="green",width=10,height=3,relief=tk.SUNKEN)
    lbl2.grid(row=0,column=2,padx=5)
    global a,b,c
    a=1
    b=0
    c=0

    def disablebtn():
        btn1['state']=tk.DISABLED
        btn2['state']=tk.DISABLED
        btn3['state']=tk.DISABLED
        btn4['state']=tk.DISABLED
        btn5['state']=tk.DISABLED
        btn6['state']=tk.DISABLED
        btn7['state']=tk.DISABLED
        btn8['state']=tk.DISABLED
        btn9['state']=tk.DISABLED

    def restartbtn():
        global a,b,c
        a=1
        b=0
        c=0
        lbl2['bg']="green"
        lbl2['text']='Player-1 Turn'
        btn1['text']=''
        btn1['bg']='black'
        btn2['text']=''
        btn2['bg']='black'
        btn3['text']=''
        btn3['bg']='black'
        btn4['text']=''
        btn4['bg']='black'
        btn5['text']=''
        btn5['bg']='black'
        btn6['text']=''
        btn6['bg']='black'
        btn7['text']=''
        btn7['bg']='black'
        btn8['text']=''
        btn8['bg']='black'
        btn9['text']=''
        btn9['bg']='black'
        btn1['state']=tk.NORMAL
        btn2['state']=tk.NORMAL
        btn3['state']=tk.NORMAL
        btn4['state']=tk.NORMAL
        btn5['state']=tk.NORMAL
        btn6['state']=tk.NORMAL
        btn7['state']=tk.NORMAL
        btn8['state']=tk.NORMAL
        btn9['state']=tk.NORMAL

    def btnclick(x):
        global a,b,c

        #for player 1
        if(x==1 and a==1 and btn1['text']==''):
            btn1['text']="X"
            btn1['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1
        if(x==2 and a==1 and btn2['text']==''):
            btn2['text']="X"
            btn2['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1
        if(x==3 and a==1 and btn3['text']==''):
            btn3['text']="X"
            btn3['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1
        if(x==4 and a==1 and btn4['text']==''):
            btn4['text']="X"
            btn4['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1
        if(x==5 and a==1 and btn5['text']==''):
            btn5['text']="X"
            btn5['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1
        if(x==6 and a==1 and btn6['text']==''):
            btn6['text']="X"
            btn6['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1
        if(x==7 and a==1 and btn7['text']==''):
            btn7['text']="X"
            btn7['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1
        if(x==8 and a==1 and btn8['text']==''):
            btn8['text']="X"
            btn8['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1
        if(x==9 and a==1 and btn9['text']==''):
            btn9['text']="X"
            btn9['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1

        #for player 2
        if(x==1 and a==0 and btn1['text']==''):
            btn1['text']='O'
            btn1['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Player-1 Turn'
            a=1
            b+=1
        if(x==2 and a==0 and btn2['text']==''):
            btn2['text']='O'
            btn2['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Player-1 Turn'
            a=1
            b+=1
        if(x==3 and a==0 and btn3['text']==''):
            btn3['text']='O'
            btn3['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Player-1 Turn'
            a=1
            b+=1
        if(x==4 and a==0 and btn4['text']==''):
            btn4['text']='O'
            btn4['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Player-1 Turn'
            a=1
            b+=1
        if(x==5 and a==0 and btn5['text']==''):
            btn5['text']='O'
            btn5['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Player-1 Turn'
            a=1
            b+=1
        if(x==6 and a==0 and btn6['text']==''):
            btn6['text']='O'
            btn6['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Player-1 Turn'
            a=1
            b+=1
        if(x==7 and a==0 and btn7['text']==''):
            btn7['text']='O'
            btn7['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Player-1 Turn'
            a=1
            b+=1
        if(x==8 and a==0 and btn8['text']==''):
            btn8['text']='O'
            btn8['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Player-1 Turn'
            a=1
            b+=1
        if(x==9 and a==0 and btn9['text']==''):
            btn9['text']='O'
            btn9['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Player-1 Turn'
            a=1
            b+=1

        #checking winner
        if(btn1['text']=='X' and btn2['text']=='X' and btn3['text']=='X' or
            btn4['text']=='X' and btn5['text']=='X' and btn6['text']=='X' or
            btn7['text']=='X' and btn8['text']=='X' and btn9['text']=='X' or
            btn1['text']=='X' and btn4['text']=='X' and btn7['text']=='X' or
            btn2['text']=='X' and btn5['text']=='X' and btn8['text']=='X' or
            btn3['text']=='X' and btn6['text']=='X' and btn9['text']=='X' or
            btn1['text']=='X' and btn5['text']=='X' and btn9['text']=='X' or
            btn3['text']=='X' and btn5['text']=='X' and btn7['text']=='X'):
                disablebtn()
                c=1
                tkinter.messagebox.showinfo("Tic Tac Toe","Winner is player 1")
        elif( btn1['text']=='O' and btn2['text']=='O' and btn3['text']=='O' or
            btn4['text']=='O' and btn5['text']=='O' and btn6['text']=='O' or
            btn7['text']=='O' and btn8['text']=='O' and btn9['text']=='O' or
            btn1['text']=='O' and btn4['text']=='O' and btn7['text']=='O' or
            btn2['text']=='O' and btn5['text']=='O' and btn8['text']=='O' or
            btn3['text']=='O' and btn6['text']=='O' and btn9['text']=='O' or
            btn1['text']=='O' and btn5['text']=='O' and btn9['text']=='O' or
            btn3['text']=='O' and btn5['text']=='O' and btn7['text']=='O'):
                disablebtn()
                c=1
                tkinter.messagebox.showinfo("Tic Tac Toe","Winner is player 2")
        elif(b==9):
            disablebtn()
            c=1
            tkinter.messagebox.showinfo("Tic Tac Toe","Match is Draw.")

def Computer():

    root.destroy()
    
    wndo=tk.Tk()
    wndo.title('Tic Tac Toe')
    fm=tk.Frame(master=wndo)
    fm.pack(pady=10)

    lbl=tk.Label(master=fm,text="Tic Tac Toe",font=("Cambria", 20))
    lbl.pack()

    mf = tk.Frame(master=wndo,border=2,relief=tk.SUNKEN,bg='#1bfaaa')
    mf.pack()

    fm1=tk.Frame(master=wndo,borderwidth=2,relief=tk.SUNKEN,bg='blue')
    fm1.pack(padx=10,pady=10)

    btn1=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : [btnclick(1), check(1)])
    btn1.grid(row=0,column=0,padx=5,pady=5)

    btn2=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : [btnclick(2), check(2)])
    btn2.grid(row=0,column=1,padx=5,pady=5)

    btn3=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : [btnclick(3), check(3)])
    btn3.grid(row=0,column=2,padx=5,pady=5)

    btn4=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : [btnclick(4), check(4)])
    btn4.grid(row=1,column=0,padx=5,pady=5)

    btn5=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : [btnclick(5), check(5)])
    btn5.grid(row=1,column=1,padx=5,pady=5)

    btn6=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : [btnclick(6), check(6)])
    btn6.grid(row=1,column=2,padx=5,pady=5)

    btn7=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : [btnclick(7), check(7)])
    btn7.grid(row=2,column=0,padx=5,pady=5)

    btn8=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : [btnclick(8), check(8)])
    btn8.grid(row=2,column=1,padx=5,pady=5)

    btn9=tk.Button(master=fm1,text='',width=10,height=5,bg='black',command=lambda : [btnclick(9), check(9)])
    btn9.grid(row=2,column=2,padx=5,pady=5)

    fm2=tk.Frame(master=wndo,border=2,relief=tk.SUNKEN,bg='#dadec3')
    fm2.pack()
    lbl1=tk.Label(master=fm2,text="Your  --> X\nCmptr --> O",width=10)
    lbl1.grid(row=0,column=0,padx=10)
    btn_restart=tk.Button(master=fm2,text="Restart",width=10,height=3,relief=tk.GROOVE,command=lambda: restartbtn())
    btn_restart.grid(row=0,column=1,padx=10,pady=10)
    lbl2=tk.Label(master=fm2,text='Your Turn',bg="green",width=10,height=3,relief=tk.SUNKEN)
    lbl2.grid(row=0,column=2,padx=5)
    global a,b,c
    a=1
    b=0
    c=0

    def disablebtn():
        btn1['state']=tk.DISABLED
        btn2['state']=tk.DISABLED
        btn3['state']=tk.DISABLED
        btn4['state']=tk.DISABLED
        btn5['state']=tk.DISABLED
        btn6['state']=tk.DISABLED
        btn7['state']=tk.DISABLED
        btn8['state']=tk.DISABLED
        btn9['state']=tk.DISABLED

    def restartbtn():
        global a,b,c
        a=1
        b=0
        c=0
        lbl2['bg']="green"
        lbl2['text']='Your Turn'
        btn1['text']=''
        btn1['bg']='black'
        btn2['text']=''
        btn2['bg']='black'
        btn3['text']=''
        btn3['bg']='black'
        btn4['text']=''
        btn4['bg']='black'
        btn5['text']=''
        btn5['bg']='black'
        btn6['text']=''
        btn6['bg']='black'
        btn7['text']=''
        btn7['bg']='black'
        btn8['text']=''
        btn8['bg']='black'
        btn9['text']=''
        btn9['bg']='black'
        btn1['state']=tk.NORMAL
        btn2['state']=tk.NORMAL
        btn3['state']=tk.NORMAL
        btn4['state']=tk.NORMAL
        btn5['state']=tk.NORMAL
        btn6['state']=tk.NORMAL
        btn7['state']=tk.NORMAL
        btn8['state']=tk.NORMAL
        btn9['state']=tk.NORMAL

    def btnclick(x):
        global a,b,c
        #Computer
        
        if(x==1 and a==1 and btn1['text']==''):
            
            btn1['text']="X"
            btn1['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1
            #check()
        if(x==2 and a==1 and btn2['text']==''):
            btn2['text']="X"
            btn2['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1
        if(x==3 and a==1 and btn3['text']==''):
            btn3['text']="X"
            btn3['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1
        if(x==4 and a==1 and btn4['text']==''):
            btn4['text']="X"
            btn4['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1
        if(x==5 and a==1 and btn5['text']==''):
            btn5['text']="X"
            btn5['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1
        if(x==6 and a==1 and btn6['text']==''):
            btn6['text']="X"
            btn6['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1
        if(x==7 and a==1 and btn7['text']==''):
            btn7['text']="X"
            btn7['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1
        if(x==8 and a==1 and btn8['text']==''):
            btn8['text']="X"
            btn8['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1
        if(x==9 and a==1 and btn9['text']==''):
            btn9['text']="X"
            btn9['bg']="green"
            lbl2['bg']="red"
            lbl2['text']='Player-2 Turn'
            a=0
            b+=1

        #for player 2
        if(x==1 and a==0 and btn1['text']==''):
            btn1['text']='O'
            btn1['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Your Turn'
            a=1
            b+=1
        if(x==2 and a==0 and btn2['text']==''):
            btn2['text']='O'
            btn2['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Your Turn'
            a=1
            b+=1
        if(x==3 and a==0 and btn3['text']==''):
            btn3['text']='O'
            btn3['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Your Turn'
            a=1
            b+=1
        if(x==4 and a==0 and btn4['text']==''):
            btn4['text']='O'
            btn4['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Your Turn'
            a=1
            b+=1
        if(x==5 and a==0 and btn5['text']==''):
            btn5['text']='O'
            btn5['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Your Turn'
            a=1
            b+=1
        if(x==6 and a==0 and btn6['text']==''):
            btn6['text']='O'
            btn6['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Your Turn'
            a=1
            b+=1
        if(x==7 and a==0 and btn7['text']==''):
            btn7['text']='O'
            btn7['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Your Turn'
            a=1
            b+=1
        if(x==8 and a==0 and btn8['text']==''):
            btn8['text']='O'
            btn8['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Your Turn'
            a=1
            b+=1
        if(x==9 and a==0 and btn9['text']==''):
            btn9['text']='O'
            btn9['bg']="red"
            lbl2['bg']="green"
            lbl2['text']='Your Turn'
            a=1
            b+=1

        #checking winner
        if(btn1['text']=='X' and btn2['text']=='X' and btn3['text']=='X' or
            btn4['text']=='X' and btn5['text']=='X' and btn6['text']=='X' or
            btn7['text']=='X' and btn8['text']=='X' and btn9['text']=='X' or
            btn1['text']=='X' and btn4['text']=='X' and btn7['text']=='X' or
            btn2['text']=='X' and btn5['text']=='X' and btn8['text']=='X' or
            btn3['text']=='X' and btn6['text']=='X' and btn9['text']=='X' or
            btn1['text']=='X' and btn5['text']=='X' and btn9['text']=='X' or
            btn3['text']=='X' and btn5['text']=='X' and btn7['text']=='X'):
                disablebtn()
                c=1
                tkinter.messagebox.showinfo("Tic Tac Toe","You win the match!")
        elif( btn1['text']=='O' and btn2['text']=='O' and btn3['text']=='O' or
            btn4['text']=='O' and btn5['text']=='O' and btn6['text']=='O' or
            btn7['text']=='O' and btn8['text']=='O' and btn9['text']=='O' or
            btn1['text']=='O' and btn4['text']=='O' and btn7['text']=='O' or
            btn2['text']=='O' and btn5['text']=='O' and btn8['text']=='O' or
            btn3['text']=='O' and btn6['text']=='O' and btn9['text']=='O' or
            btn1['text']=='O' and btn5['text']=='O' and btn9['text']=='O' or
            btn3['text']=='O' and btn5['text']=='O' and btn7['text']=='O'):
                disablebtn()
                c=1
                tkinter.messagebox.showinfo("Tic Tac Toe","Winner is Computer")
        elif(b==9):
            disablebtn()
            c=1
            tkinter.messagebox.showinfo("Tic Tac Toe","Match is Draw.")

    def check(z):
        if(z==1 and a==0):
            btn2.invoke()
        if(z==2 and a==0):
            btn3.invoke()

        if(z==3 and a==0):
            btn4.invoke()
        if(z==4 and a==0):
            btn5.invoke()
        if(z==5 and a==0):
            btn6.invoke()
        if(z==6 and a==0):
            btn7.invoke()
        if(z==7 and a==0):
            btn8.invoke()
        if(z==8 and a==0):
            btn9.invoke()
        if(z==9 and a==0):
            btn1.invoke()

lbl=tk.Label(master=root,text="Tic Tac Toe",font=("Cambria", 20))
lbl.pack()
 
btnm = tk.Button(root,
             text ="Pay with Cumputer",
             command =  Computer)
btnm.pack(pady=10)

btnm1 = tk.Button(root,
             text ="Pay with Friends",
             command =  Friends)
btnm1.pack(pady=10)
    
root.mainloop()