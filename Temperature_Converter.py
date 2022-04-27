from tkinter import *

root=Tk()
root.title("Jordon's Temperature Converter")
root.geometry("400x500")


def convertF():
    F =int(y.get())
    C= ( F - 32) * 5/9
    label.config(text=C)
    
Label(root, text="Enter Fahrenheit here", font=("Calibri 12")).pack()
y=Entry(root, width=35)
y.pack()

converted=Label(root, text="Temperature in Celsius", font = ("Calibri 15"))
converted.pack(pady=20)

label=Label(root,text ="Total", font=("Calibri 15"))
label.pack(pady=20)

Button(root,text="Convert Fahrenheit", padx=10, pady=5,command=convertF).pack()


def convertC():
    C =int(x.get())
    F= ( C * 9/5) + 32
    label2.config(text=F)
    
Label(root, text="Enter Celcius here", font=("Calibri 12")).pack()
x=Entry(root, width=35)
x.pack()

converted2=Label(root, text="Temperature in Fahrenheit", font = ("Calibri 15"))
converted2.pack(pady=20)

label2=Label(root,text ="Total", font=("Calibri 15"))
label2.pack(pady=20)

Button(root,text="Convert Celsius", padx=10, pady=5,command=convertC).pack()

root.mainloop()
