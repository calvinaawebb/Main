import tkinter as tk
import os
from tkinter import *
from tkinter import ttk
from collections import Counter

AVOGADROS_NUM = 6.022e23

# chemicals
elements = {"H": 1.0079, "He": 4.0026, "Li": 6.941,
    "Be": 9.0122,
    "B": 10.81,
    "C": 12.011,
    "N": 14.0067,
    "O": 15.9994,
    "F": 18.9984,
    "Ne": 20.1797,
    "Na": 22.9897,
    "Mg": 24.305,
    "Al": 26.9815,
    "Si": 28.0855,
    "P": 30.9738,
    "S": 32.065,
    "Cl": 35.45,
    "Ar": 39.948,
    "K": 39.0983,
    "Ca": 40.078,
    "Sc": 44.9559,
    "Ti": 47.867,
    "V": 50.9415,
    "Cr": 51.9961,
    "Mn": 54.938,
    "Fe": 55.845,
    "Co": 58.9332,
    "Ni": 58.6934,
    "Cu": 63.546,
    "Zn": 65.38,
    "Ga": 69.723,
    "Ge": 72.63,
    "As": 74.9216,
    "Se": 78.96,
    "Br": 79.904,
    "Kr": 83.8,
    "Rb": 85.4678,
    "Sr": 87.62,
    "Y": 88.9059,
    "Zr": 91.224,
    "Nb": 92.9064,
    "Mo": 95.94,
    "Tc": 98.00,
    "Ru": 101.07,
    "Rh": 102.9055,
    "Pd": 106.42,
    "Ag": 107.8682,
    "Cd": 112.411,
    "In": 114.818,
    "Sn": 118.71,
    "Sb": 121.76,
    "Te": 127.6,
    "I": 126.9045,
    "Xe": 131.293,
    "Cs": 132.9055,
    "Ba": 137.327,
    "La": 138.9055,
    "Ce": 140.116,
    "Pr": 140.9077,
    "Nd": 144.242,
    "Pm": 145.0,
    "Sm": 150.36,
    "Eu": 152.0,
    "Gd": 157.25,
    "Tb": 158.9254,
    "Dy": 162.5,
    "Ho": 164.9303,
    "Er": 167.259,
    "Tm": 168.9342,
    "Yb": 173.04,
    "Lu": 174.967,
    "Hf": 178.49,
"Ta": 180.9479,
"W": 183.84,
"Re": 186.207,
"Os": 190.23,
"Ir": 192.217,
"Pt": 195.084,
"Au": 196.9665,
"Hg": 200.59,
"Tl": 204.3833,
"Pb": 207.2,
"Bi": 208.9804,
"Po": 209.0,
"At": 210.0,
"Rn": 222.0,
"Fr": 223.0,
"Ra": 226.0,
"Ac": 227.0,
"Th": 232.0381,
"Pa": 231.0359,
"U": 238.0289,
"Np": 237.0,
"Pu": 244.0,
"Am": 243.0,
"Cm": 247.0,
"Bk": 247.0,
"Cf": 251.0,
"Es": 252.0,
"Fm": 257.0,
"Md": 258.0,
"No": 259.0,
"Lr": 262.0,
"Rf": 261.0,
"Db": 262.0,
"Sg": 266.0,
"Bh": 264.0,
"Hs": 277.0,
"Mt": 268.0
}
# colors
light_grey = "#%02x%02x%02x" % (33, 33, 33)
light_purple = "#%02x%02x%02x" % (187, 134, 252)
darker_purple = "#%02x%02x%02x" % (55, 0, 188)
cyan = "#%02x%02x%02x" % (3, 218, 198)
darker_grey = "#%02x%02x%02x" % (85, 85, 90)

# configuring main page window
home = Tk()
home.title("Chemiae: An Interactive and Intuitive Stoichiometry Calculator")
home.resizable(False, False)
#home.attributes("-fullscreen", True)
home.configure(bg=light_grey)

entry_var = tk.StringVar()
entry_var2 = tk.StringVar()

# screen size set
#home.geometry("%dx%d" % (home.winfo_screenwidth(), home.winfo_screenheight()))
home.geometry("%dx%d" % (800, 500))
home.update()


# getting screen's width and height in pixels
height = home.winfo_screenheight()
width = home.winfo_screenwidth()

