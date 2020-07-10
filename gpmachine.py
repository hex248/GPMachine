if True: # Imports and global variables
    import tkinter as tk
    import os
    import math
    import time
    import random
    import webbrowser
    from tkinter import messagebox
    from pyboy import PyBoy
    from tkinter import simpledialog
    root = tk.Tk()
    canvasWidth = 500
    canvasHeight = 500
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
    trigImageBig = tk.PhotoImage(file = "./images/trigBig.png") # Scaleable
    # Emulator images
    gbImage = tk.PhotoImage(file = "./images/gameboyBackground2.png") # Scaleable
    pokemonImage = tk.PhotoImage(file = "./images/pokemon/pokemonWallpaper2.png") # Scaleable
    otherImage = tk.PhotoImage(file = "./images/other/otherWallpaper2.png") # Scaleable
    # Pokemon images
    pokeblueImage = tk.PhotoImage(file = "./images/pokemon/pokeblueImage.png") # Scaleable
    pokegreenImage = tk.PhotoImage(file = "./images/pokemon/pokegreenImage.png") # Scaleable
    pokeredImage = tk.PhotoImage(file = "./images/pokemon/pokeredImage.png") # Scaleable
    pokeyellowImage = tk.PhotoImage(file = "./images/pokemon/pokeyellowImage.png") # Scaleable
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
    backButton.place(relx = 0.01, rely = 0.01)
    trigonometryButton.place_forget()
    equationButton.place_forget()
    binaryConversionButton.place_forget()
    animeButton.place_forget()
    gameboyEmulatorButton.place_forget()

    if value == "back":
        back()
    if value == "trigonometry":
        trig()
    if value == "equation":
        equations()
    if value == "gbemu":
        gbemu()
    if value == "binaryconversion":
        binaryShow()
    if value == "anime":
        animeShow()
        

if True: # Back Buttons

    def back():
        backButton.place_forget()
        hideTrig()
        hideEquations()
        hideBinary()
        hideAnime()
        hideGbemu()
        trigonometryButton.place(relx = 0.01, rely = 0.01, relwidth = 0.485, relheight = buttonHeight)
        equationButton.place(relx = 0.01, rely = 0.2575, relwidth = 0.485, relheight = buttonHeight)
        binaryConversionButton.place(relx = 0.505, rely = 0.01, relwidth = 0.485, relheight = buttonHeight)
        animeButton.place(relx = 0.505, rely = 0.2575, relwidth = 0.485, relheight = buttonHeight)
        gameboyEmulatorButton.place(relx = 0.01, rely = 0.505, relwidth = emuButtonWidth, relheight = emuButtonHeight)

    def backgame():
        pokemonHide()
        otherhide()
        gbemu()
        backgameButton.place_forget()
        button("")

    def backAnime():
        hideWebsite()
        airHide()
        animeShow()
        button("")
        backAnimeButton.place_forget()
        backButton.place(relx = 0.01, rely = 0.01)

