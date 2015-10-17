#!/usr/bin/python

from counter import PlayerTimer
import tkinter
from builtins import int

top = tkinter.Tk()
difficulty = 'easy'
window = None
numberOfPlayers = 0
label = tkinter.Label()
v = tkinter.StringVar()
currentPlayer = 1
buttonPushed = 0
pause = 0
t = None

totalTimeP1 = 0
totalTimeP2 = 0
totalTimeP3 = 0
totalTimeP4 = 0


p1 = tkinter.StringVar()
p2 = tkinter.StringVar()
p3 = tkinter.StringVar()
p4 = tkinter.StringVar()

c1 = tkinter.StringVar()
c2 = tkinter.StringVar()
c3 = tkinter.StringVar()
c4 = tkinter.StringVar()

c11 = tkinter.StringVar()
c22 = tkinter.StringVar()
c33 = tkinter.StringVar()
c44 = tkinter.StringVar()

def setDifficulty(d):
    global difficulty
    global window
    global v
    difficulty = d
    print (difficulty)
    v.set(difficulty)

def killWindow():
    global window
    window.destroy()
    
def setPlayersf(num):
    global numberOfPlayers
    global v
    global t
    global difficulty
    t = PlayerTimer(difficulty, num)
    numberOfPlayers = num
    v.set(numberOfPlayers)
    addPlayerClocks()

def addPlayerClocks():
    global top
    global numberOfPlayers
    if numberOfPlayers == 2:
        p1.set("Player One")
        p2.set("Player Two")
        tkinter.Label(top, textvariable=p1).pack()
        tkinter.Label(top, textvariable=p2).pack()

def runDifficultyWindow():
    global window
    global difficulty
    global v
    window = tkinter.Toplevel(top)
    v.set(difficulty)
    tkinter.Label(window, textvariable=v).pack()
    e = tkinter.Button(window, bg='blue', height=(1), width=(30), text="Easy", command=lambda : setDifficulty('easy'))
    m = tkinter.Button(window, bg='orange', height=(1), width=(30), text="Medium", command=lambda : setDifficulty('medium'))
    h = tkinter.Button(window, bg='red', height=(1), width=(30), text="Hard", command=lambda : setDifficulty('hard'))
    d = tkinter.Button(window, bg='red', height=(1), width=(30), text="Submit Choice", command=killWindow)
    e.pack(ipadx=10, ipady=3)
    m.pack(ipadx=10, ipady=3)
    h.pack(ipadx=10, ipady=3)
    d.pack(ipadx=10, ipady=3)

def setPlayers():
    global window
    global v
    global numberOfPlayers
    window = tkinter.Toplevel(top)
    v.set(numberOfPlayers)
    tkinter.Label(window, textvariable=v).pack()
    e = tkinter.Button(window, bg='blue', height=(1), width=(30), text="2", command=lambda : setPlayersf(2))
    f = tkinter.Button(window, bg='red', height=(1), width=(30), text="3", command=lambda : setPlayersf(3))
    g = tkinter.Button(window, bg='yellow', height=(1), width=(30), text="4", command=lambda : setPlayersf(4))
    d = tkinter.Button(window, bg='red', height=(1), width=(30), text="Submit Choice", command=killWindow)
    e.pack(ipadx=10, ipady=3)
    f.pack(ipadx=10, ipady=3)
    g.pack(ipadx=10, ipady=3)
    d.pack(ipadx=10, ipady=3)

