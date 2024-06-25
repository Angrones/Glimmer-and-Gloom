import pyautogui
import time
import keyboard
import math
import random

GLIMMER_FILE_LOC = "glimmer.png" # The local file location of the glimmer button image
GLOOM_FILE_LOC = "gloom.png" # The local file location of the gloom button image

TILE_REMOVE_LENIENCY = 5 # The maximum number of pixels different two buttons can be before they're considered duplicates and one is pruned.
TILE_SORT_LENIENCY = 5 # The maximum number of pixels different the top left y coordinate can be for buttons before they're considered not in the same row.

CLICK_DELAY = .1 # How much our default delay is before the next click is made.

BAN_EVASION_MODE = True # If set to True, waits a little and moves the mouse a little to evade suspicion. If set to False, we're just being efficient.
DELAY_FUZZING = .5 # The maximum amount of time we can delay a click.
HOVER_FUZZING = (8, 8) # The maximum (and negative minumum) we can alter the mouse click position by.

ENDSCRIPTKEY = "q" # Use this to quit the script immediately. HOLD the key, NOT spam it.
MOUSE_EXIT_BOX = (2, 2) # Where we bring the mouse near to allow for an easy quit out.

CONFIDENCE_VALUE = .7 # The confidence value we're searching the screen with. A lower number will lead to more false positives.

TERMINAL_BOARD_PATTERNS = (
	(0, 0, 0, 1, 0, 1, 0, 0, 1),
	(0, 0, 0, 0, 1, 1, 1, 1, 0),
	(0, 0, 1, 1, 0, 1, 0, 1, 0),
	(1, 0, 1, 1, 0, 1, 1, 1, 1),
	(0, 1, 0, 0, 1, 0, 0, 1, 0),
	(1, 1, 1, 1, 0, 1, 1, 0, 1),
	(0, 1, 0, 1, 0, 1, 1, 0, 0),
	(0, 1, 1, 1, 1, 0, 0, 0, 0),
	(1, 0, 0, 1, 0, 1, 0, 0, 0)
)

