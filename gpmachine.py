import tkinter as tk

import os

print(os.getcwd())

root = tk.Tk()

canvasWidth = 500
canvasHeight = 500

buttonWidth = 118.75
buttonHeight = 118.75

mColour = "#36b3ac"
bColour = "#b52126"
gColour = "#808080"

def button(value):
    print("Button Pressed:", value)
    trigonometryButton.place_forget()
    button2.place_forget()
    button3.place_forget()
    button4.place_forget()
    button5.place_forget()
    button6.place_forget()
    button7.place_forget()
    button8.place_forget()
    button9.place_forget()
    button10.place_forget()
    button11.place_forget()
    button12.place_forget()
    button13.place_forget()
    button14.place_forget()
    button15.place_forget()
    button16.place_forget()
    backButton.place(x="5", y="5")

    if value == "back":
        home()
    if value == "trigonometry":
        trig()
def home():
    backButton.place_forget()
    hideTrig()
    trigonometryButton.place(x="5", y="5", width=buttonWidth, height=buttonHeight)
    button2.place(x="128.75", y="5", width=buttonWidth, height=buttonHeight)
    button3.place(x="252.5", y="5", width=buttonWidth, height=buttonHeight)
    button4.place(x="376.25", y="5", width=buttonWidth, height=buttonHeight)
    button5.place(x="5", y="128.75", width=buttonWidth, height=buttonHeight)
    button6.place(x="128.75", y="128.75", width=buttonWidth, height=buttonHeight)
    button7.place(x="252.5", y="128.75", width=buttonWidth, height=buttonHeight)
    button8.place(x="376.25", y="128.75", width=buttonWidth, height=buttonHeight)
    button9.place(x="5", y="252.5", width=buttonWidth, height=buttonHeight)
    button10.place(x="128.75", y="252.5", width=buttonWidth, height=buttonHeight)
    button11.place(x="252.5", y="252.5", width=buttonWidth, height=buttonHeight)
    button12.place(x="376.25", y="252.5", width=buttonWidth, height=buttonHeight)
    button13.place(x="5", y="376.25", width=buttonWidth, height=buttonHeight)
    button14.place(x="128.75", y="376.25", width=buttonWidth, height=buttonHeight)
    button15.place(x="252.5", y="376.25", width=buttonWidth, height=buttonHeight)
    button16.place(x="376.25", y="376.25", width=buttonWidth, height=buttonHeight)


canvas = tk.Canvas(root, height=canvasHeight, width=canvasWidth)
canvas.pack()

trigImage = tk.PhotoImage(file ='trig.png')
trigLabel = tk.Label(root, image = trigImage)
trigLabelA = tk.Label(font = '60', text = 'a', fg = 'black', bg = 'grey')



frame = tk.Frame(root, bg='grey')
frame.place(relwidth=1, relheight=1, anchor='n', relx = 0.5)

def trig():
    trigLabel.place(relwidth=1, relheight = 1, relx = 0.5, anchor="n", rely = 0)
    trigLabelA.place(y = 100, x = 100)

    frame.place_forget()

def hideTrig():
    trigLabel.place_forget()
    frame.place(relwidth=1, relheight=1, anchor='n', relx = 0.5)

if True: #ALL BUTTONS
    trigonometryButton = tk.Button(frame, text="Trigonometry", bg=mColour, font="60", command=lambda: button("trigonometry"))
    trigonometryButton.place(x="5", y="5", width=buttonWidth, height=buttonHeight)

    button2 = tk.Button(frame, text="button2", bg=mColour, font="60", command=lambda: button("button2"))
    button2.place(x="128.75", y="5", width=buttonWidth, height=buttonHeight)

    button3 = tk.Button(frame, text="button3", bg=mColour, font="60", command=lambda: button("button3"))
    button3.place(x="252.5", y="5", width=buttonWidth, height=buttonHeight)

    button4 = tk.Button(frame, text="button4", bg=mColour, font="60", command=lambda: button("button4"))
    button4.place(x="376.25", y="5", width=buttonWidth, height=buttonHeight)

    button5 = tk.Button(frame, text="button5", bg=mColour, font="60", command=lambda: button("button5"))
    button5.place(x="5", y="128.75", width=buttonWidth, height=buttonHeight)

    button6 = tk.Button(frame, text="button6", bg=mColour, font="60", command=lambda: button("button6"))
    button6.place(x="128.75", y="128.75", width=buttonWidth, height=buttonHeight)

    button7 = tk.Button(frame, text="button7", bg=mColour, font="60", command=lambda: button("button7"))
    button7.place(x="252.5", y="128.75", width=buttonWidth, height=buttonHeight)

    button8 = tk.Button(frame, text="button8", bg=mColour, font="60", command=lambda: button("button8"))
    button8.place(x="376.25", y="128.75", width=buttonWidth, height=buttonHeight)

    button9 = tk.Button(frame, text="button9", bg=mColour, font="60", command=lambda: button("button9"))
    button9.place(x="5", y="252.5", width=buttonWidth, height=buttonHeight)

    button10 = tk.Button(frame, text="button10", bg=mColour, font="60", command=lambda: button("button10"))
    button10.place(x="128.75", y="252.5", width=buttonWidth, height=buttonHeight)

    button11 = tk.Button(frame, text="button11", bg=mColour, font="60", command=lambda: button("button11"))
    button11.place(x="252.5", y="252.5", width=buttonWidth, height=buttonHeight)

    button12 = tk.Button(frame, text="button12", bg=mColour, font="60", command=lambda: button("button12"))
    button12.place(x="376.25", y="252.5", width=buttonWidth, height=buttonHeight)

    button13 = tk.Button(frame, text="button13", bg=mColour, font="60", command=lambda: button("button13"))
    button13.place(x="5", y="376.25", width=buttonWidth, height=buttonHeight)

    button14 = tk.Button(frame, text="button14", bg=mColour, font="60", command=lambda: button("button14"))
    button14.place(x="128.75", y="376.25", width=buttonWidth, height=buttonHeight)

    button15 = tk.Button(frame, text="button15", bg=mColour, font="60", command=lambda: button("button15"))
    button15.place(x="252.5", y="376.25", width=buttonWidth, height=buttonHeight)

    button16 = tk.Button(frame, text="button16", bg=mColour, font="60", command=lambda: button("button16"))
    button16.place(x="376.25", y="376.25", width=buttonWidth, height=buttonHeight)

    backButton = tk.Button(root, text="Back", bg=bColour, font="60", command=lambda: button("back"))






root.mainloop()
