from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def restart_clicked():
    global timer, rep
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")
    timer_label.config(text="Timer", fg=GREEN)
    marks_label.config(text="")
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep += 1

    if rep % 8 == 0:
        count_down(60 * LONG_BREAK_MIN)
        timer_label.config(text= "Break", fg=RED)
    elif rep % 2 == 0:
        count_down(60 * SHORT_BREAK_MIN)
        timer_label.config(text= "Break", fg=PINK)
    else:
        count_down(60 * WORK_MIN)
        timer_label.config(text= "Work")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    min_int = count//60
    # sec_int = count - (min_int * 60)
    sec_int = count % 60

    if sec_int < 10:
        sec_int = f"0{sec_int}"
    canvas.itemconfig(timer_text, text=f"{min_int}:{sec_int}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # Make a checkmark be shown every 2 reps
        if rep % 2 == 0:
            check = ""
            check_count = int(rep/2)
            for i in range(check_count):
                check += "✓"
            marks_label.config(text=check)
        start_timer()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My first Pomodoro🍅")
## window background color도 **kw를 통해 config()에서 변경할 수 있다.
window.config(padx= 100, pady= 50, bg=YELLOW)



#canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")
#canvas item- image
canvas.create_image(100, 112, image=tomato_img)
#canvas item- text
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



#timer_label
timer_label = Label(text="Timer", font=(FONT_NAME, 50), bg=YELLOW, fg=GREEN)
timer_label.grid(column= 1, row=0)


#start_button
start_button = Button(text= "Start", command=start_timer, width=1, height=1, highlightthickness=0)
start_button.grid(column=0, row=2)


#restart_button


restart_button = Button(text= "Reset", command=restart_clicked, width=3, height=1, highlightthickness=0)
restart_button.grid(column= 2, row=2)

#check marks label
marks_label = Label(font=(FONT_NAME, 30), fg=GREEN, bg=YELLOW)
marks_label.grid(column=1, row=3)



window.mainloop()