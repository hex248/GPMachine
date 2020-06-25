if True: # Imports and global variables
    import tkinter as tk
    import os
    import math
    root = tk.Tk()
    canvasWidth = 500
    canvasHeight = 500
    buttonWidth = 118.75
    buttonHeight = 118.75
    canvasWidth = 500
    canvasHeight = 500
    buttonWidth = 118.75
    buttonHeight = 118.75
    mColour = "#36b3ac"
    bColour = "#b52126"
    gColour = "#808080"
    canvas = tk.Canvas(root, height=canvasHeight, width=canvasWidth)
    canvas.pack()
    def fl(value):
        float(value)

def button(value):
    print("Button Pressed:", value)
    trigonometryButton.place_forget()
    equationButton.place_forget()
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
    if value == "equation":
        equations()
    if value == "thermalenergy":
        thermalEnergy()
    if value == "trigcalculate":
        trigCalculate()
    if value == "thermalenergycalculate":
        thermalEnergyCalculate()
def home():
    backButton.place_forget()
    hideTrig()
    hideEquations()
    trigonometryButton.place(x="5", y="5", width=buttonWidth, height=buttonHeight)
    equationButton.place(x="128.75", y="5", width=buttonWidth, height=buttonHeight)
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

if True: # Trigonometry elements
    trigImage = tk.PhotoImage(file ='trig.png')
    trigLabel = tk.Label(root, image = trigImage)
    trigLabelA = tk.Label(font = '60', text = 'A', fg = 'black', bg = 'grey')
    trigLabelB = tk.Label(font = '60', text = 'B', fg = 'black', bg = 'grey')
    trigLabelC = tk.Label(font = '60', text = 'C', fg = 'black', bg = 'grey')
    trigLabelθ = tk.Label(font = '60', text = 'θ', fg = 'black', bg = 'grey')
    trigEntryA = tk.Entry(font = '60')
    trigEntryB = tk.Entry(font = '60')
    trigEntryC = tk.Entry(font = '60')
    trigEntryθ = tk.Entry(font = '60')
    frame = tk.Frame(root, bg='grey')
    frame.place(relwidth=1, relheight=1, anchor='n', relx = 0.5)

def trig():
    trigLabel.place(relwidth=1, relheight = 1, relx = 0.5, anchor="n", rely = 0)
    trigLabelA.place(y = 100, x = 40)
    trigLabelB.place(y = 120, x = 40)
    trigLabelC.place(y = 140, x = 40)
    trigLabelθ.place(y = 160, x = 40)
    trigEntryA.place(y = 100, x = 80, width = 80, height = 20)
    trigEntryB.place(y = 120, x = 80, width = 80, height = 20)
    trigEntryC.place(y = 140, x = 80, width = 80, height = 20)
    trigEntryθ.place(y = 160, x = 80, width = 80, height = 20)
    trigCalculateButton.place(y = 200, x = 120, width = 70, height = 40, anchor = 'n')
    frame.place_forget()

def trigCalculate():
    a = trigEntryA.get()
    if a:
        a = float(a)
    b = trigEntryB.get()
    if b:
        b = float(b)
    c = trigEntryC.get()
    if c:
        c = float(c)
    θ = trigEntryθ.get()
    if θ:
        θ = float(θ)
    print(a, type(a))
    print(b, type(b))
    print(c, type(c))
    print(θ, type(θ))
    if a and b:
        trigEntryC.delete(0, tk.END)
        trigEntryC.insert(0, str(math.hypot(a, b)))
    elif c and b:
        trigEntryA.delete(0, tk.END)
        trigEntryA.insert(0, str(math.sqrt(c ** 2 - b ** 2)))
    elif c and a:
        trigEntryB.delete(0, tk.END)
        trigEntryB.insert(0, str(math.sqrt(c ** 2 - a ** 2)))
    elif a and c:
        trigEntryB.delete(0, tk.END)
        trigEntryB.insert(0, str(math.degrees(math.asin(a / c))))
    elif b and c:
        trigEntryA.delete(0, tk.END)
        trigEntryA.insert(0, str(math.degrees(math.acos(b / c))))
    elif a and b:
        trigEntryC.delete(0, tk.END)
        trigEntryC.insert(0, str(math.degrees(math.atan(a / b))))
    elif θ and a:
        trigEntryB.delete(0, tk.END)
        trigEntryB.insert(0, str(a / math.tan(math.radians(θ)))) # finding adj(b)
        trigEntryC.delete(0, tk.END)
        trigEntryC.insert(0, str(a * math.sin(math.radians(θ)))) # finding hyp(c)
    elif θ and b:
        trigEntryA.delete(0, tk.END)
        trigEntryA.insert(0, str(b * math.tan(math.radians(θ)))) # finding opp(a)
        trigEntryC.delete(0, tk.END)
        trigEntryC.insert(0, str(b / math.cos(math.radians(θ)))) # finding hyp(c)
    elif θ and c:
        trigEntryB.delete(0, tk.END)
        trigEntryB.insert(0, str(c * math.cos(math.radians(θ)))) # finding adj(b)
        trigEntryA.delete(0, tk.END)
        trigEntryA.insert(0, str(c * math.sin(math.radians(θ)))) # finding opp(a)

