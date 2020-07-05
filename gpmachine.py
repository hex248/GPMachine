if True: # Imports and global variables
    import tkinter as tk
    import os
    import math

    import time
    import random
    from tkinter import messagebox
    from pyboy import PyBoy
    root = tk.Tk()
    canvasWidth = 800
    canvasHeight = 800
    buttonWidth = 0.2375
    buttonHeight = 0.2375
    emuButtonWidth = 0.98
    emuButtonHeight = 0.485
    mColour = "#36b3ac"
    bColour = "#b52126"
    gColour = "#808080"
    canvas = tk.Canvas(root, height = canvasHeight, width = canvasWidth)
    canvas.pack()
    root.title("GPMachine")
    icon = tk.PhotoImage(file = "./icons/GPicon.png")
    root.iconphoto(False, icon)

    # Menu images
    trigImageBig = tk.PhotoImage(file = "./images/trigBig.png")
    # Emulator images
    gbImage = tk.PhotoImage(file = "./images/gameboyBackground1.png")
    pokemonImage = tk.PhotoImage(file = "./images/pokemon/pokemonWallpaper1.png")
    otherImage = tk.PhotoImage(file = "./images/other/otherWallpaper.png")
    # Pokemon images
    pokeblueImage = tk.PhotoImage(file = "./images/pokemon/pokeblueImage.png")
    pokegreenImage = tk.PhotoImage(file = "./images/pokemon/pokegreenImage.png")
    pokeredImage = tk.PhotoImage(file = "./images/pokemon/pokeredImage.png")
    pokeyellowImage = tk.PhotoImage(file = "./images/pokemon/pokeyellowImage.png")
    pokegoldImage = tk.PhotoImage(file = "./images/pokemon/pokegoldImage.png")
    pokesilverImage = tk.PhotoImage(file = "./images/pokemon/pokesilverImage.png")
    pokepinballImage = tk.PhotoImage(file = "./images/pokemon/pokepinballImage.png")
    # Other games images
    zeldaImage = tk.PhotoImage(file = "./images/other/zeldaImage.png")
    tetrisImage = tk.PhotoImage(file = "./images/other/tetrisImage.png")
    donkeykongImage = tk.PhotoImage(file = "./images/other/donkeykongImage.png")
    pacmanImage = tk.PhotoImage(file = "./images/other/pacmanImage.png")
    supermarioImage = tk.PhotoImage(file = "./images/other/supermarioImage.png")
    spidermanImage = tk.PhotoImage(file = "./images/other/spidermanImage.png")
    snakeyImage = tk.PhotoImage(file = "./images/other/snakeyImage.png")
    kirbyImage = tk.PhotoImage(file = "./images/other/kirbyImage.png")
    bomblissImage = tk.PhotoImage(file = "./images/other/bomblissImage.png")
    supermario4Image = tk.PhotoImage(file = "./images/other/supermario4Image.png")
    simpsonsImage = tk.PhotoImage(file = "./images/other/simpsonsImage.png")
    tamagotchiImage = tk.PhotoImage(file = "./images/other/tamagotchiImage.png")

def button(value):
    # print("Button Pressed:", value)
    trigonometryButton.place_forget()
    equationButton.place_forget()
    button3.place_forget()
    button4.place_forget()
    button5.place_forget()
    button6.place_forget()
    button7.place_forget()
    button8.place_forget()
    gameboyEmulatorButton.place_forget()
    hideGbemu()

    if value == "back":
        back()
    if value == "trigonometry":
        trig()
    if value == "equation":
        equations()
    if value == "gbemu":
        gbemu()
    if value == "backgame":
        backgame()

