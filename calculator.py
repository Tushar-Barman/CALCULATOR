import tkinter as tk
root=tk.Tk()
root.geometry('500x400')
root.title("CALCULATOR")
c=1
acum=[]
res=""
#output screen 
new=tk.Frame(root)
new.grid(row=0,column=0,columnspan=3)

screen = tk.Entry(new,width=30, font=("Arial", 15))
screen.grid(row=0, column=0, columnspan=3)
def backspace():
    global res
    global acum
    curr=screen.get()
    if acum!=[]:

        if acum[-1] in "+-/*" and res=="":
            screen.delete(len(curr)-1,tk.END)
            acum.pop()
        elif acum[-1] in "+-/*" and res!="":
            screen.delete(len(curr)-1,tk.END)
            res=res[:-1]
        elif acum[-1] not in "+-/*" :
            screen.delete(len(curr)-1,tk.END)
            res=acum.pop()[:-1]
            acum.append(res)
    else:
        screen.delete(len(curr)-1,tk.END)
        res=res[:-1]

def append(inp):
    global res
    global acum
    res+=str(inp)
def accum(op):
    global res
    global acum
    if acum!=[] and acum[-1] in "+-/*"  and op!="=" and res=="":
        acum[-1]=op
    else:
        if op=="=":
            acum.append(res)
            result()            
           ## screen.insert(tk.END,op)
        else :
            acum.extend([res,op])
    res=""
def clear():
    global res
    global acum
    res=""
    acum.clear()
    screen.delete(0,tk.END)
def result():
    global acum
    global res
    ans=""
    for i in acum:
        ans=ans+str(i)
    acum.clear()
    val=str(eval(ans))
    acum.append(val)
    res=val
    screen.delete(0,tk.END)
    screen.insert(tk.END,eval(ans))
def show(ch):
    screen.insert(tk.END, ch)

#exit button
top = tk.Frame(root)
top.grid(row=1, column=0, sticky="w")
tk.Button(top, text="EXIT", width=10, height=3,
          bg="red", command=root.destroy).grid(row=0,column=0,sticky="w",padx=5, pady=5)
tk.Button(top,text="<-",width=7,height=3,command=backspace).grid(row=0,column=1,sticky="w",padx=5, pady=5)
# Calculator frame
calc = tk.Frame(root)
calc.grid(row=2, column=0,sticky="w")

for i in range(0,4):
    
    for j in range(0,3):
        
         if i==3:
              if j==0:
                   tk.Button(calc,text=0,height=3,width=5,command=lambda: (append("0"),show("0"))).grid(row=i,column=j,sticky="w",padx=5,pady=5)
              elif j==1:
                   tk.Button(calc,text="=",height=3,width=5,command=lambda :(accum("="))).grid(row=i,column=j,sticky="w",padx=5,pady=5)
              elif j==2:
                   tk.Button(calc,text=".",height=3,width=5,command=lambda: (append("."),show("."))).grid(row=i,column=j,sticky="w",padx=5,pady=5)
         else:
               
               tk.Button(calc,text=c,height=3,width=5,command=lambda x=c :(append(x),show(str(x)))).grid(row=i,column=j,sticky="w",padx=5,pady=5)
               c+=1
tk.Button(top,text="AC",height=3,width=6,command=clear).grid(row=0,column=3,padx=5,pady=5)
tk.Button(calc,text="+",height=3,width=5,command=lambda: (show("+"),accum("+"))).grid(row=0,column=3,padx=5,pady=5)
tk.Button(calc,text="-",height=3,width=5,command=lambda: (show("-"),accum("-"))).grid(row=1,column=3,padx=5,pady=5)
tk.Button(calc,text="*",height=3,width=5,command=lambda: (show("*"),accum("*"))).grid(row=2,column=3,padx=5,pady=5)
tk.Button(calc,text="/",height=3,width=5,command=lambda: (show("/"),accum("/"))).grid(row=3,column=3,padx=5,pady=5)
root.mainloop()