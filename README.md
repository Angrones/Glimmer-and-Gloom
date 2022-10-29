# WIP! WORK IN PROGRESS!
A fork of [**jraynolds**](https://github.com/jraynolds)'s [**Glimmer and Gloom Script**](https://github.com/jraynolds/Glimmer-and-Gloom).
> # Glimmer-and-Gloom
> A python automated bot to play Flight Rising's Glimmer and Gloom minigame on the Very Hard difficulty.
> The bot will work its way, clicking down from the top left to the bottom right. When it runs out of gloom hexes that aren't on the bottom right edges, it'll calculate the appropriate glimmers to click on and work them down to cancel out the remaining edge hexes. Calculations from the excellent <a href="https://docs.google.com/spreadsheets/d/1zrLIjer2FKmknXpyopCSEfVDdEP5rgxWsTOBVFkW8lQ/edit#gid=0">spreadsheet</a> done by <a href="https://flightrising.com/main.php?p=lair&tab=userpage&id=186567">Sqld</a>.
> If at any time the program has to be stopped, move your cursor to the top left corner of the screen and keep it there. That will terminate the project.

# Set-up
## Requirements
- Python (https://www.python.org/downloads/)
  - Pip (https://pip.pypa.io/en/stable/installation/#get-pip-py)
  - Pillow (https://pillow.readthedocs.io/en/stable/installation.html#basic-installation)

## Installation
- Download Python through the official website.<img align="right" height="200" src="https://user-images.githubusercontent.com/102916830/198846955-49a9a00f-7de5-4e2b-bbd1-18a122bd9349.png">
  - During the installaton, there will be a option to add Python to PATH. **Make sure to toggle it on!** This will allow you to install the other two things _without_ requiring to manually add Python to PATH (aka what allows you to use python in the Command Prompt).
- Download get-pip.py (in Requirements) and use the Command Prompt > `py get-pip.py`, let Python do its thing. To test if it's been installed properly, do `pip list`.
- The Script will asks for Pillow, use the Command Prompt and use the commands below. It should install Pillow.
```
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow
``` 
- Download the script by clicking on Code > Download ZIP. Extract it and enjoy.<img align="right" height="150" src="https://user-images.githubusercontent.com/102916830/198846956-62dd0a63-9859-4e62-849d-2728b992beba.png">

# Basics
## Label Rundown
This is a rundown of the `board_solver.py` and `autorun.py` options. Some options are best not to be touched with such as TILE_REMOVE_LENIENCY, TILE_SORT_LENIENCY, and BAN_EVASION_MODE.
### Board_solver.py
- **GLIMMER_FILE_LOC** & **GLOOM_FILE_LOC** are links to the PNGs of each tile. These are what will represent the tiles for the Script to follow.
- **CLICK_DELAY** is the default click delay, it's at its lowest.
- **DELAY_FUZZING** is to add additional delay to the click, so if you feel the click is going too fast or too slow, change the speed here.
- **HOVER_FUZZING** is to alter the mouse position within the tile limits.
- **MOUSE_EXIT_BOX** is to alter the size of the exit box.
- **CONFIDENCE_VALUE** is to alter the Script's detection level of the PNGs in the tiles. Check Confidence & PNGs section for more information.
### Autorun.py
- **PLAY_FILE_LOC** has the same functions of GLIMMER_FILE_LOC and GLOOM_FILE_LOC but for the Play button after finishing a round.
- **GAME_DELAY_1**
- **GAME_DELAY_2**
- **CONFIDENCE_VALUE**
- **NUM_LOOPS**
