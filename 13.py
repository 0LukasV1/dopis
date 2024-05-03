import tkinter as tk
import random

root = tk.Tk()

Height = 500
Width = 500
canvas = tk.Canvas(height=Height,width=Width,bg='white')
canvas.pack()
move = [5,0]
eater = canvas.create_oval(0,0,40,40,fill='blue')
x1,y1,x2,y2 = canvas.bbox(eater)

list_of_foods = []
def players(number):
    for i in range(number):
        x = random.randrange(40,Width-40)
        y = random.randrange(40,Height-40)
        circle = canvas.create_oval(x,y,x+40,y+40,fill='red')
        list_of_foods.append(circle)

def check_collision():
    eater_coords = canvas.coords(eater)
    for food in list_of_foods:
        food_coords = canvas.coords(food)
        if (eater_coords[0] < food_coords[2] and eater_coords[2] > food_coords[0]) and (eater_coords[1] < food_coords[3] and eater_coords[3] > food_coords[1]):
            canvas.delete(food)
            list_of_foods.remove(food)

def movement():
    canvas.move(eater, move[0], move[1])
    check_collision()
    if list_of_foods == []:
        canvas.create_text(Width//2, Height//2, text="Gratulujem, vyhral si!", font=("Arial", 20), fill="black")
    else:
        canvas.after(100, movement)

def changer(e):
    global move
    if e.char == ('d'):
        move = [5,0]
    elif e.char == ('a'):
        move = [-5,0]
    elif e.char == ('s'):
        move = [0,5]
    elif e.char == ('w'):
        move = [0,-5]

players(5)
root.bind("<KeyPress>",changer)
movement()

root.mainloop()
