from tkinter import *
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_command():
    duration = 1000  # milliseconds
    freq = 440  # Hz
    global reps
    if reps>7 and reps%7==0:
        text["text"] = "Break"
        text.config(fg=RED)
        winsound.PlaySound("break_speech.wav", winsound.SND_FILENAME)
        count_down(LONG_BREAK_MIN*60)
    elif reps%2 ==0:
        text.config(fg=GREEN)
        text["text"] = "Work"
        winsound.PlaySound("work_speech.wav", winsound.SND_FILENAME)
        count_down(WORK_MIN*60)
    else:
        winsound.PlaySound("break_speech.wav", winsound.SND_FILENAME)
        text.config(fg=PINK)
        text["text"] = "Break"
        count_down(SHORT_BREAK_MIN*60)
    # count_down(5*60)


def reset_command():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    text["text"] = "Timer"
    check["text"] = ""
    global reps
    reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    minute = count//60
    second = count % 60
    minute = str(minute)
    second = str(second)
    if len(minute) < 2:
        minute = "0"+minute
    if len(second) < 2:
        second = "0"+second
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        global reps
        reps += 1
        ch_text = ""
        if reps%3 == 0:
            for _ in range(reps // 2):
                ch_text += "✅"
            check.config(text=ch_text)
        start_command()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

text = Label(fg=GREEN, bg=YELLOW )
text["text"] = "Timer"
text.config(font=(FONT_NAME, 40, "bold"), highlightcolor=YELLOW)
text.grid(column=1, row=0)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img,)
timer_text = canvas.create_text(103, 135, text="00:00", font=(FONT_NAME, 24, "bold"), fill="white")
canvas.grid(column=1, row=1)

start = Button(text="Start", command=start_command)
start.grid(row=2, column=0)

reset = Button(text="Reset", command=reset_command)
reset.grid(row=2, column=2)


check = Label(fg=GREEN, bg=YELLOW)
check.grid(column=1, row=3)
# count_down(5)

window.mainloop()
