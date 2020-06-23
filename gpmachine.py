import tkinter as tk

root = tk.Tk()

canvasWidth = 500
canvasHeight = 500

canvas = tk.Canvas(root, height=canvasHeight, width=canvasWidth)
canvas.pack()

frame = tk.Frame(root, bg='gray')
frame.place(relwidth="1", relheight="1")

button = tk.Button(frame, text="Go", bg="lightblue")
button.pack()
button.place(x="400", y="250")

label = tk.Label(frame, text="Type Below", bg="lightblue")
label.pack()
label.place(x="250", y="220")

entry = tk.Entry(frame, bg="white")
entry.pack()
entry.place(x="250", y="250")

root.mainloop()