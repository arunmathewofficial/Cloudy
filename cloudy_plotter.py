import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np


##################################################################
def load_labled_data(file_path, comment_prefix='#'):
    data = []
    labels = None

    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith(comment_prefix):
                comment = line.strip()[len(comment_prefix):].strip()
                if labels is None and comment:  # Check if it's the first comment line
                    labels = comment.split('\t')  # Split labels using tab as separator
            else:
                row_data = line.strip().split('\t')
                data.append(row_data)

    return labels, data
##################################################################

##################################################################
def plot_data_from_dataframe(df, plotdir):
    """
    Plot data from a DataFrame where the first column is assumed to be the 'x' data
    and the rest of the columns are assumed to be 'y' data.

    Parameters:
        df (pd.DataFrame): The DataFrame containing the data to be plotted.
    """
    x_data = df.iloc[:, 0]
    y_data = df.iloc[:, 1:]

    plt.figure(figsize=(16, 12))
    # Create a figure and axis
    fig, ax = plt.subplots()
    for col in y_data.columns:
        ax.plot(x_data, y_data[col], label=col)

    # Set the tick locator for both x-axis and y-axis
    max_ticks = 6  # You can adjust this value based on your preference
    ax.xaxis.set_major_locator(MaxNLocator(5))
    ax.yaxis.set_major_locator(MaxNLocator(6))

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    # Set custom margins
    plt.subplots_adjust(left=0.2, right=0.9, top=0.78, bottom=0.1)
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.32), ncol=6, fontsize=8)
    plt.grid(True)
    plt.savefig(plotdir + 'HII_region.png', dpi=200)
##################################################################


##################################################################
# Function to create the plot for a specified column
def create_plot(df, column_index, column_label, plotdir):

    depth = df.iloc[:, 0]
    column_data = df.iloc[:, column_index]

    plt.figure(figsize=(10, 6))
    plt.plot(depth, column_data)
    plt.xlabel('Depth')
    plt.ylabel(column_label)
    plt.title(f'{column_label} vs Depth')
    #plt.grid()
    plt.savefig(plotdir + column_label + '.png')
##################################################################



# Read the example data
file = '/home/mathew/Desktop/pion/photoionisation_test/cloudy/HII_region.ovr'
plotdir = '/home/mathew/Desktop/pion/photoionisation_test/cloudy/'

file_path = file # Replace with your file path
labels, data = load_labled_data(file_path)

# Create a DataFrame using pandas
df = pd.DataFrame(data, columns=labels)


# Call the function to plot data
plot_data_from_dataframe(df, plotdir)

# plot temperature
column_index = 1  # Replace with the index of the desired column (Te in this case)
column_label = 'T'  # Replace with the label of the desired column

create_plot(df, column_index, column_label, plotdir)

#print(df)
