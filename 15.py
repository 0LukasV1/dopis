import tkinter as tk

def check_brackets(expression):
    stack = []
    for char in expression:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return False
    return not stack

def color_brackets(expression):
    colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'orange']
    color_index = 0
    colored_expression = ''
    stack = []
    for char in expression:
        if char == '(':
            stack.append(colors[color_index])
            colored_expression += f'{{"{colors[color_index]}"}}{char}'
            color_index = (color_index + 1) % len(colors)
        elif char == ')':
            if stack:
                colored_expression += f'{{"{stack.pop()}"}}{char}'
            else:
                colored_expression += char
        else:
            colored_expression += char
    return colored_expression

def display_expression():
    expression = entry.get()
    if check_brackets(expression):
        colored_expression = color_brackets(expression)
        label.config(text=colored_expression)
    else:
        label.config(text="Výraz nie je správne uzátvorkovaný")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Zobraz výraz", command=display_expression)
button.pack()
label = tk.Label(root)
label.pack()
root.mainloop()

