> [!WARNING]
> I'M NOT A PYTHON EXPERT! This means I can't create support for Mac/Linux, and I can't tell if the code is updated or not. Until someone with python knowledge can step in, it is what it is. This script also requires low maintenance.

# Glimmer-and-Gloom
A python automated bot to play Flight Rising's Glimmer and Gloom minigame on the Very Hard difficulty.

The bot will work its way, clicking down from the top left to the bottom right. When it runs out of gloom hexes that aren't on the bottom right edges, it'll calculate the appropriate glimmers to click on and work them down to cancel out the remaining edge hexes. Calculations from the excellent <a href="https://docs.google.com/spreadsheets/d/1zrLIjer2FKmknXpyopCSEfVDdEP5rgxWsTOBVFkW8lQ/edit#gid=0">spreadsheet</a> done by <a href="https://flightrising.com/main.php?p=lair&tab=userpage&id=186567">Sqld</a>.
If at any time the program has to be stopped, move your cursor to the top left corner of the screen and keep it there. That will terminate the project.

---
A fork of [**jraynolds**](https://github.com/jraynolds)'s [**Glimmer and Gloom Script**](https://github.com/jraynolds/Glimmer-and-Gloom). This fork includes:
- A fix for the "TypeError: can only concatenate str (not "int") to str" and Ending game 1 > Beginning game 11 error
- An In-depth Installation and Script Setup
- A rundown of the basis
- An in-depth explanation of how Confidence and the PNGs works for those who still have troubles figuring this out.

# Check the [WIKI](https://github.com/Angrones/Glimmer-and-Gloom/wiki) for more information!
