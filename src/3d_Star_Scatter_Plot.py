from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv
import math

# Dwarf data found at https://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=V/130/gcs3
# Red Giant data found at https://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=J/A%2bA/597/A30/corogee1&-out.max=50&-out.form=HTML%20Table&-out.add=_r&-out.add=_RAJ,_DEJ&-sort=_r&-oc.form=sexa
file = open("New_Star_Data.tsv")
reader = csv.reader(file, delimiter = '\t')

giants = open("RedGiantData.tsv")
giants_reader = csv.reader(giants, delimiter = '\t')

temps = list() # Temperatures
ages = list() # Ages
lums = list() # Luminosities

# Scan through dwarf data
for values in reader:
    # Skips through all the extra description text above the data
    try:
        temp = 10**float(values[0]) # Temperature (in K)
    except:
        continue

    # Checks to see if the star has all pieces of data
    if len(values) < 3:
        continue

    absmag = float(values[1]) # Absolute Magnitude
    age = float(values[2]) # Age (in Gyrs)

    # Luminosity is found using these equations:
    # https://www.omnicalculator.com/physics/luminosity#luminosity-equation
    lum = (10**(absmag/-2.5)) # Luminosity (in Zero-Point Luminosities)

    temps.append(temp)
    ages.append(age)
    lums.append(lum)

# Scan through red giant data
for values in giants_reader:
    # Skips through all the extra description text above the data
    try:
        x = float(values[0]) # log(Temperature) (in K)
    except:
        continue

    temp = float(values[2]) # Temperature (in Kelvins)
    logg = float(values[4]) # log(gravity) (in cm/s^2)
    mass = float(values[7]) # Stellar mass (in Solar masses)
    radius = float(values[8]) # Stellar radius (in Solar radii)
    age = float(values[9]) # Age (in Gyrs)

    # Do some calculations to find luminosity in Zero-Point Luminosities
    # L = 4 * pi * R**2 * sigma * T**4
    # https://www.atnf.csiro.au/outreach/education/senior/astrophysics/photometry_luminosity.html
    # https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html
    # https://arxiv.org/abs/1510.06262
    lum = 4 * math.pi * (radius * 695.7 * 10**6)**2 * (5.670374 * 10**(-8)) * (temp**4) / (3.0128 * 10**28) # Luminosity (in Zero-Point Luminosities)

    temps.append(temp)
    ages.append(age)
    lums.append(lum)

fig = plt.figure()
ax = fig.add_subplot(projection = '3d')

ax.scatter(temps, ages, lums, c = 'r', marker = 'o')
ax.set_xlabel('Temperature (in K)')
ax.set_ylabel('Age (in Gyrs)')
ax.set_zlabel('Luminosity (in Zero-Point Luminosities)')
plt.show()
