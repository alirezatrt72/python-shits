import tkinter as tk
import random
t = tk.Tk()
t.title('Guess!')
la=1 #lowest number for alireza's guess
ba=100 #highest number for alireza's guess
ng=0 #user guesses
ag=1 #alireza guesses
r = random.randint(la, ba)
def ugoption():
    btna.pack_forget()
    btnu.pack_forget()
    label.config(text=f"Guess\nGuesses: {ng}")
    entry.pack()
    btnsend.pack()
def ugcheck():
    global ng , r
    try:
        i = int(entry.get())
        entry.delete(0, tk.END)
    except ValueError:
        label.config(text="Please enter a valid number.")
        entry.delete(0, tk.END)
        return
    if not (1 <= i <= 100):
        label.config(text="Please enter a number between 1 and 100.")
        return
    if i == r:
        entry.pack_forget()
        btnsend.pack_forget()
        ng+=1
        label.config(text=(f'you won with {ng} guesses'))
        btn_again.pack()
    elif i > r:
        ng += 1
        label.config(text=f"It's lower\nGuesses: {ng}")
    else:
        ng += 1
        label.config(text=f"It's higher\nGuesses: {ng}")
def agoption():
    global la , ba , r
    btna.pack_forget()
    btnu.pack_forget()
    r = (la + ba) // 2
    label.config(text=f"Your number is {r}?\nGuesses: {ag}")
    btn_low.pack()
    btn_high.pack()
    btn_correct.pack()
def lower():
    global la, ba, r, ag
    ag += 1
    ba = r - 1
    if la > ba:
        label.config(text="You gave inconsistent answers!")
        btn_low.pack_forget()
        btn_high.pack_forget()
        btn_correct.pack_forget()
        btn_again.pack()
        return
    r = (la + ba) // 2
    label.config(text=f"Your number is {r}?\nGuesses: {ag}")
def higher():
    global la, ba, r, ag
    ag += 1
    la = r + 1
    if la > ba:
        label.config(text="You gave inconsistent answers!")
        btn_low.pack_forget()
        btn_high.pack_forget()
        btn_correct.pack_forget()
        btn_again.pack()
        return
    r = (la + ba) // 2
    label.config(text=f"Your number is {r}?\nGuesses: {ag}")
def correct():
    label.config(text=(f'yipeeeeeeeee , i won with {ag} guesses'))
    btn_low.pack_forget()
    btn_high.pack_forget()
    btn_correct.pack_forget()
    btn_again.pack()
def restart():
    global la, ba, ng, ag, r
    la = 1
    ba = 100
    ng = 0
    ag = 1
    r = random.randint(la, ba)
    label.config(text='choose')
    btn_again.pack_forget()
    btna.pack()
    btnu.pack()
    entry.pack_forget()
    btnsend.pack_forget()
    btn_low.pack_forget()
    btn_high.pack_forget()
    btn_correct.pack_forget()
    entry.delete(0, tk.END)
    
label = tk.Label(t, text='choose')
label.pack()
btna = tk.Button(t, text='alireza will guess',command=agoption)
btna.pack()
btnu = tk.Button(t, text='user will guess', command=ugoption)
btnu.pack()
entry = tk.Entry(t)
btnsend = tk.Button(t, text='send' , command=ugcheck)
btn_low = tk.Button(t, text='its lower' , command=lower)
btn_high = tk.Button(t, text='its higher' , command=higher)
btn_correct = tk.Button(t, text='you win!' , command=correct)
btn_again = tk.Button(t, text='Click to Play Again', command=restart)
t.mainloop()
