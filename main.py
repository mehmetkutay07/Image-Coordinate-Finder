import tkinter as tk
from time import sleep
from threading import Thread

root = tk.Tk()
root.geometry("300x300")

def sayaç():
	zaman = 0
	while zaman < 10000000:
		sleep(1)
		label["text"] = zaman
		zaman += 1


label = tk.Label(root,text="",fg="RED")
label.pack()

root.mainloop()