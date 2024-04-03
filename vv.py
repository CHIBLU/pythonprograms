import matplotlib.pyplot as plt

# Data
fa_values = [1, 2, 3, 4, 5]
power_values = [2.7473, 4.0134, 3.0357, 3.0660, 3.1823]

# Create a bar graph
plt.bar(fa_values, power_values, color='blue')

# Add labels and title
plt.xlabel('FA')
plt.ylabel('Power')
plt.title('Bar Graph for FA Values with Various Power')

# Show the plot
plt.show()
