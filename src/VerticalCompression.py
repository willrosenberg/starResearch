import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
import numpy as np 
import math
from tqdm import tqdm
import scipy.io as sio
import csv
import math
import pickle


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

#ax.scatter(temps, ages, lums, c = 'r', marker = 'o')
#ax.set_xlabel('Temperature (in K)')
#ax.set_ylabel('Age (in Gyrs)')
#ax.set_zlabel('Luminosity (in Zero-Point Luminosities)')
#plt.show()


#fig = pyplot.figure()
#ax = Axes3D(fig)

#print(min(temps))
#print(max(temps))

randomlist1 = []
for i in range(0,10000):
	n = random.uniform(0,10)
	randomlist1.append(n)

randomlist2 = []
for i in range(0,10000):
	n = random.uniform(0,10)
	randomlist2.append(n)

randomlist3 = []
for i in range(0,10000):
	#n = random.randint(0,100)
	#randomlist3.append(n)
	#randomlist3.append(2**(math.sin(randomlist1[i])) + 1/(2+math.cos(randomlist2[i])) + random.uniform(-1,1))
	#randomlist3.append(5 + random.uniform(-2,2))
	#randomlist3.append(9 - randomlist1[i]**(2) - randomlist2[i]**(2) + random.uniform(-30,30))
	#randomlist3.append(math.sin(5*randomlist1[i])*math.cos(5*randomlist2[i])/5)
	randomlist3.append((randomlist1[i]-5)**(2) - (randomlist2[i]-5)**(2) + random.uniform(-20,20))

Mat = []
for x in range(len(temps)):
	Mat.append([temps[x],ages[x],lums[x]])

newM = []
xlist = []
ylist = []
for x in range(len(Mat)):
	xlist.append(Mat[x][0])
	ylist.append(Mat[x][1])
xmax = max(xlist)
ymax = max(ylist)
gran = 50
dx = xmax/gran
dy = ymax/gran
for x in tqdm(range(gran)):
	for y in range(gran):
		xvals = []
		yvals = []
		zvals = []
		for m in Mat:
			if (m[0] >= (x*dx)) & (m[0] < ((x*dx) + dx)) & (m[1] >= (y*dy)) & (m[1] < ((y*dy) + dy)):
				xvals.append(m[0])
				yvals.append(m[1])
				zvals.append(m[2])
				#print(m[2])
		xmean = np.average(xvals)
		ymean = np.average(yvals)
		#print(zvals)
		zmean = np.average(zvals)
		if (zmean>=0) | (zmean<=0):
			#newM.append([xmean,ymean,zmean])
			newM.append([(x*dx)+(dx/2),(y*dy)+(dy/2),zmean])

#print(gran**2)

x_vals = []
y_vals = []
z_vals = []
for x in range(len(newM)):
	x_vals.append(newM[x][0])
	y_vals.append(newM[x][1])
	z_vals.append(newM[x][2])

#print(x_vals)
#print(y_vals)
#print(z_vals)


#sequence_containing_x_vals = list(range(0, 100))
#sequence_containing_y_vals = list(range(0, 100))
#sequence_containing_z_vals = list(range(0, 100))

#random.shuffle(sequence_containing_x_vals)
#random.shuffle(sequence_containing_y_vals)
#random.shuffle(sequence_containing_z_vals)

#ax.scatter(x_vals,y_vals,z_vals)
#pyplot.show()

#ax.scatter(randomlist1, randomlist2, randomlist3)
#pyplot.show()

mat = sio.loadmat('testdata6.mat', squeeze_me = True)
data = mat['z4']
xs = mat['xq']
ys = mat['yq']
interdata = []
for x in range(len(data)):
	for y in range(len(data)):
		if (data[y][x]>=0)|(data[y][x]<=0):
			interdata.append([xs[0][x],ys[y][0],data[y][x]])

pickle.dump(interdata, open("interdata.dat", "wb"))

#print(interdata)

morex = []
morey = []
morez = []
for x in interdata:
	morex.append(x[0])
	morey.append(x[1])
	morez.append(x[2])

#ax.scatter(morex,morey,morez)
#pyplot.show()
#print(len(morex))
#print(data[0])

print(len(interdata))







trilist = []
count = 0
for star in interdata:
	count = count + 1
	print(count)
	vertexlist = [interdata.index(star)]
	dlist = []
	for x in interdata:
		disp = np.subtract(x,star)
		dist = np.linalg.norm(disp)
		dlist.append(dist)
	#print(dlist)
	templist = []
	for x in dlist:
		templist.append(x)
	#print(len(templist))
	#print(len(dlist))
	templist.remove(0)
	#print(len(templist))
	#print(len(dlist))
	vertex2 = dlist.index(min(templist))
	vertexlist.append(vertex2)
	templist.remove(min(templist))
	vertex3 = dlist.index(min(templist))
	vertexlist.append(vertex3)
	trilist.append(vertexlist)
	print(vertexlist)

#print(trilist)
