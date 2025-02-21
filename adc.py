import tkinter as tk

running = False
counter = 0

def update_time():
    global running, counter
    minutes, seconds = divmod(counter // 100, 60)
    hundredths = counter % 100
    label.config(text=f'{minutes:02}:{seconds:02}:{hundredths:02}')
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

label = tk.Label(root, text='00:00:00', font=('Arial', 30), width=10)
label.pack()

buttons = tk.Frame(root)
buttons.pack()

tk.Button(buttons, text="Start", command=start).pack(side='left')
tk.Button(buttons, text="Stop", command=stop).pack(side='left')
tk.Button(buttons, text="Reset", command=reset).pack(side='left')

root.mainloop()
