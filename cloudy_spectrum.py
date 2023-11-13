import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

# Read the example data
file_path = '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth_Atlas/HII_region.cont'
plotdir = '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth_Atlas/'


# Adjust the column indices based on your file structure
usecols = (0, 1)

# Specify the comment marker to skip lines starting with #
comment_marker = '#'

# Load data skipping lines starting with #
cloudy_spectrum  = np.loadtxt(file_path, skiprows=1, usecols=usecols, comments=comment_marker)

# pion
total_luminosity = pow(10, 39.22573)
pymicropion_spectrum = total_luminosity * np.array([2.050111e-01, 1.529011e-01, 8.966990e-02, 1.524399e-01,
                                                    6.224274e-02, 9.455588e-02, 1.657247e-02, 3.712941e-03,
                                                    6.460184e-03, 1.054762e-04, 8.920415e-09, 3.555624e-10])

energy_bins= [[7.640000e+00, 1.120000e+01], [1.120000e+01, 1.360000e+01],
              [1.360000e+01, 1.630000e+01], [1.630000e+01, 2.156000e+01],
              [2.156000e+01, 2.460000e+01], [2.460000e+01, 3.065000e+01],
              [3.065000e+01, 3.510000e+01], [3.510000e+01, 4.096000e+01],
              [4.096000e+01, 4.789000e+01], [4.789000e+01, 5.440000e+01],
              [5.440000e+01, 6.450000e+01], [6.450000e+01, 7.700000e+01]]

# Calculate bin centers from edge values
bin_centers = [(edge[0] + edge[1]) / 2 for edge in energy_bins]
# Calculate bar widths
bar_widths = [edge[1] - edge[0] for edge in energy_bins]


scale_factor = 1e39

# Create a figure with subplots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

# Plot the curve
ax1.plot(13.605703976*cloudy_spectrum[:, 0], np.log10(cloudy_spectrum[:, 1]/total_luminosity), label="cloudy-cont", color='black',
         linestyle='-', linewidth=2)
ax1.set_xlabel("Energy, eV")
ax1.set_ylabel("L$_\\nu$, $10^{39}$ erg/s")
ax1.xaxis.set_minor_locator(AutoMinorLocator())
ax1.yaxis.set_minor_locator(AutoMinorLocator())
ax1.tick_params(axis="both", direction="in", which="both", bottom=True, top=True,
                left=True, right=True, length=3)
ax1.legend(loc='upper right')

ax1.set_xlim(0, 80)

# Creating a twin axis sharing the x-axis
#ax2 = ax1.twinx()

# Plot the bar
ax2.bar(bin_centers, pymicropion_spectrum/total_luminosity, width=bar_widths, align='center', color='orange',
        alpha=0.5, edgecolor='red', label="Binned SED")



ax2.set_xlabel("Energy, eV")
ax2.set_ylabel("erg/s/bin")
ax2.xaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())
ax2.tick_params(axis="both", direction="in", which="both", bottom=True, top=True,
                left=True, right=True, length=3)
ax2.legend(loc='upper right')
ax2.set_xlim(0, 80)


plt.tight_layout()  # To prevent overlapping of subplots
# Show the combined plot
image = plotdir + 'spectrum' + ".png"
print("saving " + image)
plt.savefig(image, dpi=200)
plt.close(fig)




