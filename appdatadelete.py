from tkinter import *
import  os
import shutil

root = Tk()
root.title('Delete')
root.geometry("400x200")
root.configure(bg= '#000000')


def bt_dlt():

    path = os.path.abspath(str(tb.get()))
    dlt = shutil.rmtree(path)
    tb.delete(0, END)




lbl1 = Label(root, bg='#000000', fg='#ad0000', text="EX : C:\\Users\\Mihai-PC\\PycharmProjects\\App\\New folder")
lbl1.pack()
lbl = Label(root,bg='#000000', fg='#ffffff', text="Path: ")
lbl.pack()


tb = Entry(root, width=50)
tb.pack(padx=10, pady=20)


bt_dlt = Button(root, text="DELETE FOLDER", padx=41, pady=20, bg='#00FFCE', command= bt_dlt)
bt_dlt.pack()



root.mainloop()
