if True: # Imports and global variables
    import tkinter as tk
    import os
    import math
    import time
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    import pygame
    import random
    from tkinter import messagebox
    from pyboy import PyBoy
    root = tk.Tk()
    canvasWidth = 500
    canvasHeight = 500
    buttonWidth = 118.75
    buttonHeight = 118.75
    canvasWidth = 500
    canvasHeight = 500
    emuButtonWidth = 490
    emuButtonHeight = 242.5
    mColour = "#36b3ac"
    bColour = "#b52126"
    gColour = "#808080"
    canvas = tk.Canvas(root, height=canvasHeight, width=canvasWidth)
    canvas.pack()
    root.title("GPMachine")
    icon = tk.PhotoImage(file = "./icons/GPicon.png")
    root.iconphoto(False, icon)

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
    snakerunbutton.place_forget()
    button4.place_forget()
    button5.place_forget()
    button6.place_forget()
    button7.place_forget()
    button8.place_forget()
    gameboyEmulatorButton.place_forget()
    hideGbemu()
    backButton.place(x="5", y="5")

    if value == "back":
        home()
    if value == "trigonometry":
        trig()
    if value == "equation":
        equations()
    if value == "gbemu":
        gbemu()

def home():
    backButton.place_forget()
    hideTrig()
    hideEquations()
    hideGbemu()
    trigonometryButton.place(x="5", y="5", width=buttonWidth, height=buttonHeight)
    equationButton.place(x="128.75", y="5", width=buttonWidth, height=buttonHeight)
    snakerunbutton.place(x="252.5", y="5", width=buttonWidth, height=buttonHeight)
    button4.place(x="376.25", y="5", width=buttonWidth, height=buttonHeight)
    button5.place(x="5", y="128.75", width=buttonWidth, height=buttonHeight)
    button6.place(x="128.75", y="128.75", width=buttonWidth, height=buttonHeight)
    button7.place(x="252.5", y="128.75", width=buttonWidth, height=buttonHeight)
    button8.place(x="376.25", y="128.75", width=buttonWidth, height=buttonHeight)
    gameboyEmulatorButton.place(x="5", y="252.5", width=emuButtonWidth, height=emuButtonHeight)

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
        trigImage = tk.PhotoImage(file ='trig.png')
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
        trigLabelA.place(y = 100, x = 40)
        trigLabelB.place(y = 120, x = 40)
        trigLabelC.place(y = 140, x = 40)
        trigLabelθ.place(y = 160, x = 40)
        trigEntryA.place(y = 100, x = 80, width = 80, height = 20)
        trigEntryB.place(y = 120, x = 80, width = 80, height = 20)
        trigEntryC.place(y = 140, x = 80, width = 80, height = 20)
        trigEntryθ.place(y = 160, x = 80, width = 80, height = 20)
        ResetButton.place(y = 245, x = 120, width = 70, height = 40, anchor = 'n')
        trigCalculateButton.place(y = 200, x = 120, width = 70, height = 40, anchor = 'n')
        frame.place_forget()

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
            trigErrorLabel.place(y = 300, x = 250, width = 490, height = 200, anchor = 'n')
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
        thermalEnergyChangeLabel.place(y = 120, x = 20, anchor = "w")
        thermalEnergyChangeEntry.place(y = 120, x = 285, anchor = "w", width = 45, height = 20)
        thermalEnergyMassLabel.place(y = 160, x = 210, anchor = "w")
        thermalEnergyMassEntry.place(y = 160, x = 285, anchor = "w", width = 45, height = 20)
        thermalEnergyHeatCapacityLabel.place(y = 200, x = 35, anchor = "w")
        thermalEnergyHeatCapacityEntry.place(y = 200, x = 285, anchor = "w", width = 45, height = 20)
        thermalEnergyTemperatureChangeLabel.place(y = 240, x = 95, anchor = "w")
        thermalEnergyTemperatureChangeEntry.place(y = 240, x = 285, anchor = "w", width = 45, height = 20)
        thermalEnergyCalculateButton.place(y = 280, x = 285, anchor = "w", width = 90, height = 20)
        ResetButton.place(y = 325, x = 285, width = 70, height = 40, anchor = 'w')

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
        ResetButton.place(y = 325, x = 285, width = 70, height = 40, anchor = 'n')
        kineticEnergyTitle.place(y = 30, x = 250, anchor = "n")
        kineticEnergyLabel.place(y = 120, x = 205, anchor = "n")
        kineticEnergyEntry.place(y = 120, x = 285, anchor = "n", width = 45, height = 20)
        kineticEnergyMassLabel.place(y = 157, x = 238, anchor = "n")
        kineticEnergyMassEntry.place(y = 160, x = 285, anchor = "n", width = 45, height = 20)
        kineticEnergyVelocityLabel.place(y = 197, x = 228, anchor = "n")
        kineticEnergyVelocityEntry.place(y = 200, x = 285, anchor = "n", width = 45, height = 20)
        kineticEnergyCalculateButton.place(y = 280, x = 285, anchor = "n", width = 90, height = 20)

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