def Reset():
        trigEntryA.delete(0, tk.END)
        trigEntryB.delete(0, tk.END)
        trigEntryC.delete(0, tk.END)
        trigEntryθ.delete(0, tk.END)
        thermalEnergyChangeEntry.delete(0, tk.END)
        thermalEnergyEntry.delete(0, tk.END)
        thermalEnergyMassEntry.delete(0, tk.END)
        thermalEnergyHeatCapacityEntry.delete(0, tk.END)
        thermalEnergyTemperatureChangeEntry.delete(0, tk.END)
        kineticEnergyEntry.delete(0, tk.END)
        kineticEnergyMassEntry.delete(0, tk.END)
        kineticEnergyVelocityEntry.delete(0, tk.END)
        trigErrorLabel.place_forget()
        decimalEntry.delete(0, tk.END)
        binaryEntry.delete(0, tk.END)
        conversionErrorLabel.place_forget()


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
        thermalEnergyTitle = tk.Label(font = ("Arial", "30"), text = "Change in Thermal Energy", fg = "black", bg = "grey")
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

    def backscience():
        hideThermalEnergy()
        hideKineticEnergy()
        equations()
        backscienceButton.place_forget()
        backButton.place(relx = 0.01, rely = 0.01)

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
        thermalEnergyTitle.place(relx = 0.5, rely = 0.08, anchor = "n")
        thermalEnergyChangeLabel.place(rely = 0.24, relx = 0.04, anchor = "w")
        thermalEnergyChangeEntry.place(rely = 0.24, relx = 0.57, anchor = "w", relwidth = 0.09, relheight = 0.04)
        thermalEnergyMassLabel.place(rely = 0.32, relx = 0.42, anchor = "w")
        thermalEnergyMassEntry.place(rely = 0.32, relx = 0.57, anchor = "w", relwidth = 0.09, relheight = 0.04)
        thermalEnergyHeatCapacityLabel.place(rely = 0.4, relx = 0.07, anchor = "w")
        thermalEnergyHeatCapacityEntry.place(rely = 0.4, relx = 0.57, anchor = "w", relwidth = 0.09, relheight = 0.04)
        thermalEnergyTemperatureChangeLabel.place(rely = 0.48, relx = 0.19, anchor = "w")
        thermalEnergyTemperatureChangeEntry.place(rely = 0.48, relx = 0.57, anchor = "w", relwidth = 0.09, relheight = 0.04)
        thermalEnergyCalculateButton.place(rely = 0.56, relx = 0.57, anchor = "w", relwidth = 0.18, relheight = 0.04)
        ResetButton.place(rely = 0.65, relx = 0.57, relwidth = 0.14, relheight = 0.08, anchor = 'w')
        backscienceButton.place(relx = 0.01, rely = 0.01)
        backButton.place_forget()
        hideEquationMenu()

    def hideThermalEnergy():
        ResetButton.place_forget()
        thermalEnergyTitle.place_forget()
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
        ResetButton.place(rely = 0.65, relx = 0.57, relwidth = 0.14, relheight = 0.08, anchor = 'n')
        kineticEnergyTitle.place(rely = 0.06, relx = 0.5, anchor = "n")
        kineticEnergyLabel.place(rely = 0.24, relx = 0.41, anchor = "n")
        kineticEnergyEntry.place(rely = 0.24, relx = 0.57, anchor = "n", relwidth = 0.09, relheight = 0.04)
        kineticEnergyMassLabel.place(rely = 0.314, relx = 0.476, anchor = "n")
        kineticEnergyMassEntry.place(rely = 0.32, relx = 0.57, anchor = "n", relwidth = 0.09, relheight = 0.04)
        kineticEnergyVelocityLabel.place(rely = 0.394, relx = 0.456, anchor = "n")
        kineticEnergyVelocityEntry.place(rely = 0.4, relx = 0.57, anchor = "n", relwidth = 0.09, relheight = 0.04)
        kineticEnergyCalculateButton.place(rely = 0.56, relx = 0.57, anchor = "n", relwidth = 0.18, relheight = 0.04)
        backscienceButton.place(relx = 0.01, rely = 0.01)
        backButton.place_forget()

    def hideKineticEnergy():
        ResetButton.place_forget()
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

if True: # Binary Conversion

    if True: # Binary Conversion elements
        decimalLabel = tk.Label(font = '60', text = 'Decimal/Denary', fg = 'black', bg = 'grey')
        binaryLabel = tk.Label(font = '60', text = 'Binary', fg = 'black', bg = 'grey')
        conversionErrorLabel = tk.Label(font = '50, 100', text = 'ERROR', fg = 'red', bg = 'grey')
        decimalEntry = tk.Entry(font = '60')
        binaryEntry = tk.Entry(font = '60')

    def binaryShow():
        decimalLabel.place(rely = 0.2, relx = 0.35, anchor = 'e')
        binaryLabel.place(rely = 0.24, relx = 0.35, anchor = 'e')
        decimalEntry.place(rely = 0.2, relx = 0.36, relwidth = 0.24, relheight = 0.04, anchor = 'w')
        binaryEntry.place(rely = 0.24, relx = 0.36, relwidth = 0.24, relheight = 0.04, anchor = 'w')
        ResetButton.place(rely = 0.41, relx = 0.48, relwidth = 0.16, relheight = 0.08, anchor = 'n')
        binaryCalculateButton.place(rely = 0.32, relx = 0.48, relwidth = 0.16, relheight = 0.08, anchor = 'n')

    def hideBinary():
        decimalLabel.place_forget()
        binaryLabel.place_forget()
        decimalEntry.place_forget()
        binaryEntry.place_forget()
        ResetButton.place_forget()
        binaryCalculateButton.place_forget()

    def binaryCalculate():
        conversionErrorLabel.place_forget()
        decimal = decimalEntry.get()
        if decimal:
            decimal = int(decimal)
        binary = binaryEntry.get()
        if decimal:
            binaryEntry.delete(0, tk.END)
            binaryEntry.insert(0, str(bin(decimal)[2:]))
        elif binary:
            decimal = 0
            for digit in binary:
                decimal = decimal*2 + int(digit)
            decimalEntry.delete(0, tk.END)
            decimalEntry.insert(0, str(decimal))
        else:
            conversionErrorLabel.place(rely = 0.6, relx = 0.5, relwidth = 490, relheight = 200, anchor = 'n')

