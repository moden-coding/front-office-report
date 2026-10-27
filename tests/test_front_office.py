import numbers
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

try:
    import pandas as pd
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "pandas is not installed for the Python running these tests:\n"
        f"    {sys.executable}\n"
        "Select the conda/Anaconda interpreter (Cmd/Ctrl+Shift+P → Python: Select Interpreter), "
        "trash the terminal and open a new one. If you have the extension "
        "'Python Test Explorer for Visual Studio Code', uninstall it and run tests "
        "from the 'Python Tests' tree."
    ) from None

from src.front_office import (league_average_points, assist_leader, top_scorers,
                              celtics_second_option, starter_scoring_gap)

REAL = pd.read_csv(Path(__file__).resolve().parent.parent / "data" / "nba_2024_25.csv")

MINI = pd.DataFrame({
    "Player": ["Ana Ruiz", "Bo Grant", "Cy Lowe", "Dax Ford", "Eve Park", "Fin Hale", "Gil Moss"],
    "Team":   ["NYK", "BOS", "LAL", "BOS", "BOS", "MIA", "NYK"],
    "Age":    [24, 27, 22, 31, 25, 29, 21],
    "Games":  [70, 72, 65, 60, 80, 55, 50],
    "MIN":    [34.0, 30.0, 25.0, 33.0, 29.9, 36.0, 12.0],
    "PTS":    [21.0, 18.0, 9.0, 24.0, 12.0, 27.0, 4.0],
    "REB":    [5.0, 4.0, 3.0, 6.0, 7.0, 5.0, 2.0],
    "AST":    [9.0, 4.0, 2.0, 5.0, 3.0, 6.0, 1.0],
    "STL":    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    "BLK":    [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
}, index=[100, 101, 102, 103, 104, 105, 106])

AVERAGE = "should be the average PTS of every player"
ASSISTS = "should be the Player with the highest AST"
NOT_A_TABLE = "should return a DataFrame (a table)"
COLUMNS = "columns should be exactly Player, Team, PTS — in that order"
TOP_FIVE = "should be the 5 highest PTS, most first"
SECOND = "second-best means second in a highest-first ranking — positions start at 0"
STARTERS = ("'30 or more' includes players at exactly 30.0 minutes; "
            "compare starters to everyone ELSE, not to all players")


def run(function, df):
    """Call a student function. If it crashes, return the error as text so the test fails with a message."""
    try:
        return function(df)
    except Exception as error:
        return type(error).__name__ + ": " + str(error)


class NumberTestCase(unittest.TestCase):
    def check_number(self, result, expected, msg):
        if not isinstance(result, numbers.Real):
            self.fail(repr(result) + " is not a number : " + msg)
        self.assertAlmostEqual(result, expected, places=1, msg=msg)


class TestLeagueAveragePoints(NumberTestCase):
    def test_real_league(self):
        self.check_number(run(league_average_points, REAL.copy()), 8.9343, AVERAGE)

    def test_small_table(self):
        self.check_number(run(league_average_points, MINI.copy()), 16.4286, AVERAGE)


class TestAssistLeader(unittest.TestCase):
    def test_real_league(self):
        self.assertEqual(run(assist_leader, REAL.copy()), "Trae Young", msg=ASSISTS)

    def test_small_table(self):
        self.assertEqual(run(assist_leader, MINI.copy()), "Ana Ruiz", msg=ASSISTS)


class TestTopScorers(NumberTestCase):
    def check_table(self, result, players, points):
        self.assertIsInstance(result, pd.DataFrame, msg=NOT_A_TABLE)
        self.assertEqual(list(result.columns), ["Player", "Team", "PTS"], msg=COLUMNS)
        self.assertEqual(list(result["Player"]), players, msg=TOP_FIVE)
        for result_points, expected_points in zip(result["PTS"], points):
            self.check_number(result_points, expected_points, TOP_FIVE)

    def test_real_league(self):
        self.check_table(
            run(top_scorers, REAL.copy()),
            ["Shai Gilgeous-Alexander", "Giannis Antetokounmpo", "Nikola Jokić",
             "Luka Dončić", "Anthony Edwards"],
            [32.7, 30.4, 29.6, 28.2, 27.6],
        )

    def test_small_table(self):
        self.check_table(
            run(top_scorers, MINI.copy()),
            ["Fin Hale", "Dax Ford", "Ana Ruiz", "Bo Grant", "Eve Park"],
            [27.0, 24.0, 21.0, 18.0, 12.0],
        )


class TestCelticsSecondOption(unittest.TestCase):
    def test_real_league(self):
        self.assertEqual(run(celtics_second_option, REAL.copy()), "Jaylen Brown", msg=SECOND)

    def test_small_table(self):
        self.assertEqual(run(celtics_second_option, MINI.copy()), "Bo Grant", msg=SECOND)


class TestStarterScoringGap(NumberTestCase):
    def test_real_league(self):
        self.check_number(run(starter_scoring_gap, REAL.copy()), 12.8967, STARTERS)

    def test_small_table(self):
        self.check_number(run(starter_scoring_gap, MINI.copy()), 14.1667, STARTERS)


if __name__ == "__main__":
    unittest.main()
