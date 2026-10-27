# Front Office Report

You run an NBA front office. Answer five questions about the 2024–25 season, one function each.

## The data

`data/nba_2024_25.csv` has one row per player:

- **Player**
- **Team**: 3-letter abbreviation (e.g. BOS = Boston Celtics)
- **Age**
- **Games**: games played
- Per-game averages: **MIN** minutes, **PTS** points, **REB** rebounds, **AST** assists, **STL** steals, **BLK** blocks

## The questions

All five functions are in `src/front_office.py`.

1. **How many points does the average player score per game?** `league_average_points(df)` returns the average of PTS.
2. **Who led the league in assists?** `assist_leader(df)` returns the Player with the highest AST.
3. **Who were the top 5 scorers?** `top_scorers(df)` returns a table of the 5 highest PTS, most first, with only the Player, Team and PTS columns, in that order.
4. **Who is the Celtics' second-best scorer?** `celtics_second_option(df)` returns the Player on BOS with the second-highest PTS.
5. **Starters play 30 or more minutes a game. How many more points do starters score than everyone else?** `starter_scoring_gap(df)` returns the average PTS of players with MIN of 30 or more, minus the average PTS of everyone else.

Questions 1–2 warm you up; 4–5 combine several steps. Question 3 returns a table; the others return a number or a name. You don't need to round.

Every function must work on any table with these columns; the tests also use a small practice table.

## How to run

- See your findings: `python src/front_office.py`
- Run the tests: `python -m unittest discover` (or use the "Python Tests" tree in the Testing panel)

## If tests won't run

- **"No module named pandas"**: select the conda/Anaconda interpreter (Cmd/Ctrl+Shift+P → Python: Select Interpreter), then trash the terminal and open a new one.
- If "Python Test Explorer for Visual Studio Code" is installed, uninstall it; it ignores your interpreter choice.
- Open the assignment folder itself (File → Open Folder), not a folder above it.
- Windows: if conda won't activate in the terminal, run `conda init powershell` once in Anaconda Prompt and restart VS Code.
