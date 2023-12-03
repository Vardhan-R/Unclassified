import pynput, pyperclip, time

pyperclip.copy("mfmmfm")
print(pyperclip.paste())

mouse = pynput.mouse.Controller()

while True:
	print(mouse.position)
	time.sleep(1)