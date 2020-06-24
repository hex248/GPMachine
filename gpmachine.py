import tkinter as tk

root = tk.Tk()

canvasWidth = 500
canvasHeight = 500

buttonWidth = 118.75
buttonHeight = 118.75

def button(value):
    print("Button Pressed:", value)
    
    trigonometryButton.place_forget()
    TesttryButton.place_forget()
    entry.place_forget()
    entry.pack_forget()
    label.place_forget()
    label.pack_forget()
    backButton.place(x="5", y="5", width=buttonWidth, height=buttonHeight)

    if value == "back":
        home()

def home():
    backButton.place_forget()
    trigonometryButton.place(x="5", y="5", width=buttonWidth, height=buttonHeight)
    TesttryButton.place(x="128.75", y="5", width=buttonWidth, height=buttonHeight)
    entry.place(x="250", y="250")
    entry.pack()
    label.place(x="250", y="250")
    entry.pack()

canvas = tk.Canvas(root, height=canvasHeight, width=canvasWidth)
canvas.pack()

frame = tk.Frame(root, bg='gray')
frame.place(relwidth="1", relheight="1")

trigonometryButton = tk.Button(frame, text="Trigonometry", bg="lightblue", font="60", command=lambda: button("trigonometry"))
trigonometryButton.place(x="5", y="5", width=buttonWidth, height=buttonHeight)

TesttryButton = tk.Button(frame, text="Test", bg="Blue", font="60", command=lambda: button("Test"))
TesttryButton.place(x="128.75", y="5", width=buttonWidth, height=buttonHeight)

backButton = tk.Button(frame, text="Back", bg="lightblue", font="60", command=lambda: button("back"))

entry = tk.Entry(frame, bg="white")
entry.pack()
entry.place(x="250", y="250")

label = tk.Label(frame, text="Type Below", bg="lightblue")
label.pack()
label.place(x="250", y="220")


root.mainloop()