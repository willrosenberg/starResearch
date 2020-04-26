from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import csv

# Data found at https://vizier.u-strasbg.fr/viz-bin/VizieR-3?-source=V/130/gcs3
file = open("New_Star_Data.tsv")
reader = csv.reader(file, delimiter = '\t')

temps = list() # Temperatures
ages = list() # Ages
lums = list() # Luminosities

for values in reader:
    # Skips through all the extra description text above the data
    try:
        temp = float(values[0]) # log(Temperature) (in K)
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

fig = plt.figure()
ax = fig.add_subplot(projection = '3d')

ax.scatter(temps, ages, lums, c = 'r', marker = 'o')
ax.set_xlabel('log(Temperature) (in K)')
ax.set_ylabel('Age (in Gyrs)')
ax.set_zlabel('Luminosity (in Zero-Point Luminosities)')
plt.show()
