import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

parsec = 3.086E+18

# Function to read the data from the file
def read_data(file):
    first_line = np.genfromtxt(file, delimiter='\t', dtype=str, max_rows=1, comments=None)
    data = np.genfromtxt(file, delimiter='\t', skip_header=1)

    # Remove "#" from each element in the array
    column_labels = [element.strip('#') for element in first_line]
    Nrow = len(data)
    Ncol = len(data[0])
    data = pd.DataFrame(data)
    return {'data': data, 'column_labels': column_labels, 'Ncol': Ncol, 'Nrow': Nrow}

# Function to create the plot for a specified column
def create_plots(plotdata, dir_path):

    depth = plotdata['data'].iloc[:, 0] / parsec
    plt.figure(figsize=(10, 8))

    for i in range(1, plotdata['Ncol']):
        column_data = plotdata['data'].iloc[:, i]
        plt.plot(depth, column_data, label=plotdata['column_labels'][i])

        if i > 6:
            break;

    plt.xlabel('Depth (pc)')
    plt.ylabel('Ionization fraction')
    #plt.title(f'{column_label} vs Depth')
    plt.grid()
    plt.legend()
    print('Plotting Ionisation Profile: ' + plotdata['column_labels'][1])
    plt.savefig(dir_path + plotdata['column_labels'][1] + '.png')
    plt.close()



if __name__ == "__main__":

    filelist = ['/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth/HII_region.ele_H',
                '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth/HII_region.ele_He',
                '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth/HII_region.ele_C',
                '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth/HII_region.ele_N',
                '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth/HII_region.ele_O',
                '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth/HII_region.ele_Ne',
                #'/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth/HII_region.ele_Si',
                '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth/HII_region.ele_S'
                #'/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth/HII_region.ele_Fe',
                ]

    dir_path = '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth/'

    for file in filelist:
        data = read_data(file)
        create_plots(data, dir_path)



