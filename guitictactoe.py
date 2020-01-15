from tkinter import *
#https://github.com/abhishek305/ProgrammingKnowlegde-Tkinter-Series/blob/master/11th/my%20tic%20tac%202.py
#(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7) Zmagovalne kombinacije
root = Tk()

root.title("Tic Tac Toe")
root.config(background='Dark gray')

        poteza = True
poteza = True

stevec=0

zmaga=False

def btnClick(button):
    global poteza, stevec
    if button['text'] == ' ' and poteza == True and zmaga == False:
        button['text'] = 'X'
        poteza=False
        stevec+=1
    elif button['text'] == ' ' and poteza == False and zmaga == False:
        button['text'] = 'O'
        stevec += 1


gumb1 = Button(root, text=" ", bg='gray', height=4, width=8, command=lambda: btnClick(gumb1))
gumb1.grid(row=1, column=0)
gumb2 = Button(root, text=" ", bg='gray', height=4, width=8, command=lambda: btnClick(gumb2))
gumb2.grid(row=1, column=1)
gumb3 = Button(root, text=" ", bg='gray', height=4, width=8, command=lambda: btnClick(gumb3))
gumb3.grid(row=1, column=2)
gumb4 = Button(root, text=" ", bg='gray', height=4, width=8, command=lambda: btnClick(gumb4))
gumb4.grid(row=2, column=0)
gumb5 = Button(root, text=" ", bg='gray', height=4, width=8, command=lambda: btnClick(gumb5))
gumb5.grid(row=2, column=1)
gumb6 = Button(root, text=" ", bg='gray', height=4, width=8, command=lambda: btnClick(gumb6))
gumb6.grid(row=2, column=2)
gumb7 = Button(root, text=" ", bg='gray', height=4, width=8, command=lambda: btnClick(gumb7))
gumb7.grid(row=3, column=0)
gumb8 = Button(root, text=" ", bg='gray', height=4, width=8, command=lambda: btnClick(gumb8))
gumb8.grid(row=3, column=1)
gumb9 = Button(root, text=" ", bg='gray', height=4, width=8, command=lambda: btnClick(gumb9))
gumb9.grid(row=3, column=2)


root.mainloop()