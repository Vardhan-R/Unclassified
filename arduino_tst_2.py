# import pyfirmata, time

# board = pyfirmata.Arduino("COM3")
# a = False

# while True:
# 	# analogWrite(3, 1023 * a);
# 	# analogWrite(5, 512);
# 	# digitalWrite(6, LOW);
# 	# a = !a;
# 	# delay(1000);
# 	print(a)
# 	board.digital[3].write(int(a))
# 	# board.digital[5].write(1)
# 	board.digital[6].write(0)
# 	a = not(a)
# 	time.sleep(1)

import pyfirmata
import time

# Connect to the Arduino board
board = pyfirmata.Arduino("COM3")

# Set up the pins
led_pin = 3
board.digital[led_pin].mode = pyfirmata.PWM  # Set the pin mode to PWM for analog output

# Initialize variables
a = False

try:
	while True:
		# Write values to the pins
		board.digital[led_pin].write(int(a))
		board.digital[5].write(1)  # Assuming pin 5 is another digital pin you want to set to HIGH
		board.digital[6].write(0)  # Assuming pin 6 is another digital pin you want to set to LOW

		# Toggle the variable for blinking
		a = not a

		# Delay for 1 second
		time.sleep(1)
		print(a)

except KeyboardInterrupt:
	# Close the connection when the program is interrupted
	board.exit()