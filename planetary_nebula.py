import numpy as np
import matplotlib.pyplot as plt

# Function to read the data from the file
def read_data(file_path):
    data = np.genfromtxt(file_path, delimiter='\t', skip_header=1)
    return data

# Function to create the plot for a specified column
def create_plot(data, column_index, column_label):
    depth = data[:, 0]
    column_data = data[:, column_index]

    plt.figure(figsize=(10, 6))
    plt.plot(depth, column_data)
    plt.xlabel('Depth')
    plt.ylabel(column_label)
    plt.title(f'{column_label} vs Depth')
    plt.grid()
    plt.savefig('Temperature_profile.png')

if __name__ == "__main__":
    file_path = '/home/mathew/Desktop/Simulations/Cloudy/planetary_nebula/planetary_nebulapn.ovr'  # Replace with your file path
    data = read_data(file_path)

    column_index = 1  # Replace with the index of the desired column (Te in this case)
    column_label = 'T'  # Replace with the label of the desired column

    create_plot(data, column_index, column_label)
