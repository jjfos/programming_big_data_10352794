import pandas as pd
# create the commit class to hold each of the elements - I am hoping there will be 422
# otherwise I have messed up.
class Commit:
    'class for commits'
   
    COLUMNS = ['revision', 'author', 'date', 'comment line count', 'changes', 'comment']
       
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment
    

    def get_commit(self):
        return {'revision': self.revision,'author': self.author, 'date': self.date, 'comment line count': self.comment_line_count,'changes': self.changes,'comment': self.comment}