class main():

    def __init__(self):
        title = tk.Label(home, text="Chemiae: The Stoichiometry Calculator", font=("Arial", 24), fg=light_purple, bg=light_grey)
        title.pack()
        title.update()
        title.place(x=10, y=0)
        title_sub = tk.Label(home, text="By: Calvin Webb", font=("Arial", 18), fg=light_purple, bg=light_grey)
        title_sub.pack()
        title_sub.update()
        title_sub.place(x=10, y=title.winfo_height() + 5)

        self.out_1 = tk.Label(home, text="", font=("Arial", 18), fg=light_purple, bg=light_grey)
        self.out_1.pack()
        self.out_1.update()
        self.out_1.place(x=10, y=250)

        self.out_2 = tk.Label(home, text="", font=("Arial", 18), fg=light_purple, bg=light_grey)
        self.out_2.pack()
        self.out_2.update()
        self.out_2.place(x=10, y=300)

        desc = tk.Label(home, text="To use the calculator, type\n your chemcial formula\n with the subscripts as numbers\n to the right of your element letters.\n All element letters need to be uppercase.", font=("Arial", 12), fg=light_purple,bg=light_grey)
        desc.pack()
        desc.update()
        desc.place(x=500, y=400)

        self.button2 = tk.Button(home, text="Convert", font=("Arial", 12), bd=5, bg=light_purple, fg=darker_purple, command=self.convert)
        self.button2.pack()
        self.button2.update()
        self.button2.place(x=10, y=200)

    def convert(self):
        value_value = float(value.get())
        formula_value = formula.get()

        if value_value != '' and formula_value != '':
            try:
                molecule = parseMolecule(formula_value)
                molarmass = calcMolarMass(molecule, elements)
                metric = drop.list1.get()
                if metric == "Mass":
                    moles = value_value / molarmass
                    particles = calcParticles(moles)
                    self.out_1['text'] = f"Moles: {moles}"
                    self.out_2['text'] = f"Particles: {particles}"

                elif metric == "Moles":
                    mass = molarmass * value_value
                    particles = calcParticles(value_value)
                    self.out_1['text'] = f"Mass: {mass}"
                    self.out_2['text'] = f"Particles: {particles}"

                elif metric == "Particles":
                    moles = value_value / AVOGADROS_NUM
                    mass = molarmass / moles
                    self.out_1['text'] = f"Moles: {moles}"
                    self.out_2['text'] = f"Mass: {mass}"
            except ValueError as err:
                self.out_1['text'] = err
                self.out_2['text'] = ''


formula = tk.Entry(home, width=116, textvariable=entry_var)
formula.place(x=10, y=100, height=25)
value = tk.Entry(home, width=116, textvariable=entry_var2)
value.place(x=10, y=150, height=25)
mole = value.get()

class drop_downs:

    def __init__(self):
        self.type = ["Mass", "Moles", "Particles"]
        self.list1 = tk.StringVar(home)
        self.list1.set(self.type[0])

    def drop_down(self):
        self.metric_drop_down = tk.OptionMenu(home, self.list1, *self.type)
        self.metric_drop_down["menu"].config(bg=light_purple)
        self.metric_drop_down["highlightthickness"]=0
        self.metric_drop_down.config(bg=light_purple)
        self.metric_drop_down.pack()
        self.metric_drop_down.update()
        self.metric_drop_down.place(x=700, y=150)


def parseNum(inp):
  end_idx = 0
  for letter in inp:
    if not letter.isdigit():
      break
    else:
      end_idx += 1

  return inp[:end_idx]

def parseMolecule(mole):
  if mole[0].isdigit():
    raise ValueError("Molecules must start with an element letter, please enter a valid element.")

  result = Counter()
  while mole != '':
    found_molecule = False
    element_names = sorted(elements.keys(), key=lambda x: len(x), reverse=True)
    for key in element_names:
      #print(f"key: {key}\tmole: {mole}")
      # Parse molecule
      if mole.startswith(key):
        molecule = key
        mole = mole[len(key):]

        # Parse number
        if mole == "":
          number = 1
        elif mole[0].isdigit():
          number = parseNum(mole)
          mole = mole[len(number):]
          number = float(number)
        else:
          number = 1

        #print(f"Found molecule: {molecule}\tnumber: {number}")
        result[molecule] += number
        found_molecule = True
        break

    if not found_molecule:
      raise ValueError("Molecules must start with an element letter, please enter a valid element.")

  return result

def calcMolarMass(molecule, elements):
  mass = 0
  for element, count in molecule.items():
    mass += elements[element]*count
  return mass

def calcParticles(moles):
  return AVOGADROS_NUM * moles


area = main()
drop = drop_downs()
drop.drop_down()
#drop.drop_down2()
tk.mainloop()