def snakerun():
    class cube(object):
        rows = 20
        w = 500
        def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
            self.pos = start
            self.dirnx = 1
            self.dirny = 0
            self.color = color


        def move(self, dirnx, dirny):
            self.dirnx = dirnx
            self.dirny = dirny
            self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

        def draw(self, surface, eyes=False):
            dis = self.w // self.rows
            i = self.pos[0]
            j = self.pos[1]

            pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
            if eyes:
                centre = dis//2
                radius = 3
                circleMiddle = (i*dis+centre-radius,j*dis+8)
                circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
                pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
                pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)
class snake(object):
    pass

if True: # Game Boy Emulator
    def gameboyEmulatorRun():
        pyboy = PyBoy('ROMs/PokemonRed.gb')
        while not pyboy.tick():
            pass
            root.withdraw()
        

    def gbemu():
        pokemonButton.place(x = 250, y = 50, width = 490, height = 200, anchor = "n")
        otherButton.place(x = 250, y = 255, width = 490, height = 200, anchor = "n")

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
            pokemonBlueButton.place(x = 5, y = 50, width = buttonWidth, height = buttonHeight)
            pokemonGreenButton.place(x = 128.75, y = 50, width = buttonWidth, height = buttonHeight)
            pokemonRedButton.place(x = 252.5, y = 50, width = buttonWidth, height = buttonHeight)
            pokemonYellowButton.place(x = 376.25, y = 50, width = buttonWidth, height = buttonHeight)
            pokemonGoldButton.place(x = 5, y = 173.75, width = 490, height = 100)
            pokemonSilverButton.place(x = 5, y = 278.75, width = 490, height = 100)
            pokemonPinballButton.place(x = 5, y = 383.75, width = 490, height = 100)
            pokemonButton.place_forget()
            otherButton.place_forget()
        
        def pokemonHide():
            pokemonButton.place_forget()
            pokemonBlueButton.place_forget()
            pokemonGreenButton.place_forget()
            pokemonRedButton.place_forget()
            pokemonYellowButton.place_forget()
            pokemonGoldButton.place_forget()
            pokemonSilverButton.place_forget()
            pokemonPinballButton.place_forget()

    if True: #Other Games

        def otherShow():
            pokemonButton.place_forget()
            otherButton.place_forget()
            zeldalinksawakeningButton.place(x = 5, y = 50, width = buttonWidth, height = buttonHeight)
            tetrisButton.place(x = 128.75, y = 50, width = buttonWidth, height = buttonHeight)
            donkeykongButton.place(x = 252.5, y = 50, width = buttonWidth, height = buttonHeight)
            pacmanButton.place(x = 376.25, y = 50, width = buttonWidth, height = buttonHeight)
            supermariolandButton.place(x = 5, y = 173.75, width = buttonWidth, height = buttonHeight)
            amazingspidermand2Button.place(x = 128.75, y = 173.75, width = buttonWidth, height = buttonHeight)
            snakeyButton.place(x = 252.5, y = 173.75, width = buttonWidth, height = buttonHeight)
            kirbydreamlandButton.place(x = 376.25, y = 173.75, width = buttonWidth, height = buttonHeight)
            bombblisButton.place(x = 5, y = 297.5, width = buttonWidth, height = buttonHeight)
            marioland4Button.place(x = 128.75, y = 297.5, width = buttonWidth, height = buttonHeight)
            simpsonsButton.place(x = 252.5, y = 297.5, width = buttonWidth, height = buttonHeight)
            tamagotchiButton.place(x = 376.25, y = 297.5, width = buttonWidth, height = buttonHeight)
        
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

if True: #Home Screen
    trigonometryButton = tk.Button(frame, text="Trigonometry", bg=mColour, font="60", command=lambda: button("trigonometry"))
    trigonometryButton.place(x="5", y="5", width=buttonWidth, height=buttonHeight)

    equationButton = tk.Button(frame, text="Science Equations", bg=mColour, font="60", command=lambda: button("equation"), justify = 'center', wraplength = '80')
    equationButton.place(x="128.75", y="5", width=buttonWidth, height=buttonHeight)

    snakerunbutton = tk.Button(frame, text="Snake", bg=mColour, font="60",command=lambda: snakerun())
    snakerunbutton.place(x="252.5", y="5", width=buttonWidth, height=buttonHeight)

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

    gameboyEmulatorButton = tk.Button(frame, text="GameBoy Emulator", bg="grey", font="60, 50", command=lambda: button("gbemu"), justify = 'center', wraplength = '490', image=gbImage)
    gameboyEmulatorButton.place(x="5", y="252.5", width=emuButtonWidth, height=emuButtonHeight)

    backButton = tk.Button(root, text="Back", bg=bColour, font="60", command=lambda: button("back"))

if True: ### Internal Buttons
    
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