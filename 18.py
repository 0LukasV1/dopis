import tkinter as tk
root = tk.Tk()

canvas = tk.Canvas(height=500,width=500,bg='white')
canvas.pack()

new_rect = canvas.create_rectangle(500//2-2,500//2+2,500//2+2,500/2-2,fill='black')
x1,y1,x2,y2 = canvas.bbox(new_rect)
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
direction = 0


def move(lenght):
    global x1,y1
    for i in range(lenght):
        r = canvas.create_rectangle(x1 ,y1,x1 + 5,y1 + 5)
        x1 += directions[direction][0]
        y1 += directions[direction][1]


def left():
    global direction
    direction = (direction - 1) % 4

def right():
    global direction
    direction = (direction + 1) % 4


def execute():
    command = entry.get()
    splitted = command.split(' ')
    if command.startswith('ciara'):
        move(int(splitted[-1]))
    elif command.startswith('vpravo'):
        right()
    elif command.startswith('vlavo'):
        left()


entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text='Vykonaj', command=execute)
button.pack()

root.mainloop()

root.mainloop()
