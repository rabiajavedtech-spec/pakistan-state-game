import turtle
import pandas
import tkinter as tk

screen = turtle.Screen()
screen.title("Pakistan State Game")
screen.setup(width=900, height=600)
image="blank_state_image.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

data = pandas.read_csv("50_state(1).csv")
all_states=data.state.to_list()
guessed_states=[]

# ---------------- CUSTOM INPUT BOX ----------------

def get_answer() -> str | None:
    answer = None

    def ok():
        nonlocal answer
        answer = entry.get()
        window.destroy()

    def cancel():
        nonlocal answer
        answer = None
        window.destroy()

    window = tk.Toplevel(screen.getcanvas().winfo_toplevel())
    window.title(f"{len(guessed_states)}/60 States Correct")

    # width x height + left + top
    window.geometry("300x110+300+200")
    window.resizable(False, False)

    label = tk.Label(window,text="What's another state's name?")
    label.pack(pady=(8, 3))

    entry = tk.Entry(window, width=35)
    entry.pack()

    button_frame = tk.Frame(window)
    button_frame.pack(pady=6)

    ok_button = tk.Button(button_frame,text="OK",width=8,command=ok)
    ok_button.pack(side="left", padx=4)

    cancel_button = tk.Button(button_frame,text="Cancel",width=8,command=cancel)
    cancel_button.pack(side="left", padx=4)

    entry.focus()

    # Enter = OK
    window.bind("<Return>", lambda event: ok())

    # Escape = Cancel
    window.bind("<Escape>", lambda event: cancel())

    window.grab_set()
    window.wait_window()

    return answer

while len(guessed_states) < 60:
    answer_state = get_answer()
    if answer_state is None:
        break

    answer_state = answer_state.title()
    state_data = data[data.state == answer_state]

    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_x = state_data.x.item()
        state_y = state_data.y.item()
        writer.goto(state_x, state_y)
        writer.write(answer_state, align="center", font=("Arial", 8, "normal"))

turtle.mainloop()