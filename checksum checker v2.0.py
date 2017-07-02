import tkinter as tk
import tkinter.messagebox

#Setup class for main window

class GUI:
	def __init__(self):
		self.main = tk.Tk()
		
		self.main.title('Checksum Checker v1.0')
		
		#Create frames
	
		self.top = tk.Frame(self.main)
		self.middle = tk.Frame(self.main)
		self.bottom = tk.Frame(self.main)
		self.buttons = tk.Frame(self.main)
		
		#-------------------------------
		
		#Create widgets
			#Text 1
		self.checksum_1 = tk.Label(self.top, text=
		'Checksum #1')
			
			#Entry Box 1
		self.checksum_entry_1 = tk.Entry(self.top,width=70)
		
			#Text 2 
		self.checksum_2 = tk.Label(self.middle, text = 
		'Checksum #2')
		
			#Entry Box 2
		self.checksum_entry_2 = tk.Entry(self.middle, width = 70)
		
		#Pack the widgets into the frame
		
		self.checksum_1.pack(side='left')
		self.checksum_entry_1.pack(side='left')
		self.checksum_2.pack(side='left')
		self.checksum_entry_2.pack(side='left')
		
		#-------------------------------
		
		#Create output placeholder label
		
		self.label_1 = tkinter.Label(self.bottom,text=
		'Result:')
		
		#Convert this label to a dynamic string
		
		self.output = tk.StringVar()
		
		self.label_2 = tk.Label(self.bottom,textvariable=self.output)
		
		#Pack bottom frame widgets
		
		self.label_1.pack(side='left')
		self.label_2.pack(side='left')
		
		#---------------------------------
		
		#Create button
		
		self.calc_button = tk.Button(self.buttons,text='Compare',
		command=self.convert)
		
		#Create a second button to quit
		
		self.leave = tk.Button(self.buttons,text='Quit',command=
		self.main.destroy)
		
		#Pack the button
		
		self.calc_button.pack(side='left')
		self.leave.pack(side='left')
		
		#Pack the frames into the program
		
		self.top.pack()
		self.middle.pack()
		self.bottom.pack()
		self.buttons.pack()
		
		#Run the mainloop
		
		tkinter.mainloop()
		
	def convert(self):
		
		#Getting input from entry boxes entry box

		
		first_entry = str(self.checksum_entry_1.get())
		second_entry = str(self.checksum_entry_2.get())
		
		if first_entry.strip() == second_entry.strip():
			
		#Send the text message to output
		
			self.output.set('Success! Checksums match')
			
		else:
			
			self.output.set('Checksums did not match.')
		
gui = GUI()
