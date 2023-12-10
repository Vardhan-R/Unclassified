import matplotlib.pyplot as plt, numpy as np

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

def detectRisingEdges(arr: np.ndarray, amplitude: float, threshold: float, sample_spacing: int) -> np.ndarray:
	arr_size = arr.size
	rising_edges_arr = np.zeros(arr_size)
	curr_state = False
	prev_state = curr_state

	for i in range(0, arr_size, sample_spacing):
		curr_state = arr[i] >= threshold
		rising_edges_arr[i] += int(not(prev_state) and curr_state) * amplitude
		prev_state = curr_state

	return rising_edges_arr

def movingAverage(arr: np.ndarray, kernel_size: int) -> np.ndarray:
	return np.convolve(arr, np.ones(kernel_size) / kernel_size, "same")

def peakNoise(size: int, mean: float, sd: float, count: int) -> np.ndarray:
	rng = np.random.default_rng()
	arr = np.zeros(size)
	for _ in range(count):
		arr[rng.integers(0, size)] += np.random.normal(mean, sd)
	return arr

def pulse(size: int, start: int, length: int, amplitude: float) -> np.ndarray:
	arr = np.zeros(size)
	for i in range(start, start + length):
		arr[i] = amplitude
	return arr

def randomNoise(size: int, max_val: float) -> np.ndarray:
	return 2 * max_val * np.random.random(size) - 1

size = 1000
amplitude = 1000
raw_signal = np.zeros(size)
raw_signal += pulse(size, 10, 30, amplitude)
raw_signal += pulse(size, 79, 90, amplitude)
raw_signal += pulse(size, 208, 25, amplitude)
raw_signal += pulse(size, 252, 20, amplitude)
raw_signal += pulse(size, 408, 70, amplitude)
raw_signal += pulse(size, 809, 30, amplitude)
raw_signal += peakNoise(size, amplitude, 200, 5)
raw_signal += peakNoise(size, -amplitude, 200, 5)
raw_signal += randomNoise(size, 10)

ma_5 = movingAverage(raw_signal, 5)

fe_5 = detectFallingEdges(ma_5, amplitude, 500, 1)
re_5 = detectRisingEdges(ma_5, amplitude, 500, 1)
print(sum(re_5) / amplitude)

sw = amplitude * np.sin(np.arange(size) / 10)
ma_sw = movingAverage(movingAverage(np.absolute(sw), 100), 1)

# plt.plot(raw_signal)
# plt.plot(ma_5)
# plt.plot(-fe_5)
# plt.plot(-re_5)
plt.plot(sw)
plt.plot(ma_sw)
plt.show()
