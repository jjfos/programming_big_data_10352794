
import unittest
import pandas as pd
from commit import Commit
from datetime import date

from analyse_data import get_commits, read_file, get_data_frame, get_no_authors, get_no_dates,get_most_lines_per_comment

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.log')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0].author)
        self.assertEqual(1551925, commits[0].revision)

    def test_data_frame(self):
        #set up dataframe
        commits = get_commits(self.data)
        df = get_data_frame(commits)


        self.assertEqual(422, (len(df.index)))
        data_frame_columns = list(df)
        
        # test column labels are correct
        commit_labels = Commit.COLUMNS
        self.assertEqual(commit_labels, data_frame_columns)
        
        # test correct number of columns
        self.assertEqual(len(df.columns), 6)

        no_authors = get_no_authors(df)
        self.assertEqual(no_authors , 10)

        no_dates = get_no_dates(df)
        self.assertEqual(no_dates , 76)

        most_comments = get_most_lines_per_comment(df)
        self.assertEqual(most_comments , 7)


if __name__ == '__main__':
    unittest.main()
