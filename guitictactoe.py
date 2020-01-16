from tkinter import *
from tkinter import messagebox
#(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7) Zmagovalne kombinacije
root = Tk()

poteza = True

a= 0

stevec=0

zmaga=False

root.title("Tic Tac Toe")
root.config(background='Dark gray')
root.resizable(0,0)
label1 = Label(text = " d", font='Times 20 bold', height=1, width=12,)
label1.grid(row=0, column=0, columnspan=8)
def stanjeCheck():
    if poteza == True:
        label1.configure(text="X so na potezi.", fg="blue")
    elif poteza == False:
        label1.configure(text="O so na potezi.", fg="red")

stanjeCheck()

def btnClick(button):
    global poteza, stevec
    if button['text'] == ' ' and poteza == True and zmaga == False:
        button['text'] = 'X'
        poteza=False
        stevec+=1
        checkForWin()
        stanjeCheck()
    elif button['text'] == ' ' and poteza == False and zmaga == False:
        button['text'] = 'O'
        stevec += 1
        poteza=True
        checkForWin()
        stanjeCheck()
    elif(zmaga == False and button["text"] != " "):
        messagebox.showinfo("Opozorilo.", "Gumb je že bil kliknjen.")

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

def checkForWin():
    global zmaga,label1
    if (gumb1['text'] == 'X' and gumb2['text'] == 'X' and gumb3['text'] == 'X' or
        gumb4['text'] == 'X' and gumb5['text'] == 'X' and gumb6['text'] == 'X' or
        gumb7['text'] =='X' and gumb8['text'] == 'X' and gumb9['text'] == 'X' or
        gumb1['text'] == 'X' and gumb5['text'] == 'X' and gumb9['text'] == 'X' or
        gumb3['text'] == 'X' and gumb5['text'] == 'X' and gumb7['text'] == 'X' or
        gumb1['text'] == 'X' and gumb2['text'] == 'X' and gumb3['text'] == 'X' or
        gumb1['text'] == 'X' and gumb4['text'] == 'X' and gumb7['text'] == 'X' or
        gumb2['text'] == 'X' and gumb5['text'] == 'X' and gumb8['text'] == 'X' or
        gumb3['text'] == 'X' and gumb6['text'] == 'X' and gumb9['text'] == 'X'):
        zmaga = True
        messagebox.showinfo("Konec", "Križci so zmagali.")
    elif(stevec == 8):
        zmaga = True
        messagebox.showinfo("Konec", "Igralca sta izenačena.")
    elif (gumb1['text'] == 'O' and gumb2['text'] == 'O' and gumb3['text'] == 'O' or
        gumb4['text'] == 'O' and gumb5['text'] == 'O' and gumb6['text'] == 'O' or
        gumb7['text'] =='O' and gumb8['text'] == 'O' and gumb9['text'] == 'O' or
        gumb1['text'] == 'O' and gumb5['text'] == 'O' and gumb9['text'] == 'O' or
        gumb3['text'] == 'O' and gumb5['text'] == 'O' and gumb7['text'] == 'O' or
        gumb1['text'] == 'O' and gumb2['text'] == 'O' and gumb3['text'] == 'O' or
        gumb1['text'] == 'O' and gumb4['text'] == 'O' and gumb7['text'] == 'O' or
        gumb2['text'] == 'O' and gumb5['text'] == 'O' and gumb8['text'] == 'O' or
        gumb3['text'] == 'O' and gumb6['text'] == 'O' and gumb9['text'] == 'O'):
        zmaga = True
        messagebox.showinfo("Konec", "Krogci so zmagali.")


root.mainloop()
