import time
n = input("Enter your name: ")
t = int(time.strftime("%H", time.localtime()))
if t > 3 and t < 12:
    print("Good Morning", n + "!")
elif t > 11 and t < 16:
    print("Good Afternoon", n + "!")
else:
    print("Good Evening", n + "!")