import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

w = 3
k = -3
t = 0

# Function to generate random data for the plot
def generate_data():
	global t
	x = np.linspace(0, 2 * np.pi, 100)
	y = np.sin(w * t - k * x)
	t += 0.01
	return x, y

# Function to update the plot data for animation
def update(frame):
	x, y = generate_data()
	line.set_data(x, y)

	# Adjust x-axis limits to make the left side disappear after 50 frames
	# ax.set_xlim(0.01 * frame, 0.01 * frame + 50)

	return line,

# Create a figure and axis
fig, ax = plt.subplots()
x, y = generate_data()

# Plot the initial data
line, = ax.plot(x, y)
plt.ylim(-1.1, 1.1)

# Set up the animation
animation = FuncAnimation(fig, update, blit=True, interval=20)

# Show the plot
plt.show()