def start():
    global currentPlayer
    global t
    global totalTimeP1
    global totalTimeP2
    global totalTimeP3
    global totalTimeP4
    global buttonPushed
    global pause
    counter = 0

    while 1:
        # reset the clock point
        if counter == 0:
            t.takeInput('stop', currentPlayer)
        t.takeInput('go', currentPlayer)
        if(buttonPushed == 1):
            t.takeInput('stop', currentPlayer)
            if (currentPlayer == 1):
                totalTimeP1 = totalTimeP1 + float(t.getTimer(currentPlayer))
                c11.set(totalTimeP1)
                t.storeTotalTime(1, totalTimeP1)
            elif currentPlayer == 2:
                totalTimeP2 = totalTimeP2 + float(t.getTimer(currentPlayer))
                c22.set(totalTimeP2)
                t.storeTotalTime(2, totalTimeP2)
            elif currentPlayer == 3:
                totalTimeP3 = totalTimeP3 + float(t.getTimer(currentPlayer))
                c33.set(totalTimeP3)
                t.storeTotalTime(3, totalTimeP3)
            elif currentPlayer == 4:
                totalTimeP4 = totalTimeP4 + float(t.getTimer(currentPlayer))
                c44.set(totalTimeP4)
                t.storeTotalTime(4, totalTimeP4)
            if currentPlayer == numberOfPlayers:
                currentPlayer = 1
            else:
                currentPlayer += 1
            counter = 0
            buttonPushed = 0

        if (pause == 1):
            pause = 0
            break

        if (currentPlayer == 1):
            c1.set(t.getTimer(currentPlayer))
        elif (currentPlayer == 2):
            c2.set(t.getTimer(currentPlayer))
        elif (currentPlayer == 3):
            c3.set(t.getTimer(currentPlayer))
        elif (currentPlayer == 4):
            c4.set(t.getTimer(currentPlayer))
        counter += 1
        top.update()

def pause():
    global pause
    pause = 1

def pushButton():
    global buttonPushed
    buttonPushed = 1

def main():
    global difficulty
    global numberOfPlayers
    global top
    global buttonPushed

    w, h = top.winfo_screenwidth(), top.winfo_screenheight()
    top.geometry("%dx%d+0+0" % (w, h))

    menubar = tkinter.Menu(top)
    menu = tkinter.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Control Center", menu=menu)
    menu.add_command(label="Difficulty", command=runDifficultyWindow)
    menu.add_command(label="Players", command=setPlayers)
    menu.add_command(label="Start!", command=start)
    menu.add_command(label="Pause", command=pause)
    top.config(menu=menubar)
    
    p1.set("Player One")
    p2.set("Player Two")
    p3.set("Player Three")
    p4.set("Player Four")
    c1.set("0.0")
    c2.set("0.0")
    c3.set("0.0")
    c4.set("0.0")
    c11.set("0.0")
    c22.set("0.0")
    c33.set("0.0")
    c44.set("0.0")
    tkinter.Label(top, textvariable=p1).place(x = 20, y = 10)
    tkinter.Label(top, textvariable=c1).place(x = 20, y = 60)
    tkinter.Label(top, text="Total: ").place(x = 20, y = 110)
    tkinter.Label(top, textvariable=c11).place(x = 20, y = 160)

    tkinter.Label(top, textvariable=p2).place(x = w - 175, y = 10)
    tkinter.Label(top, textvariable=c2).place(x = w - 175, y = 60)
    tkinter.Label(top, text="Total: ").place(x = w - 175, y = 110)
    tkinter.Label(top, textvariable=c22).place(x = w - 175, y = 160)

    tkinter.Label(top, textvariable=p3).place(x = 20, y = h - 275)
    tkinter.Label(top, textvariable=c3).place(x = 20, y = h - 225)
    tkinter.Label(top, text="Total: ").place(x = 20, y = h - 175)
    tkinter.Label(top, textvariable=c33).place(x = 20, y = h - 125)

    tkinter.Label(top, textvariable=p4).place(x = w - 175, y = h - 275)
    tkinter.Label(top, textvariable=c4).place(x = w - 175, y = h - 225)
    tkinter.Label(top, text="Total: ").place(x = w - 175, y = h - 175)
    tkinter.Label(top, textvariable=c44).place(x = w - 175, y = h - 125)

    b = tkinter.Button(top, bg='blue', height=(10), width=(30), text="End Turn!", command=pushButton)

    b.place(x=7, y=5)
    b.pack(ipadx=10, ipady=300)
    top.mainloop()
    
if __name__=='__main__':main()    