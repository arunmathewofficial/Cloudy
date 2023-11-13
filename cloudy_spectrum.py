



# Read the example data
file_path = '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth_Atlas/HII_region.cont'
plotdir = '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth_Atlas/'


import numpy as np
import matplotlib.pyplot as plt


# Adjust the column indices based on your file structure
usecols = (0, 1)

# Load data with specified columns and skipping the first line
data = np.loadtxt(file_path, skiprows=1, usecols=usecols)




plt.plot(data[:,0], np.log10(data[:,1]))
#plt.xlim(1.0, 7.0)
#plt.xlabel("D, pc", fontsize=14)
#plt.ylabel("Temperature, K", fontsize=14)
plt.show()