def back():
    backButton.place_forget()
    hideTrig()
    hideEquations()
    hideGbemu()
    trigonometryButton.place(relx = 0.01, rely = 0.01, relwidth = buttonWidth, relheight = buttonHeight)
    equationButton.place(relx = 0.2575, rely = 0.01, relwidth = buttonWidth, relheight = buttonHeight)
    button3.place(relx = 0.505, rely = 0.01, relwidth = buttonWidth, relheight = buttonHeight)
    button4.place(relx = 0.7525, rely = 0.01, relwidth = buttonWidth, relheight = buttonHeight)
    button5.place(relx = 0.01, rely = 0.2575, relwidth = buttonWidth, relheight = buttonHeight)
    button6.place(relx = 0.2575, rely = 0.2575, relwidth = buttonWidth, relheight = buttonHeight)
    button7.place(relx = 0.505, rely = 0.2575, relwidth = buttonWidth, relheight = buttonHeight)
    button8.place(relx = 0.7525, rely = 0.2575, relwidth = buttonWidth, relheight = buttonHeight)
    gameboyEmulatorButton.place(relx = 0.01, rely = 0.505, relwidth = emuButtonWidth, relheight = emuButtonHeight)

def backgame():
    pokemonHide()
    otherhide()
    gbemu()
    backgame.place_forget()


def Reset():
        trigEntryA.delete(0, tk.END)
        trigEntryB.delete(0, tk.END)
        trigEntryC.delete(0, tk.END)
        trigEntryθ.delete(0, tk.END)
        thermalEnergyChangeEntry(0, tk.END)
        thermalEnergyEntry(0, tk.END)
        thermalEnergyMassEntry(0, tk.END)
        thermalEnergyHeatCapacityEntry(0, tk.END)
        thermalEnergyTemperatureChangeEntry(0, tk.END)
        kineticEnergyEntry(0, tk.END)
        kineticEnergyMassEntry(0, tk.END)
        kineticEnergyVelocityEntry(0, tk.END)
        trigErrorLabel.place_forget()

if True: # Trigonometry

    if True: # Trigonometry elements
        trigImage = tk.PhotoImage(file ='./images/trig.png')
        trigLabel = tk.Label(root, image = trigImage)
        trigLabelA = tk.Label(font = '60', text = 'A', fg = 'black', bg = 'grey')
        trigLabelB = tk.Label(font = '60', text = 'B', fg = 'black', bg = 'grey')
        trigLabelC = tk.Label(font = '60', text = 'C', fg = 'black', bg = 'grey')
        trigLabelθ = tk.Label(font = '60', text = 'θ', fg = 'black', bg = 'grey')
        trigErrorLabel = tk.Label(font = '50, 100', text = 'ERROR', fg = 'red', bg = 'grey')
        trigEntryA = tk.Entry(font = '60')
        trigEntryB = tk.Entry(font = '60')
        trigEntryC = tk.Entry(font = '60')
        trigEntryθ = tk.Entry(font = '60')
        frame = tk.Frame(root, bg='grey')
        frame.place(relwidth=1, relheight=1, anchor='n', relx = 0.5)

    def trig():
        trigLabel.place(relwidth=1, relheight = 1, relx = 0.5, anchor="n", rely = 0)
        trigLabelA.place(rely = 0.2, relx = 0.08)
        trigLabelB.place(rely = 0.24,relx = 0.08)
        trigLabelC.place(rely = 0.28,relx = 0.08)
        trigLabelθ.place(rely = 0.32,relx = 0.08)
        trigEntryA.place(rely = 0.2, relx = 0.16, relwidth = 0.16, relheight = 0.04)
        trigEntryB.place(rely = 0.24, relx = 0.16, relwidth = 0.16, relheight = 0.04)
        trigEntryC.place(rely = 0.28, relx = 0.16, relwidth = 0.16, relheight = 0.04)
        trigEntryθ.place(rely = 0.32, relx = 0.16, relwidth = 0.16, relheight = 0.04)
        ResetButton.place(rely = 0.49, relx = 0.24, relwidth = 0.14, relheight = 0.08, anchor = 'n')
        trigCalculateButton.place(rely = 0.4, relx = 0.24, relwidth = 0.14, relheight = 0.08, anchor = 'n')
        frame.place_forget()
        backButton.place(relx = 0.01, rely = 0.01)

    def trigCalculate():
        trigErrorLabel.place_forget()
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
        
        if θ >= 90:
            trigErrorLabel.place(rely = 0.6, relx = 0.5, relwidth = 490, relheight = 200, anchor = 'n')
        if a and b:
            trigEntryC.delete(0, tk.END)
            trigEntryC.insert(0, str(math.hypot(a, b)))
        if c and b:
            trigEntryA.delete(0, tk.END)
            trigEntryA.insert(0, str(math.sqrt(c ** 2 - b ** 2)))
        if c and a:
            trigEntryB.delete(0, tk.END)
            trigEntryB.insert(0, str(math.sqrt(c ** 2 - a ** 2)))
        if a and c:
            trigEntryθ.delete(0, tk.END)
            trigEntryθ.insert(0, str(math.degrees(math.asin(a / c))))
        if b and c:
            trigEntryθ.delete(0, tk.END)
            trigEntryθ.insert(0, str(math.degrees(math.acos(b / c))))
        if a and b:
            trigEntryθ.delete(0, tk.END)
            trigEntryθ.insert(0, str(math.degrees(math.atan(a / b))))
        if θ and a:
            trigEntryB.delete(0, tk.END)
            trigEntryB.insert(0, str(a / math.tan(math.radians(θ)))) # finding adj(b)
            trigEntryC.delete(0, tk.END)
            trigEntryC.insert(0, str(a * math.sin(math.radians(θ)))) # finding hyp(c)
        if θ and b:
            trigEntryA.delete(0, tk.END)
            trigEntryA.insert(0, str(b * math.tan(math.radians(θ)))) # finding opp(a)
            trigEntryC.delete(0, tk.END)
            trigEntryC.insert(0, str(b / math.cos(math.radians(θ)))) # finding hyp(c)
        if θ and c:
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
        trigErrorLabel.place_forget()
        ResetButton.place_forget()
        trigCalculateButton.place_forget()
        frame.place(relwidth=1, relheight=1, anchor='n', relx = 0.5)

