# Author: Chris Antes
# Date: 2/16/2020
# Description: To visualize some data
'''
Or you could do this
'''
#Import tkinter to create GUI
from tkinter import *
from tkinter import messagebox
import time
import math
from menu1 import *
#My files
from RPNCalc1 import RPNCalc
from todo1 import ToDo
from sudoku1 import Sudoku
import time
#run the RPN CALC
def runRPN():
	Calculator.createStack()
	Calculator.createCalc()
def runTODO():
	ToDoList.createToDo()
def runSudoku():
	GameBoard.createGame()
def readMe():
	print('Chris was here')
	Calculator.readMe()
#Create the GUI
main = Tk()
main.iconbitmap(r'C:\Users\chris\source\repos\PythonApplication3\PythonApplication3\icon.ico')
#Need full map, create calculator right in main and todolist
Calculator = RPNCalc(main)
GameBoard = Sudoku()
ToDoList = ToDo(main)
main.title('Moon-Gui')
main.geometry('900x600')
main.config(bg = '#bbbbbb')
#Create the array of items
myMenu = Menu()
myMenu.addMenu(runRPN, "1. Use the RPN Calc")
myMenu.addMenu(runTODO, "2. ToDo List")
myMenu.addMenu(runSudoku, "3. Sudoku Solver")
myMenu.addMenu(readMe, "4. Read me")
#Now create them all under list number names
for i,x in enumerate(myMenu.returnMenu()):
	Label(main,text = x.description,font= 'arial 24').grid(row=0+i,column=0)
	Button(main,width=15,height=2, text='Click', bg='light blue', command=x.func).grid(row = 0+i, column = 0+1, padx = 5)
#Creating the reset button
btnRestart = Button(main,text='Go to main', command=lambda:[Calculator.clearFrames(), ToDoList.clearFrames()])
btnRestart.config(width=30)
btnRestart.place(x=350,y=500)
#Hold time
date = Label(main, text= time.asctime(time.localtime(time.time())))
date.config(fg = '#000000', font= 'verdana 12')
date.place(x=0,y=500)
#Self updating time every second (Maybe change to minute?)
def tick():
	time2 = time.strftime('%b %d %Y %H:%M:%S')
	date.config(text=time2)
	date.after(1000, tick)
#Run the main Loop..
tick()
main.mainloop()
#Hmm..
#Cantes(Moon)