def hideTrig():
    trigLabel.place_forget()
    trigLabelA.place_forget()
    trigLabelB.place_forget()
    trigLabelC.place_forget()
    trigLabelθ.place_forget()
    trigEntryA.place_forget()
    trigEntryB.place_forget()
    trigEntryC.place_forget()
    trigEntryθ.place_forget()
    trigCalculateButton.place_forget()
    frame.place(relwidth=1, relheight=1, anchor='n', relx = 0.5)


if True: # Equations elements
    equationsTitle = tk.Label(font = ("Arial", "30"), text = "Equations", fg = "black", bg = "grey")
    physicsTitle = tk.Label(font = ("Arial", "20"), text = "Physics", fg = "black", bg = "grey")
    thermalEnergyLabel = tk.Label(font = ("Arial", "20"), text = "Change in thermal energy", fg = "black", bg = "grey")
    thermalEnergyEntry = tk.Entry(font = ("Arial", "20"), )
    thermalEnergyChangeLabel = tk.Label(font = ("Arial", "13"), text = "Change in thermal energy (Joules):", fg = "black", bg = "grey")
    thermalEnergyChangeEntry = tk.Entry(font = ("Arial", "10"))
    thermalEnergyMassLabel = tk.Label(font = ("Arial", "13"), text = "Mass (g):", fg = "black", bg = "grey")
    thermalEnergyMassEntry = tk.Entry(font = ("Arial", "10"))
    thermalEnergyHeatCapacityLabel = tk.Label(font = ("Arial", "13"), text = "Specific heat capacity (J/(K kg)):", fg = "black", bg = "grey")
    thermalEnergyHeatCapacityEntry = tk.Entry(font = ("Arial", "10"))
    thermalEnergyTemperatureChangeLabel = tk.Label(font = ("Arial", "13"), text = "Temperature change (C):", fg = "black", bg = "grey")
    thermalEnergyTemperatureChangeEntry = tk.Entry(font = ("Arial", "10"))
    thermalEnergyCalculateButton = tk.Button(root, text="Calculate", bg=mColour, font="60", command=lambda: button("thermalenergycalculate"))

def equations():
    equationsTitle.place(y = 10, x = 250, anchor = "n")
    physicsTitle.place(y = 80, x = 125, anchor = "n")
    thermalEnergyButton.place(y = 120, x = 125, anchor = "n")

def hideEquations():
    equationsTitle.place_forget()
    physicsTitle.place_forget()
    thermalEnergyButton.place_forget()
    thermalEnergyLabel.place_forget()
    thermalEnergyEntry.place_forget()
    thermalEnergyChangeLabel.place_forget()
    thermalEnergyChangeEntry.place_forget()
    thermalEnergyMassLabel.place_forget()
    thermalEnergyMassEntry.place_forget()
    thermalEnergyHeatCapacityLabel.place_forget()
    thermalEnergyHeatCapacityEntry.place_forget()

def thermalEnergy():
    thermalEnergyButton.place_forget()
    equationsTitle.place_forget()
    physicsTitle.place_forget()
    thermalEnergyChangeLabel.place(y = 120, x = 20, anchor = "w")
    thermalEnergyChangeEntry.place(y = 120, x = 285, anchor = "w", width = 45, height = 20)
    thermalEnergyMassLabel.place(y = 160, x = 210, anchor = "w")
    thermalEnergyMassEntry.place(y = 160, x = 285, anchor = "w", width = 45, height = 20)
    thermalEnergyHeatCapacityLabel.place(y = 200, x = 35, anchor = "w")
    thermalEnergyHeatCapacityEntry.place(y = 200, x = 285, anchor = "w", width = 45, height = 20)
    thermalEnergyTemperatureChangeLabel.place(y = 240, x = 95, anchor = "w")
    thermalEnergyTemperatureChangeEntry.place(y = 240, x = 285, anchor = "w", width = 45, height = 20)
    thermalEnergyCalculateButton.place(y = 280, x = 285, anchor = "w", width = 45, height = 20)

def thermalEnergyCalculate():
    thermal = thermalEnergyChangeEntry.get()
    if thermal:
        thermal = float(thermal)
    mass = thermalEnergyMassEntry.get()
    if mass:
        mass = float(mass)
    heatCapacity = thermalEnergyHeatCapacityEntry.get()
    if heatCapacity:
        heatCapacity = float(heatCapacity)
    temperatureChange = thermalEnergyTemperatureChangeEntry.get()
    if temperatureChange:
        temperatureChange = float(temperatureChange)
    print(thermal, type(thermal))
    print(mass, type(mass))
    print(heatCapacity, type(heatCapacity))
    print(temperatureChange, type(temperatureChange))

if True: #Home Screen
    trigonometryButton = tk.Button(frame, text="Trigonometry", bg=mColour, font="60", command=lambda: button("trigonometry"))
    trigonometryButton.place(x="5", y="5", width=buttonWidth, height=buttonHeight)

    equationButton = tk.Button(frame, text="Science Equations", bg=mColour, font="60", command=lambda: button("equation"))
    equationButton.place(x="128.75", y="5", width=buttonWidth, height=buttonHeight)

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

if True: ### Internal Buttons
    
    if True: # Equation Buttons
        thermalEnergyButton = tk.Button(root, text="Change in thermal energy", bg=mColour, font="60", command=lambda: button("thermalenergy"))
    
    if True: # Trig Buttons
        trigCalculateButton = tk.Button(root, text="Calculate", bg=mColour, font="60", command=lambda: button("trigcalculate"))

#end
root.mainloop()