if True: # Equations

    if True: # Equations elements
        equationsTitle = tk.Label(font = ("Arial", "30"), text = "Equations", fg = "black", bg = "grey")
        physicsTitle = tk.Label(font = ("Arial", "20"), text = "Physics", fg = "black", bg = "grey")
        # thermal elements
        thermalEnergyTitle = tk.Label(font = ("Arial", "50"), text = "Change in Thermal Energy", fg = "black", bg = "grey")
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
        # kinetic elements
        kineticEnergyTitle = tk.Label(font = ("Arial", "30"), text = "Kinetic Energy", fg = "black", bg = "grey")
        kineticEnergyLabel = tk.Label(font = ("Arial", "13"), text = "Kinetic energy:", fg = "black", bg = "grey")
        kineticEnergyEntry = tk.Entry(font = ("Arial", "10"))
        kineticEnergyMassLabel = tk.Label(font = ("Arial", "13"), text = "Mass:", fg = "black", bg = "grey")
        kineticEnergyMassEntry = tk.Entry(font = ("Arial", "10"))
        kineticEnergyVelocityLabel = tk.Label(font = ("Arial", "13"), text = "Velocity:", fg = "black", bg = "grey")
        kineticEnergyVelocityEntry = tk.Entry(font = ("Arial", "10"))

    def equations():
        equationsTitle.place(y = 10, x = 250, anchor = "n")
        physicsTitle.place(y = 80, x = 125, anchor = "n")
        thermalEnergyButton.place(y = 120, x = 125, anchor = "n")
        kineticEnergyButton.place(y = 160, x = 125, anchor = "n")
        backButton.place(relx = 0.01, rely = 0.01)

    def hideEquations():
        hideEquationMenu()
        hideThermalEnergy()
        hideKineticEnergy()

    def hideEquationMenu():
        # hide buttons
        thermalEnergyButton.place_forget()
        kineticEnergyButton.place_forget()
        # hide labels
        equationsTitle.place_forget()
        physicsTitle.place_forget()

    def thermalEnergy():
        hideEquationMenu()
        thermalEnergyTitle.place
        thermalEnergyChangeLabel.place(rely = 0.24, relx = 0.04, anchor = "w")
        thermalEnergyChangeEntry.place(rely = 0.24, relx = 0.57, anchor = "w", relwidth = 45, relheight = 20)
        thermalEnergyMassLabel.place(rely = 0.32, relx = 0.42, anchor = "w")
        thermalEnergyMassEntry.place(rely = 0.32, relx = 0.57, anchor = "w", relwidth = 45, relheight = 20)
        thermalEnergyHeatCapacityLabel.place(rely = 0.4, relx = 0.07, anchor = "w")
        thermalEnergyHeatCapacityEntry.place(rely = 0.4, relx = 0.57, anchor = "w", relwidth = 45, relheight = 20)
        thermalEnergyTemperatureChangeLabel.place(rely = 0.48, relx = 0.19, anchor = "w")
        thermalEnergyTemperatureChangeEntry.place(rely = 0.48, relx = 0.57, anchor = "w", relwidth = 45, relheight = 20)
        thermalEnergyCalculateButton.place(rely = 0.56, relx = 0.57, anchor = "w", relwidth = 90, relheight = 20)
        ResetButton.place(rely = 0.65, relx = 0.57, relwidth = 70, relheight = 40, anchor = 'w')

    def hideThermalEnergy():
        thermalEnergyLabel.place_forget()
        thermalEnergyEntry.place_forget()
        thermalEnergyChangeLabel.place_forget()
        thermalEnergyChangeEntry.place_forget()
        thermalEnergyMassLabel.place_forget()
        thermalEnergyMassEntry.place_forget()
        thermalEnergyHeatCapacityLabel.place_forget()
        thermalEnergyHeatCapacityEntry.place_forget()
        thermalEnergyTemperatureChangeLabel.place_forget()
        thermalEnergyTemperatureChangeEntry.place_forget()
        thermalEnergyCalculateButton.place_forget()

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
        if thermal and mass and heatCapacity:
            thermalEnergyTemperatureChangeEntry.delete(0, tk.END)
            thermalEnergyTemperatureChangeEntry.insert(0, str(thermal / (mass * heatCapacity)))
        elif thermal and mass and temperatureChange:
            thermalEnergyHeatCapacityEntry.delete(0, tk.END)
            thermalEnergyHeatCapacityEntry.insert(0, str(thermal / (mass * temperatureChange)))
        elif thermal and heatCapacity and temperatureChange:
            thermalEnergyMassEntry.delete(0, tk.END)
            thermalEnergyMassEntry.insert(0, str(thermal / (heatCapacity * temperatureChange)))
            thermalEnergyChangeEntry.delete(0, tk.END)
            thermalEnergyChangeEntry.insert(0, str(mass * heatCapacity * temperatureChange))

    def kineticEnergy():
        hideEquationMenu()
        ResetButton.place(rely = 0.65, relx = 0.57, relwidth = 70, relheight = 40, anchor = 'n')
        kineticEnergyTitle.place(rely = 0.06, relx = 0.5, anchor = "n")
        kineticEnergyLabel.place(rely = 0.24, relx = 0.41, anchor = "n")
        kineticEnergyEntry.place(rely = 0.24, relx = 0.57, anchor = "n", relwidth = 45, relheight = 20)
        kineticEnergyMassLabel.place(rely = 0.314, relx = 0.476, anchor = "n")
        kineticEnergyMassEntry.place(rely = 0.32, relx = 0.57, anchor = "n", relwidth = 45, relheight = 20)
        kineticEnergyVelocityLabel.place(rely = 0.394, relx = 0.456, anchor = "n")
        kineticEnergyVelocityEntry.place(rely = 0.4, relx = 0.57, anchor = "n", relwidth = 45, relheight = 20)
        kineticEnergyCalculateButton.place(rely = 0.56, relx = 0.57, anchor = "n", relwidth = 90, relheight = 20)

    def hideKineticEnergy():
        kineticEnergyTitle.place_forget()
        kineticEnergyLabel.place_forget()
        kineticEnergyEntry.place_forget()
        kineticEnergyMassLabel.place_forget()
        kineticEnergyMassEntry.place_forget()
        kineticEnergyVelocityLabel.place_forget()
        kineticEnergyVelocityEntry.place_forget()
        kineticEnergyCalculateButton.place_forget()

    def kineticEnergyCalculate():
        kinetic = kineticEnergyEntry.get()
        if kinetic:
            kinetic = float(kinetic)
        mass = kineticEnergyMassEntry.get()
        if mass:
            mass = float(mass)
        velocity = kineticEnergyVelocityEntry.get()
        if velocity:
            velocity = float(velocity)

        if kinetic and mass:
            kineticEnergyVelocityEntry.delete(0, tk.END)
            kineticEnergyVelocityEntry.insert(0, str(math.sqrt((mass / 2) / kinetic)))
        if kinetic and velocity:
            kineticEnergyMassEntry.delete(0, tk.END)
            kineticEnergyMassEntry.insert(0, str(((velocity ** 2) / kinetic) * 2))
        if mass and velocity:
            kineticEnergyEntry.delete(0, tk.END)
            kineticEnergyEntry.insert(0, str((mass / 2) * velocity ** 2))