class GameBoard:
	def __init__(self):
		self.tiles = [
			[None] * 5,
			[None] * 6,
			[None] * 7,
			[None] * 8,
			[None] * 9,
			[None] * 8,
			[None] * 7,
			[None] * 6,
			[None] * 5,
		]
		self.solving_terminal = False
		self.isSolved = False
		self.find_all()

	def __str__(self):
		string = ""
		i = 4
		for row in self.tiles:
			string += " " * abs(i)
			for col in row:
				if col[1] == "gloom":
					string += "o "
				elif col[1] == "glimmer":
					string += "i "
				else :
					string += "? "
			string += "\n"
			i-=1
		return string

	def find_all(self):
		tiles = []
		for box in pyautogui.locateAllOnScreen(
			GLOOM_FILE_LOC, 
			confidence=CONFIDENCE_VALUE
		):
			tiles.append([box, "gloom"])
		for box in pyautogui.locateAllOnScreen(
			GLIMMER_FILE_LOC, 
			confidence=CONFIDENCE_VALUE
		):
			tiles.append([box, "glimmer"])

		dupes = []
		i = 0
		while(i < len(tiles)):
			tile = tiles[i]
			if i < (len(tiles) - 1):
				for j in range(len(tiles) - i - 1):
					compare_tile = tiles[j+i+1]
					if abs(compare_tile[0].left - tile[0].left) < TILE_REMOVE_LENIENCY:
						if abs(compare_tile[0].top - tile[0].top) < TILE_REMOVE_LENIENCY:
							if compare_tile not in dupes:
								dupes.append(compare_tile)
			i+=1

		for dupe in dupes:
			tiles.remove(dupe)

		sorted_tiles = sorted(tiles, key=lambda tile: tile[0].top)

		rows = [[] for _ in range(9)]
		for row in rows:
			for tile in sorted_tiles:
				if abs(tile[0].top - sorted_tiles[0][0].top) < TILE_SORT_LENIENCY:
					row.append(tile)
			for tile in row:
				sorted_tiles.remove(tile)

		sorted_rows = sorted(rows, key=lambda row: row[0][0].top)

		for i in range(len(sorted_rows)):
			sorted_rows[i] = sorted(sorted_rows[i], key=lambda tile: tile[0].left)

		for row in range(len(sorted_rows)):
			for col in range(len(sorted_rows[row])):
				self.tiles[row][col] = sorted_rows[row][col]

	def find_next_tile(self):
		for y in range(len(self.tiles)):
			for x in range(len(self.tiles[y])):
				if self.tiles[y][x][1] == "gloom":
					print(self.tiles[y][x])
					neighbors = self.get_neighboring_tiles(self.tiles[y][x])
					if neighbors[5]:
						return neighbors[5]
		if self.solving_terminal == False:
			print("Time to start solving this terminal!")
			self.solving_terminal = True
			self.solve_terminal()
			return self.find_next_tile()
		else :
			print("Done!")
			self.isSolved = True

	def get_neighboring_tiles(self, tile):
		indices = self.get_tile_indices(tile)
		neighbors = []
		top_half_directions = ((-1, -1), (0, -1), (-1, 0), (1, 0), (0, 1), (1, 1))
		middle_directions = ((-1, -1), (0, -1), (-1, 0), (1, 0), (-1, 1), (0, 1))
		bottom_half_directions = ((0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1))
		if indices[1] < 4:
			directions = top_half_directions
		elif indices[1] == 4:
			directions = middle_directions
		elif indices[1] > 4:
			directions = bottom_half_directions
		for direction in directions:
			neighbor_indices = (indices[0] + direction[0], indices[1] + direction[1])
			if neighbor_indices[1] in range(0, len(self.tiles)):
				if neighbor_indices[0] in range(0, len(self.tiles[neighbor_indices[1]])):
					neighbors.append(
						self.tiles[neighbor_indices[1]][neighbor_indices[0]]
					)
				else :
					neighbors.append(None)
			else :
				neighbors.append(None)
		return neighbors

	def solve_terminal(self):
		terminal_row = (
			1 if self.tiles[8][0][1] == "gloom" else 0,
			1 if self.tiles[8][1][1] == "gloom" else 0,
			1 if self.tiles[8][2][1] == "gloom" else 0,
			1 if self.tiles[8][3][1] == "gloom" else 0,
			1 if self.tiles[8][4][1] == "gloom" else 0,
			1 if self.tiles[7][5][1] == "gloom" else 0,
			1 if self.tiles[6][6][1] == "gloom" else 0,
			1 if self.tiles[5][7][1] == "gloom" else 0,
			1 if self.tiles[4][8][1] == "gloom" else 0,
		)

		testing_rows = [[0 for _ in range(9)] for x in range(9)]

		for y in range(len(testing_rows)):
			row = testing_rows[y]
			compare = terminal_row[y]
			if compare == 1:
				for x in range(len(row)):
					testing_rows[y][x] = TERMINAL_BOARD_PATTERNS[y][x]

		solution_row = [0 for _ in range(9)]
		for x in range(len(solution_row)):
			one_sum = 0
			for row in testing_rows:
				one_sum += row[x]
			if one_sum % 2 != 0:
				solution_row[x] = 1

		beginning_row = (
			self.tiles[4][0],
			self.tiles[3][0],
			self.tiles[2][0],
			self.tiles[1][0],
			self.tiles[0][0],
			self.tiles[0][1],
			self.tiles[0][2],
			self.tiles[0][3],
			self.tiles[0][4]
		)

		tile_clicks = []
		for x in range(len(solution_row)):
			if solution_row[x] == 1:
				tile_clicks.append(beginning_row[x])

		for tile in tile_clicks:
			self.click_tile(tile)

	def get_tile_indices(self, tile):
		for y in range(len(self.tiles)):
			for x in range(len(self.tiles[y])):
				if self.tiles[y][x] == tile:
					return (x, y)
		return None

	def click_tile(self, tile):
		print("Clicking tile:")
		print(tile)
		delay = CLICK_DELAY
		if BAN_EVASION_MODE:
			delay += random.uniform(0, DELAY_FUZZING)
		time.sleep(delay)
		center = pyautogui.center(tile[0])
		if BAN_EVASION_MODE:
			center = (
				center[0] + random.randint(-HOVER_FUZZING[0], HOVER_FUZZING[0]), 
				center[1] + random.randint(-HOVER_FUZZING[1], HOVER_FUZZING[1])
			)
		print(center)
		pyautogui.click(center[0], center[1])
		neighbors = self.get_neighboring_tiles(tile)
		neighbors.append(tile)
		for neighbor in neighbors:
			if neighbor == None:
				continue
			elif neighbor[1] == "gloom":
				neighbor[1] = "glimmer"
			elif neighbor[1] == "glimmer":
				neighbor[1] = "gloom"
		# pyautogui.moveTo(MOUSE_EXIT_BOX[0] + 10, MOUSE_EXIT_BOX[1] + 10)
		print(self)

def solve_board():
	gameBoard = GameBoard()
	print(gameBoard)
	while(not gameBoard.isSolved):
		next_tile = gameBoard.find_next_tile()
		print(next_tile)
		if next_tile is not None:
			gameBoard.click_tile(next_tile)
		if keyboard.is_pressed(ENDSCRIPTKEY):
			print("Key press detected! Aborting script...")
			break
	return

if __name__ == "__main__":
	solve_board()
