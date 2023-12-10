import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
import threading

def detectFallingEdges(arr: np.ndarray, amplitude: float, threshold: float, sample_spacing: int) -> np.ndarray:
	arr_size = arr.size
	falling_edges_arr = np.zeros(arr_size)
	curr_state = False
	prev_state = curr_state

	for i in range(0, arr_size, sample_spacing):
		curr_state = arr[i] >= threshold
		falling_edges_arr[i] += int(prev_state and not(curr_state)) * amplitude
		prev_state = curr_state

	return falling_edges_arr

def detectRisingEdges(arr: np.ndarray, amplitude: float, threshold: float, sample_spacing: int) -> bool:
	arr_size = arr.size
	rising_edges_arr = np.zeros(arr_size)
	curr_state = False
	prev_state = curr_state
	f = False

	for i in range(0, arr_size, sample_spacing):
		curr_state = arr[i] >= threshold
		# rising_edges_arr[i] += int(not(prev_state) and curr_state) * amplitude
		if not(prev_state) and curr_state:
			f = True
			break
		prev_state = curr_state

	return f

def movingAverage(arr: np.ndarray, kernel_size: int) -> np.ndarray:
	return np.convolve(arr, np.ones(kernel_size) / kernel_size, "same")

# Global variables
fs = 44100  # Sampling frequency
duration = 1  # Recording duration in seconds

# Initialize variables for audio recording
audio_data = np.zeros(fs * duration)
time_axis = np.linspace(0, duration, fs * duration)

# Function to update the plot in real-time
def update_plot():
	plt.ion()  # Turn on interactive mode
	fig, ax = plt.subplots()
	line, = ax.plot(time_axis, audio_data)
	ax.set_ylim(-2, 2)
	ax.set_title('Real-time Audio Waveform')
	ax.set_xlabel('Time (s)')
	ax.set_ylabel('Amplitude')

	i = 0
	curr_state = False
	prev_state = curr_state
	while True:
		ma = movingAverage(np.abs(audio_data), 1001)
		# line.set_ydata(audio_data)
		line.set_ydata(ma)
		if (i % 10 == 0):
			curr_state = detectRisingEdges(ma, 1, 0.4, 100)
			print(not(prev_state) and curr_state)
			prev_state = curr_state
			i = 0
		plt.draw()
		plt.pause(0.1)
		i += 1

# Function to record audio data
def audio_callback(indata, frames, time, status):
	if status:
		print(f"Error: {status}")
	global audio_data
	audio_data = np.concatenate((audio_data[frames:], indata[:, 0]))

# Start a separate thread for real-time plotting
plot_thread = threading.Thread(target=update_plot)
plot_thread.start()

# Start recording audio
with sd.InputStream(callback=audio_callback, channels=1, samplerate=fs):
	# print(f"Recording audio for {duration} seconds...")
	# sd.sleep(int(duration * 1000))  # Sleep for the recording duration
	while True:
		sd.sleep(1000)

# Join the plot thread to avoid prematurely closing the plot
plot_thread.join()
