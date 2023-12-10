from manim import *
import numpy as np, pygame

pygame.init()

width = 1400
height = 800
running = True
n = 10
length_arr = np.zeros(int(np.ceil(np.log2(n))))
pos = np.zeros((n, 2))
primes = []

scrn = pygame.display.set_mode((width, height))

for i in range(2, n + 1):
	primes.append(i)
	for j in range(2, int(np.floor(np.sqrt(i))) + 1):
		if not(i % j):
			primes.pop()
			break

for i in range(1, n + 1):
	if not(i % 10000):
		print(i)

	f = 0
	i_copy = i
	for j in primes:
		while not(i % j):
			f += 1
			i /= j
	pos[i_copy - 1][0] = length_arr[f - 1] # x
	pos[i_copy - 1][1] = f # y
	length_arr[f - 1] += 1

print(length_arr)
arr = np.array(eval("[9.5920e+03, 2.3378e+04, 2.5556e+04, 1.8744e+04, 1.1185e+04, 5.9330e+03, 2.9730e+03, 1.4180e+03, 6.7100e+02, 3.0600e+02, 1.3800e+02, 6.3000e+01, 2.5000e+01, 1.1000e+01, 4.0000e+00, 2.0000e+00, 1.0000e+00]"))
print(np.average(np.arange(1, arr.size + 1), weights=arr))

# pos[:, 0] *= 0.5
# pos[:, 0] += 10
# pos[:, 1] *= 60
# pos[:, 1] *= -1
# pos[:, 1] += height

# while running:
# 	scrn.fill(BLACK)

# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			running = False

# 	for i in range(0, n - 1, 10):
# 		pygame.draw.line(scrn, BLUE, pos[i], pos[i + 1], 1)

# 	for i in range(n):
# 		pygame.draw.circle(scrn, RED, pos[i], 1)

# 	pygame.display.update()

pygame.quit()