if True: # Game Boy Emulator
    def gameboyEmulatorRun():
        pyboy = PyBoy('ROMs/PokemonRed.gb')
        while not pyboy.tick():
            pass
            root.withdraw()

    def gbemu():
        pokemonButton.place(x = 250, y = 50, width = 490, height = 200, anchor = "n")
        otherButton.place(x = 250, y = 255, width = 490, height = 200, anchor = "n")
        backButton.place(relx="0.1", rely="0.1")

    def hideGbemu():
        pokemonHide()
        otherhide()

    def game(game):
        if game == "blue":
            pyboy = PyBoy('ROMs/Pokemon/PokemonBlue.gb')
        elif game == "green":
            pyboy = PyBoy('ROMs/Pokemon/PokemonGreen.gb')
        elif game == "red":
            pyboy = PyBoy('ROMs/Pokemon/PokemonRed.gb')
        elif game == "yellow":
            pyboy = PyBoy('ROMs/Pokemon/PokemonYellow.gb')
        elif game == "gold":
            pyboy = PyBoy('ROMs/Pokemon/PokemonGold.gbc')
        elif game == "silver":
            pyboy = PyBoy('ROMs/Pokemon/PokemonSilver.gbc')
        elif game == "pinball":
            pyboy = PyBoy('ROMs/Pokemon/PokemonPinball.gbc')
        elif game == "zelda":
            pyboy = PyBoy('ROMs/other/LegendofZeldaLinksAwakening.gbc')
        elif game == "tetris":
            pyboy = PyBoy('ROMs/other/Tetris.gb')
        elif game == "donkeykong":
            pyboy = PyBoy('ROMs/other/DonkeyKongLand.gb')
        elif game == "pacman":
            pyboy = PyBoy('ROMs/other/Pac-Man.gbc')
        elif game == "mario":
            pyboy = PyBoy('ROMs/other/SuperMarioLand.gb')
        elif game == "spiderman":
            pyboy = PyBoy('ROMs/other/AmazingSpiderMan2.gb')
        elif game == "snakey":
            pyboy = PyBoy('ROMs/other/SuperSnakey.gb')
        elif game == "kirby":
            pyboy = PyBoy('ROMs/other/KirbysDreamLand.gb')
        elif game == "bombliss":
            pyboy = PyBoy('ROMs/other/SuperBombliss.gb')
        elif game == "mario4":
            pyboy = PyBoy('ROMs/other/SuperMarioLand4.gb')
        elif game == "simpsons":
            pyboy = PyBoy('ROMs/other/Simpsons.gb')
        elif game == "tamagotchi":
            pyboy = PyBoy('ROMs/other/Tamagotchi.gb')
        if game:
            while not pyboy.tick():
                pass
                root.withdraw()

    if True: # Pokémon
        def pokemonShow():
            pokemonBlueButton.place(relx = 0.01, rely = 0.1, relwidth = buttonWidth, relheight = buttonHeight)
            pokemonGreenButton.place(relx = 0.2575, rely = 0.1, relwidth = buttonWidth, relheight = buttonHeight)
            pokemonRedButton.place(relx = 0.505, rely = 0.1, relwidth = buttonWidth, relheight = buttonHeight)
            pokemonYellowButton.place(relx = 0.7525, rely = 0.1, relwidth = buttonWidth, relheight = buttonHeight)
            pokemonGoldButton.place(relx = 0.01, rely = 0.3475, relwidth = 0.98, relheight = 0.2)
            pokemonSilverButton.place(relx = 0.01, rely = 0.5575, relwidth = 0.98, relheight = 0.2)
            pokemonPinballButton.place(relx = 0.01, rely = 0.7675, relwidth = 0.98, relheight = 0.2)
            pokemonButton.place_forget()
            otherButton.place_forget()
            backgame.place(relx = 0.1, rely =  0.1, relwidth = 0.06, relheight = 0.06)
        
        def pokemonHide():
            pokemonButton.place_forget()
            pokemonBlueButton.place_forget()
            pokemonGreenButton.place_forget()
            pokemonRedButton.place_forget()
            pokemonYellowButton.place_forget()
            pokemonGoldButton.place_forget()
            pokemonSilverButton.place_forget()
            pokemonPinballButton.place_forget()

    if True: # Other Games

        def otherShow():
            pokemonButton.place_forget()
            otherButton.place_forget()
            backgame.place(relx = 0.1, rely =  0.1)
            zeldalinksawakeningButton.place(relx = 0.01, rely = 0.1, relwidth = buttonWidth, relheight = buttonHeight)
            tetrisButton.place(relx = 0.2575, rely = 0.1, relwidth = buttonWidth, relheight = buttonHeight)
            donkeykongButton.place(relx = 0.505, rely = 0.1, relwidth = buttonWidth, relheight = buttonHeight)
            pacmanButton.place(relx = 0.7525, rely = 0.1, relwidth = buttonWidth, relheight = buttonHeight)
            supermariolandButton.place(relx = 0.01, rely = 0.3475, relwidth = buttonWidth, relheight = buttonHeight)
            amazingspidermand2Button.place(relx = 0.2575, rely = 0.3475, relwidth = buttonWidth, relheight = buttonHeight)
            snakeyButton.place(relx = 0.505, rely = 0.3475, relwidth = buttonWidth, relheight = buttonHeight)
            kirbydreamlandButton.place(relx = 0.7525, rely = 0.3475, relwidth = buttonWidth, relheight = buttonHeight)
            bombblisButton.place(relx = 0.01, rely = 0.595, relwidth = buttonWidth, relheight = buttonHeight)
            marioland4Button.place(relx = 0.2575, rely = 0.595, relwidth = buttonWidth, relheight = buttonHeight)
            simpsonsButton.place(relx = 0.505, rely = 0.595, relwidth = buttonWidth, relheight = buttonHeight)
            tamagotchiButton.place(relx = 0.7525, rely = 0.595, relwidth = buttonWidth, relheight = buttonHeight)
        
        def otherhide():
            otherButton.place_forget()

            zeldalinksawakeningButton.place_forget()
            tetrisButton.place_forget()
            donkeykongButton.place_forget()
            pacmanButton.place_forget()
            supermariolandButton.place_forget()
            amazingspidermand2Button.place_forget()
            snakeyButton.place_forget()
            kirbydreamlandButton.place_forget()
            bombblisButton.place_forget()
            marioland4Button.place_forget()
            simpsonsButton.place_forget()
            tamagotchiButton.place_forget()

