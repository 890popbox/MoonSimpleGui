#Let's try this without stack, just using list.
from tkinter import *
class Sudoku(object):
	def __init__(self):
		self.game = None
		self.visualFrames = []
		self.gameBoard = []
		self.theMsg = None

#Create this class
	def createGame(self):
		self.game = Tk()
		main = self.game
		#Create gameboard
		main.iconbitmap(r'C:\Users\chris\source\repos\PythonApplication3\PythonApplication3\icon.ico')
		main.title('Sudoku-Solver')
		main.geometry('600x420')
		main.config(bg = '#bbbbbb')
		sudokuFRAME = Frame(main,width=600,height=450,bg='#bbbbbb')
		sudokuFRAME.place(x=0,y=0)
		self.visualFrames.append(sudokuFRAME)
		#Create the board..
		self.createBoard()

#Create Sudoku Board (9x9)
	def createBoard(self):
		main = self.game
		blockRow = []
		colours = ['red','green','blue']
		#Create colouring
		for r in range(0,9,3):
			for c in range(0,9,3):
				cblock = Frame(main,width=180,height=100,bg=colours[((r+c)//3)%3])
				cblock.place(x=r*60,y=c*33) #This just took a bit of trail and error..
				self.visualFrames.append(cblock)

		n = 0 #Entry number
		for r in range(0,9):
			blockRow = [] #Just to make sure
			for c in range(0,9):
				#x = 5 if (c+1)%3==0 else 0 (no need for these atm)
				#y = 5 if (r+1)%3==0 else 0
				block = Entry(main,text=str(n),width=5, font=("Calibri 14 bold"))
				block.grid(row=r, column=c,padx = 3,pady=3)
				blockRow.append(block)
				n+=1
			self.gameBoard.append(blockRow)		

		#The buttons..
		solve_ = Button(main,text="solve",width=25, command=lambda:self.checkSolution(self.gameBoard))
		solve_.grid(row=11, column=2,columnspan=5)
		self.visualFrames.append(solve_)
		clean_ = Button(main,text="clear board",width=25, command=lambda:self.clearBoard(self.gameBoard))
		clean_.grid(row=12, column=2,columnspan=5)
		self.visualFrames.append(clean_)


		#The message..
		msg_ = Label(main,text='Enter valid input and I\'ll try solving it!',width=50)
		msg_.grid(row=13, column=0,columnspan=15,ipady=5)
		self.theMsg = msg_

#Yes, this will make time complexity really long, but help with accuracy
	def checkSolution(self,bo):
		ck = True
		for r in range(len(bo)):
			for c in range(len(bo[0])):
				#Make sure it's not None, if None just say that position is valid..
				t = bo[r][c].get()
				ck = True if t=='' else self.valid(bo,(r,c),bo[r][c].get()) #Check if number you put in is valid.. 
				if not ck:
					break
				#The second something isn't, we end this method..
			if not ck:
				break
		#If it's still true, than solve it..
		self.solve(bo) if ck else False
		vd = "Solved the puzzle!" if ck else "Invalid input/can't solve this position, please try again!"
		self.theMsg.config(text=vd)	

# solver.py, (Thanks techwithtim) I understand this but needed ref, it's just recursion and backtracking.. 
#Take's a while to do this properly..

	def solve(self, bo):
		find = self.find_empty(bo) #If we find something, use the row's and cols..
		if find:
			row, col = find
		else: #If we found no free spot, board is solved..
			return True
		#Try numbers 1 to 9..
		for i in range(1,10):
			if self.valid(bo, (row, col), str(i)):
				bo[row][col].insert(0,str(i))

				if self.solve(bo):
					return True
				#Delete it, and then input the zero..
				bo[row][col].delete(0,END)

		return False


	def valid(self, bo, pos, num):
		"""
		Check row, col, box to see if we can put that number here..
		"""

		# Check row, row can't be the number you are searching for, make sure the col is different than original pos
		for i in range(0, len(bo)): 
			if bo[pos[0]][i].get() == num  and pos[1] != i:
				return False

		# Check Col, col can't be the number you are searching for, make sure the row is different than original pos
		for i in range(0, len(bo)):
			if bo[i][pos[1]].get() == num  and pos[0] != i:
				return False

		# Check box
		box_x = pos[1]//3
		box_y = pos[0]//3

		for i in range(box_y*3, box_y*3 + 3):
			for j in range(box_x*3, box_x*3 + 3):
				if bo[i][j].get() == num and (i,j) != pos:
					return False

		return True


	def find_empty(self, bo):
		"""
		Take in the board, and look for a spot that is empty or 0
		"""
		for r in range(len(bo)):
			for c in range(len(bo[0])):
				t = bo[r][c].get()
				if t == '0' or t == '':
					return (r, c) #Return an open position..
		return None


	def print_board(self, bo):
		"""
		prints the board
		:param bo: 2d List of ints
		:return: None
		"""
		for i in range(len(bo)):
			if i % 3 == 0 and i != 0:
				print("- - - - - - - - - - - - - -")
			for j in range(len(bo[0])):
				if j % 3 == 0:
					print(" | ",end="")

				if j == 8:
					print(bo[i][j], end="\n")
				else:
					print(str(bo[i][j]) + " ", end="")

#Clear board..
	def clearBoard(self, bo):
		"""
		Clean board..
		"""
		for r in range(len(bo)):
			for c in range(len(bo[0])):
				bo[r][c].delete(0,END)
		self.theMsg.config(text='Enter valid input and I\'ll try solving it!')	

#Clean frames
	def clearFrames(self):
		for a in self.visualFrames:
			a.destroy()
		self.visualFrames.clear()