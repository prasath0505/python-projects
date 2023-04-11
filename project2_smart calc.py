from tkinter import * #(import everything from tkinter)
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def lcm(a,b):                    #a=2,b=3
    L=a if a>b else b            #L<=6
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L=L+1                     #L=4

def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H=H-1

#extracting num from text
def extract_from_text(text):
    L=[]
    for t in text.split(' '):
        try:
            float(t)
            L.append(float(t))
        except ValueError:
            pass
    return L

def calculate():
    text = textin.get()  # get text
    l = extract_from_text(text)
    if len(l) < 2:
        list.delete(0, END)
        list.insert(END, 'Please enter at least two numbers')
        return
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                r = operations[word.upper()](l[0], l[1])
                list.delete(0, END)
                list.insert(END, r)
            except:
                list.delete(0, END)
                list.insert(END, 'Something went wrong please try again')
            finally:
                break
    else:
        list.delete(0, END)
        list.insert(END, 'Something went wrong please try again')

            
operations={'+':add,'ADD':add,'ADDITION':add,'PLUS':add,'-':sub,'SUBTRACT':sub,'MINUS':sub,'DIFFERENCE':sub,'SUB':sub,'*':mul,'PRODUCT':mul,'MULTIPICATION':mul,'MULTIPY':mul,'DIVSION':div,'/':div,'DIV':div,'DIVIDE':div,
'LCM':lcm,'HCF':hcf,'MOD':mod,'REMAINDER':mod}

       
#create window using tk method
win=Tk()
win.geometry('500x250')
win.title("Smart Calculator")
win.configure(bg="skyblue")

#create label
l1=Label(win,text="Hi,I am  a Smart Calculator",font="Cambria 12 bold",width=25,padx=3) 

#giving label x and y position
l1.place(x=140,y=18)

#create label2
l2=Label(win,text="What can I help You?",font="Cambria 12 bold",width=25,padx=3) 

#giving label2 x and y position
l2.place(x=140,y=85)

#take input from user using textin variable
textin=StringVar()
e1=Entry(win,width=38,textvariable=textin)
e1.place(x=140,y=125)

#create button
b1=Button(win,text='Get Result',font='Cambria 12 bold', command=calculate)
b1.place(x=220,y=160)

#create list box to display result
list=Listbox(win,width=40,height=2)
list.place(x=140,y=200)

win.mainloop()#run mainloop
