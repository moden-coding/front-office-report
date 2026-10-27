from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "nba_2024_25.csv"


def league_average_points(df: pd.DataFrame) -> float:
    """How many points does the average player score per game? Return the average of PTS."""
    pass


def assist_leader(df: pd.DataFrame) -> str:
    """Who led the league in assists? Return the Player with the highest AST."""
    pass


def top_scorers(df: pd.DataFrame) -> pd.DataFrame:
    """Who were the top 5 scorers? Return a table of the 5 highest PTS, most first,
    with only the Player, Team and PTS columns, in that order."""
    pass


def celtics_second_option(df: pd.DataFrame) -> str:
    """Who is the Celtics' second-best scorer? Return the Player on BOS with the second-highest PTS."""
    pass


def starter_scoring_gap(df: pd.DataFrame) -> float:
    """Starters play 30 or more minutes a game. How many more points do starters score than everyone else?
    Return the average PTS of players with MIN of 30 or more, minus the average PTS of everyone else."""
    pass


def main():
    df = pd.read_csv(DATA_PATH)
    print("Average points per game:", league_average_points(df))
    print("Assist leader:", assist_leader(df))
    print()
    print("Top 5 scorers:")
    print(top_scorers(df))
    print()
    print("Celtics' second-best scorer:", celtics_second_option(df))
    print("How many more points starters score:", starter_scoring_gap(df))


if __name__ == "__main__":
    main()