if True: # Anime Button

    def animeShow():
        websitebutton.place(relx = 0.01, rely = 0.1, relwidth = buttonWidth, relheight = buttonHeight)
        animecurrentlyButton.place(relx = 0.2575, rely = 0.1, relwidth = buttonWidth, relheight = buttonHeight)

    def hideAnime():
        websitebutton.place_forget()
        animecurrentlyButton.place_forget()

    def WebsiteShow():
        backButton.place_forget()
        backAnimeButton.place(relx = 0.01, rely = 0.01)
        gogoButton.place(relx = 0.01, rely = 0.1, relwidth = buttonWidth, relheight = buttonHeight)
        kissanimeButton.place(relx = 0.2575, rely = 0.1, relwidth = buttonWidth, relheight = buttonHeight)
        animeultimaButton.place(relx = 0.505, rely = 0.1, relwidth = buttonWidth, relheight = buttonHeight)
        animetwistButton.place(relx = 0.7525, rely = 0.1, relwidth = buttonWidth, relheight = buttonHeight)
        animelistButton.place(relx = 0.01, rely = 0.3575, relwidth = buttonWidth, relheight = buttonHeight)
        animelistPersonalButton.place(relx = 0.2575, rely = 0.3575, relwidth = buttonWidth, relheight = buttonHeight)
        animecurrentlyButton.place_forget()
        
    
    def hideWebsite():
        gogoButton.place_forget()
        kissanimeButton.place_forget()
        animeultimaButton.place_forget()
        animetwistButton.place_forget()
        animelistButton.place_forget()
        animelistPersonalButton.place_forget()

    def Websitebutton(value):
        if value == ("gogo"):
            webbrowser.open("https://www.gogoanime.io/")
        if value == ("kissanime"):
            webbrowser.open("https://kissanime.ru/")
        if value == ("ultima"):
            webbrowser.open("https://www.animeultima.to/")
        if value == ("animetwist"):
            webbrowser.open("https://twist.moe/")
        if value == ("aniwatch"):
            webbrowser.open("https://aniwatch.me/home")
        if value == ("mal"):
            webbrowser.open("https://myanimelist.net/")
        if value == ("malpersonal"):
            MALusername= simpledialog.askstring("input string", "my anime list username")
            webbrowser.open("https://myanimelist.net/animelist/" + MALusername)
    
    def airShow():
        backButton.place_forget()
        backAnimeButton.place(relx = 0.01, rely = 0.01)
        websitebutton.place_forget()
        animecurrentlyButton.place_forget()
        animecurrentlyLabel.place(relx = 0.1, rely = 0.1)

    def airHide():
        animecurrentlyLabel.place_forget()
if True: # Game Boy Emulator

    def gbemu():
        pokemonButton.place(relx = 0.5, rely = 0.1, relwidth = 0.98, relheight = 0.4, anchor = "n")
        otherButton.place(relx = 0.5, rely = 0.51, relwidth = 0.98, relheight = 0.4, anchor = "n")

    def hideGbemu():
        # pokemonHide()
        # otherhide()
        pokemonButton.place_forget()
        otherButton.place_forget()

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
            backButton.place_forget()
            backgameButton.place(relx = 0.01, rely = 0.01)
        
        def pokemonHide():
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
            backButton.place_forget()
            backgameButton.place(relx = 0.01, rely = 0.01)
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
            #otherButton.place_forget()
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
    trigonometryButton.place(relx = 0.01, rely = 0.01, relwidth = 0.485, relheight = buttonHeight)

    equationButton = tk.Button(frame, text="Science Equations", bg=mColour, font="60", command=lambda: button("equation"), justify = 'center', wraplength = '80')
    equationButton.place(relx = 0.01, rely = 0.2575, relwidth = 0.485, relheight = buttonHeight)

    binaryConversionButton = tk.Button(frame, text="Binary Conversion", bg=mColour, font="60",command=lambda: button("binaryconversion"))
    binaryConversionButton.place(relx = 0.505, rely = 0.01, relwidth=0.485, relheight=buttonHeight)

    animeButton = tk.Button(frame, text="Anime", bg=mColour, font="60", command=lambda: button("anime"))
    animeButton.place(relx = 0.505, rely = 0.2575, relwidth = 0.485, relheight = buttonHeight)

    gameboyEmulatorButton = tk.Button(frame, text="GameBoy Emulator", bg="grey", font="60, 50", command=lambda: button("gbemu"), justify = 'center', wraplength = '490', image=gbImage)
    gameboyEmulatorButton.place(relx = 0.01, rely = 0.505, relwidth = emuButtonWidth, relheight = emuButtonHeight)

