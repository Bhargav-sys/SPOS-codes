import tkinter as tk

running = False
counter = 0

def update_time():
    global running, counter

    minutes, seconds = divmod(counter, 6000)
    seconds, hundredths = divmod(seconds, 100)

    time_string = f'{minutes:02}:{seconds:02}:{hundredths:02}'

    label.config(text=time_string)

    if running:
        counter += 1
        root.after(10, update_time)

def start():
    global running
    if not running:
        running = True
        update_time()

def stop():
    global running
    running = False

def reset():
    global counter, running
    running = False
    counter = 0
    label.config(text='00:00:00')

root = tk.Tk()
root.title("Stopwatch")
root.configure(bg='black')

label = tk.Label(root, text='00:00:00', font=('Arial',40), bg='white', fg='black')
label.pack(pady = 20)

button_frame = tk.Frame(root, bg='black')
button_frame.pack(pady = 20)

start_button = tk.Button(button_frame, text="Start", command=start)
start_button.pack(side='left', padx = 5)

stop_button = tk.Button(button_frame,text="Stop", command = stop)
stop_button.pack(side='left', padx = 5)

reset_button = tk.Button(button_frame,text="Reset", command = reset)
reset_button.pack(side='left', padx = 5)

root.mainloop()
