from tkinter import*
def icalc(source, side):
	store0bj = Frame(source, borderwidth=4, bd=4,bg="power yellow")
	store0bj.pack(side=side, expand=YES, fill=BOTH)
	return store0bj

def button(source, side, text, commed=None):
	store0bj = Button(source, text=text, command=command)
	store0bj.pack(side=side, expand=YES, fill=BOTH)
	return store0bj

class app(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.option_add('*Font', 'calibri 20 bold')
		self.pack(expend=YES, fill=BOTH)
		self.master.title('calculator')
		