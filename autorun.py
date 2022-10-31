# Plays indefinitely.

import pyautogui
import time
from board_solver import *

PLAY_FILE_LOC = "play.png" # The local file location of the play button image
GAME_DELAY_1 = 2.9 # How much we wait after the game loads.
GAME_DELAY_2 = .54 # How much we wait before starting a new game.
CONFIDENCE_VALUE = .9 # The confidence value we're searching the screen with. A lower number will lead to more false positives.
NUM_LOOPS = 19 # The maximum number of games we'll play. After this number, the script will quit.
n = 1

print("Starting the game, we'll play " + str(NUM_LOOPS) + " rounds.")
while n < NUM_LOOPS:
	print("Beginning round #" + str(n) + "...")
	solve_board()
	time.sleep(GAME_DELAY_1)
	pyautogui.click(
		pyautogui.center(
			pyautogui.locateOnScreen(
				PLAY_FILE_LOC, 
				confidence=CONFIDENCE_VALUE
			)
		)
	)
	time.sleep(GAME_DELAY_2)
	print("Ending round #" + str(n) + "...")
	n += 1
print("Exiting Script.")
