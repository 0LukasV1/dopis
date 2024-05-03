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
    text.delete('1.0', tk.END)
    if check_brackets(expression):
        colors = ['red', 'green', 'blue', 'cyan', 'magenta', 'yellow', 'orange']
        color_index = 0
        stack = []
        for index, char in enumerate(expression):
            if char == '(':
                stack.append(colors[color_index])
                text.insert(tk.END, char)
                text.tag_add(colors[color_index], f'{index+1}.0', f'{index+1}.1')
                text.tag_config(colors[color_index], foreground=colors[color_index])
                color_index = (color_index + 1) % len(colors)
            elif char == ')':
                if stack:
                    color = stack.pop()
                    text.insert(tk.END, char)
                    text.tag_add(color, f'{index+1}.0', f'{index+1}.1')
                    text.tag_config(color, foreground=color)
                else:
                    text.insert(tk.END, char)
            else:
                text.insert(tk.END, char)
    else:
        text.insert(tk.END, "Výraz nie je správne uzátvorkovaný")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text="Zobraz výraz", command=display_expression)
button.pack()
text = tk.Text(root)
text.pack()
root.mainloop()