if True: # Home Screen
    trigonometryButton = tk.Button(frame, text="Trigonometry", bg="grey", font="60", command=lambda: button("trigonometry"), image=trigImageBig)
    trigonometryButton.place(relx = 0.01, rely = 0.01, relwidth = buttonWidth, relheight = buttonHeight)

    equationButton = tk.Button(frame, text="Science Equations", bg=mColour, font="60", command=lambda: button("equation"), justify = 'center', wraplength = '80')
    equationButton.place(relx = 0.2575, rely = 0.01, relwidth = buttonWidth, relheight = buttonHeight)

    button3 = tk.Button(frame, text="button3", bg=mColour, font="60",command=lambda:button3())
    button3.place(relx = 0.505, rely = 0.01, relwidth=buttonWidth, relheight=buttonHeight)

    button4 = tk.Button(frame, text="button4", bg=mColour, font="60", command=lambda: button("button4"))
    button4.place(relx = 0.7525, rely = 0.01, relwidth = 0.2375, relheight = 0.2375)

    button5 = tk.Button(frame, text="button5", bg=mColour, font="60", command=lambda: button("button5"))
    button5.place(relx = 0.01, rely = 0.2575, relwidth = buttonWidth, relheight = buttonHeight)

    button6 = tk.Button(frame, text="button6", bg=mColour, font="60", command=lambda: button("button6"))
    button6.place(relx = 0.2575, rely = 0.2575, relwidth = buttonWidth, relheight = buttonHeight)

    button7 = tk.Button(frame, text="button7", bg=mColour, font="60", command=lambda: button("button7"))
    button7.place(relx = 0.505, rely = 0.2575, relwidth = buttonWidth, relheight = buttonHeight)

    button8 = tk.Button(frame, text="button8", bg=mColour, font="60", command=lambda: button("button8"))
    button8.place(relx = 0.7525, rely = 0.2575, relwidth = buttonWidth, relheight = buttonHeight)

    gameboyEmulatorButton = tk.Button(frame, text="GameBoy Emulator", bg="grey", font="60, 50", command=lambda: button("gbemu"), justify = 'center', wraplength = '490', image=gbImage)
    gameboyEmulatorButton.place(relx = 0.01, rely = 0.505, relwidth = emuButtonWidth, relheight = emuButtonHeight)

