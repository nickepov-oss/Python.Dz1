import tkinter as tk
root = tk.Tk()
root.title("Simple Window")
root.geometry("1280x1024+500+200")#Розмір вікна
root.iconbitmap('click.ico')#Вибір іконки
click_count = 0
bomb = 100
score = 0
press_return = True
label = tk.Label(root, text="Press [Enter] to start the game", font=("Arial", 20))
label.pack()
fuse_label = tk.Label(root, text=f"Fuse: {str(score)}", font=("Arial",20))
fuse_label.pack()
score_label = tk.Label(root, text=f"Score: {score}", font=("Arial",20))
score_label.pack()
img_1= tk.PhotoImage(file="1.gif")
img_2= tk.PhotoImage(file="2.gif")
img_3= tk.PhotoImage(file="3.gif")
img_4= tk.PhotoImage(file="4.gif")
bomb_label = tk.Label(root, image=img_1)
bomb_label.pack()
def update_display():
    pass
def update_bomb():
    pass
def update_score():
    pass
def start(event):
    pass
def click():
    print("Clicked")
    pass
def click():
    global click_count
    click_count += 1

    if click_count == 5:
        label.config(image=img_4)
click_button = tk.Button(root, text="Click me", bg="black", fg="white", width=15,font=("Comic Sans MS",14), command=click)
click_button.pack()
root.resizable(True,True)#Забороняє зміну вікна по висоті та ширині
root.minsize(800,600)#мінімальний розмір вікна
root.maxsize(1920,1080)#максимальний розмір вікна
click_button = tk.Button(root, text="Boost 1 ", bg="cyan", fg="white", width=25,font=("Comic Sans MS",14), command=click)
click_button.pack()
root.resizable(True,True)#Забороняє зміну вікна по висоті та ширині
root.minsize(800,600)#мінімальний розмір вікна
root.maxsize(1920,1080)#максимальний розмір вікна
click_button = tk.Button(root, text="AutoClick", bg="red", fg="white", width=20,font=("Comic Sans MS",14), command=click)
click_button.pack()
root.resizable(True,True)#Забороняє зміну вікна по висоті та ширині
root.minsize(800,600)#мінімальний розмір вікна
root.maxsize(1920,1080)#максимальний розмір вікна
root.bind('<Return>', start)
root.mainloop()