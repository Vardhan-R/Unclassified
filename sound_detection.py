from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt, multiprocessing, numpy as np, pyaudio, pygame, time

FRAMES_PER_BUFFER = 10
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()

threshold = 10
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

def childFunc(data_arr):
	# while True:
	# 	np_array = np.frombuffer(data_arr.get_obj(), dtype=np.int16)
	# 	plt.plot(np_array)
	# 	plt.show()

	# Set up the animation
	animation = FuncAnimation(fig, update, blit=True, interval=20)

	# Show the plot
	plt.show()

# starts recording
stream = p.open(
	format=FORMAT,
	channels=CHANNELS,
	rate=RATE,
	input=True,
	frames_per_buffer=FRAMES_PER_BUFFER
)

if __name__ == "__main__":
	data_arr = multiprocessing.Array("i", 10)
	child_1 = multiprocessing.Process(target=childFunc, args=(data_arr,))
	child_1.start()

	while True:
		np_array = np.frombuffer(data_arr.get_obj(), dtype=np.int16)
		data = stream.read(FRAMES_PER_BUFFER)
		np_array = np.frombuffer(data, dtype = np.int16)
		# pick_from_arr = np.arange(len(data_arr))
		# pick_from_arr = np.array(data_arr > threshold)
		# l = pick_from_arr.size
		# pick_from_lst = []
		# for i in range(l):
		# 	if not(pick_from_arr[i]):
		# 		continue
		# 	print(i)
		# 	for j in range(i + 3200, l):
		# 		if pick_from_arr[j]:
		# 			if j > i + 9600:
			# if data_arr[i] > threshold:
				# pick_from_lst.append(i)
		
		# pick_from_arr = np.array(pick_from_lst) - pick_from_lst[0]
		# if any(pick_from_arr > 1600):

		# stream.close()

		print(np_array.max())

		# if any(data_arr > threshold):
		# 	scrn = pygame.display.set_mode((1600, 1200))
		# 	scrn.fill((255, 255, 255))
		# 	pygame.display.update()
		# 	time.sleep(1)
		# 	pygame.quit()

		# 	stream.close()

		# 	stream = p.open(
		# 		format=FORMAT,
		# 		channels=CHANNELS,
		# 		rate=RATE,
		# 		input=True,
		# 		frames_per_buffer=FRAMES_PER_BUFFER
		# 	)