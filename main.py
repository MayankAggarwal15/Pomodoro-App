# PROJECT ON POMODORO APP

from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

total_min = 150
work_min = 25
short_break_min = 5
long_break_min = 20
reps = 0
checks = ""
timer = None

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    minutes = int(count / 60)
    seconds = count % 60

    if seconds <= 9:
        seconds = f"0{seconds}"

    if minutes <= 9:
        minutes = f"0{minutes}"

    canvas.itemconfig(timer_text, text=f"{minutes} : {seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:

        global checks

        if reps % 2 != 0:
            checks += "✔"
            check_marks.config(text=checks)

        start_timer()

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():

    global reps
    reps += 1

    count = 0

    work_sec = int(work_min * 60)
    short_break_sec = int(short_break_min * 60)
    long_break_sec = int(long_break_min * 60)

    window.state("normal")
    window.attributes('-topmost', True)

    if reps <= 8:

        if reps == 8:
            count = long_break_sec
            timer_label.config(text="LONG BREAK", fg="violet")
        elif reps % 2 == 0:
            count = short_break_sec
            timer_label.config(text="SHORT BREAK", fg="violet")
        else:
            count = work_sec
            timer_label.config(text="WORK", fg="blue")

        count_down(count)

    else:
        reset_timer()


def reset_timer():

    window.after_cancel(timer)
    timer_label.config(text="TIMER", fg="blue")
    canvas.itemconfig(timer_text, text="00 : 00")
    check_marks.config(text="")

    global reps
    reps = 0

    global checks
    checks = ""

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()

window.title("POMODORO APP")
window.config(padx=100, pady=50, bg="cyan")


canvas = Canvas(width=300, height=300, bg="cyan", highlightthickness=0)
tomato_img = PhotoImage(
    file="tomato.png")
canvas.create_image(150, 150, image=tomato_img)

# In functions related to canvas , we put coordinates according to width and height of canvas , not on the basis of coordinates of screen

timer_text = canvas.create_text(
    150, 170, text="00 : 00", fill="white", font=("Calibri", 40, "bold"))
canvas.grid(row=2, column=2)

timer_label = Label(text="TIMER", font=(
    "Cambria", 50, "bold"), fg="blue", bg="cyan")
timer_label.grid(row=1, column=2)

start_button = Button(text="START", font=("Calibri", 15, "bold"),
                      bd=7, height=1, width=7, bg="cyan", fg="red", command=start_timer)
reset_button = Button(text="RESET", font=("Calibri", 15, "bold"),
                      bd=7, height=1, width=7, bg="cyan", fg="red", command=reset_timer)

start_button.grid(row=3, column=1)
reset_button.grid(row=3, column=3)

check_marks = Label(font=("Calibri", 15, "bold"), fg="green", bg="cyan")
check_marks.grid(row=4, column=2)


window.mainloop()
