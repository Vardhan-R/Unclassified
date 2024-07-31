import os
# import warnings

# warnings.filterwarnings("ignore")
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

from pynput.keyboard import Key
from pynput.mouse import Button
import cv2, HandTrackingModule as htm, mss, numpy as np, pynput

def dispClicker(pos: tuple[int, int]) -> None:
	if click_val:
		cv2.ellipse(img, (pos[0], pos[1]), (17, 17), 0, -90, -90 + 360 * click_val, (0, 100, 0), 2)

def doDetectionStuff() -> None:
	global click_val, curr_selection, img, prev_selection

	finger_pos = detector.getPosition(img, [8], draw=False)
	img = np.zeros_like(img)

	curr_selection = None
	if finger_pos:
		mouse.position = (finger_pos[0][0] * m_width / width, finger_pos[0][1] * m_height / height)
		if finger_pos[0][0] < left_margin:
			curr_selection = Key.left
		elif finger_pos[0][0] > width - right_margin:
			curr_selection = Key.right

		if curr_selection == prev_selection != None:
			click_val += click_speed
		else:
			click_val = 0
			prev_selection = curr_selection

		if click_val >= 1:
			# game_status = selection_status_pairs[curr_selection]
			keyboard.tap(curr_selection)
			# print("Pressed", curr_selection)
			click_val = 0

		cv2.circle(img, finger_pos[0], 10, (206, 175, 16), -1)
		dispClicker(finger_pos[0])

running = True
# cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
# cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cap = cv2.VideoCapture(0)
success, img = cap.read()
height, width = img.shape[:2]
click_val = 0
prev_selection = None
left_margin, right_margin = 75, 75
click_speed = 0.1

m = mss.mss()
m_width, m_height = m.monitors[0]["width"], m.monitors[0]["height"]

keyboard = pynput.keyboard.Controller()
mouse = pynput.mouse.Controller()

detector = htm.FindHands()

while running:
	success, img = cap.read()
	img = cv2.flip(img, 1)

	doDetectionStuff()

	cv2.line(img, (left_margin, 0), (left_margin, height), (0, 0, 255), 2)
	cv2.line(img, (width - right_margin, 0), (width - right_margin, height), (0, 0, 255), 2)

	cv2.imshow("Image", img)

	if chr(cv2.waitKey(1) & 0xFF) == 'q':
		break
