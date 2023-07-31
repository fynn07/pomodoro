import tkinter
import math
from playsound import playsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK = ""
TIMER = None
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
REPS = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global CHECK
    global REPS 
    global RUN
    window.after_cancel(TIMER)
    CHECK = ""
    REPS = 0
    RUN = 0
    playsound("pomodoro/soundeffects/reset.mp3", False)
    timer_label.config(text="TIMER", fg=GREEN)
    checkmark_label.config(text=CHECK)
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    global CHECK
    global RUN
    REPS += 1

    if REPS == 1 or REPS == 3 or REPS == 5 or REPS == 7:
        timer_label.config(text="WORK", fg=GREEN)
        count_down(WORK_MIN * 60)
    elif REPS == 2 or REPS == 4 or REPS == 6:
        CHECK += "✔"
        timer_label.config(text="BREAK", fg=PINK)
        checkmark_label.config(text=CHECK)
        count_down(SHORT_BREAK_MIN * 60)
            
    elif REPS == 8:
        CHECK += "🍅"
        timer_label.config(text="BREAK", fg=RED)
        checkmark_label.config(text=CHECK)
        count_down(LONG_BREAK_MIN * 60)
     
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec  < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count-1)
    else:
        if REPS == 8:
            window.after_cancel(TIMER)
        else:
            playsound('pomodoro/soundeffects/alarm_clock.mp3', False)
            start_timer()
   

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro by Fynn")
window.resizable(False, False)
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = tkinter.PhotoImage(file = 'pomodoro/tomato.png')
canvas.create_image(100, 112, image=tomato_photo)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

timer_label = tkinter.Label(font=(FONT_NAME, 40, "bold"), text="TIMER", fg=GREEN, background=YELLOW, highlightthickness=0)
timer_label.grid(row=0, column=1)

checkmark_label = tkinter.Label(font=(18), fg=GREEN, bg=YELLOW, highlightthickness=0)
checkmark_label.grid(row=3, column=1)

start_button = tkinter.Button(font=("arial"), text="Start", command=start_timer)
start_button.grid(row=2, column=0)

stop_button = tkinter.Button(font=("arial"), text="Reset", command=reset_timer)
stop_button.grid(row=2, column=2)

window.mainloop()