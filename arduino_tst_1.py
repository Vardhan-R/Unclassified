import pyfirmata, time

board = pyfirmata.Arduino("COM3")

while True:
	board.digital[4].write(1)
	time.sleep(1)
	board.digital[4].write(0)
	time.sleep(1)