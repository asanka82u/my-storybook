

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = 0

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_txt , text = "00:00")
    title_lbl.config(text = "Timer")
    global rep
    rep = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global rep

    rep += 1 
    if rep % 8 == 0:
        count_down(LONG_BREAK_MIN*60)
        title_lbl.config(text="Long Break", fg=RED)
    elif rep % 2 == 0:
        count_down(SHORT_BREAK_MIN*60)
        title_lbl.config(text="Short Break", fg=PINK)
    else:
        count_down(WORK_MIN*60)
        title_lbl.config(text="Working time")
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    min = math.floor(count/60)
    sec = count % 60
    if sec < 10:
        canvas.itemconfig(timer_txt, text = f"{min}:0{sec}")
    else:
        canvas.itemconfig(timer_txt, text = f"{min}:{sec}")

    if count> 0:
        timer = window.after(1000, count_down, count- 1)
    else:
        start_timer()
        mark = ''
        work_session = math.floor(rep/2)
        for i in range(work_session):
            mark = "✔"
        check_mark.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=205, height= 224 , bg=YELLOW , highlightthickness=0)

title_lbl = Label(text="Timer", font = (FONT_NAME , 20 , 'bold') ,fg=GREEN, bg=YELLOW)
title_lbl.grid(column=1, row=0)

tomato = PhotoImage(file="tomato.png")
canvas.create_image(103,112,  image=tomato)
timer_txt = canvas.create_text(103,130, text='00:00', fill = 'white' , font = (FONT_NAME,35,'bold'))
canvas.grid(column=1, row=1)


start_btn = Button(text='start', highlightthickness=0 , bg=YELLOW , command=start_timer )
start_btn.grid(column=0, row=2)

reset_btn = Button(text='reset', highlightthickness=0, bg=YELLOW , command=reset_timer)
reset_btn.grid(column=2, row=2)

check_mark = Label(fg= GREEN, bg=YELLOW)
check_mark.grid(column=1, row=3)





window.mainloop()