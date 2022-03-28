from math import floor
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .5  # 25
SHORT_BREAK_MIN = 0.1  # 5
LONG_BREAK_MIN = 1.5  # 20
reps = 0
timer = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer
    window.after_cancel(timer)
    # reset to 00:00
    canvas.itemconfig(timer_text, text="00:00")

    # reset timer_label to "timer"
    timer_label.config(text="Timer")

    # reset reps to 0
    global reps
    reps = 0

    # reset checkmarks
    checkmark.configure(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count_down():
    global reps
    reps += 1

    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.configure(text="Long Break")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.configure(text="Short Break")
    else:
        count_down(WORK_MIN * 60)
        timer_label.configure(text="Work")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    marks = ""
    count_min = floor(count / 60)
    count_sec = int(count % 60)

    if count_min >= 0:
        if count_sec < 10:
            canvas.itemconfig(timer_text, text=f"{count_min} : 0{count_sec}")

        else:
            canvas.itemconfig(timer_text, text=f"{count_min} : {count_sec}")

        timer = window.after(1000, count_down, count - 1)
    else:
        start_count_down()
        for _ in range(floor(reps / 2)):
            marks += "✔"
        checkmark.configure(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# create and configure a window
window = Tk()
window.config(width=50, height=40, padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro 2")

# create canvas of image and text
canvas = Canvas(width=400, height=270, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(180, 120, image=tomato_img)
timer_text = canvas.create_text(180, 145, text="00:00", font=(FONT_NAME, 40, "bold"), fill="white")
canvas.grid(row=1, column=1)

# create widgets
timer_label = Label()
timer_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "normal"))
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", fg=GREEN, font=(FONT_NAME, 20, "normal"), highlightcolor=YELLOW,
                      highlightbackground="white", command=start_count_down)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", fg=RED, font=(FONT_NAME, 20, "normal"), highlightcolor=YELLOW,
                      highlightbackground="white", command=reset_timer)
reset_button.grid(row=2, column=2)

checkmark = Label(bg=YELLOW, fg=GREEN)
checkmark.grid(row=3, column=1)

window.mainloop()
