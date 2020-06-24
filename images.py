import tkinter as tk
root = tk.Tk()

HEIGHT = 500
WIDTH = 500

# canvas = tk.Canvas(root, height=500, width=500)
# canvas.pack()
# frame = tk.Frame(root, bg="gray", bd=5)
# frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
# image = tk.PhotoImage(file='trig.gif')
# label = tk.Label(frame, image=image, anchor="n")
# label.place(relwidth=1, relheight=1)
# frame.pack()
# root.mainloop()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='krone.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()