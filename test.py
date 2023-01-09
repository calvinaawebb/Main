from collections import Counter

elements = {
    "H": 1.00797,
  "He": 4.00260,
  "Li": 6.941,
  "Be": 9.01218,
  "B": 10.81,
  "C": 12.011,
  "N": 14.0067,
  "O": 15.9994,
  "F": 18.998403,
  "Ne": 20.179,
  "Na": 22.98977,
  "Mg": 24.305,
  "Al": 26.98154,
  "Si": 28.0855,
  "P": 30.97376,
  "S": 32.06,
  "Cl": 35.453,
  "Ar": 39.948,
  "K": 39.0983,
  "Ca": 40.08,
  "Sc": 44.9559,
  "Ti": 47.90
}

mole = input("Enter your molecule:")


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
    print("Molecules must start with an element letter, please enter a valid element.")
    exit(0)


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
      print("Molecules must start with an element letter, please enter a valid element.")
      exit(0)

  return result

molecule = parseMolecule(mole)

def calcMolarMass(molecule, elements):
  mass = 0
  for element, count in molecule.items():
    mass += elements[element]*count
  return mass


avogadros_num = 6.022e23

def calcParticles(moles):
  return avogadros_num / moles



moles = 4.5
molarmass = calcMolarMass(molecule,elements) / moles
print(molarmass)
particles = calcParticles(moles)
print(particles)

mass = 10
moles = mass/molarmass
print(moles)
particles = calcParticles(moles)
print(particles)

particles = 1
moles = particles / avogadros_num
print(f"moles: {moles}")
mass = molarmass/moles
print(f"mass: {mass}")
0.22399333333333335