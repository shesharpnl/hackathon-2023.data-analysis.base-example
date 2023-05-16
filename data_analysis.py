import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
print("Reading the CSV file...")
df = pd.read_csv('assets/sourcestack-data-id_bcu86flyul.csv')

# Create a new figure with a size of 15x10 inches
print("Creating a new figure...")
plt.figure(figsize=(15, 10))

# Count the occurrences of each value in the 'hours' column and create a bar plot
print("Generating the bar plot...")
ax = df['hours'].value_counts().plot(kind='bar')

# Rotate the x-axis labels by 90 degrees for better readability
print("Rotating x-axis labels...")
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

# Add a margin to the plot to prevent the labels from being cut off
print("Adding margins to the plot...")
plt.margins(0.1)

# Save the plot as a PNG image file named 'bar_plot.png'
image_path = 'bar_plot.png'
print(f"Saving the bar plot as '{image_path}'...")
plt.savefig(image_path)

print("Script execution completed.")
