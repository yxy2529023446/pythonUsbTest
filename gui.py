from tkinter import *
import sys
import findUsb

def msg_handler(info):
	key = list(info.keys())
	if len(key):
		return '检测到U盘!' + '\n' + key[0] + info[key[0]]
	
"""def func1():
	pass
	
def func2():
	pass"""

if __name__ == '__main__':	
	info = findUsb.usb_info()
	root = Tk()
	root.title('U盘小偷')

	label = Label(root, text=msg_handler(info), pady=12)
	label.pack(expand=YES, fill=BOTH)
	label.config(bg='light green', fg='black')
	label.config(font=('times', 12))

	"""button1 = Button(text='Button1', padx=15, pady=3, command=func1)
	button1.pack(side=LEFT, fill=BOTH, expand=YES)
	button1.config(cursor='hand2')
	button1.config(bd=1, relief=RAISED)
	button1.config(bg='white', fg='blue')
	button1.config(font=('times', 11))

	button2 = Button(text='Button2', padx=15, pady=3, command=func2)
	button2.pack(side=RIGHT, fill=BOTH, expand=YES)
	button2.config(cursor='hand2')
	button2.config(bd=1, relief=RAISED)
	button2.config(bg='white', fg='red')
	button2.config(font=('times', 11))"""

	root.geometry('220x110-200-200')
	root.resizable(False, False)
	root.mainloop()
