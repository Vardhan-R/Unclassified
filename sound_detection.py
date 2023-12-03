import matplotlib.pyplot as plt, numpy as np, pyaudio, pygame, time

FRAMES_PER_BUFFER = 10
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()

threshold = 10

# starts recording
stream = p.open(
	format=FORMAT,
	channels=CHANNELS,
	rate=RATE,
	input=True,
	frames_per_buffer=FRAMES_PER_BUFFER
)

while True:
	data = stream.read(FRAMES_PER_BUFFER)
	data_arr = np.frombuffer(data, dtype = np.int16)
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

	plt.plot(data_arr)
	plt.show()

	# print(data_arr.max())

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