# Glimmer-and-Gloom
A python automated bot to play Flight Rising's Glimmer and Gloom minigame on the Very Hard difficulty.

The bot will work its way, clicking down from the top left to the bottom right. When it runs out of gloom hexes that aren't on the bottom right edges, it'll calculate the appropriate glimmers to click on and work them down to cancel out the remaining edge hexes. Calculations from the excellent <a href="https://docs.google.com/spreadsheets/d/1zrLIjer2FKmknXpyopCSEfVDdEP5rgxWsTOBVFkW8lQ/edit#gid=0">spreadsheet</a> done by <a href="https://flightrising.com/main.php?p=lair&tab=userpage&id=186567">Sqld</a>.
If at any time the program has to be stopped, move your cursor to the top left corner of the screen and keep it there. That will terminate the project.

---
A fork of [**jraynolds**](https://github.com/jraynolds)'s [**Glimmer and Gloom Script**](https://github.com/jraynolds/Glimmer-and-Gloom). This fork includes:
- A fix for the "TypeError: can only concatenate str (not "int") to str" and Ending game 1 > Beginning game 11 error;
- An In-depth Installation and Script Setup;
- A rundown of the basis;
- An in-depth explanation of how Confidence and the PNGs works for those who still have troubles figuring this out.

# Setup
## Requirements
- Python (https://www.python.org/downloads/)
  - Pip (https://pip.pypa.io/en/stable/installation/#get-pip-py)
  - Pillow (https://pillow.readthedocs.io/en/stable/installation.html#basic-installation)

## Installation
- Download Python through the official website.<img align="right" height="100" src="https://user-images.githubusercontent.com/102916830/198846955-49a9a00f-7de5-4e2b-bbd1-18a122bd9349.png">
  - During the installaton, there will be a option to add Python to PATH which is what will allow you to use Python commands through Command Prompt (Pic. 1). **MAKE SURE TO TOGGLE THIS ON!** It automatically adds Python _without_ requiring a manual action (a very tricky manual action too).
- Download get-pip.py (in Requirements) and use the Command Prompt > `py get-pip.py`, let Python do its thing. To test if it's been installed properly, do `pip list`.<img align="right" height="100" src="https://user-images.githubusercontent.com/102916830/198846956-62dd0a63-9859-4e62-849d-2728b992beba.png">
- The Script will asks for Pillow, use the Command Prompt and use the commands below. It should install Pillow.
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
``` 
- Download the script by clicking on Code > Download ZIP (Pic. 2). Extract it and enjoy.

## Script Setup
<img align="right" height="100" src="https://user-images.githubusercontent.com/102916830/198889205-8600019f-fb9e-4985-b967-61c464ac2cfb.png">

- Open the Glimmer-and-Gloom-master and on the address bar type "cmd", it will bring a Command Prompt with the Glimmer-and-Gloom-master already on it (Pic. 3).
- Open Flight Rising > Fairgrounds > Glimmer and Gloom
  - If the game doesn't cover the screen, zoom out. Remember to edit the PNGs and the Script's setting as well, check [Confidence & PNGs](https://github.com/HjOtal-1/Glimmer-and-Gloom/blob/master/README.md#confidence--pngs) section for more information. 
- Drag the cmd window to the left or right, it will prompt a thing that will automatically resize the prompt window to be half the screen and let you select the (window to be the) other half.
- Select Flight Rising and the end result should look like below (Pic. 4).

<p align="center"><img height="250" src="https://user-images.githubusercontent.com/102916830/198889212-77617e8a-ae71-4444-9951-4d7d7b77b337.png"></p>

# Basics
## Label Rundown
This is a rundown of the `board_solver.py` and `autorun.py` options. Some options are best not to be touched with such as TILE_REMOVE_LENIENCY and TILE_SORT_LENIENCY (directly will ), and BAN_EVASION_MODE.
### Board_solver.py
- **GLIMMER_FILE_LOC** & **GLOOM_FILE_LOC** are links to the PNGs of each tile. These are what will represent the tiles for the Script to follow.
- **CLICK_DELAY** is the default click delay, it's at its lowest.
- **DELAY_FUZZING** is to add additional delay to the click, so if you feel the click is going too fast or too slow, change the speed here.
- **HOVER_FUZZING** is to alter the mouse position within the tile limits.
- **MOUSE_EXIT_BOX** is to alter the size of the exit box.
- **CONFIDENCE_VALUE** is to alter the Script's detection level of the PNGs in the tiles. Check [Confidence & PNGs](https://github.com/HjOtal-1/Glimmer-and-Gloom/blob/master/README.md#confidence--pngs) section for more information.
### Autorun.py
- **PLAY_FILE_LOC** has the same functions of GLIMMER_FILE_LOC and GLOOM_FILE_LOC but for the Play button after finishing a round.
- **GAME_DELAY_1** is the delay between starting a new game and letting the board load.
- **GAME_DELAY_2** is the delay between finishing the board and loading the result screen.
- **CONFIDENCE_VALUE** has the same functionality as Board_solver.py's CONFIDENCE_VALUE but for the Play button.
- **NUM_LOOPS** how many times will the Autorun loop for. Default setting will obtain all 75,000 Treasure in one sitting (`18*4000 = 72,000+3000 (19th round) = 75,000`).

## Renaming Scripts
To rename the scripts, just change the name directly and in Board_solver.py's case, remember to edit the `from board_solver import *` to `from [NAME] import *` with the Board_solver.py's new name otherwise the Autorun.py will throw an error because they can't locate the renamed Board_solver.py.

# Confidence & PNGs
**CONFIDENCE_VALUE** or just Confidence is how well can the script detect the Glimmer.png and Gloom.png (**PNGs**) that correspond to the board tiles, they systematically work together.
<p align="center">The higher the Confidence, the better the script can detect the PNGs as the tiles.</p>
<p align="center">↕</p>
<p align="center">The more evenly matched the PNGs are to the board tiles, the better the script can confidently detect the PNGs on the board.</p>
It's important to evenly match these two elements otherwise the Script won't be able to work. To get the PNGs, you must first setup your board according to how it better suits you - change the zoom, align the windows around, ect. The important factors are 1. Make sure the board is visible and 2. Make sure the script is visible.

The PNGs must represent _all_ the tiles of the board and the Play button meaning the PNG you choose must be taken directly from a screenshot of your current display setup of the board (e.g: if you zoomed out about 80% to make the board visible, then that's how your current display setup works). The PNGs must evenly match the tiles on the board without any major visual difference as seen in the pic below otherwise it will display the "_list index out of range_" error.
<p align="center"><img height="150" src="https://user-images.githubusercontent.com/102916830/198897941-416dac1f-4fd9-4417-adf9-0d2252b03802.png"></p>

After gathering the new PNGs, you must setup the Confidence according to what the Script confidently (no pun intended) thinks they can detect the PNGs as tiles. I recommend doing a run with the script (type board_solver.py in the cmd from [Script Setup](https://github.com/HjOtal-1/Glimmer-and-Gloom/blob/master/README.md#script-setup)) and test out the Confidence. If you get a "_'NoneType' object is not subscriptable_", low it till you can keep it running for a full round and remember to check the PNGs if the error is a "_list index out of range_" instead.

In my case, I have a system scaling that isn't divisible by 100 hence my tiles being riddled with visual differences, the PNGs I have are very small with minor differences but because they aren't perfect, the Script would only work if I lowered the Confidence to .8.

## Autorun's Confidence & PNG
The Autorun's Confidence and PNGs work exactly the same as the Board_solver.py except it's for the Play button after a game has been completed. Just like the tile PNGs, the Play PNG must contain minor visual differences so the Script can confidently detect it as the Play button. Take the example below:
<p align="center"><img height="150" src="https://user-images.githubusercontent.com/102916830/198839758-0482050b-b55d-48a4-b60f-47b4f268f998.png"></p>

# Troubleshooting Q&A
**Q:** I'm having issues installing Python and/or the other additions.

**A:** We suggest searching on how to install Python. As for the other additions, Python requires to be installed in PATH which lets you use Python commands through the Command Prompt. To check if Python is installed in your PATH, consult this [article](https://projects.raspberrypi.org/en/projects/using-pip-on-windows/4).

---
**Q:** When I started the Script, I got a "_IndexError: list assignment index out of range/IndexError: list index out of range_" error.

**A:** This is because your PNGs are not taken from how your screen displays the G&G board. The PNGs **must** be direct screenshot of _your_ board display in order to represent the tiles, make sure to read [Confidence & PNGs](https://github.com/HjOtal-1/Glimmer-and-Gloom/blob/master/README.md#confidence--pngs) Section for more information.

---
**Q:** When I starter the Script, I got a "_TypeError: 'Nonetype' object is not subscriptable_" error.

**A:** Usually, this is the first error that will appear and it's due to the Board_solver.py's Confidence being too high to be able to detect the current PNGs as the tile. We recommend to first edit the PNGs (read [Confidence & PNGs](https://github.com/HjOtal-1/Glimmer-and-Gloom/blob/master/README.md#confidence--pngs) Section for more information), if it still displays the error, decrease the Confidence from .9 to .8 and so on depending on whether or not it keeps getting the error.
