import pyfirmata, smbus, time

board = pyfirmata.Arduino("COM3")
it = pyfirmata.util.Iterator(board)
it.start()

epsilon = 0.025
s = ""

A2 = board.get_pin("a:2:i")
##D6 = board.get_pin("d:6:i")
LiquidCrystal_I2C.LiquidCrystal_I2C

def binToDec(s: str) -> int:
    l = len(s)
    return sum([2 ** x * int(s[l - x - 1]) for x in range(l)])

while True:
    v = A2.read()
    if v != None:
        if abs(v - 1) <= epsilon:
            s += "1"
            print(1, end="")
        elif abs(v - 2 / 3) <= epsilon:
            s += "0"
            print(0, end="")
        elif abs(v - 1 / 3) <= epsilon:
            s = s[:-1]
            print('\n' + s, end="")
        elif abs(v) <= epsilon:
            print()
            for i in range(len(s) // 7):
                print(chr(binToDec(s[7 * i:7 * (i + 1)])), end="")
            print()
    time.sleep(1)
