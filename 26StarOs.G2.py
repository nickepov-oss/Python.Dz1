import tkinter as tk
from tkinter import messagebox
import random
import time

# ---------------- SYSTEM ----------------
PASSWORD = "2600"

files = {
    "welcome.txt": "Добро пожаловать в 26StarOS.G2 🌌",
}

trash = {}

# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("⭐ 26StarOS.G2")
root.geometry("1000x650")
root.configure(bg="black")

# ---------------- STAR BACKGROUND ----------------
def stars(canvas):
    for _ in range(250):
        x = random.randint(0, 1000)
        y = random.randint(0, 650)
        canvas.create_oval(x, y, x+2, y+2, fill="white")

# ---------------- LOGIN ----------------
login = tk.Frame(root, bg="black")
login.pack(fill="both", expand=True)

tk.Label(login, text="26StarOS.G2", fg="white", bg="black", font=("Consolas", 30)).pack(pady=30)

entry = tk.Entry(login, show="*", bg="black", fg="white")
entry.pack()

def start():
    if entry.get() == PASSWORD:
        login.pack_forget()
        desktop.pack(fill="both", expand=True)
        taskbar.pack(side="bottom", fill="x")
        stars(desktop)
    else:
        messagebox.showerror("Error", "Wrong password")

tk.Button(login, text="ENTER", command=start).pack()

# ---------------- DESKTOP ----------------
desktop = tk.Canvas(root, bg="black")

# ---------------- TASKBAR ----------------
taskbar = tk.Frame(root, bg="#111")

clock = tk.Label(taskbar, fg="white", bg="#111")
clock.pack(side="right")

def time_update():
    clock.config(text=time.strftime("%H:%M:%S"))
    root.after(1000, time_update)

# ---------------- WINDOWS ----------------
def window(title, w=350, h=300):
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry(f"{w}x{h}")
    win.configure(bg="black")
    return win

# ---------------- FILE SYSTEM ----------------
def file_manager():
    win = window("📁 Files")

    listbox = tk.Listbox(win, bg="black", fg="lime")
    listbox.pack(fill="both", expand=True)

    def refresh():
        listbox.delete(0, tk.END)
        for f in files:
            listbox.insert(tk.END, f)

    def open_file():
        f = listbox.get(tk.ACTIVE)
        messagebox.showinfo(f, files[f])

    def new_file():
        name = f"file{len(files)+1}.txt"
        files[name] = "New file created"
        refresh()

    def delete_file():
        f = listbox.get(tk.ACTIVE)
        trash[f] = files.pop(f)
        refresh()

    refresh()

    tk.Button(win, text="Open", command=open_file).pack()
    tk.Button(win, text="New", command=new_file).pack()
    tk.Button(win, text="Delete → Trash", command=delete_file).pack()

# ---------------- TRASH ----------------
def open_trash():
    win = window("🗑️ Trash")

    listbox = tk.Listbox(win, bg="black", fg="red")
    listbox.pack(fill="both", expand=True)

    def refresh():
        listbox.delete(0, tk.END)
        for f in trash:
            listbox.insert(tk.END, f)

    def restore():
        f = listbox.get(tk.ACTIVE)
        files[f] = trash.pop(f)
        refresh()

    refresh()

    tk.Button(win, text="Restore", command=restore).pack()

# ---------------- GAMES ----------------
def guess_game():
    win = window("🎮 Guess")
    num = random.randint(1, 10)

    e = tk.Entry(win)
    e.pack()

    def check():
        if int(e.get()) == num:
            messagebox.showinfo("Win", "Correct!")
        else:
            messagebox.showinfo("Lose", f"It was {num}")

    tk.Button(win, text="Check", command=check).pack()

def snake_game():
    win = window("🐍 Snake", 400, 300)
    c = tk.Canvas(win, width=400, height=300, bg="black")
    c.pack()

    snake = [(100, 100)]
    dir = "Right"
    food = (200, 200)

    def draw():
        c.delete("all")
        for x, y in snake:
            c.create_rectangle(x, y, x+20, y+20, fill="lime")
        c.create_rectangle(food[0], food[1], food[0]+20, food[1]+20, fill="red")

    def move():
        nonlocal food
        x, y = snake[0]

        if dir == "Right": x += 20
        if dir == "Left": x -= 20
        if dir == "Up": y -= 20
        if dir == "Down": y += 20

        snake.insert(0, (x, y))
        if (x, y) == food:
            food = (random.randint(0, 19) * 20, random.randint(0, 14) * 20)
        else:
            snake.pop()

        draw()
        win.after(120, move)

    def key(e):
        nonlocal dir
        dir = e.keysym

    win.bind("<Key>", key)
    draw()
    move()


def shooter_game():
    win = window("👾 Space Shooter", 400, 300)
    c = tk.Canvas(win, bg="black", width=400, height=300)
    c.pack()

    player = 180
    bullets = []
    enemies = [(random.randint(0, 380), 0)]

    def draw():
        c.delete("all")
        c.create_rectangle(player, 260, player + 30, 280, fill="lime")

        for b in bullets:
            c.create_rectangle(b[0], b[1], b[0] + 5, b[1] + 10, fill="yellow")

        for e in enemies:
            c.create_rectangle(e[0], e[1], e[0] + 20, e[1] + 20, fill="red")

    def update():
        nonlocal enemies

        for b in bullets:
            b[1] -= 10

        enemies = [(x, y + 5) for x, y in enemies]

        draw()
        win.after(100, update)

    def shoot(event):
        bullets.append([player + 10, 250])

    def move(event):
        nonlocal player
        if event.keysym == "Left":
            player -= 10
        if event.keysym == "Right":
            player += 10

    win.bind("<space>", shoot)
    win.bind("<Key>", move)

    update()


# ---------------- DESKTOP ICONS ----------------
frame = tk.Frame(root, bg="black")
frame.pack()

tk.Button(frame, text="📁 Files", command=file_manager).grid(row=0, column=0)
tk.Button(frame, text="🗑️ Trash", command=open_trash).grid(row=0, column=1)
tk.Button(frame, text="🎮 Guess", command=guess_game).grid(row=0, column=2)
tk.Button(frame, text="🐍 Snake", command=snake_game).grid(row=0, column=3)
tk.Button(frame, text="👾 Shooter", command=shooter_game).grid(row=0, column=4)

# ---------------- START ----------------
time_update()
root.mainloop()