if True: ### Internal Buttons

    if True: # Back button
            backButton = tk.Button(root, text="Back", bg="red", font="60", command=lambda: button("back"))
            backgameButton = tk.Button(frame, text="Back", bg="red", font="60", command=lambda: backgame())
            backscienceButton = tk.Button(frame, text="Back", bg="red", font="60", command=lambda: backscience())
            backAnimeButton = tk.Button(root, text="Back", bg="red", font="60", command=lambda: backAnime())
    
    if True: # Equation Buttons
        thermalEnergyButton = tk.Button(root, text="Change in thermal energy", bg=mColour, font="60", command=lambda: thermalEnergy())
        thermalEnergyCalculateButton = tk.Button(root, text="Calculate", bg=mColour, font="60", command=lambda: thermalEnergyCalculate())
        kineticEnergyButton = tk.Button(root, text="Kinetic energy", bg=mColour, font="60", command=lambda: kineticEnergy())
        kineticEnergyCalculateButton = tk.Button(root, text="Calculate", bg=mColour, font="60", command=lambda: kineticEnergyCalculate())
    
    if True: # Trig Buttons
        trigCalculateButton = tk.Button(root, text="Calculate", bg=mColour, font="60", command=lambda: trigCalculate())
        ResetButton = tk.Button(root, text="Reset", bg=bColour, font="60", command=lambda: Reset())

    if True: # Binary Conversion Buttons
        binaryCalculateButton = tk.Button(root, text="Calculate", bg=mColour, font="60", command=lambda: binaryCalculate())

    if True: # Anime Buttons
        websitebutton = tk.Button(root, text = "Websites", font="60, 20", bg = "grey", justify = "center", wraplength = '118.75', command=lambda: WebsiteShow())

        gogoButton = tk.Button(root, text = "GOGO ANiME", font="60, 20", bg = "grey", justify = "center", wraplength = '118.75', command=lambda: Websitebutton("gogo"))
        kissanimeButton = tk.Button(root, text = "Kiss Anime", font="60, 20", bg = "grey", justify = "center", wraplength = '118.75', command=lambda: Websitebutton("kissanime"))
        animeultimaButton = tk.Button(root, text = "AnimeUltima", font="60, 20", bg = "grey", justify = "center", wraplength = '90', command=lambda: Websitebutton("ultima"))
        animetwistButton = tk.Button(root, text = "Anime Twist", font="60, 20", bg = "grey", justify = "center", wraplength = '118.75', command=lambda: Websitebutton("animetwist"))
        aniwatchButton = tk.Button(root, text = "Ani Watch", font="60, 20", bg = "grey", justify = "center", wraplength = '118.75', command=lambda: Websitebutton("aniwatch"))
        animelistButton = tk.Button(root, text = "My Anime List", font="60, 20", bg = "grey", justify = "center", wraplength = '118.75', command=lambda: Websitebutton("mal"))
        animelistPersonalButton = tk.Button(root, text = "My Anime List With Name", font="60, 20", bg = "grey", justify = "center", wraplength = '118.75', command=lambda: Websitebutton("malpersonal"))

        animecurrentlyButton = tk.Button(root, text = "Currently Airing", font="60, 20", bg = "grey", justify = "center", wraplength = '118.75', command=lambda: airShow())
        animecurrentlyLabel = tk.Label(font = ("Arial", "30"), text = "Lable", fg = "black", bg = "grey")




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