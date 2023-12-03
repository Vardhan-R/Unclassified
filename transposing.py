fp = open("C:/Users/vrdhn/Desktop/CS/transposed_song.txt", 'r')
full_lst = fp.readlines()
fp.close()

# lst = input("Input: ").upper().replace("  ", " \n ").split(" ")
# print(lst)

while True:
	transpose = input('Transpose ("+" or "-"): ')
	fp = open("C:/Users/vrdhn/Desktop/CS/transposed_song.txt", 'w')

	for s in full_lst:
		lst = s.upper().split(" ")
		if lst[-1][-1] == '\n':
			lst[-1] = lst[-1][:-1]

		if transpose == '+':
			for i in range(len(lst)):
				if lst[i][:2] == 'C#':
					lst[i] = 'D' + lst[i][2:]
				elif lst[i][:2] == 'D#':
					lst[i] = 'E' + lst[i][2:]
				elif lst[i][:2] == 'F#':
					lst[i] = 'G' + lst[i][2:]
				elif lst[i][:2] == 'G#':
					lst[i] = 'A' + lst[i][2:]
				elif lst[i][:2] == 'A#':
					lst[i] = 'B' + lst[i][2:]
				elif lst[i][:1] == 'C':
					lst[i] = 'C#' + lst[i][1:]
				elif lst[i][:1] == 'D':
					lst[i] = 'D#' + lst[i][1:]
				elif lst[i][:1] == 'E':
					lst[i] = 'F' + lst[i][1:]
				elif lst[i][:1] == 'F':
					lst[i] = 'F#' + lst[i][1:]
				elif lst[i][:1] == 'G':
					lst[i] = 'G#' + lst[i][1:]
				elif lst[i][:1] == 'A':
					lst[i] = 'A#' + lst[i][1:]
				elif lst[i][:1] == 'B':
					if type(lst[i][1:]) == int:
						lst[i] = 'C' + str(int(lst[i][1:]) + 1)
					else:
						lst[i] = 'C'
		else:
			for i in range(len(lst)):
				if lst[i][:2] == 'C#':
					lst[i] = 'C' + lst[i][2:]
				elif lst[i][:2] == 'D#':
					lst[i] = 'D' + lst[i][2:]
				elif lst[i][:2] == 'F#':
					lst[i] = 'F' + lst[i][2:]
				elif lst[i][:2] == 'G#':
					lst[i] = 'G' + lst[i][2:]
				elif lst[i][:2] == 'A#':
					lst[i] = 'A' + lst[i][2:]
				elif lst[i][:1] == 'C':
					if type(lst[i][1:]) == int:
						lst[i] = 'B' + str(int(lst[i][1:]) - 1)
					else:
						lst[i] = 'B'
				elif lst[i][:1] == 'D':
					lst[i] = 'C#' + lst[i][1:]
				elif lst[i][:1] == 'E':
					lst[i] = 'D#' + lst[i][1:]
				elif lst[i][:1] == 'F':
					lst[i] = 'E' + lst[i][1:]
				elif lst[i][:1] == 'G':
					lst[i] = 'F#' + lst[i][1:]
				elif lst[i][:1] == 'A':
					lst[i] = 'G#' + lst[i][1:]
				elif lst[i][:1] == 'B':
					lst[i] = 'A#' + lst[i][1:]

		fp.write(" ".join(lst) + '\n')

	fp.close()