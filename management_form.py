import datetime
import os
from tkinter import ttk
import tkinter as tk

ql = tk.Tk()
title = ttk.Label(ql,text="Quản Lý Thống Kê").grid(row=0,column=1)
tab_ctr = ttk.Notebook(ql)
tab1 = ttk.Frame(tab_ctr)
tab2 = ttk.Frame(tab_ctr)
#
day = ttk.Label(tab1,text=datetime.datetime.now())
day.grid(row=1)
import sqlite3

namedatabase =str( datetime.date.today())
def connect(name):
    con1 = sqlite3.connect(name+".db")
    cur1 = con1.cursor()
    cur1.execute("CREATE TABLE IF NOT EXISTS emp(id,  name TEXT, status TEXT)")
    #for i in range(1,6):
    #   cur1.execute("INSERT INTO emp VALUES (?, ?, ?)", (i, "bao Huu", "muon"))
    # cur1.execute("INSERT INTO emp VALUES (?, ?, ?)", (1, "hai dang", "dung gio"))
    # cur1.execute("INSERT INTO emp VALUES (?, ?, ?)", (2, "hong thai", "muon"))
    # cur1.execute("INSERT INTO emp VALUES (?, ?, ?)", (3, "huu bao", "muon"))
    # cur1.execute("INSERT INTO emp VALUES (?, ?, ?)", (4, "tien dat", "dung gio"))
    # cur1.execute("INSERT INTO emp VALUES (?, ?, ?)", (5, "xuan thuong", "dung gio"))
    # cur1.execute("INSERT INTO emp VALUES (?, ?, ?)", (6, "dinh luc", "muon"))
    con1.commit()
    con1.close()


def View():
    con1 = sqlite3.connect("data.db")
    con2 = sqlite3.connect(namedatabase + ".db")
    cur1 = con1.cursor()
    cur2 = con2.cursor()
    cur2.execute("SELECT * FROM emp")
    rows = cur2.fetchall()
    for row in rows:
        tree.insert("", tk.END, values=row)
    con1.close()
    con2.close()

def SecondWD(id):
    sc=tk.Tk()
    var = tk.IntVar()
    def sel():
        selection = "You selected the option " + str(var.get())
        print(selection)
        con1 = sqlite3.connect(namedatabase + ".db")
        if(var.get()==1):
            tt = "vang"
        else: tt = "Du"
        con1.execute(f'UPDATE emp SET status="{tt}" WHERE id={id}')
        for i in tree.get_children():
            tree.delete(i)
        cur2 = con1.cursor()
        cur2.execute("SELECT * FROM emp")
        rows = cur2.fetchall()
        for row in rows:
            tree.insert("", tk.END, values=row)
        con1.commit()
        con1.close()
    ttk.Radiobutton(sc,text="vang",variable=var,value=0,command=sel).grid(row=0,column=1)
    ttk.Radiobutton(sc, text="Du", variable=var, value=1,command=sel).grid(row=1,column=1)
    sc.mainloop()


def selectItem(a):
    trv = tree.selection()[0]
    print(trv)
    curItem = tree.focus()
    print(tree.item(curItem)['values'][0])
    SecondWD(tree.item(curItem)['values'][0])


connect(namedatabase)
tree = ttk.Treeview(tab1, column=("c1", "c2", "c3"), show='headings')
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="Mã Nhân Viên")
tree.column("#2", anchor=tk.CENTER)
tree.heading( "#2", text="Tên Nhân Viên")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="Tình trạng")
tree.grid(row=2)
button =ttk.Button(tab1,text="Sửa thông tin",command=View())
button.grid(row=3)
tab_ctr.add(tab1,text='Ngày')
tab_ctr.add(tab2,text='Tuần')
tab_ctr.grid(row=1,column=1)

tree.bind('<ButtonRelease-1>', selectItem)
ql.mainloop()