if True: ### Internal Buttons

    if True: #Back button
            backButton = tk.Button(root, text="Back", bg="red", font="60", command=lambda: button("back"))
            backgame = tk.Button(frame, text="Back", bg="red", font="60", command=lambda: button("backgame"))
            backscience = tk.Button(frame, text="Back", bg="red", font="60", command=lambda: button("backscience"))
    
    if True: # Equation Buttons
        thermalEnergyButton = tk.Button(root, text="Change in thermal energy", bg=mColour, font="60", command=lambda: thermalEnergy())
        thermalEnergyCalculateButton = tk.Button(root, text="Calculate", bg=mColour, font="60", command=lambda: thermalEnergyCalculate())
        kineticEnergyButton = tk.Button(root, text="Kinetic energy", bg=mColour, font="60", command=lambda: kineticEnergy())
        kineticEnergyCalculateButton = tk.Button(root, text="Calculate", bg=mColour, font="60", command=lambda: kineticEnergyCalculate())
    
    if True: # Trig Buttons
        trigCalculateButton = tk.Button(root, text="Calculate", bg=mColour, font="60", command=lambda: trigCalculate())
        ResetButton = tk.Button(root, text="Reset", bg=bColour, font="60", command=lambda: Reset())

    if True: # Emulator Buttons
        if True: # Pokémon
            pokemonButton = tk.Button(root, text = "Pokémon", font="60, 50", bg = "grey", command=lambda: pokemonShow(), justify = "center", wraplength = '400', image=pokemonImage)
            
            pokemonBlueButton = tk.Button(root, text = "Blue", font="60, 20", bg = "grey", command=lambda: game("blue"), justify = "center", wraplength = '118.75', image=pokeblueImage)
            pokemonGreenButton = tk.Button(root, text = "Green", font="60, 20", bg = "grey", command=lambda: game("green"), justify = "center", wraplength = '118.75', image=pokegreenImage)
            pokemonRedButton = tk.Button(root, text = "Red", font="60, 20", bg = "grey", command=lambda: game("red"), justify = "center", wraplength = '118.75', image=pokeredImage)
            pokemonYellowButton = tk.Button(root, text = "Yellow", font="60, 20", bg = "grey", command=lambda: game("yellow"), justify = "center", wraplength = '118.75', image=pokeyellowImage)
            pokemonGoldButton = tk.Button(root, text = "Gold", font="60, 20", bg = "grey", command=lambda: game("gold"), justify = "center", wraplength = '118.75', image=pokegoldImage)
            pokemonSilverButton = tk.Button(root, text = "Silver", font="60, 20", bg = "grey", command=lambda: game("silver"), justify = "center", wraplength = '118.75', image=pokesilverImage)
            pokemonPinballButton = tk.Button(root, text = "Pinball", font="60, 20", bg = "grey", command=lambda: game("pinball"), justify = "center", wraplength = '118.75', image=pokepinballImage)
        if True: # other games buttons
            otherButton = tk.Button(root, text = "Other", font="60, 50", bg = "grey", command=lambda: otherShow(), justify = "center", wraplength = '400', image=otherImage)

            zeldalinksawakeningButton = tk.Button(root, text = "The Ledgend of Zelda: Link's Awakening", font="60, 15", bg = "grey", command=lambda: game("zelda"), justify = "center", wraplength = '118.75', image=zeldaImage)
            tetrisButton = tk.Button(root, text = "Tetris", font="60, 20", bg = "grey", command=lambda: game("tetris"), justify = "center", wraplength = '118.75', image=tetrisImage)
            donkeykongButton = tk.Button(root, text = "Donkey Kong Land", font="60, 20", bg = "grey", command=lambda: game("donkeykong"), justify = "center", wraplength = '118.75', image=donkeykongImage)
            pacmanButton = tk.Button(root, text = "Pac-Man", font="60, 20", bg = "grey", command=lambda: game("pacman"), justify = "center", wraplength = '118.75', image=pacmanImage)
            supermariolandButton = tk.Button(root, text = "Super Mario Land", font="60, 20", bg = "grey", command=lambda: game("mario"), justify = "center", wraplength = '118.75', image=supermarioImage)
            amazingspidermand2Button = tk.Button(root, text = "Amazing Spiderman 2", font="60, 18", bg = "grey", command=lambda: game("spiderman"), justify = "center", wraplength = '118.75', image=spidermanImage)
            snakeyButton = tk.Button(root, text = "Super Snakey", font="60, 20", bg = "grey", command=lambda: game("snakey"), justify = "center", wraplength = '118.75', image=snakeyImage)
            kirbydreamlandButton = tk.Button(root, text = "Kirby's Dream Land", font="60, 20", bg = "grey", command=lambda: game("kirby"), justify = "center", wraplength = '118.75', image=kirbyImage)
            bombblisButton= tk.Button(root, text = "Super Bombliss", font="60, 20", bg = "grey", command=lambda: game("bombliss"), justify = "center", wraplength = '118.75', image=bomblissImage)
            marioland4Button = tk.Button(root, text = "Super Mario Land 4", font="60, 20", bg = "grey", command=lambda: game("mario4"), justify = "center", wraplength = '118.75', image=supermario4Image)
            simpsonsButton = tk.Button(root, text = "Simpons", font="60, 20", bg = "grey", command=lambda: game("simpsons"), justify = "center", wraplength = '118.75', image=simpsonsImage)
            tamagotchiButton = tk.Button(root, text = "Tamagotchi", font="60, 20", bg = "grey", command=lambda: game("tamagotchi"), justify = "center", wraplength = '118.75', image=tamagotchiImage)

root.mainloop()