from tkinter import *

root = Tk()
root.title("TicketSales")
root.geometry("400x500")
root.config(bg="#346ab3")
root.resizable(height=False, width=False)


def nextscreen():
    root.destroy()
    import TicketSales


button1 = Button(root, text="Welcome To TicketSales", fg="white", border=4, bg="#9ccb3b", command=nextscreen)
button1.place(x=105, y=230)

root.mainloop()
